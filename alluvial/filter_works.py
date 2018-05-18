import sys
import util
import get_works as gw
import collect_from_source as cfs



if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    works = gw.unpack_works(config)
    years, flows, names = cfs.get_stuff(config)

    ids = util.invert_map(names)
    problems = []
    for name in works:
        try:
            current_id = ids[name]
            relevant_years = set()
            for year in flows[current_id]:
                coordination = flows[current_id][year]
                if coordination == 'CA':
                    relevant_years.add(year)
            # BUG Why are there empty sets? Maybe the invertion is not working
            # TODO remove irrelevant production years from works
        except KeyError:
            problems.append(name)

    print("problems:")
    for name in problems:
        print('- {0}'.format(name))
