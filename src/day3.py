from utils import get_input

input = get_input()


def evaluate_potential_instruction(pi):
    first_split = pi.split(',', 1)
    if len(first_split) != 2:
        return 0

    first_operand, rest = first_split
    if any(not c.isdigit() for c in first_operand):
        return 0

    second_split = rest.split(')', 1)
    if len(second_split) != 2:
        return 0

    second_operand = second_split[0]
    if any(not c.isdigit() for c in second_operand):
        return 0
    
    return int(first_operand) * int(second_operand)

def part1():
    result = 0
    for line in input:
        # Always skip the first element because it will proceed the first
        # potential valid instruction (if the string starts with 'mul(',
        # the first element will be '')
        potential_instructions = line.split('mul(')[1:]
        for pi in potential_instructions:
            result += evaluate_potential_instruction(pi)
    
    print(result)
            



def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
