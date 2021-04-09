
from enum import Enum


class EventType(Enum):
    START_SHOPPING = 1
    ENTER_STATION = 2
    LEAVE_STATION = 3


id = 0


class EventArgs:
    def __init__(self, stationId, time):
        self.stationId = stationId
        self.time = time


class Event:
    def __init__(self, type, time, priority, func, args):
        global id

        self.type = type
        self.time = time
        self.priority = priority
        self.id = id
        self.func = func
        self.args = args

        id += 1

    def execute(self):
        return self.func(self.args)

    def __lt__(self, other):
        print(self, other)

        return (self.time, self.priority, self.id) < (other.time, other.priority, other.id)

    def __str__(self):
        return f'Event: {self.type},{self.time},{self.priority},{self.id}'
