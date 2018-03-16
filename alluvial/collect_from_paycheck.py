import sys
import excel
import flow
import urllib.request


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

def check_for_consultant():
    """
    Checks if the consultant is available for use.
    """
    health = urllib.request.urlopen("http://localhost:5000/health").read().decode('utf-8')
    return health == 'ok'

def turn_processes_to_coordinations(processes):
    """
    Translate the process numbers into coordinations.
    """
    memo = {}
    outlet = {}

    for year in processes:
        process = processes[year].replace('/', '').replace('-', '')

        if process not in memo:
            query = "http://localhost:5000/consult/{0}".format(process)
            coordination = urllib.request.urlopen(query).read().decode('utf-8')
            memo[process] = coordination
        else:
            coordination = memo[process]

        outlet[year] = coordination if len(coordination) < 5 else 'ghost'

    return outlet

def save_stuff(config, periods_by_id):
    """
    Stores the extracted information in a better table.
    """
    src = config['working'] + 'ids_by_period.csv'
    years = get_years(config)
    consultant_available = check_for_consultant()

    with open(src, 'w') as fp:
        fp.write('ids;{0}\n'.format(';'.join(map(str, years))))
        for current_id in periods_by_id:
            processes = periods_by_id[current_id]
            if consultant_available:
                coordinations = turn_processes_to_coordinations(processes)
                valid_years = map(lambda year: coordinations[year] if year in coordinations else ' ', years)
            else:
                valid_years = map(lambda year: processes[year] if year in processes else ' ', years)
            fp.write("'{0}';{1}\n".format(current_id, ';'.join(valid_years)))

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    periods_by_id = get_everything(config)
    save_stuff(config, periods_by_id)
