def too_many_fish(part2):
    with open("input.txt") as file:
        fish = [int(num) for num in file.readline().split(",")]

    state_array = [0 for _ in range(9)]

    for num in fish:
        state_array[num] += 1

    day = 0
    if part2:
        last_day = 256
    else:
        last_day = 80

    while day < last_day:
        day += 1
        new_state = [0 for _ in range(9)]

        for x in range(len(state_array)):
            if x > 0:
                new_state[x - 1] += state_array[x]
            else:
                new_state[6] += state_array[0]
                new_state[8] += state_array[0]
        state_array = new_state

    return sum(state_array)


f = open("output.txt", "w")
f.write(f'Part 1: {too_many_fish(0)}\n')
f.write(f'Part 2: {too_many_fish(1)}\n')
