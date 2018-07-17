import util
import sys
import house

def extract_cv_data(json_config):
    h = house.House('cv-extraction')
    h.local = True
    h.add_command('{0} main.py {1}'.format(util.get_python(), json_config))
    h.build()
    return util.load_config(json_config)['pwd'] + 'cv.csv'

def analyze_similarity(cv_data):
    h = house.House('similarity')
    h.local = True
    h.add_command('{0} main.py {1} dd'.format(util.get_python(), cv_data))
    h.build()
    return cv_data.replace('cv.csv', 'cv_dd.csv')

if __name__ == '__main__':
    config = sys.argv[1]
    cv_data = extract_cv_data(config)
    cv_dd = analyze_similarity(cv_data)
    print(cv_dd)
