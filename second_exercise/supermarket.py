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

        time.sleep(terminateAfter * terminateFactor)
        self.terminate.set()

        self.eventQueue.work()

    def print(self):
        l = list(self.eventQueue.queue)
        l.sort()
        for i in l:
            print(i)
        print("served customers: ", Statistics.servedCustomers())
        print("last customer time K1: ", Statistics.lastCustomerTime("K1"))
        print("last customer time K2: ", Statistics.lastCustomerTime("K2"))
        print("average shopping time K1: ",
              Statistics.averageCompleteShoppingTime("K1"))
        print("average shopping time K2: ",
              Statistics.averageCompleteShoppingTime("K2"))
        for station in self.stations:
            print("dropped customer percentage for station: ", station.name,
                  Statistics.droppedStationCustomerPercentages(station.name))


supermarket = Supermarket()
supermarket.run()
supermarket.print()