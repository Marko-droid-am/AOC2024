line = []

with open("/home/moosthuizen/AOC2024/day9/input.txt") as f:
    for l in f:
        line.extend([int(char) for char in l.strip()])



files = [file_size for idx, file_size in enumerate(line) if idx % 2 == 0]
gaps = [gap_size for idx, gap_size in enumerate(line) if idx % 2 != 0]

files = [(id, f) for id, f in enumerate(files)]
files_copy = files.copy()

memory_map = {}
holes = []
for id, file_size in files[::-1]:
    if id > 0:
        for idx, gap in enumerate(gaps):
            if not id > idx:
                break
            if gap >= file_size:
                if idx not in memory_map:
                    memory_map[idx] = []
                memory_map[idx].append((id, file_size))
                gaps[idx] -= file_size
                holes.append((id, file_size))

                # Delete the file from files
                index = files_copy.index((id, file_size))
                del files_copy[index]

                break

gaps_n = [(0, f) for id, f in enumerate(gaps)]

# Create a new list [files_copy[0], memory_map[0], gaps[0], files_copy[1], memory_map[1], gaps[1], ...]
new_files_map = []
for i in range(len(files)):
    # Check if there is a file in files_copy with id == i
    file = None
    for f in files_copy:
        if f[0] == i:
            file = f
            break

    if file is not None:
        new_files_map.append(file)

    hole = None
    for h in holes:
        if h[0] == i:
            hole = h
            break

    if hole is not None:
        new_files_map.append((0, hole[1]))

    if i in memory_map:
        new_files_map.extend(memory_map[i])


    if i < len(gaps_n):
        new_files_map.append(gaps_n[i])


checksum = 0
location = 0
for file in new_files_map:
    for i in range(file[1]):
        checksum += file[0] * location
        location += 1

print(checksum)
