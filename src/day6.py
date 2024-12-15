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


def simulate_path(obstacles, starting_state, state_history, check_for_loops):
    loops = 0
    is_looping = False

    starting_pos = state_history[0][0] if len(state_history) else starting_state[0]

    state = starting_state
    while not out_of_bounds(*state[0]):
        state_history.append(state)
        pos, direction = state
        next_pos = move(*pos, *direction)
        if next_pos in obstacles:
            direction = ROTATION[direction]
            next_state = (pos, direction)
        else:
            if (
                check_for_loops
                and not out_of_bounds(*next_pos)
                and next_pos not in obstacles
                and next_pos != starting_pos
                and next_pos not in [pos for pos, _ in state_history]
            ):
                loops += can_loop(obstacles, next_pos, state, list(state_history))
            next_state = (next_pos, direction)

        if next_state in state_history:
            is_looping = True
            break

        state = next_state

    return loops, is_looping


def can_loop(obstacles, new_obstacle, current_state, state_history):
    _, is_looping = simulate_path(
        obstacles=obstacles | {new_obstacle},
        starting_state=current_state,
        state_history=list(state_history),
        check_for_loops=False,
    )
    return is_looping


def part2():
    obstacles, starting_pos, direction = parse_input()
    starting_state = (starting_pos, direction)
    state_history = []
    loops, _ = simulate_path(
        obstacles=obstacles,
        starting_state=starting_state,
        state_history=state_history,
        check_for_loops=True,
    )
    print(loops)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
