from day1 import solve_a, PUZZLE




def test_example_a():
    input_data = PUZZLE.examples[0].input_data
    answer_a = PUZZLE.examples[0].answer_a
    assert solve_a(input_data) == answer_a