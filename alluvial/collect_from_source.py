# -*- coding: utf-8 -*-
import sys
import util

def parse_line(stuff, fields, data={}, names={}):
    try:
        year = util.fix_payment_year(stuff[fields.index('Data Ano Pagamento')])
        cpf = util.fix_id(stuff[fields.index('CPF')])
        coordination = stuff[fields.index('Código Comitê Assessor')]
        name = stuff[fields.index('Nome Beneficiário')]
    except IndexError:
        print('index error: {0}'.format(stuff))
        return -1, data, names
    except SyntaxError:
        print('syntax error: {0}'.format(stuff))
        return -1, data, names

    # Fact checking
    if cpf == '0'*11:
        return -1, data, names

    # Parsing data
    if cpf not in data:
        data[cpf] = {}
    if year not in data[cpf]:
        data[cpf][year] = ''
    if coordination not in data[cpf][year]:
        # There is a decision to be taken here. I can't just stack stuff
        # because I can't generate an alluvial with this kind of data.
        # What do I do?
        data[cpf][year] += coordination

    # Parsing name
    names[cpf] = name

    return year, data, names

def get_stuff(config):
    """
    Reads the fish source table to get the desired data. Returns:
    1. a `list` with all years in the process.
    2. a `dict` where each key is an ID and each value is another `dict`, where
    each key is a year and each value is the coordination that ID belonged to
    that year.
    3. a `dict` telling the name of each ID.
    """
    min_year = 3000
    max_year = 1000
    data = {}
    names = {}

    with open(get_input(config), 'r', encoding='utf-8') as fp:
        first_line = True

        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                fields = stuff
                first_line = False
            else:
                year, data, names = parse_line(stuff, fields, data, names)
                if year > 0:
                    if year > max_year:
                        max_year = year
                    elif year < min_year:
                        min_year = year

    years = list(range(min_year, max_year+1))

    return years, data, names

def get_input(config):
    return config['working'] + config['source']

def get_output(config):
    """
    Creates an output file name for the current procedure.
    """
    inlet = config['working'] + config['source']
    return '.'.join(inlet.split('.')[0:-1]) + '_processed.csv'

def save_stuff(config, years, data, names):
    """
    Stores data in memory
    """
    with open(get_output(config), 'w', encoding='utf-8') as fp:
        fp.write('CPF\tNome\t{0}\n'.format('\t'.join(map(str, years))))
        for cpf in data:
            states = []
            appeared = False
            coordinations = data[cpf]
            for year in years:
                state = 'never'
                if year in coordinations:
                    state = coordinations[year]
                    appeared = True
                elif appeared:
                    state = 'nope'

                if (len(state) > 2) and (state not in ['never', 'nope']):
                    # XXX What if there are transitions in consecutive years?
                    next_state = str(coordinations.get(year+1))
                    previous_state = str(coordinations.get(year-1))
                    if next_state in state:
                        state = next_state
                    elif previous_state in state:
                        state = previous_state
                    else:
                        state = state.replace(previous_state, '').replace(next_state, '')
                if (len(state) > 2) and ('00' in state):
                    state = state.replace("00", '')

                states.append(state)
            fp.write("'{0}'\t{1}\t{2}\n".format(cpf, names[cpf], '\t'.join(states)))

def load_stuff(where):
    years = []
    flow = {}
    names = {}

    with open(where, 'r') as fp:
        first_line = True
        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                years = [int(y) for y in stuff[2:]]
                first_line = False
            else:
                cid = stuff[0].strip('\'')
                names[cid] = stuff[1]
                flow[cid] = {}
                for i, year in enumerate(years):
                    flow[cid][year] = stuff[2+i]

    return years, flow, names

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    years, data, names = get_stuff(config)
    save_stuff(config, years, data, names)
