import util
import sys
import os
import os.path

def get_all_cv(config):
    p = config['pwd'] + config['cv']
    all = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
    all_cv = [f for f in all if '.xml' in f]
    return all_cv

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    all_cv = get_all_cv(config)
    print(all_cv)
    # TODO parse each cv
