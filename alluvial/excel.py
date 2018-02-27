import pandas as pd

def get_ids(excelname):
    """Gets all ids from a structured excel file."""
    ids = []
    sheet = pd.read_excel(excelname)

    for row in range(3, sheet.shape[0]):
        ids.append(sheet.iat[row, 7])

    return ids
