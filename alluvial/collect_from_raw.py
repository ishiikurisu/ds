import sys
import excel
import flow

def get_all_valid_ids(config):
    """Stores in memory a list with ids based on the configuration."""
    ids = {}
    years = config['years']
    src = config['working']
    valid_program = config['program']

    for year in years:
        print('Getting ids from {0}'.format(year))
        excelname = config['years'][year]
        current_ids = excel.get_ids_from_program(src + excelname, valid_program)
        for current_id in current_ids:
            if current_id not in ids:
                ids[current_id] = set()
            ids[current_id].add(year)

    return ids

def save_all_valid_ids(config, valid_ids):
    csvname = config['working'] + 'valid.csv'
    years = config['years']

    with open(csvname, 'w') as fp:
        fp.write('id;' + ';'.join(years) + '\n')
        for valid_id in valid_ids:
            p = valid_ids[valid_id] # of participation
            fp.write('{0};{1}\n'.format(valid_id,
                                        ';'.join(map(lambda y: '1' if y in p else ' ',
                                                     years))))

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    valid_ids = get_all_valid_ids(config)
    save_all_valid_ids(config, valid_ids)
