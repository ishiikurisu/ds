import util
import sys
import os
import cvextraction
import similarity

def extract_cv_data(config):
    # Getting all CV
    p = config['pwd'] + config['cv']
    all = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
    all_cv = [p+f for f in all if '.xml' in f]

    # Analyzing CV
    ka_data = {} # knowledge area data
    names = {}
    how_many = {}
    for cv in all_cv:
        root = cvextraction.get_cv_root(cv)
        if root is not None:
            stuff = [
                cvextraction.get_fields_from_complete_articles(root),
                cvextraction.get_fields_from_conference_articles(root),
                cvextraction.get_fields_from_book_chapters(root),
                cvextraction.get_fields_from_phd(root),
                cvextraction.get_fields_from_masters(root)
            ]

            names[cv] = cvextraction.get_name(root)
            how_many[cv] = [len(it) for it in stuff]
            ka_data[cv] = sum(stuff, [])

    # Similarity Analysis
    ka_data_file = config['pwd'] + 'cv.csv'
    cvextraction.generate_similarity_table(ka_data, ka_data_file)
    print(ka_data_file)

    # Metadata for further studies
    metadata_file = config['pwd'] + 'cv_meta.csv'
    cvextraction.generate_metadata_table(names, ka_data, metadata_file)
    print(metadata_file)

    # Statistics from CV data
    stats_file = config['pwd'] + 'stats.csv'
    cvextraction.generate_stats_table(how_many, stats_file)
    print(stats_file)

    return ka_data_file

def analyze_similarity(input_file, operation):
    docs, terms, tf = similarity.load_table(input_file)
    tfidf = similarity.calculate_tfidf(tf)

    if operation == 'dd':
        doc_doc_similarity = similarity.calculate_dd(tfidf)
        output_file = input_file.replace('.csv', '_dd.csv')
        # save_table(output_file, docs, doc_doc_similarity)
        similarity.save_table_with_numeric_ids(output_file, docs, doc_doc_similarity)
        print(output_file)
    elif operation == 'tt':
        print('not gonna happen anytime soon')
    else:
        print('invalid operation')

    return output_file

if __name__ == '__main__':
    config = util.load_config(sys.argv[1])
    operation = sys.argv[2]
    cv_data = extract_cv_data(config)
    cv_dd = analyze_similarity(cv_data, operation)
