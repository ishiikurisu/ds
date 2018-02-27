import sys
import json
import excel

def load_config(where):
    """Loads the configuration file."""
    config = None
    with open(where, 'r') as fp:
        config = json.loads(fp.read())
    return config

def get_all_ids(config):
    """Stores in memory a list with ids based on the configuration."""
    ids = set()
    years = config['years']
    src = config['working']

    print('# Getting all ids')
    for year in years:
        print('Getting ids from {0}'.format(year))
        excelname = config['years'][year]
        current_ids = excel.get_ids(src + excelname)
        for current_id in current_ids:
            ids.add(current_id)

    return ids

def save_all_ids(ids, config):
    csvname = config['working'] + 'ids.csv'
    content = ''.join(map(lambda s: '{0}\n'.format(s), ids))
    with open(csvname, 'w') as fp:
        fp.write(content)
    return csvname

def extract_coordinations(config, ids):
    coordinations = {}
    years = config['years']
    src = config['working']

    print('# Getting all coordinations')
    for year in years:
        print('Getting coordinations from {0}'.format(year))
        excelname = config['years'][year]
        current_coordinations = excel.get_coordinations(ids, src + excelname)
        coordinations[year] = current_coordinations

    return coordinations

def consolidate_coordinations(config, ids, coordinations):
    years = config['years']
    src = config['working']
    output = src + 'output.csv'

    print('# Consolidating data')
    with open(output, 'w') as fp:
        # Writting header
        line = 'ids;' + ';'.join(years) + '\n'
        fp.write(line)

        # Writting remaing lines
        for current_id in ids:
            line = '{0}'.format(current_id)
            for year in years:
                coordination = 'nope'
                if current_id in coordinations[year]:
                    coordination = coordinations[year][current_id]
                line += ';{0}'.format(coordination)
            fp.write(line + '\n')


if __name__ == '__main__':
    config = load_config(sys.argv[1])
    ids = get_all_ids(config)
    save_all_ids(ids, config)
    coordinations = extract_coordinations(config, ids)
    consolidate_coordinations(config, ids, coordinations)
