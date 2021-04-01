from functools import total_ordering

@total_ordering
class Event:
    def __init__(self, time, priority, id, func, args):
        self.time = time
        self.priority = priority
        self.id = id
        self.func = func
        self.args = args

    def do(self):
        return self.func(self.args)

    def __eq__(self, other):
        return ((self.time, self.priority, self.id) == (other.time, other.priority, other.id))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.time, self.priority, self.id) < (other.time, other.priority, other.id))