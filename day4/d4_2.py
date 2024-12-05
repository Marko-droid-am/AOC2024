import numpy as np

lines = []

mat1 = np.array([['M', '0', 'S'],
                 ['0', 'A', '0'],
                 ['M', '0', 'S']])
mats_dict = {}
for i in range(4):
    mats_dict[i] = np.rot90(mat1, i)

with open("/home/moosthuizen/AOC2024/day4/input.txt") as f:
    for line in f:
        r = [] 
        for char in line.strip():
            if char in ['M', 'A', 'S']:
                r.append(char)
            else:
                r.append('.')
        lines.append(r)

data = np.array(lines)
rows, cols = data.shape

seq_len = mat1.shape[0]
true_count = 5
count = 0

for mat in mats_dict.values():
    for row in range(rows - seq_len + 1):
        for col in range(cols - seq_len + 1):
            sub_mat = data[row:row + seq_len, col:col + seq_len]
            eq_mat = np.equal(sub_mat, mat)
            if np.sum(eq_mat) == true_count:
                count += 1

print(count)