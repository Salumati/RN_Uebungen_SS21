from station import Station
from config import sleepFactor
import time
from threading import Lock

class StationVisit:
    def __init__(self, station, arrivalTime, servings=0, maxWait=0):
        self.station = station
        self.arrivalTime = arrivalTime
        self.servings = servings
        self.maxWait = maxWait
        self.lock = Lock()
        self.hasBeenVisited = False

    def do(self, customer):
        self.hasBeenVisited = True
        print(customer.name + " is entering ", self.station.name)
        return

    def visited(self):
        return self.hasBeenVisited

    def queue(self, customer):
        self.station.queueCustomer(customer, self.maxWait)

    def serve(self):
        self.station.serveCustomer(self.servings)

    def shouldNotSkip(self):
        # needs locks
        self.lock.acquire()
        shouldNotSkip = self.maxWait == 0 or (self.maxWait > self.station.queuedCustomers())
        self.lock.release()
        return shouldNotSkip

    def servingTime(self):
        return self.servings * self.station.servingTime

    def copyShallow(self):
        return StationVisit(self.station.copyShallow(), self.arrivalTime, self.servings, self.maxWait)
