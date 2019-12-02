import unittest

from day2 import (
    execute_opcode,
    parse_intcodes,
    ADDITION_OPCODE,
    MULTIPLICATION_OPCODE,
)


class TestDay2(unittest.TestCase):
    def test_addition_opcode(self):
        intcodes = [1, 0, 0, 0, 99]
        execute_opcode(intcodes, 0, ADDITION_OPCODE)
        self.assertEqual(intcodes, [2, 0, 0, 0, 99])

    def test_multiplication_opcode(self):
        intcodes = [2, 3, 0, 3, 99]
        execute_opcode(intcodes, 0, MULTIPLICATION_OPCODE)
        self.assertEqual(intcodes, [2, 3, 0, 6, 99])

    def test_parse_intcodes(self):
        intcodes = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        parse_intcodes(intcodes)
        self.assertEqual(intcodes, [30, 1, 1, 4, 2, 5, 6, 0, 99])

        intcodes = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        parse_intcodes(intcodes)
        self.assertEqual(
            intcodes, [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        )


if __name__ == "__main__":
    unittest.main()
