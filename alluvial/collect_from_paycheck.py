import sys
import excel
import flow

def get_everything(config):
    """
    Extracts the ids and the valid periods from the paycheck. Returns a hashmap where each key is
    an id and each value is a set containing all years when that id received something.
    """
    src = config['working'] + config['paycheck']
    years = sorted([int(y) for y in config['years'].keys()][1:])
    return excel.extract_periods_from_paycheck(src, years)

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    periods_by_id = get_everything(config)
    print(periods_by_id)
    print(periods_by_id['5753767672'])
    # TODO Save stuff
