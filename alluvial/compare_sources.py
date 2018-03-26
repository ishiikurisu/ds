import sys
import flow
import collect_from_source as cfs
import collect_from_raw as cfr
import excel

def get_ids_from_source(config):
    _, data = cfs.get_stuff(config)
    return set(data.keys())

def get_ids_from_committee(config):
    ids = excel.get_ids_from_csv_table(config['working'] + 'emerson/emerson.csv')
    return set(ids)

def get_ids_from_raw(config):
    _, data = cfr.get_stuff(config)
    return set(data.keys())

def save_stuff(config, src_ids, cmt_ids):
    all_ids = src_ids | cmt_ids
    with open(config['working'] + 'emerson/compare.csv', 'w') as fp:
        fp.write("id\tsrc\traw\n")
        for current_id in all_ids:
            fp.write("'{0}'\t{1}\t{2}\n".format(current_id,
                                                1 if current_id in src_ids else 0,
                                                1 if current_id in cmt_ids else 0))

if __name__ == '__main__':
    config = flow.load_config(sys.argv[1])
    source_ids = get_ids_from_source(config)
    raw_ids = get_ids_from_raw(config)
    save_stuff(config, source_ids, raw_ids)
