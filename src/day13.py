import math

from utils import get_input

input = get_input()


def init_config(a, b, prize):
    return {
        "a": a,
        "b": b,
        "prize": prize,
    }


def parse_line(line):
    _, content = line.split(": ")
    x_part, y_part = content.split(", ")
    x_num = int(x_part[2:])
    y_num = int(y_part[2:])
    return x_num, y_num


def parse_input():
    configs = []

    i = 0
    while i < len(input):
        a_line = input[i]
        b_line = input[i + 1]
        prize_line = input[i + 2]
        i += 4
        configs.append(
            init_config(
                a=parse_line(a_line),
                b=parse_line(b_line),
                prize=parse_line(prize_line),
            )
        )

    return configs


def extract_values(config):
    ax, ay = config["a"]
    bx, by = config["b"]
    px, py = config["prize"]
    return ax, ay, bx, by, px, py


def is_int(n):
    return math.isclose(n, round(n))


def get_move_count(config):
    ax, ay, bx, by, px, py = extract_values(config)

    bn_top = py - (ay * px) / ax
    bn_bot = by - (ay * bx) / ax
    bn = bn_top / bn_bot

    an = (px - bx * bn) / ax

    a_close = is_int(an)
    b_close = is_int(bn)
    if not a_close or not b_close:
        return None

    return round(an), round(bn)


def get_tokens(config):
    move_count = get_move_count(config)
    if move_count is None:
        return 0

    an, bn = move_count
    if an < 0 or bn < 0:
        return 0

    return 3 * an + bn


def part1():
    configs = parse_input()
    result = 0
    for config in configs:
        result += get_tokens(config)

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
