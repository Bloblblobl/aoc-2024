from collections import defaultdict
from utils import get_input

input = get_input()


def part1():
    search_term = "XMAS"
    height = len(input) - 1
    width = len(input[0]) - 1

    def out_of_range(x, y):
        return x < 0 or y < 0 or x > width or y > height

    def get_search_patterns(start_x, start_y):
        patterns = defaultdict(list)
        for i in range(1, len(search_term)):
            patterns["right"].append((start_x + i, start_y))
            patterns["right-down"].append((start_x + i, start_y + i))
            patterns["down"].append((start_x, start_y + i))
            patterns["left-down"].append((start_x - i, start_y + i))
            patterns["left"].append((start_x - i, start_y))
            patterns["left-up"].append((start_x - i, start_y - i))
            patterns["up"].append((start_x, start_y - i))
            patterns["right-up"].append((start_x + i, start_y - i))

        return [
            pattern
            for pattern in patterns.values()
            if not any(out_of_range(*coords) for coords in pattern)
        ]

    result = 0
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != search_term[0]:
                continue

            search_patterns = get_search_patterns(x, y)
            for p in search_patterns:
                valid_pattern = True
                for i, coord in enumerate(p):
                    index = i + 1
                    cx, cy = coord
                    if input[cy][cx] != search_term[index]:
                        valid_pattern = False
                        break

                if valid_pattern:
                    result += 1

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
