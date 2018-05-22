import sys
import util
import get_works as gw
import collect_from_source as cfs
import subprocess
import filter as fltr

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    works = gw.unpack_works(config)

    # Selecting only relevant people
    filtered = cfs.get_output(config)
    years, flows, names = cfs.load_stuff(fltr.get_output(config, filtered))
    ids = util.invert_map(names)

    # Filtering work data
    problems = []
    filtered = {}
    for name in works:
        filtered[name] = {}
        try:
            current_id = ids[name]
            relevant_years = set()

            # collecting relevant production years
            for year in flows[current_id]:
                coordination = flows[current_id][year]
                if coordination == 'CA':
                    relevant_years.add(year)

            # filtering production years by selecting only years in committee
            for kind in works[name]:
                filtered[name][kind] = []
                for year in works[name][kind]:
                    if year in relevant_years:
                        filtered[name][kind].append(year)
        except KeyError:
            problems.append(name)

    print("problems:")
    for name in problems:
        print('- {0}'.format(name))

    # Storing stuff
    gw.store_production_by_kind(config, filtered)
