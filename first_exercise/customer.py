from copy import deepcopy
import time
from threading import Timer
from event import Event
from event import EventType
from event import EventArgs


class Customer:
    def __init__(self, name, stationVisits, startTime, spawnTime, appendEvent, removeEvent):
        self.name = name
        self.stationVisits = stationVisits
        self.startTime = startTime
        self.spawnTime = spawnTime
        self.appendEvent = appendEvent
        self.removeEvent = removeEvent

    def startShopping(self):
        # self.start()
        # self.spawn()
        self.startEvent()
        self.stationVisits[0].do()

        return

    def arriveStation(self, args):
        if args.stationId == len(self.stationVisits):
            return
            
        stationVisit = self.stationVisits[args.stationId]

        time = args.time + stationVisit.arrivalTime
        if stationVisit.shouldNotSkip():
            stationVisit.do()
            if stationVisit.station.isNotEmpty():
                stationVisit.queue(self)
                # what do we do next?
            else:
                self.appendEvent(Event(EventType.ENTER_STATION, time, 2,
                                 self.work, EventArgs(args.stationId, time)))

        else:
            self.appendEvent(Event(EventType.ENTER_STATION, time, 2,
                             self.arriveStation, EventArgs(args.stationId+1, time)))

        return

    def work(self, args):
        stationVisit = self.stationVisits[args.stationId]
        time = args.time + stationVisit.servingTime()
        self.appendEvent(Event(EventType.LEAVE_STATION, time, 1,
                         self.leaveStation, EventArgs(args.stationId, time)))

    def leaveStation(self, args):
        self.arriveStation(EventArgs(args.stationId+1, args.time))

        stationVisit = self.stationVisits[args.stationId]
        if stationVisit.station.isNotEmpty():
            stationVisit.serve()
            stationVisit.station.customerQueue[0].appendEvent(
                Event(EventType.LEAVE_STATION, args.time, 1, self.leaveStation, args))

        return

    def startEvent(self):
        self.appendEvent(Event(EventType.START_SHOPPING,
                         self.startTime, 0, self.arriveStation, EventArgs(1, self.startTime)))

    def start(self):
        time.sleep(self.startTime * 60)

    def spawn(self):
        t = Timer(self.spawnTime * 60,
                  lambda _: self.spawnCustomer())
        t.start()

    def spawnCustomer(self):
        customer = deepcopy(self)
        nameSplit = self.name.split("-")
        if len(nameSplit) > 1:
            customer.name = f'{nameSplit[0]}-{nameSplit[1]+1}'
        else:
            customer.name = f'{nameSplit[0]}'

        customer.startShopping()
