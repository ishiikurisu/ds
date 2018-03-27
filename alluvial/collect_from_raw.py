import sys
import util

def get_year_range_from_ids(ids):
    start_year = 2018
    end_year = 1968

    for _, years in ids.items():
        ly = list(years.keys())
        start_year = min(ly + [start_year])
        end_year = max(ly + [end_year])

    return [y for y in range(start_year, end_year+1)]

def get_stuff(config):
    """Retrieves collected data from raw (aka Emerson's) table."""
    ids = {}
    src = config['working'] + config['raw']
    ids = util.get_coordinations_from_csv(src)
    years = get_year_range_from_ids(ids)
    return years, ids

def save_stuff(config, years, box):
    """Save collected stuff to a file"""
    csvname = config['working'] + 'emerson/processed.csv'

    with open(csvname, 'w') as fp:
        fp.write('id\t' + '\t'.join(map(str, years)) + '\n')
        for current_id in box:
            stuff = box[current_id]
            appeared = False
            outlet = []

            for year in years:
                state = 'never'
                if year in stuff:
                    state = stuff[year]
                    appeared = True
                elif appeared:
                    state = 'nope'
                outlet.append(state)

            fp.write("'{0}'\t{1}\n".format(current_id, '\t'.join(outlet)))

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    years, box = get_stuff(config)
    save_stuff(config, years, box)
