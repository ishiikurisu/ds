import sys
import re
import prometheeroc

def load_csv(filename):
    table = []

    with open(filename, 'r') as fp:
        for line in fp:
            table.append(re.split(r'[;\t]', line.strip()))

    return table

def mapl(f, x):
    return list(map(f, x))

def load_table_from_file(filename):
    """
    Loads the actions, criteria and the ranking table from a CSV file saved
    on filename. If the file name is not valid, all variables return empty.
    """
    contents = load_csv(filename)
    actions = [line[0] for line in contents[2:]]
    criteria = [s for s in contents[0] if len(s) > 0]
    table = [mapl(int, l[1:]) for l in contents[2:]]
    return actions, criteria, table

def get_weights_from_file(filename):
    """
    Loads the weights from a local standard PROMETHEE-ROC CSV file saved on
    filename. If the file name is not valid, an empty list is returned.
    """
    return [float(it) for it in load_csv(filename)[1][1:]]

if __name__ == '__main__':
    tablename = sys.argv[1]
    actions, criteria, table = load_table_from_file(tablename)
    weights = get_weights_from_file(tablename)
    promethee = prometheeroc.Promethee(actions, criteria)
    # promethee.set_weights(prometheeroc.roc(weights))
    promethee.set_weights(weights)
    scores = promethee.recommend(table)
    best_options = sorted(zip(actions, scores), key=lambda it: it[1])
    for option in best_options:
        print('{0}: {1}'.format(option[0], option[1]))
