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

def save_process_numbers(stuff, strip, p1, p2, to_file):
    with open(to_file, 'w') as outlet:
        outlet.write("id\tf\tp\n")
        for i, it in enumerate(stuff):
            if i+1 <= p1:
                outlet.write('{0}\t{1}\tp1\n'.format(it, strip))
            elif i+1 <= p2:
                outlet.write('{0}\t{1}\tp2\n'.format(it, strip))

if __name__ == '__main__':
    from_file = sys.argv[1]
    strip = sys.argv[2]
    p1_limit = int(sys.argv[3])
    p2_limit = int(sys.argv[4])
    to_file = sys.argv[5]
    process_numbers = extract_process_numbers(from_file)
    save_process_numbers(process_numbers, strip, p1_limit, p2_limit, to_file)
