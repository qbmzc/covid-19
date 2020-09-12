import re

file_path = '/data/Cong/kdds.txt'
file_path_filter = '/data/Cong/kdds_filter.txt'

valid = re.compile(r'^13[0-3][0-9]{8}$')
with open(file_path_filter, 'w', encoding='utf-8') as w:
    with open(file_path, 'r', encoding='utf-8') as f:
        f_line = f.readlines()
        for l in f_line:
            if valid.match(l) is None:
                print(l)
                w.write(l)
                print('line')

print("over")
