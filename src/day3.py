from utils import get_input

input = get_input()


def evaluate_potential_instruction(pi):
    first_split = pi.split(",", 1)
    if len(first_split) != 2:
        return None

    first_operand, rest = first_split
    if any(not c.isdigit() for c in first_operand):
        return None

    second_split = rest.split(")", 1)
    if len(second_split) != 2:
        return None

    second_operand = second_split[0]
    if any(not c.isdigit() for c in second_operand):
        return None

    return int(first_operand) * int(second_operand)


def part1():
    result = 0
    for line in input:
        # Always skip the first element because it will proceed the first
        # potential valid instruction (if the string starts with 'mul(',
        # the first element will be '')
        potential_instructions = line.split("mul(")[1:]
        for pi in potential_instructions:
            instr_result = evaluate_potential_instruction(pi)
            if instr_result is not None:
                result += instr_result

    print(result)


def part2():
    result = 0
    cursor = "".join(input)

    def get_next_mul(c):
        return c.find("mul(")

    def get_next_dont(c):
        return c.find("don't()")

    def get_next_do(c):
        return c.find("do()")

    while (next_mul := get_next_mul(cursor)) >= 0:
        if 0 <= (next_dont := get_next_dont(cursor)) < next_mul:
            cursor = cursor[next_dont + 7 :]
            next_do = get_next_do(cursor)
            cursor = cursor[next_do + 4 :]

            continue

        cursor = cursor[next_mul + 4 :]

        instr_result = evaluate_potential_instruction(cursor)
        if instr_result is not None:
            result += instr_result
            cursor = cursor[cursor.find(")") :]

    print(result)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
