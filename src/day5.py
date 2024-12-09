from collections import defaultdict

from utils import get_input

input = get_input()


def parse_input():
    parsing_rules = True
    dependencies = defaultdict(set)
    orderings = []

    for line in input:
        if not line.strip():
            parsing_rules = False
            continue

        if parsing_rules:
            dependency, target = line.split("|")
            dependencies[target].add(dependency)
        else:
            orderings.append(line.split(","))

    return dict(dependencies), orderings


def part1():
    dependencies, orderings = parse_input()
    result = 0
    for ordering in orderings:
        is_valid = True
        invalid_nums = set()
        for num in ordering:
            if num in invalid_nums:
                is_valid = False
                break

            invalid_nums |= dependencies.get(num, set())

        if not is_valid:
            continue

        result += int(ordering[len(ordering) // 2])

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
