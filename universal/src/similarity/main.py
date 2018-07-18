import sys
import numpy as np

#######
# I/O #
#######

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

def save_table(to_file, ids, table):
    with open(to_file, 'w') as fp:
        # first line
        line = ' \t%s\n' % '\t'.join(ids)
        fp.write(line)

        # remaining lines
        lx, ly = table.shape
        for x in range(lx):
            values = []
            for y in range(ly):
                values.append(('%.5f' % table[x, y]).replace('.', ','))
            line = '%s\t%s\n' % (ids[x], '\t'.join(values))
            fp.write(line)


###############
# MATHEMATICS #
###############

def calculate_tfidf(tft):
    # BUG Why is the output table always a bunch of zeros?
    tf = tft.T
    lx, ly = tf.shape
    tfidf = np.zeros([lx, ly])
    wd = np.sum(tf, axis=0)
    df = np.sum(np.asarray(tf > 0, 'i'), axis=1)
    for x in range(lx):
        for y in range(ly):
            result = float(tf[x,y])/wd[0, y] * np.log(float(ly)/df[x])
            tfidf[x, y] = 0 if np.isnan(result) else result
    return tfidf.T

def calculate_dd(tfidf):
    return np.dot(tfidf, tfidf.T)

##################
# MAIN PROCEDURE #
##################

if __name__ == '__main__':
    input_file = sys.argv[1]
    operation = sys.argv[2]

    docs, terms, tf = load_table(input_file)
    tfidf = calculate_tfidf(tf)

    if operation == 'dd':
        doc_doc_similarity = calculate_dd(tfidf)
        output_file = input_file.replace('.csv', '_dd.csv')
        save_table(output_file, docs, doc_doc_similarity)
    elif operation == 'tt':
        print('not gonna happen anytime soon')
    else:
        print('invalid operation')
