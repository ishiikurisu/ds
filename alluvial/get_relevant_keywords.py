import sys
import util
import collect_from_source as cfs
import get_keywords as gk
import consultant

def validate_years(flow, first_year, function):
    year = first_year
    years = []

    for state in flow:
        if function(state):
            years.append(year)
        year += 1

    return years

def get_output(config):
    return config['working'] + config['cv dir'] + 'keywords.csv'

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    consultant.setup(sys.argv[1])

    # Get all CA names
    flows_by_name = {}
    with open(cfs.get_output(config), 'r', encoding='utf-8') as fp:
        first_line = True
        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                fields = stuff
                first_line = False
            else:
                name = stuff[1]
                flow = stuff[2:]
                if 'CA' in flow:
                    flows_by_name[name] = flow

    # Extracting keywords from names in relevant years
    all_keywords = {}
    for name in flows_by_name:
        cv = consultant.get_cv_by_name(name)
        keywords = gk.get_keywords_from_cv(cv)
        flow = validate_years(flows_by_name[name], 2000, lambda s: s == config['program code'])
        for keyword in keywords:
            years = filter(lambda y: y in flow, keywords[keyword])
            for year in years:
                if keyword not in all_keywords:
                    all_keywords[keyword] = []
                all_keywords[keyword].append(year)

    # Consolidating data
    outlet = {}
    years = list(range(2000, 2019))
    for keyword in all_keywords:
        if keyword not in outlet:
            outlet[keyword] = {}
        for year in years:
            outlet[keyword][year] = len([y for y in all_keywords[keyword] if y == year])
    all_keywords = outlet

    # Saving data
    with open(get_output(config), 'w', encoding='utf-8') as fp:
        fp.write('keyword\tquantity\tyear\n')
        for keyword in all_keywords:
            for year in all_keywords[keyword]:
                qty = all_keywords[keyword][year]
                if qty > 0:
                    fp.write('{0}\t{1}\t{2}\n'.format(keyword, qty, year))
