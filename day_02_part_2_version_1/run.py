
class Runner:

    def __init__(self):
        self.high_number = None
        self.low_number = None
        self.password_line = None
        self.password_string = None
        self.target_letter = None

    def split_password_line(self):
        self.low_number = int(self.password_line.split('-')[0])
        self.high_number = int(self.password_line.split('-')[1].split(' ')[0])
        self.target_letter = self.password_line.split(' ')[1][0]
        self.password_string = self.password_line.split(' ')[2]

    def is_password_valid_v2(self):
        self.split_password_line()

        # My original solution is commended about below.
        # This one was taught to me by `tommyxr` on Twitch.
        # He rocks 👍

        return (
            (self.password_string[self.low_number - 1] == self.target_letter)
            ^
            (self.password_string[self.high_number - 1] == self.target_letter)
        )


        #
        # occurrences = 0
        # if self.password_string[self.low_number - 1] == self.target_letter:
        #     occurrences += 1
        # if self.password_string[self.high_number - 1] == self.target_letter:
        #     occurrences += 1
        # if occurrences == 1:
        #     return True
        # else:
        #     return False


if __name__ == '__main__':

    r = Runner()
    counter = 0
    with open('input.txt', 'r') as _file:
        for line in _file:
            r.password_line = line
            if r.is_password_valid_v2():
                counter += 1

    print(counter)

