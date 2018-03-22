import sys
import flow
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
                fields = stuff
                report = { field: {} for field in fields[1:] }
                first_line = False
            else:
                for i, field in enumerate(fields[1:]):
                    info = stuff[i+1]
                    if info not in report[field]:
                        report[field][info] = 0
                    report[field][info] += 1

    return report

def save_report(report, config):
    """
    Saves the generated report on a relevant file as described by the configuration structure.
    """
    # TODO Implement me!
    pass

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    source_output = cfs.get_output(config)
    report = generate_report(source_output)
    print(report)
    save_report(report, config)
