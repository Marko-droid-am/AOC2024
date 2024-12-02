import numpy as np

data = np.loadtxt("/home/moosthuizen/aoc2024/day1/input1.txt")

list1 = data[:, 0]
list2 = data[:, 1]

list1_sorted = np.sort(list1)
list2_sorted = np.sort(list2)

list_difference = abs(list2_sorted-list1_sorted)
sum_of_diff = np.sum(list_difference)

print(sum_of_diff)