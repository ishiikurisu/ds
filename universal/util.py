import os
import json

def load_config(where):
    """Loads the configuration file."""
    config = None
    with open(where, 'r', encoding='utf-8') as fp:
        config = json.loads(fp.read())
    return config

def get_python():
    return 'python3' if os.name == 'posix' else 'python'

def load_csv(filename, encoding='utf-8'):
    table = {}
    with open(filename, 'r', encoding=encoding) as fp:
        first_line = True
        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                fields = stuff
                first_line = False
            else:
                for i, field in enumerate(fields):
                    if field not in table:
                        table[field] = []
                    table[field].append(stuff[i])
    return table
