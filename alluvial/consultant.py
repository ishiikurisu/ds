import os
import flask
import flow
import excel

# main objects
config = flow.load_config(os.environ['WHERE'])
coordinations_by_process = excel.relate_coordinations_and_processes(config)
app = flask.Flask(__name__)

# app routings
@app.route("/")
def home():
    return 'Hello! What do you want to do today?'

@app.route("/health")
def health():
    return 'ok'

@app.route("/consult/<process>")
def consult(process):
    outlet = 'give me a valid process number, please!'

    if process in coordinations_by_process:
        outlet = coordinations_by_process[process]

    return outlet
