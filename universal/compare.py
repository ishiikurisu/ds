import sys
import util

def parse_class_by_cv(table):
    return { it[0]: it[1] for it in zip([it + '.xml' for it in table['Id']], table['modularity_class']) }

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    classes = config['classes']
    classes_table = util.load_csv(config['pwd'] + config['classes file'])
    areas_table = util.load_csv(config['pwd'] + 'cv.csv')
    class_by_cv = parse_class_by_cv(classes_table)
    # TODO include class column on area table
    # TODO save new areas table
