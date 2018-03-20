import pandas as pd

#############
# UTILITIES #
#############

def get_ids(excelname):
    """Gets all ids from a structured excel file."""
    ids = []
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        ids.append(sheet.iat[row, 7])

    return ids

def relate_coordinations_and_processes(config):
    """
    Loads all process ids from all years in configuration files and relate them to the
    coordination they belong to. Returns a dictionary.
    """
    outlet = {}
    src = config['working']
    years = config['years']

    for year in years:
        excelname = src + years[year]
        sheet = pd.read_excel(excelname, skiprows=range(3))
        # column 0 contains the process number
        # column 14 contains the coordination
        for row in range(1, sheet.shape[0]):
            process = sheet.iat[row, 0].replace('/', '').replace('-', '')
            coordination = sheet.iat[row, 14]
            outlet[process] = coordination

    return outlet

###############
# VALIDATIONS #
###############

def validate_by_situation(sheet, row):
    """Validate the current candidate by analyzing their descriptive situation."""
    # column 0 contains the situation's code
    # column 1 contains the situation's description
    # column 12 contains the program which the researcher belongs to
    # column 31 contains the coordination
    outlet = False
    situation = sheet.iat[row, 0]
    if (situation == '51') or (situation == '11'):
        coordination = sheet.iat[row, 31]
        if type(coordination) is str:
            outlet = True
    return outlet

def validate_by_program(sheet, row, program='nan'):
    """
    Validates the current candidate by analyzing their process result and their program.
    """
    result = str(sheet.iat[row, 4])
    current_program = str(sheet.iat[row, 12])
    outlet = False

    if (result == 'FV') and (program == current_program):
        outlet = True
    elif (result == 'FV') and (program == 'IGNORE'):
        outlet = True

    return outlet

def validate_by_result(sheet, row):
    """Validates the current candidate by analyzing their process result."""
    return str(sheet.iat[row, 4]) == 'FV'

###############
# EXCEL LOOPS #
###############

def get_coordinations(excelname):
    """
    Relates all given ids to a coordination in the given excel sheet given the
    id has a valid scholarship. Returns a dictionary relating the id and their
    coordination (or None lest an invalid state).
    """
    coordinations = {}
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        current_id = sheet.iat[row, 7]
        if validate_by_situation(sheet, row) and (type(current_id) is str):
            coordination = sheet.iat[row, 31]
            coordinations[current_id] = coordination

    return coordinations

def group_programs_by_id(excelname, program='IGNORE'):
    """Relates a id to the program it belongs to if it given as favorable."""
    programs = {}
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        current_id = sheet.iat[row, 7]
        if validate_by_program(sheet, row, program) and (type(current_id) is str):
            programs[current_id] = sheet.iat[row, 12]

    return programs

def group_coordinations_by_id(excelname):
    """Relates a id to the coordination it belongs to if it given as favorable."""
    coordinations = {}
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        current_id = sheet.iat[row, 7]
        if validate_by_result(sheet, row) and (type(current_id) is str):
            coordinations[current_id] = sheet.iat[row, 13]

    return coordinations

def get_ids_from_program(excelname, program):
    """Get all approved ids from a given program."""
    ids = set()
    sheet = pd.read_excel(excelname)

    for row in range(4, sheet.shape[0]):
        if validate_by_program(sheet, row, program):
            current_id = sheet.iat[row, 7]
            ids.add(current_id)

    return ids

############
# PAYCHECK #
############

def extract_periods_from_paycheck(excelname, years):
    """
    Extracts the ids and the valid periods from the paycheck. Requires the path to the excel
    spreadsheet with the desired information and the relevant years for study. Returns a hashmap
    where each key is an id and each value is a dictionary relating every valid year with a
    process identification
    """
    # column 0 contains process ids
    # column 2 contains ids
    # column 6 contains period beginning
    # column 7 contains period ending
    outlet = {}
    sheet = pd.read_excel(excelname)
    limit = sheet.shape[0]
    first_valid_year = years[0]
    last_valid_year = years[-1]

    for row in range(0, limit):
        process_id = sheet.iat[row, 0]
        person_id = str(sheet.iat[row, 2])
        beginning = sheet.iat[row, 6].year
        ending = sheet.iat[row, 7].year
        if (beginning >= first_valid_year) and (beginning <= last_valid_year):
            if len(person_id) < 11:
                person_id = ('0'*(11-len(person_id))) + person_id
            if person_id not in outlet.keys():
                outlet[person_id] = {}
            if beginning == ending:
                outlet[person_id][beginning] = process_id
            else:
                for year in range(beginning, ending):
                    outlet[person_id][year] = process_id

    return outlet
