#!/usr/bin/env python3
import unittest
import morse


class TestPyMorse(unittest.TestCase):
    def test_text_to_morse_conversion(self):
        string = "this is a test string"
        expected_morse = "- ···· ·· ···  ·· ···  ·-  - · ··· -  ··· - ·-· ·· -· --·"
        self.assertEqual(morse.convert_text_to_morse(string), expected_morse)

    def test_morse_to_text_conversion(self):
        input_morse = "- ···· ·· ···  ·· ···  ·-  - · ··· -  ··· - ·-· ·· -· --·"
        expected_string = "THIS IS A TEST STRING"
        self.assertEqual(morse.convert_morse_to_text(input_morse), expected_string)

    def test_text_to_morse_and_back(self):
        input_text = "Sed et minus inventore autem. Doloremque incidunt et aut praesentium id optio."
        expected_output_text = input_text.upper()
        self.assertEqual(
            morse.convert_morse_to_text(morse.convert_text_to_morse(input_text)),
            expected_output_text,
        )

    def test_custom_dots(self):
        input_morse = "- xxxx xx xxx  xx xxx  x-  - x xxx -  xxx - x-x xx -x --x"
        expected_string = "THIS IS A TEST STRING"
        self.assertEqual(
            morse.convert_morse_to_text(input_morse, dot="x"), expected_string
        )

    def test_custom_dashes(self):
        input_morse = "X ···· ·· ···  ·· ···  ·X  X · ··· X  ··· X ·X· ·· X· XX·"
        expected_string = "THIS IS A TEST STRING"
        self.assertEqual(
            morse.convert_morse_to_text(input_morse, dash="X"), expected_string
        )

    def test_custom_dots_and_dashes(self):
        input_morse = "X YYYY YY YYY  YY YYY  YX  X Y YYY X  YYY X YXY YY XY XXY"
        expected_string = "THIS IS A TEST STRING"
        self.assertEqual(
            morse.convert_morse_to_text(input_morse, dot="Y", dash="X"), expected_string
        )


if __name__ == "__main__":
    unittest.main()
