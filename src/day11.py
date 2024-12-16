from utils import get_input

input = get_input()


def parse_input():
    return list(map(int, input[0].split(" ")))


def blink(stone):
    if stone == 0:
        return [1]

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        midpoint = len(stone_str) // 2
        return [int(stone_str[:midpoint]), int(stone_str[midpoint:])]

    return [stone * 2024]


def part1():
    stones = parse_input()
    for _ in range(25):
        new_stones = []
        for stone in stones:
            new_stones.extend(blink(stone))
        stones = new_stones

    print(len(stones))


def cached_blink(stone, blinks, blink_cache):
    if (stone, blinks) in blink_cache:
        return blink_cache[(stone, blinks)]

    stone_str = str(stone)
    if blinks == 0:
        result = 1
    elif stone == 0:
        result = cached_blink(1, blinks - 1, blink_cache)
    elif len(stone_str) % 2 == 0:
        midpoint = len(stone_str) // 2
        stone1 = int(stone_str[:midpoint])
        stone2 = int(stone_str[midpoint:])
        result = cached_blink(stone1, blinks - 1, blink_cache) + cached_blink(
            stone2, blinks - 1, blink_cache
        )
    else:
        result = cached_blink(2024 * stone, blinks - 1, blink_cache)

    blink_cache[(stone, blinks)] = result
    return result


def part2():
    stones = parse_input()
    blink_cache = {}
    result = 0
    for stone in stones:
        result += cached_blink(stone, 75, blink_cache)

    print(result)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
