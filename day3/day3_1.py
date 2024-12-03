import re

big_string = ""

with open("/home/moosthuizen/AOC2024/day3/input1.txt") as f:
    for line in f:
        big_string += line


dos = [m.end(0) for m in re.finditer(r'do\(\)', big_string)]
donts = [m.end(0) for m in re.finditer(r'don\'t\(\)', big_string)]

keep_indexes = [(0, donts[0])]

for j in range(len(dos)):

    gt = [ n for n, i in enumerate(donts) if i > dos[j] ]
    if not gt:
        keep_indexes.append((dos[j], len(big_string)))
    else:
        keep_indexes.append((dos[j], donts[gt[0]]))

keep_indexes_n = []
latest = keep_indexes[0]

for i in range(1, len(keep_indexes)):

    if latest[1] < keep_indexes[i][0]:
        keep_indexes_n.append(latest)
        latest = keep_indexes[i]
    else:
        latest = (latest[0], keep_indexes[i][1])

keep_indexes_n.append(latest)

new_string = ""
for i in keep_indexes_n:
    new_string += big_string[i[0]:i[1]]


pattern = r'mul\(\d+,\d+\)'
muls = re.findall(pattern, new_string)

multiplication = 0
for mul in muls:
    numbers = mul.split(",")
    n1 = int(numbers[0].split("(")[1])
    n2 = int(numbers[1].split(")")[0])
    multiplication += n1 * n2

print(multiplication)