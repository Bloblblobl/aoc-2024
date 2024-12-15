from bisect import insort
from collections import defaultdict

from utils import get_input

input = get_input()
HEIGHT = len(input)
WIDTH = len(input[0])


def parse_input():
    antenna_map = defaultdict(list)
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == ".":
                continue

            insort(antenna_map[c], (x, y))
    return antenna_map


def in_bounds(p):
    px, py = p
    return 0 <= px < WIDTH and 0 <= py < HEIGHT


def reverse(p):
    px, py = p
    return -px, -py


def add(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return p1x + p2x, p1y + p2y


def calculate_antinodes(antennas):
    antinodes = set()
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            a1 = antennas[i]
            a2 = antennas[j]
            diff = add(reverse(a1), a2)
            an1 = add(a1, reverse(diff))
            an2 = add(a2, diff)
            if in_bounds(an1):
                antinodes.add(an1)
            if in_bounds(an2):
                antinodes.add(an2)

    return antinodes


def part1():
    antenna_map = parse_input()
    antinodes = set()
    for frequency, antennas in antenna_map.items():
        antinodes |= calculate_antinodes(antennas)

    print(len(antinodes))


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
