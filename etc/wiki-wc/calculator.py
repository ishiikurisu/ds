import numpy

def build_term_frequency_matrix(docs):
    """
    Creates a term frequency matrix from a list of documents from the `document` script.
    Returns a list where each string is a term, and a numpy matrix where each line is for a term
    and each column is for a document.
    """
    terms = set()
    for doc in docs:
        for word in doc.words:
            terms.add(word)
    terms = sorted(terms)

    matrix = numpy.zeros([len(docs), len(terms)])
    for i, doc in enumerate(docs):
        for j, term in enumerate(terms):
            if term in doc.bag:
                matrix[i, j] = doc.bag[term]

    return terms, matrix

def calculate_tfidf(tf):
    """Calculates a TF.IDF matrix from a Document * Term matrix."""
    N, T = tf.shape
    tfidf = numpy.zeros_like(tf)

    for t in range(T):
        df = sum(map(lambda x: 1 if x > 0 else 0, tf[:, t]))
        for d in range(N):
            tfidf[d, t] = tf[d, t] * numpy.log(N/df)

    return tfidf

def calculate_document_similarity(tfidf):
    """Calculate the similarity between all documents in a TF.IDF D*T matrix."""
    return numpy.dot(tfidf, tfidf.T)

def calculate_term_similarity(tfidf):
    """Calculate the similarity between all terms in a TF.IDF D*T matrix."""
    return calculate_document_similarity(tfidf.T)

def export(matrix, filename):
    M, _ = matrix.shape
    with open(filename, 'w') as fp:
        for m in range(M):
            line = ';'.join(map(lambda x: '%.5f' % (x), matrix[m, :]))
            fp.write(line + '\n')
