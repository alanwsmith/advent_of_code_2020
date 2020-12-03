#!/usr/bin/env python3


class MarkTheTrail:

    def __init__(self):
        self.line = None
        self.lines = []
        self.position_zero_indexed = 0
        self.section_length_zero_indexed = 0
        self.steps_to_move_right = 3
        self.total_collisions = 0

    def check_for_collision(self):
        print(self.line)
        if self.line[self.position_zero_indexed] == '#':
            print(f'{self.position_zero_indexed} - Hit a tree...')
            self.total_collisions += 1
        else:
            print(f'{self.position_zero_indexed} - Missed the tree...')

    def examine_course(self):
        for current_line in self.lines:
            self.line = current_line
            self.section_length_zero_indexed = len(current_line) - 1
            self.check_for_collision()
            self.move_position()

    def move_position(self):
        new_position_raw = self.position_zero_indexed + self.steps_to_move_right
        if new_position_raw > self.section_length_zero_indexed:
            self.position_zero_indexed = new_position_raw - self.section_length_zero_indexed - 1
        else:
            self.position_zero_indexed = new_position_raw

if __name__ == '__main__':
    mtt = MarkTheTrail()
    with open('input.txt') as _file:
        lines = _file.read().split('\n')
    mtt.lines = lines
    mtt.examine_course()
    print(mtt.total_collisions)
