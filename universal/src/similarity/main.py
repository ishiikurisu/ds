import sys
import numpy as np
import numpy.linalg as linalg

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
                table.append([float(it) for it in stuff[1:]])

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
            values = ['%.8f' % table[x, y] for y in range(ly)]
            line = '%s\t%s\n' % (ids[x], '\t'.join(values).replace('.', ','))
            fp.write(line)

def save_table_with_numeric_ids(to_file, cvs, table):
    with open(to_file, 'w') as fp:
        # first line
        ids = [(str(i)) for i in range(1, len(cvs)+1)]
        line = ' \t%s\n' % '\t'.join(ids)
        fp.write(line)

        # remaining lines
        lx, ly = table.shape
        for x in range(lx):
            values = ['%.8f' % table[x, y] for y in range(ly)]
            line = '%s\t%s\n' % (ids[x], '\t'.join(values).replace('.', ','))
            fp.write(line)


###############
# MATHEMATICS #
###############

def calculate_tfidf(tft):
    tf = tft.T
    lx, ly = tf.shape
    tfidf = np.zeros([lx, ly])
    wd = np.sum(tf, axis=0)
    df = np.sum(np.asarray(tf > 0, 'i'), axis=1)
    for x in range(lx):
        for y in range(ly):
            result = (tf[x,y]/wd[0,y]) * np.log(float(ly)/df[x])
            tfidf[x, y] = 0 if np.isnan(result) else result
    return tfidf.T

def calculate_dd(tfidf):
    lx, ly = tfidf.shape
    dd = np.zeros([lx, lx])
    for x in range(lx):
        for y in range(lx):
            dx = tfidf[x, :]
            dy = tfidf[y, :]
            s = np.dot(dx, dy)/linalg.norm(dx)/linalg.norm(dy)
            dd[x, y] = 0 if (np.isnan(s)) or (x == y) else s
    return dd

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
        # save_table(output_file, docs, doc_doc_similarity)
        save_table_with_numeric_ids(output_file, docs, doc_doc_similarity)
        print(output_file)
    elif operation == 'tt':
        print('not gonna happen anytime soon')
    else:
        print('invalid operation')
