#!/usr/bin/env python3

import unittest

from .mark_the_trail import MarkTheTrail

class MarkTheTrailTest(unittest.TestCase):

    def setUp(self):
        global mtt
        mtt = MarkTheTrail()

    def test__check_for_collision__miss(self):
        mtt.line = '####.##'
        mtt.position_zero_indexed = 4
        mtt.total_collisions = 4
        expected = 4
        mtt.check_for_collision()
        actual = mtt.total_collisions
        self.assertEqual(expected, actual)

    def test__check_for_collision__hit(self):
        mtt.line = '...#...'
        mtt.position_zero_indexed = 3
        mtt.total_collisions = 7
        expected = 8
        mtt.check_for_collision()
        actual = mtt.total_collisions
        self.assertEqual(expected, actual)

    def test__move_position__current_section(self):
        mtt.section_length_zero_indexed = 20
        mtt.position_zero_indexed = 5
        mtt.steps_to_move_right = 3
        mtt.move_position()
        expected = 8
        actual = mtt.position_zero_indexed
        self.assertEqual(expected, actual)

    def test__move_position__next_section_over(self):
        mtt.section_length_zero_indexed = 9
        mtt.position_zero_indexed = 8
        mtt.steps_to_move_right = 3
        mtt.move_position()
        expected = 1
        actual = mtt.position_zero_indexed
        self.assertEqual(expected, actual)

    def test_integration_1(self):
        with open('day_03_part_1_version_1/test_input_2.txt') as _file:
            lines = _file.read().split('\n')
        mtt.lines = lines
        mtt.examine_course()
        expected = 2
        actual = mtt.total_collisions
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

