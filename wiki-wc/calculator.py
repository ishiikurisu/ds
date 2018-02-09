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

    print([len(docs), len(terms)])
    matrix = numpy.zeros([len(docs), len(terms)])
    for i, doc in enumerate(docs):
        for j, term in enumerate(terms):
            if term in doc.bag:
                matrix[i, j] = doc.bag[term]

    return terms, matrix
