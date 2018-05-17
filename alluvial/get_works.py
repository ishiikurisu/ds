# -*- coding: cp1252 -*-
import sys
import util
import xml.etree.ElementTree
import re

##########################
# XML PARSING PROCEDURES #
##########################

def get_complete_articles_from_cv(root, debug=False):
    count = 0

    producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
    if producao_bibliografica is not None:
        artigos_publicados = producao_bibliografica.find('ARTIGOS-PUBLICADOS')
        todos_artigos = artigos_publicados.findall('ARTIGO-PUBLICADO')
        if todos_artigos is not None:
            for artigo_publicado in todos_artigos:
                dados_basicos = artigo_publicado.find('DADOS-BASICOS-DO-ARTIGO')
                if dados_basicos.attrib['NATUREZA'] == 'COMPLETO':
                    count += 1
        else:
            if debug: print('Problems with {0}: no published articles'.format(cv))
    else:
        if debug: print('Problems with {0}: no bibliographic production'.format(cv))

    return count

def get_complete_conference_articles_from_cv(root, debug=False):
    count = 0

    producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
    if producao_bibliografica is not None:
        artigos_publicados = producao_bibliografica.find('TRABALHOS-EM-EVENTOS')
        todos_artigos = artigos_publicados.findall('TRABALHO-EM-EVENTOS')
        if todos_artigos is not None:
            for artigo_publicado in todos_artigos:
                dados_basicos = artigo_publicado.find('DADOS-BASICOS-DO-TRABALHO')
                if dados_basicos.attrib['NATUREZA'] == 'COMPLETO':
                    count += 1
        else:
            if debug: print('Problems with {0}: no published articles'.format(cv))
    else:
        if debug: print('Problems with {0}: no bibliographic production'.format(cv))

    return count

def get_book_chapters_from_cv(root, debug=False):
    count = 0

    producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
    if producao_bibliografica is not None:
        livros_e_capitulos = producao_bibliografica.find('LIVROS-E-CAPITULOS')
        if livros_e_capitulos is not None:
            coisas_publicadas = livros_e_capitulos.find('CAPITULOS-DE-LIVROS-PUBLICADOS')
            if coisas_publicadas is not None:
                todos_capitulos = coisas_publicadas.findall('CAPITULO-DE-LIVRO-PUBLICADO')
                count += len(todos_capitulos)
    else:
        if debug: print('Problems with {0}: no bibliographic production'.format(cv))

    return count

def get_works_from_cv(cv, debug=False):
    """
    Collect all works for a cv file and store in a dict relating every year to another dict,
    indicating how many items there are in each of the following categories:
    - "complete article"
    - "conference article"
    - "book chapter"
    """
    outlet = {}

    if debug: print('--- # {0}'.format(cv))
    root = None
    try:
        root = xml.etree.ElementTree.parse(cv).getroot()
    except Exception as e:
        if debug: print('Problems with {0}: {1}'.format(cv, e))
        return None
    outlet["complete article"] = get_complete_articles_from_cv(root, debug)
    outlet["conference article"] = get_complete_conference_articles_from_cv(root, debug)
    outlet["book chapter"] = get_book_chapters_from_cv(root, debug)

    return outlet

##################
# MAIN FUNCTIONS #
##################

def unpack_works_from_all_cv(all_cv, debug=False):
    outlet = {}
    pattern = re.compile(r'[\\/]')

    for cv in all_cv:
        stuff = get_works_from_cv(cv, debug)
        if stuff is not None:
            outlet[pattern.split(cv)[-1]] = stuff

    return outlet

    cv_folder = config['working'] + config['cv dir']
    return util.get_all_files(cv_folder)

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    cv_folder = config['working'] + config['cv dir']
    all_cv = util.get_all_files(cv_folder)
    works = unpack_works_from_all_cv(all_cv)
    print(works)
    # TODO Save kinds of works
