# Read in input
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
horizontal = 0
vertical = 0

for line in lines:
    command, num = line.split()
    if command == 'forward':
        horizontal += int(num)
    elif command == 'down':
        vertical += int(num)
    elif command == 'up':
        vertical -= int(num)

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
    command, num = line.split()
    if command == 'forward':
        horizontal += int(num)
        vertical += (aim * int(num))
    elif command == 'down':
        aim += int(num)
    elif command == 'up':
        aim -= int(num)

total = horizontal * vertical

f = open("output.txt", "a")
f.write(f'\nPart 2:\n')
f.write(f'Total: {total}\n')
f.write(f'Horizontal: {horizontal}\n')
f.write(f'Vertical: {vertical}\n')