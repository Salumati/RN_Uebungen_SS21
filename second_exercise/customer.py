from copy import deepcopy
import time
from statistics import Statistics
from threading import Thread, Timer
from event import Event, EventType, EventArgs
from config import sleepFactor, customerK1SpawnTime, customerK2SpawnTime

class Customer(Thread):
    def __init__(self, name, stationVisits, startTime, appendEvent, removeEvent, terminate):
        Thread.__init__(self)
        self.name = name
        self.stationVisits = stationVisits
        self.startTime = startTime
        self.appendEvent = appendEvent
        self.removeEvent = removeEvent
        self.terminate = terminate
        self.totalTimeInMarket = 0
        self.didCompleteShopping = True
        # we assume the customer will visit all stations and set it false if they skip at least one

    def run(self):
        if self.terminate.is_set():
            return
        self.spawn()
        self.startShopping()
        self.enter()
        self.spawnNext()
        return

    def arriveStation(self, args):
        if args.stationId == len(self.stationVisits):
            return

        stationVisit = self.stationVisits[args.stationId]

        time = args.time + stationVisit.arrivalTime
        self.totalTimeInMarket += time
        if stationVisit.shouldNotSkip():
            stationVisit.do(self)
            if stationVisit.station.isNotEmpty():
                stationVisit.queue(self)
            else:
                self.appendEvent(Event(EventType.ENTER_STATION, time, 2,
                                 self.work, EventArgs(args.stationId, time)))

        else:
            self.didCompleteShopping = False
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

    def startShopping(self):
        self.appendEvent(Event(EventType.START_SHOPPING,
                         self.startTime, 0, self.arriveStation, EventArgs(1, self.startTime)))

    def spawn(self):
        print("spawning " + self.name + " at time" + str(self.startTime))
        Statistics.addCustomer(self)
        time.sleep(self.startTime * sleepFactor)

    def enter(self):
        self.stationVisits[0].do(self)

    def spawnNext(self):
        customer = Customer(self.name, self.stationVisits, self.startTime,
                            self.appendEvent, self.removeEvent, self.terminate)
        nameSplit = self.name.split("-")
        customer.name = f'{nameSplit[0]}-{int(nameSplit[1])+1}'
        if nameSplit[0] == "K1":
            customer.startTime += customerK1SpawnTime
        elif nameSplit[0] == "K2":
            customer.startTime += customerK2SpawnTime

        customer.start()