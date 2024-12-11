import numpy as np

matrix = []

with open("/home/moosthuizen/AOC2024/day10/input.txt") as f:
    for l in f:
        matrix.append([int(char) for char in l.strip()])


data = np.array(matrix)

def paths_to_nine(data):
    rows, cols = data.shape
    def helper(fvids, to_val):
        tvids = []
        for from_val_indexes in fvids:
            to_val_indexes = []
            for idx in from_val_indexes:
                ids = [(idx[0] - 1, idx[1])]
                ids.append((idx[0] + 1, idx[1]))
                ids.append((idx[0], idx[1] - 1))
                ids.append((idx[0], idx[1] + 1))

                for id in ids:
                    if id[0] >= 0 and id[1] >= 0 and id[0] < rows and id[1] < cols:
                        if data[id] == to_val:
                            to_val_indexes.append(id)
            tvids.append(to_val_indexes)
            
        if to_val == 9:
            return tvids
        
        else:
            return helper(tvids, to_val+1)
    
    from_indexes = np.argwhere(data==0)
    from_indexes = [ [val] for val in from_indexes ]
    
    return helper(from_indexes, 1)

paths = paths_to_nine(data)

paths = [ set(path) for path in paths ]

nums =0
for path in paths:
    nums += len(path)

print(nums)
            
