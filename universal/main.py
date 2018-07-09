import subprocess
import os
import os.path
import sys

def pdf2txt(pdf):
    txt = pdf.replace('pdf', 'txt')
    house_config = 'src/pdf2txt/house.yml'
    config = '''
---
build:
  local: true
  commands:
  - node main.js {0} {1}
'''.format(pdf, txt)
    with open(house_config, 'w') as fp:
        fp.write(config)
    subprocess.call(['house', 'build', 'pdf2txt'])
    os.remove(house_config)
    return txt

def txt2csv(txt):
    csv = txt.replace('txt', 'csv')
    house_config = 'src/txt2csv/house.yml'
    config = '''
---
build:
  local: true
  commands:
  - python main.py {0} {1}
'''.format(txt, csv)
    with open(house_config, 'w') as fp:
        fp.write(config)
    subprocess.call(['house', 'build', 'txt2csv'])
    os.remove(house_config)
    return csv

def cat_csv(all_csv, to_file):
    processes = []
    for csv in all_csv:
        print(csv)
        with open(csv, 'r') as inlet:
            for line in inlet:
                processes.append(line)
        os.remove(csv)
    with open(to_file, 'w') as outlet:
        for process in processes:
            outlet.write(process)

def db2id(excel_file, process_file, to_file):
    house_config = 'src/xls2id/house.yml'
    config = '''
---
build:
  local: true
  commands:
  - python main.py {0} {1} {2}
'''.format(excel_file, process_file, to_file)
    with open(house_config, 'w') as fp:
        fp.write(config)
    subprocess.call(['house', 'build', 'xls2id'])
    os.remove(house_config)

if __name__ == '__main__':
    where = sys.argv[1]
    pwd = os.path.dirname(os.path.realpath(__file__))
    process_file = where + '/process.csv'
    database = where + '/14-2013.xls'
    ids = where + '/ids.txt'

    # Extracting process numbers
    all_pdf = ["{0}/{1}".format(where, f) for f in os.listdir(where) if (os.path.isfile(os.path.join(where, f)) and (".pdf" in f))]
    all_csv = []
    for pdf in all_pdf:
        print(pdf)
        txt = pdf2txt(pdf)
        csv = txt2csv(txt)
        all_csv.append(csv)
        os.remove(txt)
    cat_csv(all_csv, process_file)

    # Turning process numbers into individual identifications
    print(process_file)
    db2id(database, process_file, ids)
    print(ids)
