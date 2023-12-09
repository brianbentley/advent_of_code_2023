from day1 import solve

SAMPLE_INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
SAMPLE_OUTPUT = 142

def test_sample_input():
    assert solve(SAMPLE_INPUT) == SAMPLE_OUTPUT