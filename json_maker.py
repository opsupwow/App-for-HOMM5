f = open('monsters.csv', 'r')
data = f.readlines()

header = data[0].split(';')
header[-1] = header[-1][:-1]

res = {}
for d in data[1:]:
    line = d.replace('\n', '').split(';')
    prop = dict.fromkeys(header[1:])
    for i, h in enumerate(header[1:]):
        prop[h] = line[i + 1]
    res[line[0]] = prop

import json

with open('output.json', 'w', encoding='utf8') as f:
    json.dump(res, f)
