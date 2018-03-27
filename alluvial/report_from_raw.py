import sys
import util
import collect_from_raw as cfr
import report_from_source as rfs

def save_report(report, config):
    """
    Saves the generated report on a relevant file as described by the configuration structure.
    """
    with open(config['working'] + 'raw_report.csv', 'w') as fp:
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
    source_output = cfr.get_output(config)
    report = rfs.generate_report(source_output)
    save_report(report, config)
