import util
import sys
import house

def extract_cv_data(json_config):
    h = house.House('cv-extraction')
    h.local = True
    h.add_command('{0} main.py {1}'.format(util.get_python(), json_config))
    h.build()
    return json_config

if __name__ == '__main__':
    config = sys.argv[1]
    extract_cv_data(config)
    # TODO Perform similarity analysis
