import util
import collect_from_source as cfs
import get_keywords as gk
from flask import Flask
import xml.etree.ElementTree

def setup(config_file=None):
    global flows_by_names
    global cv_by_name

    if config_file is None:
        config_file = input()
    config = util.load_config(config_file)

    # Getting flows
    flows_by_names = {}
    with open(cfs.get_output(config), 'r', encoding='utf-8') as fp:
        first_line = True
        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                first_line = False
            else:
                flows_by_names[stuff[1]] = stuff[2:]

    # Getting cv
    cv_by_name = {}
    all_cv = gk.get_all_cv_files(config)
    for cv in all_cv:
        root = None
        try:
            root = xml.etree.ElementTree.parse(cv).getroot()
        except Exception as e:
            continue
        dados_gerais = root.getchildren()[0]
        name = dados_gerais.get('NOME-COMPLETO')
        cv_by_name[name] = cv


def get_flow_by_name(name):
    global flows_by_names
    return flows_by_names.get(name)

def get_cv_by_name(name):
    global cv_by_name
    return cv_by_name.get(name)

# Flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
