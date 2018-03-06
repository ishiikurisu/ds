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

def extract_groups(config, operation=excel.group_coordinations_by_id):
    groups = {}
    years = config['years']
    src = config['working']
    ids = set()

    print('# Getting all groups for each id')
    for year in years:
        print('Getting programs from {0}'.format(year))
        excelname = config['years'][year]
        current_groups = operation(src + excelname)
        groups[year] = current_groups
        for current_id in current_groups:
            ids.add(current_id)

    return ids, groups

def consolidate_groups(config, ids, groups):
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
                group = ''
                if current_id in groups[year]:
                    group = groups[year][current_id]
                line += ';{0}'.format(group)
            fp.write(line + '\n')
        print('{0} ids written'.format(len(ids)))


if __name__ == '__main__':
    config = load_config(sys.argv[1])
    ids, groups = extract_groups(config)
    consolidate_groups(config, ids, groups)
