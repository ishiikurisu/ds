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
        try:
            if debug: print('--- # {0}'.format(cv))
            root = xml.etree.ElementTree.parse(cv).getroot()
            producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
            artigos_publicados = producao_bibliografica.find('ARTIGOS-PUBLICADOS')
            todos_artigos = artigos_publicados.findall('ARTIGO-PUBLICADO')
            for artigo_publicado in todos_artigos:
                dados_basicos = artigo_publicado.find('DADOS-BASICOS-DO-ARTIGO')
                ano = int(dados_basicos.get('ANO-DO-ARTIGO'))
                palavras_chave = artigo_publicado.find('PALAVRAS-CHAVE')
                for key in palavras_chave.attrib:
                    value = palavras_chave.attrib[key]
                    keywords = map(lambda k: k.strip(), value.upper().split(';'))
                    for keyword in keywords:
                        if len(keyword) > 0:
                            if keyword not in outlet:
                                outlet[keyword] = []
                            outlet[keyword].append(ano)
            if debug: print('ok')
        except Exception as e:
            if debug: print('Problems in {0}: {1}'.format(cv, e))

    return outlet

def save_keywords_by_year(where, what):
    years = list(range(2000, 2019))
    with open(where + 'processed.csv', 'w') as fp:
        fp.write('keyword\t{0}\n'.format('\t'.join(map(str, years))))
        for keyword in what:
            appears = what[keyword]
            outlet = [len([a for a in appears if a == y]) for y in years]
            fp.write('{0}\t{1}\n'.format(keyword, '\t'.join([str(it) for it in outlet])))

if __name__ == '__main__':
    type = 'ARTIGOS-PUBLICADOS'
    config = util.load_config(sys.argv[1])
    cv_folder = config['working'] + config['cv dir']
    all_cv = get_all_cv_from(cv_folder)
    keywords_by_pubs = get_keywords_from_all_cv(all_cv)
    save_keywords_by_year(cv_folder, keywords_by_pubs)
