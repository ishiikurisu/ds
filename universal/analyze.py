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

def get_fields_from_phd(cv):
    outlet = []

    root = None
    try:
        root = xml.etree.ElementTree.parse(cv).getroot()
    except Exception as e:
        print('{0}: {1}'.format(cv, e))
        return None

    formacao = root.getchildren()[0].find('FORMACAO-ACADEMICA-TITULACAO')
    if formacao is not None:
        doutorado = formacao.find('DOUTORADO')
        if doutorado is not None:
            areas_do_conhecimento = doutorado.find('AREAS-DO-CONHECIMENTO')
            if areas_do_conhecimento is not None:
                areas_do_conhecimento = areas_do_conhecimento.getchildren()
                for area_do_conhecimento in areas_do_conhecimento:
                    area = area_do_conhecimento.attrib.get('NOME-GRANDE-AREA-DO-CONHECIMENTO')
                    if area is not None:
                        outlet.append(area)
                    area = area_do_conhecimento.attrib.get('NOME-AREA-DO-CONHECIMENTO')
                    if area is not None:
                        outlet.append(area)

    if len(outlet) == 0:
        outlet = None
    return outlet


if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    all_cv = get_all_cv(config)
    stuff = {}
    invalid = []
    for cv in all_cv:
        fields = get_fields_from_phd(cv)
        if fields is not None:
            stuff[cv] = fields
        else:
            invalid.append(cv)

    print(stuff)
    for cv in invalid:
        print(cv + 'is invalid')
    print('invalid: ' + str(len(invalid)) + '/' + str(len(all_cv)))
    # TODO relate all researchers to all fields
