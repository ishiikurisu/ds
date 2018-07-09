import sys
import re

def extract_process_numbers(from_file):
    outlet = []
    regex = re.compile(r'[Rr]ecomendada')
    with open(from_file, 'r', encoding='utf-8') as inlet:
        for line in inlet:
            if regex.search(line) is not None:
                parts = regex.split(line)
                maybe = parts[1][0:13]
                if len(maybe) == 13:
                    outlet.append(maybe)
    return outlet

def save_process_numbers(stuff, to_file):
    with open(to_file, 'w') as outlet:
        for it in stuff:
            outlet.write('{0}\n'.format(it))

if __name__ == '__main__':
    from_file = sys.argv[1]
    to_file = sys.argv[2]

    process_numbers = extract_process_numbers(from_file)
    save_process_numbers(process_numbers, to_file)
