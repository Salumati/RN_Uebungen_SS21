from copy import deepcopy
import time
from threading import Timer
from event import Event
from event import EventType
from event import EventArgs

from statistics import Statistic


class Customer:
    def __init__(self, name, stationVisits, startTime, spawnTime, addEvent, removeEvent):
        self.name = name
        self.stationVisits = stationVisits
        self.startTime = startTime
        self.spawnTime = spawnTime
        self.appendEvent = addEvent
        self.removeEvent = removeEvent
        self.totalTimeInMarket = 0
        self.didCompleteShopping = True

    def startShopping(self, endTime=18000):
        # self.start()
        self.startEvent()
        self.spawnCustomer(endTime)
        self.stationVisits[0].do()

        return

    def arriveStation(self, args):
        if args.stationId == len(self.stationVisits):
            return
            
        stationVisit = self.stationVisits[args.stationId]
        self.totalTimeInMarket += stationVisit.arrivalTime

        time = args.time + stationVisit.arrivalTime
        if stationVisit.shouldNotSkip():
            stationVisit.do()
            # self.durationOfVisit = self.durationOfVisit + stationVisit.servingTime
            if stationVisit.station.isNotEmpty():
                stationVisit.queue(self)
                # how to tell since how long the customer has been queued?
                # what do we do next?
            else:
                self.appendEvent(Event(EventType.ENTER_STATION, time, 2,
                                 self.work, self.name, stationVisit.station.name, EventArgs(args.stationId, time)))

        else:
            self.didCompleteShopping = False
            self.appendEvent(Event(EventType.ENTER_STATION, time, 2,
                             self.arriveStation, self.name, stationVisit.station.name, EventArgs(args.stationId+1, time)))

        return

    def work(self, args):
        stationVisit = self.stationVisits[args.stationId]
        time = args.time + stationVisit.servingTime()
        self.appendEvent(Event(EventType.LEAVE_STATION, time, 1,
                         self.leaveStation, self.name, stationVisit.station.name, EventArgs(args.stationId, time)))

    def leaveStation(self, args):
        self.arriveStation(EventArgs(args.stationId+1, args.time))

        stationVisit = self.stationVisits[args.stationId]
        if stationVisit.station.isNotEmpty():
            stationVisit.serve()
            stationVisit.station.customerQueue[0].appendEvent(
                Event(EventType.LEAVE_STATION, args.time, 1, self.leaveStation, self.name, stationVisit.station.name, args))

        return

    def startEvent(self):
        self.appendEvent(Event(EventType.START_SHOPPING,
                         self.startTime, 0, self.arriveStation, self.name, "",  EventArgs(1, self.startTime)))

    def start(self):
        print(str(self.startTime) + " : " + self.name + " started Shopping!")

    def spawnCustomer(self, endTime):
        customer = deepcopy(self)
        nameSplit = self.name.split("-")
        if len(nameSplit) > 1:
            customer.name = f'{nameSplit[0]}-{int(nameSplit[1])+1}'
        else:
            customer.name = f'{nameSplit[0]}'
        customer.startTime += customer.spawnTime
        if (customer.startTime >= endTime):
            return
        customer.appendEvent = self.appendEvent
        customer.removeEvent = self.removeEvent
        Statistic.addCustomer(customer)
        customer.startShopping()
