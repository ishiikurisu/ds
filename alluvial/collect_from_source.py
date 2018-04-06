import sys
import util

def get_years_from_line(line, fields):
    """
    Gets the yearly valid period from the given line. Throws a `ValueError` exception if the
    desired fields do not contain valid data.
    """
    stuff = line.strip().split('\t')
    process_id = stuff[fields.index('Código Processo Formatado')]
    start = int(stuff[fields.index('Data Início Contrato')].split(' ')[0].split('/')[-1])
    ending = int(stuff[fields.index('Data Término Contrato')].split(' ')[0].split('/')[-1])
    start = int(process_id.split('/')[1].split('-')[0]) if start < 1970 else start
    ending += 1 if start == ending else 0
    return start, ending


def treat_line(line, fields, data={}):
    """
    Updates the information in the box based on the current line. Returns the input hashmap with
    incremented information.
    """
    try:
        stuff = line.strip().split('\t')
        current_id = stuff[fields.index('CPF')]
        coordination = stuff[fields.index('Código Comitê Assessor')]
        start, ending = get_years_from_line(line, fields)
    except ValueError:
        return data

    if len(current_id) == 11:
        if current_id not in data:
            data[current_id] = {}
        for year in range(start, ending):
            current = data[current_id].get(year)
            if current is None:
                data[current_id][year] = coordination
            else:
                # XXX How to deal with that?
                pass

    return data

def get_stuff(config):
    """
    Loads the revelant data from the source data set. Returns a hashmap relating each id to another
    dictionary, relating each year to a coordination.
    """
    years = set()
    data = {}
    src = config['working'] + config['source']

    with open(src, 'r') as fp:
        first_line = True
        fields = []

        for line in fp.readlines()[2:]:
            if first_line:
                fields = line.strip().split('\t')
                first_line = False
            else:
                line = '0' + line if line[0] == '\t' else line
                data = treat_line(line, fields, data)
                try:
                    start, ending = get_years_from_line(line, fields)
                    for year in range(start, ending):
                        years.add(year)
                except:
                    pass

    years = list(sorted(years))
    return years, data

def get_output(config):
    """Generates an output file name from the source for this procedure."""
    return config['working'] + 'source.csv'

def save_stuff(config, years, data):
    """
    Saves relevant data to a "source.csv" file in the working folder set in the configuration
    structure.
    """
    with open(config['working'] + 'source.csv', 'w') as fp:
        first_line = 'ids\t' + '\t'.join(map(str, years)) + '\n'
        fp.write(first_line)
        for current_id in data.keys():
            appeared = False
            content = ["'{0}'".format(current_id)]
            coordinations = data[current_id]
            for year in years:
                current_state = 'never'
                if year in coordinations:
                    current_state = coordinations[year]
                    appeared = True
                elif appeared:
                    current_state = 'nope'
                content.append(current_state)
            line = '\t'.join(content) + '\n'
            fp.write(line)

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    years, data = get_stuff(config)
    save_stuff(config, years, data)
