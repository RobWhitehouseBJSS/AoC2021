# Read in input
file = open("input.txt", "r")
lines = file.readlines()

# Part 1
count = 0
prev = -1
current = -1

for line in lines:
    if 0 < prev < int(line):
        count += 1
    prev = int(line)

f = open("output.txt", "w")
f.write(f'Part 1: {count}\n')
f.close()

# Part 2
count = 0
prev = -1
current = -1

for i in range(len(lines)-2):
    current = int(lines[i])+int(lines[i+1])+int(lines[i+2])
    if 0 < prev < current:
        count += 1
    prev = current

f = open("output.txt", "a")
f.write(f'Part 2: {count}')
