class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]")


schedule = [[Interval(1, 3), Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]

