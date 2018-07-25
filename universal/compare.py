import sys
import util

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    classes = config['classes']
    table = util.load_csv(config['pwd'] + config['classes file'])
    # TODO Group people by classes
    # TODO Indicate most common knowledge area by class
