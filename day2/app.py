# Read in input
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
horizontal = 0
vertical = 0

for line in lines:
    if line[0] == 'f':
        horizontal = horizontal + int(line[-1])
    elif line[0] == 'd':
        vertical = vertical + int(line[-1])
    elif line[0] == 'u':
        vertical = vertical - int(line[-1])

total = horizontal * vertical

f = open("output.txt", "w")
f.write(f'Part 1:\n')
f.write(f'Total: {total}\n')
f.write(f'Horizontal: {horizontal}\n')
f.write(f'Vertical: {vertical}\n')

# Part 2
horizontal = 0
vertical = 0
aim = 0

for line in lines:
    if line[0] == 'f':
        horizontal = horizontal + int(line[-1])
        vertical = vertical + (aim * int(line[-1]))
    elif line[0] == 'd':
        aim = aim + int(line[-1])
    elif line[0] == 'u':
        aim = aim - int(line[-1])

total = horizontal * vertical

f = open("output.txt", "a")
f.write(f'\nPart 2:\n')
f.write(f'Total: {total}\n')
f.write(f'Horizontal: {horizontal}\n')
f.write(f'Vertical: {vertical}\n')