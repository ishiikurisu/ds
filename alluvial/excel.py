import pandas as pd

def get_ids(excelname):
    """Gets all ids from a structured excel file."""
    ids = []
    xls = pd.ExcelFile(excelname)
    # TODO Understand spreadsheet structure
    sheet = xls.parse(xls.sheet_names[0])
    print(sheet.head)
    return ids
