import math

from utils import get_input


input = get_input()


def sign(num):
    return int(math.copysign(1, num))


def is_report_safe(levels):
    last_diff = None
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if not (1 <= abs(diff) <= 3):
            return False

        if last_diff is not None and sign(diff) != sign(last_diff):
            return False

        last_diff = diff

    return True


def part1():
    safe_count = 0
    for line in input:
        levels = [int(level) for level in line.split(" ")]
        if is_report_safe(levels):
            safe_count += 1

    print(safe_count)


def part2():
    safe_count = 0
    for line in input:
        levels = [int(level) for level in line.split(" ")]
        level_permutations = [levels]
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i + 1:]
            level_permutations.append(new_levels)

        if any(is_report_safe(lp) for lp in level_permutations):
            safe_count += 1
            
    print(safe_count)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
