#!/usr/bin/evn python3

import unittest

from .run import Runner


class RunnerTest(unittest.TestCase):

    def setUp(self):
        global r
        r = Runner()

    def test_low_number(self):
        r.password_line = '10-11 f: fffffffpfff'
        r.split_password_line()
        expected = 10
        actual = r.low_number
        self.assertEqual(expected, actual)

    def test_high_number(self):
        r.password_line = '4-11 g: gggvgg'
        r.split_password_line()
        expected = 11
        actual = r.high_number
        self.assertEqual(expected, actual)

    def test_make_compressed_number(self):
        r.password_string = 'bbbbbbwbbbbbbbb'
        r.target_letter = 'b'
        r.make_compressed_number()
        expected = 1
        actual = r.compressed_number
        self.assertEqual(expected, actual)

    def test_make_diff_number(self):
        r.original_number_count = 7
        r.compressed_number = 4
        r.make_diff_number()
        expected = 3
        actual = r.diff_number
        self.assertEqual(expected, actual)

    def test_original_number_count(self):
        r.password_line = '2-4 n: nvxf'
        r.split_password_line()
        expected = 4
        actual = r.original_number_count
        self.assertEqual(expected, actual)

    def test_password_string(self):
        r.password_line = '11-14 p: ppppppppppgpppp'
        r.split_password_line()
        expected = 'ppppppppppgpppp'
        actual = r.password_string
        self.assertEqual(expected, actual)

    def test_target_letter(self):
        r.password_line = '18-19 n: nnslnnnnnmnnnnnnnxnn'
        r.split_password_line()
        expected = 'n'
        actual = r.target_letter
        self.assertEqual(expected, actual)

    def test_integration_false_low(self):
        r.password_line = '3-4 l: bllk'
        expected = False
        actual = r.is_password_valid()
        self.assertEqual(expected, actual)

    def test_integration_false_high(self):
        r.password_line = '1-3 v: jlcvvvv'
        expected = False
        actual = r.is_password_valid()
        self.assertEqual(expected, actual)

    def test_integration_true(self):
        r.password_line = '3-4 l: vlcll'
        expected = True
        actual = r.is_password_valid()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
