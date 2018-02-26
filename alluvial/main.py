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

    for year in years:
        print('Getting ids from {0}'.format(year))
        excelname = config['years'][year]
        currentIds = excel.get_ids(src + excelname)

    return ids

if __name__ == '__main__':
    config = load_config(sys.argv[1])
    ids = get_all_ids(config)
    print(ids)
