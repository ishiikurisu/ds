import sys

def load_csv(filename):
    table = []

    with open(filename, 'r') as fp:
        for line in fp:
            table.append(line.strip().split(';'))

    return table

def load_table_from_file(filename):
    """
    Loads the actions, criteria and the ranking table from a CSV file saved
    on filename. If the file name is not valid, all variables return empty.
    """
    actions, criteria, table = [], [], []
    contents = load_csv(filename)
    table = contents

    # TODO Populate variables

    return actions, criteria, table

def get_weights_from_file(filename):
    """
    Loads the weights from a local standard PROMETHEE-ROC CSV file saved on
    filename. If the file name is not valid, an empty list is returned.
    """
    weights = []

    # TODO Implement me!

    return weights

if __name__ == '__main__':
    tablename = sys.argv[1]
    actions, criteria, table = load_table_from_file(tablename)
    weights = get_weights_from_file(tablename)

    print(actions)
    print(criteria)
    print(weights)
    print(table)
