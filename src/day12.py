from random import randint

from utils import get_input

input = get_input()
HEIGHT = len(input)
WIDTH = len(input[0])

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


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


def initialize_perimeter():
    return {UP: [], RIGHT: [], DOWN: [], LEFT: []}


def explore_region2(unvisited, map_chars, pos, symbol):
    expanded_region = []
    perimeter_directions = []
    for dir in DIRECTIONS:
        neighbor = move(pos, dir)
        if in_bounds(neighbor) and char_at(map_chars, neighbor) == symbol:
            if neighbor in unvisited:
                expanded_region.append(neighbor)
        else:
            perimeter_directions.append(dir)

    return expanded_region, perimeter_directions


def map_region2(unvisited, map_chars):
    start_pos = unvisited.pop(randint(0, len(unvisited) - 1))
    symbol = char_at(map_chars, start_pos)
    region = {
        "symbol": symbol,
        "coords": [start_pos],
        "perimeter": initialize_perimeter(),
    }
    q = [start_pos]
    while len(q):
        curr_pos = q.pop(0)
        expanded_region, perimeter_directions = explore_region2(
            unvisited, map_chars, curr_pos, symbol
        )
        region["coords"].extend(expanded_region)
        for dir in perimeter_directions:
            region["perimeter"][dir].append(curr_pos)
        for pos in expanded_region:
            unvisited.remove(pos)
        q.extend(expanded_region)

    return region


def get_orthogonals(dir):
    return {
        UP: [LEFT, RIGHT],
        RIGHT: [UP, DOWN],
        DOWN: [LEFT, RIGHT],
        LEFT: [UP, DOWN],
    }[dir]


def calculate_perimeter_sides(region):
    side_groups = initialize_perimeter()
    perimeter = region["perimeter"]
    for dir in DIRECTIONS:
        orthogonals = get_orthogonals(dir)
        visited = set()
        for pos in sorted(perimeter[dir]):
            if pos in visited:
                continue
            group = []
            for orthogonal in orthogonals:
                cursor = pos
                while cursor in perimeter[dir]:
                    group.append(cursor)
                    visited.add(cursor)
                    cursor = move(cursor, orthogonal)
            side_groups[dir].append(group)

    return side_groups


def part2():
    map_coords, map_chars = parse_input()
    unvisited = map_coords
    result = 0
    while len(unvisited):
        region = map_region2(unvisited, map_chars)
        perimeter_sides = calculate_perimeter_sides(region)
        side_count = sum(len(side) for side in perimeter_sides.values())
        result += len(region["coords"]) * side_count

    print(result)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
