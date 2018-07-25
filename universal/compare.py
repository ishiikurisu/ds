import sys
import util

def parse_class_by_cv(table):
    return { it[0]: it[1] for it in zip([it + '.xml' for it in table['Id']], table['modularity_class']) }

def include_class_by_cv(areas_table, class_by_cv):
    limit = max([len(areas_table[key]) for key in areas_table])
    areas_table['class'] = ['-1'] * limit
    cvs = areas_table['cv']
    for cv in class_by_cv:
        areas_table['class'][cvs.index(cv)] = class_by_cv[cv]
    return areas_table

def save_table(table, where):
    limit = max([len(table[key]) for key in table])
    columns = list(table.keys())
    with open(where, 'w') as fp:
        fp.write('%s\n' % '\t'.join(columns))
        for i in range(limit):
            stuff = []
            for column in columns:
                stuff.append(table[column][i])
            fp.write('%s\n' % ('\t'.join(stuff)))

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    classes = config['classes']
    classes_table = util.load_csv(config['pwd'] + config['classes file'])
    areas_table = util.load_csv(config['pwd'] + 'cv.csv')
    class_by_cv = parse_class_by_cv(classes_table)
    areas_table = include_class_by_cv(areas_table, class_by_cv)
    save_table(areas_table, config['pwd'] + 'cv-class.csv')
