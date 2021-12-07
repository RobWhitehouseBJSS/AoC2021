import statistics


def gauss(x):
    return x * (x + 1) // 2


with open("input.txt") as file:
    data = list(map(int, file.readline().strip().split(',')))

median = round(statistics.median(data))
p1_fuel_consumption = sum(abs(num - median) for num in data)

mean = round(statistics.mean(data))
p2_fuel_consumption = sum(gauss(abs(num - mean)) for num in data)

f = open("output.txt", "w")
f.write(f'Part 1: {p1_fuel_consumption}\n')
f.write(f'Part 2: {p2_fuel_consumption}')
