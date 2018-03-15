import sys
import excel
import flow

def get_everything(config):
    """
    Extracts the ids and the valid periods from the paycheck. Returns a hashmap where each key is
    an id and each value is a set containing all years when that id received something.
    """
    src = config['working']
    years = config['years']
    paycheck = config['paycheck']
    # TODO Implement me on `excel`!
    return {}


if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    periods_by_id = get_everything(config)
    print(periods_by_id)
    # TODO Save stuff
