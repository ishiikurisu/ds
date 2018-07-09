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

if __name__ == '__main__':
    where = sys.argv[1]
    pwd = os.path.dirname(os.path.realpath(__file__))
    all_pdf = ["{0}/{1}".format(where, f) for f in os.listdir(where) if (os.path.isfile(os.path.join(where, f)) and (".pdf" in f))]
    all_csv = []
    for pdf in all_pdf:
        print(pdf)
        txt = pdf2txt(pdf)
        csv = txt2csv(txt)
        all_csv.append(csv)
        os.remove(txt)
    # TODO cat all csv
