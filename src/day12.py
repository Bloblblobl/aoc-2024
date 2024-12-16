from random import randint

from utils import get_input

input = get_input()
HEIGHT = len(input)
WIDTH = len(input[0])
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_input():
    map_coords = []
    map_chars = []
    for y, line in enumerate(input):
        map_line = []
        for x, c in enumerate(line):
            map_coords.append((x, y))
            map_line.append(c)
        map_chars.append(map_line)
    return map_coords, map_chars


def char_at(m, pos):
    px, py = pos
    return m[py][px]


def in_bounds(pos):
    px, py = pos
    return 0 <= px < WIDTH and 0 <= py < HEIGHT


def move(pos, direction):
    px, py = pos
    dx, dy = direction
    return px + dx, py + dy


def explore_region(unvisited, map_chars, pos, symbol):
    expanded_region = []
    expanded_perimeter = 0
    for dir in DIRECTIONS:
        neighbor = move(pos, dir)
        if in_bounds(neighbor) and char_at(map_chars, neighbor) == symbol:
            if neighbor in unvisited:
                expanded_region.append(neighbor)
        else:
            expanded_perimeter += 1

    return expanded_region, expanded_perimeter


def map_region(unvisited, map_chars):
    start_pos = unvisited.pop(randint(0, len(unvisited) - 1))
    symbol = char_at(map_chars, start_pos)
    region = {"symbol": symbol, "coords": [start_pos], "perimeter": 0}
    q = [start_pos]
    while len(q):
        curr_pos = q.pop(0)
        expanded_region, expanded_perimeter = explore_region(
            unvisited, map_chars, curr_pos, symbol
        )
        region["coords"].extend(expanded_region)
        region["perimeter"] += expanded_perimeter
        for pos in expanded_region:
            unvisited.remove(pos)
        q.extend(expanded_region)

    return region


def part1():
    map_coords, map_chars = parse_input()
    unvisited = map_coords
    result = 0
    while len(unvisited):
        region = map_region(unvisited, map_chars)
        result += len(region["coords"]) * region["perimeter"]

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
