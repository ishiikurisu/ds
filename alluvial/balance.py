import sys
import util
import collect_from_source as cfs

def get_output(config):
    return cfs.get_output(config).replace('.csv', '_balanced.csv')

def extract_balance(from_file):
    """
    Calculates the balance for each coordination in every year of the table.
    Returns a list of dicts, and each dict contains 4 keys:
    - The `source` coordination
    - The `target` coordination
    - The `year` that flow is referentiating
    - The personnel `flow` for that year between the coordinations
    """
    outlet = []
    # TODO Implement me please
    return outlet

def save_balance(balance, to_file):
    with open(to_file, 'w', encoding='utf-8') as outlet:
        outlet.write('source\ttarget\tyear\tflow\n')
        for entry in balance:
            line = '{0}\t{1}\t{2}\t{3}\n'.format(entry['source'],
                                                 entry['target'],
                                                 entry['year'],
                                                 entry['flow'])
            outlet.write(line)

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    from_file = cfs.get_output(config)
    to_file = get_output(config)
    balance = extract_balance(from_file)
    save_balance(balance, to_file)
