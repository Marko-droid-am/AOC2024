import multiprocessing as mp

with open("/home/moosthuizen/AOC2024/day11/input.txt") as f:
    numbers = [int(num) for num in f.readline().split()]

def expand_number(v):
    if v == 0:
        return [1]
    elif len(str(v)) % 2 == 0:
        str_k = str(v)
        digts = len(str_k) // 2
        return [int(str_k[:digts]), int(str_k[digts:])]
    else:
        return [v * 2024]

def expand_numbers(og_numbers, expansions):
    def helper(numbers, expansions):
        with mp.Pool(mp.cpu_count()) as pool:
            results = pool.map(expand_number, numbers)
        
        new_numbers = [item for sublist in results for item in sublist]
        
        if expansions == 1:
            return new_numbers
        else:
            return helper(new_numbers, expansions - 1)

    return helper(og_numbers, expansions)

num = expand_numbers(numbers, 75)
print(len(num))
# print(num)