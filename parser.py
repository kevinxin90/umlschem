import csv
import os


def load_data(data_folder):
    # load cellular component and biological proces info from semmed neo4j
    nodes_path = os.path.join(data_folder, "nodes_neo4j.csv")
    with open(nodes_path) as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader)
        for _item in csv_reader:
            semantic = _item[-2]
            if semantic == 'chemical_substance':
                yield {'_id': _item[-1],
                       'umls': _item[-1].split(':')[-1],
                       'name': _item[1]}

