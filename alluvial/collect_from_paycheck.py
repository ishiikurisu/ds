import sys
import excel
import flow

def get_years(config):
    return sorted([int(y) for y in config['years'].keys()][1:])

def get_everything(config):
    """
    Extracts the ids and the valid periods from the paycheck. Returns a hashmap where each key is
    an id and each value is a set containing all years when that id received something.
    """
    src = config['working'] + config['paycheck']
    years = get_years(config)
    return excel.extract_periods_from_paycheck(src, years)

def save_stuff(config, periods_by_id):
    src = config['working'] + 'ids_by_period.csv'
    years = get_years(config)

    with open(src, 'w') as fp:
        fp.write('ids;{0}\n'.format(';'.join(map(str, years))))
        for current_id in periods_by_id:
            line = '{0};'.format(current_id)
            valid_years = map(lambda year: '1' if year in periods_by_id[current_id] else ' ', years)
            line += ';'.join(valid_years)
            fp.write(line + '\n')

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    periods_by_id = get_everything(config)
    save_stuff(config, periods_by_id)
