
from aocd.models import Puzzle

PUZZLE = Puzzle(year=2023, day=1)

def solve_a(puzzle_input):
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
    return str(sum(calibration_values))

if __name__ == "__main__":
    puzzle_input = solve_a(PUZZLE.input_data)
    print(f"answer_a = {puzzle_input}")