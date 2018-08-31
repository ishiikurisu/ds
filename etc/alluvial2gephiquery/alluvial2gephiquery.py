import sys

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # getting ids
    ids = []
    with open(input_file, 'r', encoding='utf-8') as fp:
        first_line = True
        for line in fp:
            fields = line.strip('\n').split('\t')
            if first_line:
                first_line = False
            else:
                ids.append(fields[0].strip("'"))

    # storing ids
    with open(output_file, 'w') as fp:
        fp.write('cpf:{0};\n'.format(','.join(ids)))
