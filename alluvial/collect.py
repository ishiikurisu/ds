import sys
import excel
import flow

def get_all_valid_ids(config):
    """Stores in memory a list with ids based on the configuration."""
    ids = set()
    years = config['years']
    src = config['working']
    valid_program = config['program']

    for year in years:
        print('Getting ids from {0}'.format(year))
        excelname = config['years'][year]
        current_ids = excel.get_ids_from_program(src + excelname, valid_program)
        # IDEA List these ids by year when saving
        ids |= current_ids

    return ids

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    valid_ids = get_all_valid_ids(config)
    # TODO Save valid ids in file
    print(valid_ids)
