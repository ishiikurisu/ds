import sys

def get_ids_from_file(from_file):
    cpfs = []

    with open(from_file, 'r') as fp:
        first_line = True
        for line in fp:
            if first_line:
                first_line = False
            else:
                cpf = line.strip().split('\t')[0].strip('\'')
                cpfs.append(cpf)

    return cpfs

def save_ids_for_query(to_file, cpfs):
    with open(to_file, 'w') as fp:
        fp.write('cpf:{0}\n'.format(','.join(cpfs)))

if __name__ == '__main__':
    from_file = sys.argv[1]
    to_file = sys.argv[2]
    save_ids_for_query(to_file, get_ids_from_file(from_file))
