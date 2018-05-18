import sys
import util
import get_works as gw
import collect_from_source as cfs
import subprocess
import filter as fltr

def load_fics(where):
    out = set()
    with open(where, 'r') as fp:
        for line in fp:
            out.add(line.strip().strip("'"))
    return out

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    works = gw.unpack_works(config)
    fics = load_fics(config['working'] + 'fics.csv')

    # Selecting only relevant people
    filtered = cfs.get_output(config)
    subprocess.call(['make',
                     'filter',
                     'WHERE={0}'.format(sys.argv[1]),
                     'TARGET={0}'.format(filtered)])
    years, flows, names = cfs.load_stuff(fltr.get_output(config, filtered))
    ids = util.invert_map(names)

    # Filtering work data
    filtered = {}
    problems = []
    processed = []
    for current_id in fics:
        try:
            name = names[current_id]
            filtered[name] = {}
            relevant_years = set()

            # collecting relevant production years
            for year in flows[current_id]:
                coordination = flows[current_id][year]
                if coordination == config['program code']:
                    relevant_years.add(year)

            # filtering production years by selecting only years in committee
            for kind in works[name]:
                filtered[name][kind] = []
                for year in works[name][kind]:
                    if year in relevant_years:
                        filtered[name][kind].append(year)
        except KeyError:
            pass

    # Storing stuff
    gw.store_production_by_kind(config, filtered)
