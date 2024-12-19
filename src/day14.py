from utils import get_input

input = get_input()


def parse_input():
    robots = []
    for line in input:
        p_str, v_str = line[2:].split(" v=")
        p = tuple(int(d) for d in p_str.split(","))
        v = tuple(int(d) for d in v_str.split(","))
        robots.append((p, v))

    return robots


def sum_robots_in_quadrant(robots_end, quadrant):
    top_left, bottom_right = quadrant
    tx, ty = top_left
    bx, by = bottom_right
    result = 0
    for rx, ry in robots_end:
        result += tx <= rx <= bx and ty <= ry <= by

    return result


def calculate_safety_factor(robots_end, w, h):
    midw = w // 2
    midh = h // 2
    xlo, xhi = midw - 1, midw + 1
    ylo, yhi = midh - 1, midh + 1
    quadrants = [
        ((0, 0), (xlo, ylo)),
        ((xhi, 0), (w - 1, ylo)),
        ((0, yhi), (xlo, h - 1)),
        ((xhi, yhi), (w - 1, h - 1)),
    ]
    safety_factor = 1
    for quadrant in quadrants:
        safety_factor *= sum_robots_in_quadrant(robots_end, quadrant)

    return safety_factor


def part1():
    w = 101
    h = 103
    s = 100
    robots = parse_input()
    robots_end = []
    for p, v in robots:
        px, py = p
        vx, vy = v
        robots_end.append(((px + vx * s) % w, (py + vy * s) % h))

    safety_factor = calculate_safety_factor(robots_end, w, h)

    print(safety_factor)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
