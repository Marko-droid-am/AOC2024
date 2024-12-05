import numpy as np

map_d = {
'X' : 3,
'M' : 6,
'A' : 9,
'S' : 12}

lines = []

with open("/home/moosthuizen/AOC2024/day4/input.txt") as f:
    for line in f:
        r = [] 
        for char in line.strip():
            if char in map_d:
                r.append(map_d[char])
            else:
                r.append(1)
        lines.append(r)

data = np.array(lines)

mats_dict = {}

mats_dict[0] = np.array([[map_d['X'], map_d['M'], map_d['A'], map_d['S']],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]])

mats_dict[1] = mats_dict[0][:, ::-1]

mats_dict[2] = np.rot90(mats_dict[0],1)
mats_dict[3] = np.rot90(mats_dict[0][:, ::-1],1)

mat3 = np.array([[map_d['X'], 0, 0, 0],
                 [0, map_d['M'], 0, 0],
                 [0, 0, map_d['A'], 0],
                 [0, 0, 0, map_d['S']]])

for i in range(4):
    mats_dict[i+4] = np.rot90(mat3, i)


rows, cols = data.shape
seq_len = 4

count = 0

data_padded = np.pad(data, [(0, 4), (0, 4)], mode='constant', constant_values=1)
padded_rows, padded_cols = data_padded.shape

for mat in mats_dict.values():
    for row in range(rows + 1):
        for col in range(cols + 1):
            sub_mat = data_padded[row:row + seq_len, col:col + seq_len]
        
            eq_mat = np.equal(sub_mat, mat)
            if np.sum(eq_mat) == 4:
                count += 1
            
print(count)
# 2639