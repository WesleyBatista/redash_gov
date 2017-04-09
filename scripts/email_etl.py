import os
import email as emailParser
import click
import imaplib
from datetime import datetime, timedelta, date
import google_drive


def search_inbox(conn, subject, days):
    """receive conn, subject and days as arguments and search in the inbox"""
    conn.select(subject)
    searchTmpl = '(SENTSINCE {DATE})'
    dateIni = (date.today() - timedelta(days=days)).strftime("%d-%b-%Y")
    searchStr = searchTmpl.format(DATE=dateIni)
    typ, results = conn.search(None, searchStr)

    if typ != 'OK':
        print('Error searching Inbox for "{}"'.format(searchStr))
        raise

    return results


def _get_destination_file_path(exportDir, filename):
    return "{}/{}".format(exportDir, filename)


def _write_file(filePath, content):
    fp = open(filePath, 'wb')
    fp.write(content.get_payload(decode=True))
    fp.close()
    return True


def _get_files_from_email(mail, exportDir):
    files = list()
    for part in mail.walk():

        if part.get_content_maintype() == 'multipart':
            continue

        if part.get('Content-Disposition') is None:
            continue

        fileName = part.get_filename()

        if fileName:
            filePath = _get_destination_file_path(exportDir, fileName)
            _write_file(filePath)
            files.append(filePath)

    return files


def download_files(conn, emails, path, credentials_json_file):
    """after the '_search_inbox', execute this to get the files"""
    allFiles = list()
    for msgId in emails[0].split():
        typ, messageParts = conn.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print('Error fetching mail.')
            raise
        emailBody = messageParts[0][1]
        mail = emailParser.message_from_string(emailBody)
        emailFiles = _get_files_from_email(mail, path)
        driveFiles = google_drive.download_files(mail, path, credentials_json_file)
        allFiles.append(list(set(emailFiles + driveFiles)))

    return allFiles


def login(email, password, imap):
    imapSession = imaplib.IMAP4_SSL(imap)
    typ, accountDetails = imapSession.login(email, password)
    if typ != 'OK':
        print('Not able to sign in!')
    print('successfull signed in!')
    return imapSession
