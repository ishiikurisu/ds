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
