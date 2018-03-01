import pandas as pd

def get_ids(excelname):
    """Gets all ids from a structured excel file."""
    ids = []
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        ids.append(sheet.iat[row, 7])

    return ids

def get_coordinations(ids, excelname):
    """
    Relates all given ids to a coordination in the given excel sheet given the
    id has a valid scholarship. Returns a dictionary relating the id and their
    coordination (or None lest an invalid state).
    """
    coordinations = {}
    sheet = pd.read_excel(excelname)

    # column 0 contains the situation's code
    # column 1 contains the situation's description
    # column 31 contains the coordination
    for row in range(4, sheet.shape[0]):
        current_id = sheet.iat[row, 7]
        situation = sheet.iat[row, 0]
        if (situation == '51') or (situation == '11'):
            coordination = sheet.iat[row, 31]
            if type(coordination) is str:
                coordinations[current_id] = coordination

    return coordinations

def get_ids_from_program(excelname, program):
    """Get all approved ids from a given program."""
    ids = set()
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        current_id = sheet.iat[row, 7]
        result = str(sheet.iat[row, 4])
        current_program = str(sheet.iat[row, 12])

        if (result == 'FV') and (program == current_program):
            ids.add(current_id)

    return ids
