import sys
import excel
import flow

def get_years(config):
    return sorted([int(y) for y in config['years'].keys()])

def get_everything(config):
    """
    Extracts the ids and the valid periods from the paycheck. Returns a hashmap where each key is
    an id and each value is a hashmap containing all years when that id received something from
    a given process.
    """
    src = config['working'] + config['paycheck']
    years = get_years(config)
    return excel.extract_periods_from_paycheck(src, years)

def save_stuff(config, periods_by_id):
    """
    Stores the extracted information in a better table.
    """
    src = config['working'] + 'ids_by_period.csv'
    years = get_years(config)

    with open(src, 'w') as fp:
        fp.write('ids;{0}\n'.format(';'.join(map(str, years))))
        for current_id in periods_by_id:
            processes = periods_by_id[current_id]
            valid_years = map(lambda year: processes[year] if year in processes else ' ', years)
            fp.write("'{0}';{1}\n".format(current_id, ';'.join(valid_years)))

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    periods_by_id = get_everything(config)
    save_stuff(config, periods_by_id)
