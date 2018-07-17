import util
import sys
import subprocess
import os

def extract_cv_data(json_config):
    house_config = 'src/cv-extraction/house.yml'
    config = '''
---
build:
  local: true
  commands:
  - {0} main.py {1}
'''.format(util.get_python(), json_config)
    with open(house_config, 'w') as fp:
        fp.write(config)
    subprocess.call(['house', 'build', 'cv-extraction'])
    os.remove(house_config)
    return json_config

if __name__ == '__main__':
    config = sys.argv[1]
    extract_cv_data(config)
    # TODO Perform similarity analysis
