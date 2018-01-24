import json
import research

if __name__ == '__main__':
    config = { }
    with open('config.json', 'r') as fp:
        config = json.loads(fp.read())
    researcher = research.Researcher(config['quantity'])
    researcher.debug = True
    researcher.study_from(config['start'])
