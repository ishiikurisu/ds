import os.path
import sys
import json
import util
import txt2csv
import xls2id
import subprocess
import os

def pdf2txt(pdf):
    os.chdir('pdf2txt')
    txt = pdf.replace('pdf', 'txt')
    subprocess.run(['node', 'main.js', pdf, txt])
    os.chdir('..')
    return txt

def txt_to_csv(txt, strip, cats):
    csv = txt.replace('.txt', '.csv')
    from_file = txt
    strip = strip
    p1_limit = cats[0]
    p2_limit = cats[1]
    to_file = csv
    process_numbers = txt2csv.extract_process_numbers(from_file)
    txt2csv.save_process_numbers(process_numbers, strip, p1_limit, p2_limit, to_file)
    return csv

def cat_csv(all_csv, to_file):
    processes = []
    for csv in all_csv:
        print(csv)
        with open(csv, 'r') as inlet:
            first_line = True
            for line in inlet:
                if first_line:
                    first_line = False
                else:
                    processes.append(line)
        os.remove(csv)
    with open(to_file, 'w') as outlet:
        outlet.write('id\tf\tp\n')
        for process in processes:
            outlet.write(process)

def db_to_id(excel_file, process_file, output_file):
    processes = xls2id.load_relevant_ids(excel_file, xls2id.load_processes(process_file))
    xls2id.save_stuff(processes, process_file)
    xls2id.save_ids(xls2id.extract_ids(processes), output_file)


if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    where = config['pwd']
    process_file = where + config['process']
    database = where + config['database']
    ids = where + config['ids']

    # Extracting process numbers
    all_csv = []
    for strip in config['strips']:
        pdf = where + strip['src']
        print(pdf)
        txt = pdf2txt(pdf)
        csv = txt_to_csv(txt, strip['name'], strip['categories'])
        all_csv.append(csv)
        os.remove(txt)

    # Turning process numbers into individual identifications
    print(process_file)
    cat_csv(all_csv, process_file)
    print(ids)
    db_to_id(database, process_file, ids)
