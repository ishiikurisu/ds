import flask

# main objects
app = flask.Flask(__name__)
# TODO Implement this thing
coordinations_by_process = {'123': 'it works!'}

# app routings
@app.route("/")
def home():
    return 'Hello! What do you want to do today?'

@app.route("/consult/<process>")
def consult(process):
    outlet = 'give me a valid process number, please!'

    if process in coordinations_by_process:
        outlet = coordinations_by_process[process]

    return outlet
