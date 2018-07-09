import sys
import pandas as pd

def remove_duplicates(l):
    o = []
    for i in l:
        if i not in o:
            o.append(i)
    return o

def load_processes(process_file):
    outlet = list()
    with open(process_file, 'r') as fp:
        first_line = True
        for line in fp:
            if first_line:
                first_line = False
            else:
                outlet.append(line.strip().split('\t'))
    return outlet

def save_ids(ids, output_file):
    with open(output_file, 'w') as outlet:
        outlet.write('cpf:')
        for cid in ids:
            outlet.write('{0},'.format(cid))
        outlet.write('\n')

def save_stuff(ps, output_file):
    with open(output_file, 'w') as outlet:
        outlet.write('p\tf\tc\tid\n')
        for p in ps:
            p = remove_duplicates(p)
            if len(p) < 4:
                p.append(-1)
            elif len(p) > 4:
                p[3] = 1
            outlet.write('{0}\t{1}\t{2}\t{3}\n'.format(p[0], p[1], p[2], p[3]))

def load_relevant_ids(xls, all):
    '''
    Extracts the ids that are related to one the processes `ps` saved in that
    excel file `xls`.
    '''
    df = pd.read_excel(xls)
    ps = [p[0] for p in all]
    try:
        y = 0
        while True:
            if df.iat[y, 0] in ps:
                id = df.iat[y, 8]
                i = ps.index(df.iat[y, 0])
                all[i].append(id)
            y += 1
    except IndexError:
        pass
    return all

def extract_ids(stuff):
    return [it[3] for it in stuff if len(it) >= 4]

if __name__ == '__main__':
    excel_file = sys.argv[1]
    process_file = sys.argv[2]
    output_file = sys.argv[3]

    processes = load_relevant_ids(excel_file, load_processes(process_file))
    save_stuff(processes, process_file)
    save_ids(extract_ids(processes), output_file)
