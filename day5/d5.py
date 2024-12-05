rules = []
updates = []

with open("/home/moosthuizen/AOC2024/day5/input.txt") as f:
    for line in f:
        # If line == eg '99|28', then split into [int('99'), int('28')]
        if '|' in line:
            rules.append([int(x) for x in line.split('|')])
        elif line != '\n':
            updates.append([int(x) for x in line.split(',')])


updates_fixed = []
sumv = 0

for update in updates:
    must_update = False
    rules_in_update = []
    for rule in rules:
        
        if rule[0] in update and rule[1] in update:
            rules_in_update.append(rule)
            if update.index(rule[0]) > update.index(rule[1]):
                must_update = True
    
    if must_update:
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if [update[j], update[i]] in rules_in_update:
                    # Move the element at index j to index i
                    update.insert(i, update.pop(j))

        sumv += update[len(update)//2]

    updates_fixed.append(update)

# Get the values at the middle index of each update
middle_values = [update[len(update)//2 -1] for update in updates_fixed if len(update) % 2 == 1]

print(sumv)




        