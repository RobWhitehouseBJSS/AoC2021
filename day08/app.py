# Part 1
def part_1(data):
    count = 0
    for value in data:
        if len(value) in [2, 4, 3, 7]:
            count += 1
    return count


# Part 2
def part_2(data):
    for data_item in data:
        data_item = frozenset(data_item)
        if len(data_item) == 2:
            one = data_item
        elif len(data_item) == 4:
            four = data_item
        elif len(data_item) == 3:
            seven = data_item
        elif len(data_item) == 7:
            eight = data_item
    for data_item in data:
        # 0, 6, 9
        data_item = frozenset(data_item)
        if len(data_item) == 6:
            if len(data_item - four) == 2:
                nine = data_item
            elif len(data_item - seven) == 3:
                zero = data_item
            else:
                six = data_item
        # 2, 3, 5
        elif len(data_item) == 5:
            if len(data_item - seven) == 2:
                three = data_item
            elif len(data_item - four) == 2:
                five = data_item
            else:
                two = data_item
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def check_length(item, length):
    if len(item) == length:
        return item


def calc_total(p2):
    count = 0
    with open("input.txt") as file:
        for line in file:
            signal_patterns, output_values = line.strip().split('|')
            if p2:
                solution = part_2(signal_patterns.split())
                decoded_num = []
                for value in output_values.strip().split():
                    decoded_num.append(solution.index(frozenset(value)))
                count += int("".join(map(str, decoded_num)))
            else:
                count += part_1(output_values.split())
    return count


part1_answer = calc_total(0)
part2_answer = calc_total(1)
f = open("output.txt", "w")
f.write(f'Part 1: {part1_answer}\n')
f.write(f'Part 1: {part2_answer}')