from event_queue import EventQueue
from customer import Customer
from station import Station
from station_visit import StationVisit
from config import customerK1StartTime, customerK1SpawnTime, customerK2StartTime, customerK2SpawnTime, terminateAfter, terminateFactor
from threading import Thread, Event
import time
from statistics import Statistics

class Supermarket:
    def __init__(self):
        self.eventQueue = EventQueue()
        self.terminate = Event()

        entrance = Station("Eingang")
        baker = Station("Bäcker", 10)
        sausage = Station("Wurst", 30)
        cheese = Station("Käse", 60)
        checkout = Station("Kasse", 5)
        outrance = Station("Ausgang")

        self.stations = [entrance, baker, sausage, cheese, checkout, outrance]
        Statistics.stations = {
            "ent": entrance,
            "bak": baker,
            "sau": sausage,
            "cheese": cheese,
            "chout": checkout,
            "out": outrance
        }

        stationVisitsK1 = [StationVisit(entrance, customerK1SpawnTime), StationVisit(baker, 10, 10, 10), StationVisit(
            sausage, 30, 5, 10), StationVisit(cheese, 45, 3, 5), StationVisit(checkout, 60, 30, 30), StationVisit(outrance, 0)]
        stationVisitsK2 = [StationVisit(entrance, customerK2SpawnTime), StationVisit(
            sausage, 30, 2, 5), StationVisit(checkout, 60, 3, 20), StationVisit(baker, 3, 20), StationVisit(outrance, 0)]

        self.customerK1 = Customer(
            "K1-1", stationVisitsK1, customerK1StartTime, self.eventQueue.push, self.eventQueue.pop, self.terminate)

        self.customerK2 = Customer(
            "K2-1", stationVisitsK2, customerK2StartTime, self.eventQueue.push, self.eventQueue.pop, self.terminate)

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