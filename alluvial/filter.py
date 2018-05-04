import sys
import util

def filter_lines(condition, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as inlet:
        with open(output_file, 'w', encoding='utf-8') as outlet:
            first_line = True
            for line in inlet:
                if first_line:
                    outlet.write(line)
                    first_line = False
                else:
                    if condition(line):
                        outlet.write(line)


if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    input_file = sys.argv[2]
    program_code = config['program code']
    extension = '_filtered_{0}.csv'.format(program_code)
    output_file = input_file.replace('.csv', extension)
    condition = lambda line: program_code in line.strip().split('\t')
    filter_lines(condition, input_file, output_file)
