from event_queue import EventQueue
from customer import Customer
from station import Station
from station_visit import StationVisit
from config import customerK1StartTime, customerK1SpawnTime, customerK2StartTime, customerK2SpawnTime, terminateAfter, terminateFactor
from threading import Thread, Event
import time
from statistics import Statistics
from extern import entrance, baker, sausage, cheese, checkout, outrance, stationVisitsK1, stationVisitsK2, stationVisitsCopy

class Supermarket:
    def __init__(self):
        self.eventQueue = EventQueue()
        self.terminate = Event()

        Statistics.stations = {
            "ent": entrance,
            "bak": baker,
            "sau": sausage,
            "cheese": cheese,
            "chout": checkout,
            "out": outrance}

        self.customerK1 = Customer(
            "K1-1", stationVisitsCopy(stationVisitsK1), customerK1StartTime, self.eventQueue.push, self.eventQueue.pop, self.terminate)

        self.customerK2 = Customer(
            "K2-1", stationVisitsCopy(stationVisitsK2), customerK2StartTime, self.eventQueue.push, self.eventQueue.pop, self.terminate)

    def run(self):
        self.customerK1.start()
        self.customerK2.start()

        print("made customers, going to sleep")
        time.sleep(terminateAfter * terminateFactor)
        self.terminate.set()
        print("customersproduction has be terminated")

        self.eventQueue.work()

    def print(self):
        """
        l = list(self.eventQueue.queue)
        l.sort()
        for i in l:
            print(i)
        """
        Statistics.showStatistics()


supermarket = Supermarket()
supermarket.run()
supermarket.print()