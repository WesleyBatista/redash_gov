import re
import io
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery
from apiclient.http import MediaIoBaseDownload
from httplib2 import Http


def _get_drive_ids_from_email(mail):
    ids = list(set(re.findall('(?<=https://drive.google.com/file/d/)\w+', str(mail), re.DOTALL)))
    return ids


def download_files(mail, path, credentials_json_file):
    files = list()
    fileIds = _get_drive_ids_from_email(mail)
    if fileIds:
        for fileId in fileIds:
            filePath = download_from_drive(fileId, credentials_json_file)
            files.append(filePath)

    return files


def _write_io_file(data, filePath):
    with open(filePath, 'wb') as f:
        f.write(data.getvalue())
    return True


def _get_drive_file_metadata(service, fileId):
    results = service.files().get(fileId=fileId).execute()
    return results


def download_from_drive(fileId, credentials_json_file):
    scopes = [
        'https://www.googleapis.com/auth/drive',
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_json_file, scopes)
    http = credentials.authorize(Http())
    drive_service = discovery.build('drive', 'v3', http=http)
    request = drive_service.files().get_media(fileId=fileId)
    metadata = _get_drive_file_metadata(drive_service, fileId)
    fileDestinationPath = metadata['name'].encode('utf-8')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    _write_io_file(fh, fileDestinationPath)
    print("{} downloaded.".format(fileDestinationPath))
