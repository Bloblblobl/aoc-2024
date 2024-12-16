from utils import get_input

input = get_input()


def parse_input():
    disk_map = []
    filled_indices = []
    empty_indices = []
    file_id = 0
    for index, c in enumerate(input[0]):
        d = int(c)
        disk_end = len(disk_map)
        if index % 2 == 0:
            disk_map.extend([file_id] * d)
            for i in range(disk_end, disk_end + d):
                filled_indices.append(i)

            file_id += 1
        else:
            disk_map.extend(["."] * d)
            for i in range(disk_end, disk_end + d):
                empty_indices.append(i)

    return disk_map, filled_indices, empty_indices


def part1():
    disk_map, filled_indices, empty_indices = parse_input()
    total_file_size = len(filled_indices)
    while len(empty_indices):
        next_empty_index = empty_indices.pop(0)
        if next_empty_index >= total_file_size:
            break

        last_full_index = filled_indices.pop()
        disk_map[next_empty_index] = disk_map[last_full_index]

    disk_map = disk_map[:total_file_size]

    result = 0
    for i, file_id in enumerate(disk_map):
        result += i * file_id

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
