import pandas as pd
import json


def _get_columns_dict(filePath):
    return json.loads(open(filePath, 'r').read())


def generate_csv(filePath, dictPath, outPath):
    df = pd.read_excel(filePath)
    columnsDict = _get_columns_dict(dictPath)
    df_renamed = df.rename(columns=columnsDict)
    df_renamed.to_csv(outPath, header=False, index=False, index_label=None, encoding='utf-8', sep=";", quoting=True)
