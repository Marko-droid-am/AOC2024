import numpy as np

data = np.loadtxt("/home/moosthuizen/aoc2024/day1/input1.txt")

list1 = data[:, 0]
list2 = data[:, 1]

unique, counts = np.unique(list1, return_counts=True)
count_in_list2 = [np.count_nonzero(list2 == i) for i in unique]

sum = 0

for u, c, c2 in zip(unique, counts, count_in_list2):
    sum += (u*c*c2)


print(sum)