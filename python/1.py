import re

def replace(x: str):
    numbers = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
    }

    for k, v in numbers.items():
        x = x.replace(k, v)
    return x

with open('../input/1.txt') as f:
    data = f.readlines()

data = [list(replace(line.strip())) for line in data]
res = 0

for line in data:
    l = 0
    r = len(line)-1
    while l <= r and not (line[r].isnumeric() and line[l].isnumeric()):
        if not line[l].isnumeric():
            l += 1
        if not line[r].isnumeric():
            r -= 1
    res += int(line[l] + line[r])

print(res)