import subprocess
import os
import os.path
import sys
import json
import util

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

def txt2csv(txt, strip, cats):
    csv = txt.replace('txt', 'csv')
    house_config = 'src/txt2csv/house.yml'
    config = '''
---
build:
  local: true
  commands:
  - python main.py {0} {1} {2} {3} {4}
'''.format(txt, strip, cats[0], cats[1], csv)
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
        csv = txt2csv(txt, strip['name'], strip['categories'])
        all_csv.append(csv)
        os.remove(txt)

    # Turning process numbers into individual identifications
    print(process_file)
    cat_csv(all_csv, process_file)
    print(ids)
    db2id(database, process_file, ids)
