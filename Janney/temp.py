from tools import local_file_util

file = [line.split('\t') for line in local_file_util.readFile('data/orgin_train_data.tsv')]

s = set([line[4] for line in file])