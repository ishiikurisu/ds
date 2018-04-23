# -*- coding: cp1252 -*-
import sys
import util

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    cv_folder = config['working'] + config['cv dir']
    keywords = config['keywords']
    from_file = cv_folder + 'processed.csv'
    to_file = cv_folder + 'processed_filtered.csv'

    with open(from_file, 'r') as inlet:
        with open(to_file, 'w') as outlet:
            first_line = True
            for line in inlet:
                flag = False
                if first_line:
                    flag = True
                    first_line = False
                else:
                    target = line.split('\t')[0]
                    if target in keywords:
                        flag = True
                if flag: outlet.write(line)
