# -*- coding: cp1252 -*-
import sys
import util
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree

def get_all_cv_from(cv_dir):
    return [cv_dir + f for f in listdir(cv_dir) if isfile(join(cv_dir, f))]

def get_keywords_from_all_cv(all_cv, debug=False):
    outlet = {}

    for cv in all_cv:
        if debug: print('--- # {0}'.format(cv))
        root = None
        try:
            root = xml.etree.ElementTree.parse(cv).getroot()
        except Exception as e:
            print('Problems with {0}: {1}'.format(cv, e))
            continue
        producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
        if producao_bibliografica is not None:
            artigos_publicados = producao_bibliografica.find('ARTIGOS-PUBLICADOS')
            todos_artigos = artigos_publicados.findall('ARTIGO-PUBLICADO')
            if todos_artigos is not None:
                for artigo_publicado in todos_artigos:
                    dados_basicos = artigo_publicado.find('DADOS-BASICOS-DO-ARTIGO')
                    try:
                        ano = int(dados_basicos.get('ANO-DO-ARTIGO'))
                        palavras_chave = artigo_publicado.find('PALAVRAS-CHAVE')
                        if palavras_chave is not None:
                            for key in palavras_chave.attrib:
                                value = palavras_chave.attrib[key]
                                keywords = map(lambda k: k.strip(), value.upper().split(';'))
                                for keyword in keywords:
                                    if len(keyword) > 0:
                                        if keyword not in outlet:
                                            outlet[keyword] = []
                                        outlet[keyword].append(ano)
                        else:
                            print('Problems with {0}: no keywords'.format(cv))
                    except ValueError:
                        print('Problems with {0}: invalid year'.format(cv))
            else:
                print('Problems with {0}: no published articles'.format(cv))
        else:
            print('Problems with {0}: no bibliographic production'.format(cv))

    return outlet

def save_keywords_by_year_for_alluvial(where, what):
    years = list(range(2000, 2019))
    with open(where + 'processed.csv', 'w') as fp:
        fp.write('keyword\t{0}\n'.format('\t'.join(map(str, years))))
        for keyword in what:
            appears = what[keyword]
            outlet = [len([a for a in appears if a == y]) for y in years]
            fp.write('{0}\t{1}\n'.format(keyword, '\t'.join([str(it) for it in outlet])))

def save_keywords_by_year_for_bump(where, what):
    years = list(range(2000, 2019))
    with open(where + 'processed.csv', 'w') as fp:
        fp.write('keyword\tyear\tquantity\n'.format('\t'.join(map(str, years))))
        for keyword in what:
            appears = { y: len([a for a in what[keyword] if a == y]) for y in years }
            for year in years:
                fp.write('{0}\t{1}\t{2}\n'.format(keyword,
                                                  str(year),
                                                  str(appears[year])))

if __name__ == '__main__':
    type = 'ARTIGOS-PUBLICADOS'
    config = util.load_config(sys.argv[1])
    cv_folder = config['working'] + config['cv dir']
    all_cv = get_all_cv_from(cv_folder)
    keywords_by_pubs = get_keywords_from_all_cv(all_cv, debug=True)
    save_keywords_by_year_for_bump(cv_folder, keywords_by_pubs)
