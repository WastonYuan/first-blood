from tools import local_file_util


e2gdp_list = [(l[1].strip(), l[2]) for l in [l.split('\t') for l in local_file_util.readFile('data/Jack/country_info.tsv')]]
e2c = local_file_util.readFile('data/Jack/country_e2c.txt')

e2c_dict = dict(zip([e2c[i] for i in range(0, e2c.__len__(), 3)], [e2c[i] for i in range(2, e2c.__len__(), 3)]))

local_file_util.writeFile('data/Jack/country_gdp.tsv', [l[0] + '\t' + l[1] for l in [(e2c_dict[e2gdp[0]], e2gdp[1]) for e2gdp in e2gdp_list]])