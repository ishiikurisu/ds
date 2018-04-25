import util
import collect_from_source as cfs
from flask import Flask

# Data setup
config = util.load_config(input())
flows_by_names = {}
with open(cfs.get_output(config), 'r', encoding='utf-8') as fp:
    first_line = True
    for line in fp:
        stuff = line.strip().split('\t')
        if first_line:
            first_line = False
        else:
            flows_by_names[stuff[1]] = stuff[2:]

def get_flow_by_name(name):
    global flows_by_names
    return flows_by_names.get(name)

# App setup
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
