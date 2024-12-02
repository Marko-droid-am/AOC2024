def asc_or_dsc(l):
    asc = all(1 <= i <= 3 for i in l)
    dsc = all(-3 <= i <= -1 for i in l)
    return asc or dsc

number = 0
with open("/home/moosthuizen/aoc2024/day2/input2_1.txt") as f:
    for line in f:
        parts = [int(i) for i in line.split()]
        l = [parts[i+1] - parts[i] for i in range(len(parts)-1)]

        if asc_or_dsc(l):
            number += 1
        else:
            for i in range(len(parts)):
                parts_without_i = parts[:i] + parts[i+1:]
                l_n = [parts_without_i[j+1] - parts_without_i[j] for j in range(len(parts_without_i)-1)]
                if asc_or_dsc(l_n):
                    number += 1
                    break

print(number)