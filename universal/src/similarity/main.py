import sys
import numpy as np

def load_table(from_file):
    docs = []
    terms = []
    table = []

    with open(from_file, 'r') as fp:
        first_line = True
        for line in fp:
            if first_line:
                terms = line.strip().split('\t')[1:]
                first_line = False
            else:
                stuff = line.strip().split('\t')
                docs.append(stuff[0])
                table.append([int(it) for it in stuff[1:]])

    table = np.matrix(table)
    return docs, terms, table

def calculate_tfidf(tf):
    tfidf = np.zeros_like(tf)
    wd = np.sum(tf, axis=0)
    df = np.sum(np.asarray(tf > 0, 'i'), axis=1)
    lx, ly = tf.shape
    for x in range(lx):
        for y in range(ly):
            # BUG Why is this line generating an array? it should be a number
            tfidf[x, y] = (tf[x,y]/wd[y]) * np.log(float(ly)/df[x])
    return np.nan_to_num(tfidf.T)


if __name__ == '__main__':
    input_file = sys.argv[1]
    operation = sys.argv[2]

    docs, terms, tf = load_table(input_file)
    tfidf = calculate_tfidf(tf)
    print(tfidf)

    if operation == 'dd':
        # TODO Implement me!
        pass
    elif operation == 'tt':
        print('not gonna happen anytime soon')
    else:
        print('invalid operation')
