def map_function(part2):
    with open("input.txt") as file:
        data = [list(map(int, line.strip().replace('->', ',').split(','))) for line in file]

    x_max = max(max([(d[0], d[2]) for d in data])) + 1
    y_max = max(max([(d[1], d[3]) for d in data])) + 1

    grid = [[0 for i in range(x_max)] for j in range(y_max)]

    for x1, y1, x2, y2 in data:
        x_min = min(x1, x2)
        y_min = min(y1, y2)
        x_dif = abs(x1 - x2)
        y_dif = abs(y1 - y2)

        if x_dif == 0:
            for i in range(y_dif + 1):
                grid[y_min + i][x1] += 1
        elif y_dif == 0:
            for i in range(x_dif + 1):
                grid[y1][x_min + i] += 1
        elif part2:
            if x1 > x2:
                x_dir = -1
            else:
                x_dir = 1
            if y1 > y2:
                y_dir = -1
            else:
                y_dir = 1
            for i in range(x_dif + 1):
                grid[y1 + i * y_dir][x1 + i * x_dir] += 1

    total = 0
    for row in grid:
        for num in row:
            if num >= 2:
                total += 1
    return total


part1_total = map_function(0)
part2_total = map_function(1)

f = open("output.txt", "w")
f.write(f'Part 1: {part1_total}\n')
f.write(f'Part 2: {part2_total}\n')
