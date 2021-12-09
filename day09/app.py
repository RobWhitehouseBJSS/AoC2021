with open("input.txt") as file:
    data = [[int(num) for num in line] for line in file.read().strip().split('\n')]

h = len(data)
w = len(data[0])


def neighbours(x, y):
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < h and 0 <= b < w]


def calc_basin(i, j, visited_points):
    if (i, j) not in visited_points:
        visited_points.append((i, j))
        return 1 + sum([calc_basin(m, n, visited_points) if 9 > data[m][n] > data[i][j] else 0 for m, n in neighbours(i, j)])
    else:
        return 0


risk = 0
basin_sizes = []
low_points = []

for x in range(h):
    for y in range(w):
        if all(data[cx][cy] > data[x][y] for cx, cy in neighbours(x, y)):
            risk += (data[x][y] + 1)
            low_points.append((x, y))

for lp in low_points:
    basin_sizes.append(calc_basin(lp[0], lp[1], []))

basin_sizes.sort(reverse=True)
p2_answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

f = open("output.txt", "w")
f.write(f'Part 1: {risk}\n')
f.write(f'Part 2: {p2_answer}')
