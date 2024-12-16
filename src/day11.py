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


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
