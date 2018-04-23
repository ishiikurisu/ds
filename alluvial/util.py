import pandas as pd
import json

#############
# UTILITIES #
#############

def load_config(where):
    """Loads the configuration file."""
    config = None
    with open(where, 'r', encoding='utf-8') as fp:
        config = json.loads(fp.read())
    return config

def fix_id(inlet):
    """
    Fix a id in number format to a valid string.
    """
    outlet = str(inlet)
    return ('0'*(11-len(outlet))) + outlet
