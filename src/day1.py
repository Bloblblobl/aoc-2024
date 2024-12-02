import bisect

from utils import get_input


SEPARATOR = "   "

input = get_input()


def part1():
    locations1 = []
    locations2 = []
    for line in input:
        loc1, loc2 = line.split(SEPARATOR)
        bisect.insort(locations1, int(loc1))
        bisect.insort(locations2, int(loc2))

    result = 0
    for i in range(len(locations1)):
        result += abs(locations1[i] - locations2[i])

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
