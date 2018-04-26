import sys
import util
import get_relevant_keywords as grk

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    keywords = config['keywords']
    from_file = grk.get_output(config)
    to_file = config['working'] + config['cv dir'] + 'keywords_filtered.csv'
    with open(from_file, 'r', encoding='utf-8') as inlet:
        with open(to_file, 'w', encoding='utf-8') as outlet:
            first_line = True
            for line in inlet:
                flag = False
                if first_line:
                    flag = True
                    first_line = False
                keyword = line.strip().split('\t')[0]
                if keyword in keywords:
                    flag = True
                if flag:
                    outlet.write(line)
