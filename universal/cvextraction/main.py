# -*- coding: cp1252 -*-
import sys
import os
import os.path
import xml.etree.ElementTree
import re

######################
# CV DATA EXTRACTION #
######################

def get_cv_root(cv):
    root = None
    try:
        root = xml.etree.ElementTree.parse(cv).getroot()
    except Exception as e:
        print('{0}: {1}'.format(cv, e))
        return None

    return root

def get_repeated_names(all_cv):
    names = {}

    # getting all names
    for cv in all_cv:
        root = xml.etree.ElementTree.parse(cv).getroot()
        dados_gerais = root.getchildren()[0]
        nome_completo = dados_gerais.attrib['NOME-COMPLETO']
        if nome_completo not in names:
            names[nome_completo] = []
        names[nome_completo].append(cv)

    # printing repeated names
    for name in names:
        print('---')
        print('name: {0}'.format(name))
        print('cv:')
        for cv in names[name]:
            print('- {0}'.format(cv))

    return names

def get_fields_from_phd(root):
    outlet = []

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
                    area = area_do_conhecimento.attrib.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO')
                    if area is not None:
                        outlet.append(area)
                    area = area_do_conhecimento.attrib.get('NOME-DA-ESPECIALIDADE')
                    if area is not None:
                        outlet.append(area)
    outlet = [it for it in outlet if len(it) > 0]
    return outlet

def get_fields_from_book_chapters(root):
    outlet = []

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
                            area = area_do_conhecimento.attrib.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)
                            area = area_do_conhecimento.attrib.get('NOME-DA-ESPECIALIDADE')
                            if area is not None:
                                outlet.append(area)
    outlet = [it for it in outlet if len(it) > 0]
    return outlet

def get_fields_from_complete_articles(root):
    outlet = []
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
                            area = area_do_conhecimento.attrib.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)
                            area = area_do_conhecimento.attrib.get('NOME-DA-ESPECIALIDADE')
                            if area is not None:
                                outlet.append(area)
    outlet = [it for it in outlet if len(it) > 0]
    return outlet

def get_fields_from_conference_articles(root):
    outlet = []
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
                            area = area_do_conhecimento.attrib.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO')
                            if area is not None:
                                outlet.append(area)
                            area = area_do_conhecimento.attrib.get('NOME-DA-ESPECIALIDADE')
                            if area is not None:
                                outlet.append(area)
    outlet = [it for it in outlet if len(it) > 0]
    return outlet

def get_name(root):
    return root.getchildren()[0].attrib['NOME-COMPLETO']

def get_fields_from_masters(root):
    outlet = []
    formacao = root.getchildren()[0].find('FORMACAO-ACADEMICA-TITULACAO')
    if formacao is not None:
        doutorado = formacao.find('MESTRADO')
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
                    area = area_do_conhecimento.attrib.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO')
                    if area is not None:
                        outlet.append(area)
                    area = area_do_conhecimento.attrib.get('NOME-DA-ESPECIALIDADE')
                    if area is not None:
                        outlet.append(area)
    outlet = [it for it in outlet if len(it) > 0]
    return outlet

######################################
# SIMILARITY ANALYSIS PRE-PROCESSING #
######################################

def generate_similarity_table(data, output_file):
    # extracting all possible fields
    fields = set()
    for cv in data:
        current_fields = data[cv]
        for field in current_fields:
            fields.add(field)
    fields = list(fields)

    # writting table to file
    with open(output_file, 'w', encoding='utf-8') as fp:
        line = 'cv\t{0}\n'.format('\t'.join(fields))
        fp.write(line)
        # IDEA instead of writting the cv name, write the index
        for cv in data:
            count = [len([f for f in data[cv] if f == field]) for field in fields]
            first_column = re.split(r'[/\\]', cv)[-1]
            remaining_columns = '\t'.join([str(x) for x in count])
            line = '{0}\t{1}\n'.format(first_column, remaining_columns)
            fp.write(line)

def generate_metadata_table(names, ka_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as fp:
        fp.write('id\tlabel\tcv\tareas\n')
        for i, fullcv in enumerate(names):
            # extracting data
            cv = re.split(r'[/\\]', fullcv)[-1]
            name = names[fullcv]
            ka_stuff = {}
            for ka in ka_data[fullcv]:
                if ka not in ka_stuff:
                    ka_stuff[ka] = 0
                ka_stuff[ka] += 1

            # turning data into information
            stuff = []
            for area in ka_stuff:
                how_many = ka_stuff[area]
                stuff.append([area, how_many])
            if len(stuff) == 0:
                ka = "vazio"
            else:
                stuff.sort(key=lambda u: u[1], reverse=True)
                ka = "{0} {1}".format(stuff[0][1], stuff[0][0])
                if len(stuff) >= 2:
                    ka += " {0} {1}".format(stuff[1][1], stuff[1][0])
                if len(stuff) >= 3:
                    ka += " {0} {1}".format(stuff[2][1], stuff[2][0])

            # writting information
            line = "{0}\t{1}\t{2}\t{3}\n".format(i+1, name, cv, ka)
            fp.write(line)

def generate_stats_table(stuff, where):
    with open(where, 'w', encoding='utf-8') as fp:
        fp.write('cv\tartigos completos\tartigos em conferencias\tcapitulos de livros\tdoutorado\tmestrado\n')
        for fullcv in stuff:
            cv = re.split(r'[/\\]', fullcv)[-1]
            data = '\t'.join([str(it) for it in stuff[fullcv]])
            fp.write('{0}\t{1}\n'.format(cv, data))

##################
# MAIN PROCEDURE #
##################

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])

    # Getting all CV
    p = config['pwd'] + config['cv']
    all = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
    all_cv = [p+f for f in all if '.xml' in f]

    # Analyzing CV
    ka_data = {} # knowledge area data
    names = {}
    how_many = {}
    for cv in all_cv:
        root = get_cv_root(cv)
        if root is not None:
            stuff = [
                get_fields_from_complete_articles(root),
                get_fields_from_conference_articles(root),
                get_fields_from_book_chapters(root),
                get_fields_from_phd(root),
                get_fields_from_masters(root)
            ]

            names[cv] = get_name(root)
            how_many[cv] = [len(it) for it in stuff]
            ka_data[cv] = sum(stuff, [])

    # Similarity Analysis
    ka_data_file = config['pwd'] + 'cv.csv'
    generate_similarity_table(ka_data, ka_data_file)
    print(ka_data_file)

    # Metadata for further studies
    metadata_file = config['pwd'] + 'cv_meta.csv'
    generate_metadata_table(names, ka_data, metadata_file)
    print(metadata_file)

    # Statistics from CV data
    stats_file = config['pwd'] + 'stats.csv'
    generate_stats_table(how_many, stats_file)
    print(stats_file)
