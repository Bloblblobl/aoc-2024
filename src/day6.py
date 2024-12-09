from utils import get_input

input = get_input()

OBSTACLE = "#"
GUARD = "^"

HEIGHT = len(input)
WIDTH = len(input[0])
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
ROTATION = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
}


def parse_input():
    obstacles = set()
    guard_position = None
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == GUARD:
                guard_position = (x, y)
            elif c == OBSTACLE:
                obstacles.add((x, y))

    return obstacles, guard_position, UP


def move(gx, gy, dx, dy):
    return gx + dx, gy + dy


def out_of_bounds(gx, gy):
    return gx < 0 or gx > WIDTH - 1 or gy < 0 or gy > HEIGHT - 1


def part1():
    obstacles, guard_position, guard_direction = parse_input()

    guard_path = {guard_position}
    while guard_position is not None:
        next_move = move(*guard_position, *guard_direction)
        if out_of_bounds(*next_move):
            guard_position = None
        elif next_move in obstacles:
            guard_direction = ROTATION[guard_direction]
        else:
            guard_position = next_move
            guard_path.add(guard_position)

    print(len(guard_path))


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
