from utils import get_input

input = get_input()


def parse_input():
    calibration_map = {}
    for line in input:
        calibration_str, operator_str = line.split(": ")
        calibration_map[int(calibration_str)] = [
            int(o) for o in operator_str.split(" ")
        ]
    return calibration_map


def generate_op_patterns(operators, num_operators):
    result = []
    if num_operators == 1:
        return [[op] for op in operators]

    subsequences = generate_op_patterns(operators, num_operators - 1)

    result = [[op] + subsequence for op in operators for subsequence in subsequences]
    return result


def evaluate_calibration(calibration_val, operands, operators):
    result = []
    for op_func, op_str in operators:
        opd1, opd2 = operands[0], operands[1]
        next_step = op_func(opd1, opd2)
        if len(operands) > 2:
            if next_step <= calibration_val:
                new_operands = [next_step] + operands[2:]
                subevaluation = evaluate_calibration(
                    calibration_val, new_operands, operators
                )
                for subeval in subevaluation:
                    result.append([op_str] + subeval)
        else:
            if next_step == calibration_val:
                result.append([op_str])

    return result


def part1():
    OPERATORS = [(lambda x, y: x + y, "+"), (lambda x, y: x * y, "*")]
    calibration_map = parse_input()
    result = 0
    for calibration_val, operands in calibration_map.items():
        evals = evaluate_calibration(calibration_val, operands, OPERATORS)
        if len(evals):
            result += calibration_val

    print(result)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
