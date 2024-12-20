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


def get_quadrants(w, h):
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
    return quadrants


def calculate_safety_factor(robots_end, w, h):
    quadrants = get_quadrants(w, h)
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


def move_robots(robots, s, w, h):
    robots_end = []
    for p, v in robots:
        px, py = p
        vx, vy = v
        robots_end.append(((px + vx * s) % w, (py + vy * s) % h))
    return robots_end


def dump_robots(robots_end, w, h):
    robots_map = [["." for _ in range(w)] for _ in range(h)]

    for rx, ry in robots_end:
        if robots_map[ry][rx] == ".":
            robots_map[ry][rx] = 1
        else:
            robots_map[ry][rx] += 1

    with open("robots.txt", "w") as f:
        for line in robots_map:
            f.write("".join(str(c) for c in line) + "\n")


def part2():
    w = 101
    h = 103
    robots = parse_input()
    s = 1
    safety_scores = {}
    while s < (w * h):
        robots_end = move_robots(robots, s, w, h)
        safety_scores[s] = calculate_safety_factor(robots_end, w, h)
        s += 1

    min_score = 1e9
    min_s = None
    for s, score in safety_scores.items():
        if score < min_score:
            min_score = score
            min_s = s

    min_robots = move_robots(robots, min_s, w, h)
    dump_robots(min_robots, w, h)

    print(min_s)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
