import sys
import util
import get_keywords as gk
import xml.etree.ElementTree

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

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    cv_folder = config['working'] + config['cv dir']
    all_cv = gk.get_all_cv_from(cv_folder) # IDEA Move this function to `util`
    names = get_name_frequency(all_cv, debug=True)
    print('---')
    print(names)
    print('...')
