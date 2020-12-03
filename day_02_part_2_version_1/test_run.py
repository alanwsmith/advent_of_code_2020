#!/usr/bin/evn python

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


    def test_integration_fail_neither_slot(self):
        r.password_line = '3-4 l: baaak'
        expected = False
        actual = r.is_password_valid_v2()
        self.assertEqual(expected, actual)

    def test_integration_fail_both_slots(self):
        r.password_line = '3-4 l: lllllllll'
        expected = False
        actual = r.is_password_valid_v2()
        self.assertEqual(expected, actual)

    def test_integration_pass_first_slot(self):
        r.password_line = '3-4 l: aalaaaa'
        expected = True
        actual = r.is_password_valid_v2()
        self.assertEqual(expected, actual)

    def test_integration_pass_second_slot(self):
        r.password_line = '3-4 l: aaalaaaa'
        expected = True
        actual = r.is_password_valid_v2()
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
