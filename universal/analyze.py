# -*- coding: cp1252 -*-
import util
import sys
import os
import os.path
import xml.etree.ElementTree

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

def get_fields_from_book_chapters(cv):
    outlet = []
    root = xml.etree.ElementTree.parse(cv).getroot()

    producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
    if producao_bibliografica is not None:
        livros_e_capitulos = producao_bibliografica.find('LIVROS-E-CAPITULOS')
        if livros_e_capitulos is not None:
            coisas_publicadas = livros_e_capitulos.find('CAPITULOS-DE-LIVROS-PUBLICADOS')
            if coisas_publicadas is not None:
                todos_capitulos = coisas_publicadas.findall('CAPITULO-DE-LIVRO-PUBLICADO')
                for capitulo in todos_capitulos:
                    areas_do_conhecimento = capitulo.find('AREAS-DO-CONHECIMENTO')
                    if areas_do_conhecimento is not None:
                        areas_do_conhecimento = areas_do_conhecimento.getchildren()
                        for area_do_conhecimento in areas_do_conhecimento:
                            area = area_do_conhecimento.attrib.get('NOME-GRANDE-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)
                            area = area_do_conhecimento.attrib.get('NOME-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)


    return None if len(outlet) == 0 else outlet

def get_fields_from_complete_articles(cv):
    outlet = []
    root = xml.etree.ElementTree.parse(cv).getroot()

    producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
    if producao_bibliografica is not None:
        artigos_publicados = producao_bibliografica.find('ARTIGOS-PUBLICADOS')
        todos_artigos = artigos_publicados.findall('ARTIGO-PUBLICADO')
        if todos_artigos is not None:
            for artigo_publicado in todos_artigos:
                dados_basicos = artigo_publicado.find('DADOS-BASICOS-DO-ARTIGO')
                if dados_basicos.attrib['NATUREZA'] == 'COMPLETO':
                    areas_do_conhecimento = artigo_publicado.find('AREAS-DO-CONHECIMENTO')
                    if areas_do_conhecimento is not None:
                        areas_do_conhecimento = areas_do_conhecimento.getchildren()
                        for area_do_conhecimento in areas_do_conhecimento:
                            area = area_do_conhecimento.attrib.get('NOME-GRANDE-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)
                            area = area_do_conhecimento.attrib.get('NOME-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)

    return None if len(outlet) == 0 else outlet

def get_fields_from_conference_articles(cv):
    outlet = []
    root = xml.etree.ElementTree.parse(cv).getroot()

    producao_bibliografica = root.find('PRODUCAO-BIBLIOGRAFICA')
    if producao_bibliografica is not None:
        artigos_publicados = producao_bibliografica.find('TRABALHOS-EM-EVENTOS')
        todos_artigos = artigos_publicados.findall('TRABALHO-EM-EVENTOS')
        if todos_artigos is not None:
            for artigo_publicado in todos_artigos:
                dados_basicos = artigo_publicado.find('DADOS-BASICOS-DO-TRABALHO')
                if dados_basicos.attrib['NATUREZA'] == 'COMPLETO':
                    areas_do_conhecimento = artigo_publicado.find('AREAS-DO-CONHECIMENTO')
                    if areas_do_conhecimento is not None:
                        areas_do_conhecimento = areas_do_conhecimento.getchildren()
                        for area_do_conhecimento in areas_do_conhecimento:
                            area = area_do_conhecimento.attrib.get('NOME-GRANDE-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)
                            area = area_do_conhecimento.attrib.get('NOME-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)

    return None if len(outlet) == 0 else outlet

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])

    # Getting all CV
    p = config['pwd'] + config['cv']
    all = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
    all_cv = [p+f for f in all if '.xml' in f]

    # Analyzing CV
    stuff = {}
    invalid = []
    for cv in all_cv:
        fields = get_fields_from_complete_articles(cv)
        if fields is not None:
            stuff[cv] = fields
        else:
            invalid.append(cv)

    # Printing relevant information from data
    print(stuff)
    for cv in invalid:
        print(cv + ' is invalid')
    print('invalid: ' + str(len(invalid)) + '/' + str(len(all_cv)))
    # TODO relate all researchers to all fields
