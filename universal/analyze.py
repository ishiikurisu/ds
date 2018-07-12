# -*- coding: cp1252 -*-
import util
import sys
import os
import os.path
import xml.etree.ElementTree

def get_all_cv(config):
    p = config['pwd'] + config['cv']
    all = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
    all_cv = [p+f for f in all if '.xml' in f]
    return all_cv

def get_fields(cv):
    outlet = []

    root = None
    try:
        root = xml.etree.ElementTree.parse(cv).getroot()
    except Exception as e:
        print('{0}: {1}'.format(cv, e))
        return None

    # TODO Decide which fields to extract
    return outlet


if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    all_cv = get_all_cv(config)
    stuff = {}
    for cv in all_cv:
        fields = get_fields(cv)
        if fields is not None:
            stuff[cv] = fields
    # TODO relate all researchers to all fields
