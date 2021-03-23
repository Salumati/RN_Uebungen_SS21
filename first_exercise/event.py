class Event:
    def __init__(self, time, priority, id, func, args):
        self.time = time
        self.priority = priority
        self.id = id
        self.func = func
        self.args = args

    def do(self):
        return self.func(self.args)

    # TODO: compare time, priority and id
    def __cmp__(self, other):
        return True