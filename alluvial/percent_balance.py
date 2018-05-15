import sys
import util
import balance

def get_output(config):
    output = balance.get_output(config)
    return output.replace('_balanced.csv', '_percentual.csv')

def unpack_stuff(config, inputfile):
    """
    Loads the information in a balanced table and turns it into a condensed
    dictionary relating the committees to another dict, relating years to a
    list indicating from many people left and how many arrived, respectively.
    """
    outlet = {}

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
                    outlet[source][year-1] = [0, 0]
                outlet[source][year-1][0] += flow

                # Adding information on target
                if year not in outlet[target]:
                    outlet[target][year] = [0, 0]
                outlet[target][year][1] += flow


    return outlet

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    from_file = balance.get_output(config)
    to_file = get_output(config)

    stuff = unpack_stuff(config, from_file)
    print(stuff)
    # TODO Save stuff
