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


def parse_input2():
    disk_map = []
    filled_blocks = []
    empty_blocks = []
    file_id = 0
    for index, c in enumerate(input[0]):
        d = int(c)
        disk_end = len(disk_map)
        if index % 2 == 0:
            disk_map.extend([file_id] * d)
            filled_blocks.append((disk_end, d))
            file_id += 1
        else:
            disk_map.extend(["."] * d)
            empty_blocks.append((disk_end, d))

    return disk_map, filled_blocks, empty_blocks


def part2():
    disk_map, filled_blocks, empty_blocks = parse_input2()
    for filled_index, filled_count in reversed(filled_blocks):
        file_id = disk_map[filled_index]
        if filled_index < empty_blocks[0][0]:
            break

        empty_block_index = 0
        while empty_block_index < len(empty_blocks):
            empty_index, empty_count = empty_blocks[empty_block_index]
            if filled_index < empty_index:
                break

            if empty_count == filled_count:
                for i in range(filled_count):
                    disk_map[empty_index + i] = file_id
                    disk_map[filled_index + i] = "."

                del empty_blocks[empty_block_index]
                break

            elif filled_count < empty_count:
                for i in range(filled_count):
                    disk_map[empty_index + i] = file_id
                    disk_map[filled_index + i] = "."

                remaining = empty_count - filled_count
                empty_blocks[empty_block_index] = (
                    empty_index + filled_count,
                    remaining,
                )
                break

            empty_block_index += 1

    result = 0
    for i, c in enumerate(disk_map):
        if c == ".":
            continue
        result += i * int(c)

    print(result)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
