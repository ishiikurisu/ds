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

def save_all_valid_ids(config, valid_ids):
    csvname = config['working'] + 'valid.csv'
    with open(csvname, 'w') as fp:
        for valid_id in valid_ids:
            fp.write('{0};\n'.format(valid_id))

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    valid_ids = get_all_valid_ids(config)
    save_all_valid_ids(config, valid_ids)
