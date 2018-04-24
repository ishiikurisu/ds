import sys
import util
import xml.etree.ElementTree
import collect_from_source as cfs

#################
# CV OPERATIONS #
#################

def get_name_frequency(all_cv, debug=False):
    outlet = {}

    for cv in all_cv:
        # Getting root
        if debug: print('--- # {0}'.format(cv))
        root = None
        try:
            root = xml.etree.ElementTree.parse(cv).getroot()
        except Exception as e:
            print('Problems with {0}: {1}'.format(cv, e))
        if root is None:
            continue

        # Getting name
        dados_gerais = root.find('DADOS-GERAIS')
        if dados_gerais is None:
            continue
        nome_completo = dados_gerais.get('NOME-COMPLETO').upper()
        if nome_completo not in outlet:
            outlet[nome_completo] = 0
        outlet[nome_completo] += 1
        if (outlet[nome_completo] > 1) and (debug):
            print('{0} repetiu!'.format(nome_completo))

    return outlet

#################
# ID OPERATIONS #
#################

def parse_line(stuff, fields):
    cpf = util.fix_id(stuff[fields.index('CPF')])
    nome = stuff[fields.index('Nome Beneficiário')]
    coordination = stuff[fields.index('Código Comitê Assessor')]

    if cpf == '0'*11:
        raise ValueError

    return cpf, nome, coordination

def relate_names_and_ids(source, debug=False):
    names2ids = {}
    ids2names = {}

    with open(source, 'r', encoding='utf-8') as fp:
        first_line = True
        fields = None
        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                fields = stuff
                first_line = False
            else:
                try:
                    idn, name, coordination = parse_line(stuff, fields)

                    if name not in names2ids:
                        names2ids[name] = set()
                    names2ids[name].add(idn)
                    if (debug) and (len(names2ids[name]) > 1):
                        print('{0} is a repeated name in {1}!'.format(name, coordination))

                    if idn not in ids2names:
                        ids2names[idn] = set()
                    ids2names[idn].add(name)
                    if (debug) and (len(ids2names[idn]) > 1):
                        print('{0} cant write their name!'.format(name))

                except ValueError:
                    print('discarded entry!')

    return names2ids, ids2names


if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    if sys.argv[2] == 'CV':
        cv_folder = config['working'] + config['cv dir']
        all_cv = util.get_all_files(cv_folder)
        names = get_name_frequency(all_cv, debug=True)
        print('---')
        print(names)
        print('...')
    elif sys.argv[2] == 'ID':
        source = cfs.get_input(config)
        names2ids, ids2names = relate_names_and_ids(source, debug=True)
        print('--- # Name -> #Ids')
        for name in names2ids:
            print('{0}: {1}'.format(name, len(names2ids[name])))
        print('--- # Id -> #names')
        for idn in ids2names:
            print('{0}: {1}'.format(idn, len(ids2names[idn])))
        print('...')
