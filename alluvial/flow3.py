import sys
import json
import excel
import flow


def extract_groups(config, operation=excel.group_coordinations_by_id):
    groups = {}
    years = config['years']
    src = config['working']
    ids = set()

    print('# Getting all groups for each id during 3 years')
    year_count = 0
    for year in years:
        # Grouping years
        if (year_count % 3) == 0:
            current_reference_year = year
            groups[current_reference_year] = {}
        year_count += 1

        # Extracting information from current year
        print('Getting programs from {0}'.format(year))
        excelname = config['years'][year]
        current_groups = operation(src + excelname)
        for current_id in current_groups:
            if current_id not in groups[current_reference_year]:
                groups[current_reference_year][current_id] = current_groups[current_id]
            ids.add(current_id)

    return ids, groups

def consolidate_groups(config, ids, groups):
    years = config['years']
    src = config['working']
    output = src + 'triads.csv'

    print('# Consolidating data')
    with open(output, 'w') as fp:
        # Writting header
        line = 'ids;' + ';'.join(groups.keys()) + '\n'
        fp.write(line)

        # Writting remaing lines
        for current_id in ids:
            line = '{0}'.format(current_id)
            for year in groups:
                group = ''
                if current_id in groups[year]:
                    group = groups[year][current_id]
                line += ';{0}'.format(group)
            fp.write(line + '\n')
        print('{0} ids written'.format(len(ids)))


if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    ids, groups = extract_groups(config)
    consolidate_groups(config, ids, groups)
