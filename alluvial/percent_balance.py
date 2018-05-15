import sys
import util
import balance
import collect_from_source as cfs

def get_output(config):
    output = balance.get_output(config)
    return output.replace('_balanced.csv', '_percentual.csv')

def unpack_balance(config, inputfile, outlet={}):
    """
    Loads the information in a balanced table and turns it into a condensed
    dictionary relating the committees to another dict, relating years to a
    list indicating from many people left and how many arrived, respectively.
    """
    with open(inputfile, 'r', encoding='utf-8') as inlet:
        first_line = True
        for line in inlet:
            stuff = line.strip().split('\t')
            if first_line:
                fields = { field: i for i, field in enumerate(stuff) }
                first_line = False
            else:
                try:
                    source = stuff[fields['source']]
                    target = stuff[fields['target']]
                    year = int(stuff[fields['year']])
                    flow = int(stuff[fields['flow']])
                except IndexError:
                    continue

                # Setting first levels
                if source not in outlet:
                    outlet[source] = {}
                if target not in outlet:
                    outlet[target] = {}

                # Adding information on source
                if (year-1) not in outlet[source]:
                    outlet[source][year-1] = [0, 0, 0]
                outlet[source][year-1][1] += flow

                # Adding information on target
                if year not in outlet[target]:
                    outlet[target][year] = [0, 0, 0]
                outlet[target][year][2] += flow

    return outlet

def unpack_alluvial(config, from_file, out={}):
    """
    Loads the information from the alluvial table and turns it into a condensed
    dictionary relating the committees to another dict, relating years to a
    list indicating from many people were in that committee for all given years
    """
    with open(from_file, 'r', encoding='utf-8') as inlet:
        first_line = True
        fields = []
        for line in inlet:
            stuff = line.strip().split('\t')[2:]
            if first_line:
                fields = [ int(it) for it in stuff ]
                first_line = False
            else:
                for i, committee in enumerate(stuff):
                    year = fields[i]
                    if committee not in out:
                        out[committee] = {}
                    if year not in out[committee]:
                        out[committee][year] = [0, 0, 0]
                    out[committee][year][0] += 1

    return out

def save_stuff(stuff, to_file):
    with open(to_file, 'w', encoding='utf-8') as outlet:
        outlet.write('CA\tano\ttotal\tsairam\tentraram\n')
        for c in stuff: # c for committee
            for y in stuff[c]:
                f = stuff[c][y]
                outlet.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(c, y, f[0], f[1], f[2]))


if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    from_balance = balance.get_output(config)
    from_alluvial = cfs.get_output(config)
    to_file = get_output(config)

    stuff = unpack_balance(config, from_balance)
    stuff = unpack_alluvial(config, from_alluvial, stuff)
    save_stuff(stuff, to_file)
