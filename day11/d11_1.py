with open("/home/moosthuizen/AOC2024/day11/input.txt") as f:
    numbers = [int(num) for num in f.readline().split()]

def expand_numbers(og_numbers, expansions):
    def helper(numbers, expansions):
        new_numbers = []
        for v in numbers:
            if v == 0:
                new_numbers.append(1)
            elif (len(str(v)) % 2 == 0):
                str_k = str(v)
                k = [char for char in str_k]
                
                digts = len(str_k)//2
                new_numbers.append(int(str_k[:digts]))
                new_numbers.append(int(str_k[digts:]))
            else:
                new_numbers.append(v * 2024)
        if expansions == 1:
            return new_numbers
        else:
            return helper(new_numbers, expansions - 1)


    return helper(og_numbers, expansions)

num = expand_numbers(numbers, 75)
print(len(num))
# print(num)

