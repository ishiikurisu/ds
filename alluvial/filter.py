import sys
import util

def filter_lines(condition, input_file, output_file):
    with open(input_file, 'r') as inlet:
        with open(output_file, 'w') as outlet:
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
    output_file = '.'.join(input_file.split('.')[0:-1]) + '_filtered.csv'
    condition = lambda line: program_code in line
    filter_lines(condition, input_file, output_file)
