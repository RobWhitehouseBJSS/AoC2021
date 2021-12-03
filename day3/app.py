with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

counts = [0] * len(lines[0])
gamma = epsilon = ""

for line in lines:
    for i in range(len(line)):
        if line[i] == '1':
            counts[i] += 1

for x in counts:
    if x > (len(lines) / 2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

power_consumption = int(gamma, 2) * int(epsilon, 2)

f = open("output.txt", "w")
f.write(f'Part 1: {power_consumption}')


# Part 2
def filter_nums(dataset, param):
    pos = 0
    while len(dataset) > 1:
        ones, zeroes = [], []
        for line in dataset:
            if line[pos] == '1':
                ones.append(line)
            else:
                zeroes.append(line)
        pos += 1

        sorted_by_len = sorted((zeroes, ones), key=len)
        print(len(ones))
        print(len(zeroes))

        if param == "CO2":
            dataset = sorted_by_len[0]
        elif param == "O2":
            dataset = sorted_by_len[1]
    return int(dataset[0], 2)


with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

co2 = filter_nums(lines, "CO2")
o2 = filter_nums(lines, "O2")

life_support_rating = co2 * o2

f = open("output.txt", "a")
f.write(f'\nPart 2: {life_support_rating}\n')
