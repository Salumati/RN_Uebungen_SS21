from event_queue import EventQueue
from customer import Customer
from station import Station
from station_visit import StationVisit
import time
from threading import Timer


class Supermarket:
    # in seconds
    customerK1StartTime = 0
    customerK1SpawnTime = 200
    customerK2StartTime = 1
    customerK2SpawnTime = 60

    def __init__(self):
        self.eventQueue = EventQueue()

        entrance = Station("Eingang")
        baker = Station("Bäcker", 10)
        sausage = Station("Wurst", 30)
        cheese = Station("Käse", 60)
        checkout = Station("Kasse", 5)
        outrance = Station("Ausgang")

        stationVisitsK1 = [StationVisit(entrance, 200), StationVisit(baker, 10, 10, 10), StationVisit(
            sausage, 30, 5, 10), StationVisit(cheese, 45, 3, 5), StationVisit(checkout, 60, 30, 30), StationVisit(outrance, 0)]
        self.customerK1 = Customer("K1", stationVisitsK1)
        stationVisitsK2 = [StationVisit(entrance, 60), StationVisit(
            sausage, 30, 2, 5), StationVisit(checkout, 60, 3, 20), StationVisit(baker, 3, 20), StationVisit(outrance, 0)]
        self.customerK2 = Customer("K2", stationVisitsK2)

        time.sleep(self.customerK1StartTime * 60)
        self.customerK1.startShopping()
        time.sleep(self.customerK2StartTime * 60)
        self.customerK2.startShopping()

        while True:
            self.spawnCustomer()
            self.eventQueue.work()

    def spawnCustomer(self):
        self.spawnCustomerK1()
        self.spawnCustomerK2()

    def spawnCustomerK1(self):
        t = Timer(self.customerK1SpawnTime * 60, lambda _ : self.customerK1.startShopping())
        t.start()

    def spawnCustomerK2(self):
        t = Timer(self.customerK2SpawnTime * 60, lambda _ : self.customerK2.startShopping())
        t.start()

