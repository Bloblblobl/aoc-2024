from utils import get_input

input = get_input()
HEIGHT = len(input)
WIDTH = len(input[0])
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_input():
    top_map = [[int(elev) for elev in line] for line in input]
    trailheads = []
    for y, line in enumerate(top_map):
        for x, c in enumerate(line):
            if c == 0:
                trailheads.append((x, y))

    return top_map, trailheads


def in_bounds(pos):
    px, py = pos
    return 0 <= px < WIDTH and 0 <= py < HEIGHT


def move(pos, direction):
    px, py = pos
    dx, dy = direction
    return px + dx, py + dy


def elev_at(m, pos):
    px, py = pos
    return m[py][px]


def get_valid_steps(top_map, pos):
    valid_steps = []
    elev = elev_at(top_map, pos)
    for direction in DIRECTIONS:
        neighbor = move(pos, direction)
        if in_bounds(neighbor) and elev_at(top_map, neighbor) == elev + 1:
            valid_steps.append(neighbor)

    return valid_steps


def find_paths(top_map, trailhead):
    starting_path = [trailhead]
    q = [starting_path]
    valid_paths = []

    while len(q):
        path = q.pop(0)
        last_pos = path[-1]
        for valid_step in get_valid_steps(top_map, last_pos):
            next_path = path + [valid_step]
            if len(next_path) == 10:
                valid_paths.append(next_path)
            else:
                q.append(next_path)

    return valid_paths


def part1():
    top_map, trailheads = parse_input()
    result = 0
    for trailhead in trailheads:
        valid_paths = find_paths(top_map, trailhead)
        trailends = set(path[-1] for path in valid_paths)
        result += len(trailends)

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
