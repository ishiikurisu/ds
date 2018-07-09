import sys
import pandas as pd

def load_processes(process_file):
    outlet = set()
    with open(process_file, 'r') as fp:
        for line in fp:
            outlet.add(line.strip())
    return outlet

def save_ids(ids, output_file):
    with open(output_file, 'w') as outlet:
        outlet.write('cpf:')
        for cid in ids:
            outlet.write('{0},'.format(cid))
        outlet.write('\n')

def load_relevant_ids(xls, ps):
    '''
    Extracts the ids that are related to one the processes `ps` saved in that
    excel file `xls`.
    '''
    out = []
    df = pd.read_excel(xls)
    try:
        y = 0
        while True:
            if df.iat[y, 0] in ps:
                out.append(df.iat[y, 8])
            y += 1
    except IndexError:
        pass

    return out

if __name__ == '__main__':
    excel_file = sys.argv[1]
    process_file = sys.argv[2]
    output_file = sys.argv[3]

    processes = load_processes(process_file)
    ids = load_relevant_ids(excel_file, processes)
    save_ids(ids, output_file)
