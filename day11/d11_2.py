import concurrent.futures

with open("/home/moosthuizen/AOC2024/day11/input.txt") as f:
    numbers = [int(num) for num in f.readline().split()]

def expand_number(v):
    if v == 0:
        return [1]
    elif (len(str(v)) % 2 == 0):
        str_k = str(v)
        digts = len(str_k) // 2
        return [int(str_k[:digts]), int(str_k[digts:])]
    else:
        return [v * 2024]

def expand_numbers(og_numbers, expansions):
    current_numbers = og_numbers
    for _ in range(expansions):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(expand_number, current_numbers)
        current_numbers = [num for sublist in results for num in sublist]
    return current_numbers

for n in numbers:
    num = expand_numbers([n], 75)
    print(len(num))