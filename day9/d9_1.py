line = []

with open("/home/moosthuizen/AOC2024/day9/input.txt") as f:
    for l in f:
        line.extend([int(char) for char in l.strip()])



files = [file_size for idx, file_size in enumerate(line) if idx % 2 == 0]
gaps = [gap_size for idx, gap_size in enumerate(line) if idx % 2 != 0]

files = [(id, f) for id, f in enumerate(files)]

# Create a dict:
# id: [(start, end), (start, end), (start, end)]

memory_map = {}
for idx, gap in enumerate(gaps):
    memory_map[idx] = []
    if idx >= files[-1][0]:
        break
    while gap > 0:
        if gap >= files[-1][1]:
            memory_map[idx].append(files[-1])
            # files delete last element
            gap -= files[-1][1]
            del files[-1]
        else:
            memory_map[idx].append((files[-1][0], gap))
            files[-1] = (files[-1][0], files[-1][1]-gap)
            gap = 0
            
new_files_map = []
# new_files_map = [files[0], memory_map[0], files[1], memory_map[1], files[2], ...]
for idx, file in enumerate(files):
    new_files_map.append(file)
    if idx in memory_map:
        new_files_map.extend(memory_map[idx])
        memory_map.pop(idx)

for key in memory_map:
    new_files_map.extend(memory_map[key])

checksum = 0
location = 0
for file in new_files_map:
    for i in range(file[1]):
        checksum += file[0] * location
        location += 1

print(checksum)

# That's not the right answer; your answer is too low. 
# 6415184585987
# 5236082827867



6415184586041