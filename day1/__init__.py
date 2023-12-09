def solve(puzzle_input):
    calibration_values = []
    for line in puzzle_input.strip().split("\n"):
        first = None
        last = None
        for char in line:
            if char.isnumeric():
                last = int(char)
                if first is None:
                    first = int(char)
        calibration_values.append(first  * 10 + last)
    return sum(calibration_values)

if __name__ == '__main__':
    with open("day1/input.txt") as input_file:
        puzzle_input = input_file.read()
    puzzle_output = solve(puzzle_input)
    print(puzzle_output)