from copy import deepcopy
import time
from threading import Thread, Timer
from event import Event, EventType, EventArgs
from config import sleepFactor
from statistics import Statistics
from datetime import datetime

class Customer(Thread):
    def __init__(self, name, stationVisits, startTime, appendEvent, removeEvent, terminate):
        Thread.__init__(self)
        self.name = name
        self.stationVisits = stationVisits
        self.startTime = startTime
        self.appendEvent = appendEvent
        self.removeEvent = removeEvent
        self.terminate = terminate

    def run(self):
        if self.terminate.is_set():
            return
        Statistics.addCustomer(self)
        self.spawn()
        self.startShopping()
        self.enter()
        self.spawnNext()
        self.startDate = datetime.now()

        return

    def arriveStation(self, args):
        if args.stationId == len(self.stationVisits):
            return

        stationVisit = self.stationVisits[args.stationId]

        time = args.time + stationVisit.arrivalTime
        if stationVisit.shouldNotSkip():
            stationVisit.do()
            stationVisit.queue(self)
            self.appendEvent(Event(EventType.ENTER_STATION, time, 2,
                                 self.work, EventArgs(args.stationId, time)))
        else:
            Statistics.addDroppedStationCustomer(stationVisit.station.name, self)
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
            Statistics.setLastCustomerTime(self.name, datetime.now())
            if args.stationId == len(self.stationVisits)-1:
                Statistics.addCompletelyServedCustomer(self)
                Statistics.setCompleteShoppingTime(self, datetime.now() - self.startDate)
            stationVisit.station.customerQueue[0].appendEvent(
                Event(EventType.LEAVE_STATION, args.time, 1, self.leaveStation, args))

        return

    def startShopping(self):
        self.appendEvent(Event(EventType.START_SHOPPING,
                         self.startTime, 0, self.arriveStation, EventArgs(1, self.startTime)))

    def spawn(self):
        print("spawning ", self.name)
        time.sleep(self.startTime * sleepFactor)

    def enter(self):
        self.stationVisits[0].do()

    def spawnNext(self):
        customer = Customer(self.name, self.stationVisits, self.startTime,
                            self.appendEvent, self.removeEvent, self.terminate)
        nameSplit = self.name.split("-")
        if len(nameSplit) > 1:
            customer.name = f'{nameSplit[0]}-{str(int(nameSplit[1])+1)}'
        else:
            customer.name = f'{nameSplit[0]}'

        customer.start()
