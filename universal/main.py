import subprocess
import os
import os.path
import sys

if __name__ == '__main__':
    where = sys.argv[1]
    pwd = os.path.dirname(os.path.realpath(__file__))
    all_pdf = ["{0}/{1}".format(where, f) for f in os.listdir(where) if (os.path.isfile(os.path.join(where, f)) and (".pdf" in f))]
    for pdf in all_pdf:
        print(pdf)
        subprocess.call(['make', '-C', './src/pdf2txt', pdf])
