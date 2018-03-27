import sys
import util
import collect_from_source as cfs

def generate_report(source_output):
    """
    Generates an accountability report for the processing done on `collect_from_source`.
    """
    report = {}

    with open(source_output, 'r') as fp:
        first_line = True
        fields = []
        for line in fp:
            stuff = line.strip().split('\t')
            if first_line:
                fields = stuff[1:]
                report = { field: {} for field in fields }
                first_line = False
            else:
                for i, field in enumerate(fields):
                    info = stuff[i+1]
                    if info not in report[field]:
                        report[field][info] = 0
                    report[field][info] += 1

    return report

def save_report(report, config):
    """
    Saves the generated report on a relevant file as described by the configuration structure.
    """
    with open(config['working'] + 'source_report.csv', 'w') as fp:
        fp.write('year\tnever\tnope\tinside\n')
        for year in report.keys():
            results = report[year]
            never = 0
            nope = 0
            inside = 0
            for state, count in results.items():
                if state == 'never':
                    never += count
                elif state == 'nope':
                    nope += count
                else:
                    inside += count
            fp.write('{0}\t{1}\t{2}\t{3}\n'.format(year, never, nope, inside))

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    source_output = cfs.get_output(config)
    report = generate_report(source_output)
    save_report(report, config)
