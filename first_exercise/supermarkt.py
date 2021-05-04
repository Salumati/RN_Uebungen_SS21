from event_queue import EventQueue
from customer import Customer
from station import Station
from station_visit import StationVisit

# in seconds
customerK1StartTime = 0
customerK1SpawnTime = 200
customerK2StartTime = 1
customerK2SpawnTime = 60


class Supermarket:
    def __init__(self):
        self.eventQueue = EventQueue()

        entrance = Station("Eingang")
        baker = Station("Bäcker", 10)
        sausage = Station("Wurst", 30)
        cheese = Station("Käse", 60)
        checkout = Station("Kasse", 5)
        outrance = Station("Ausgang")

        self.listOfStations = [entrance, baker, sausage, cheese, checkout, outrance]

        stationVisitsK1 = [StationVisit(entrance, 200), StationVisit(baker, 10, 10, 10), StationVisit(
            sausage, 30, 5, 10), StationVisit(cheese, 45, 3, 5), StationVisit(checkout, 60, 30, 30), StationVisit(outrance, 0)]
        stationVisitsK2 = [StationVisit(entrance, 60), StationVisit(
            sausage, 30, 2, 5), StationVisit(checkout, 60, 3, 20), StationVisit(baker, 3, 20), StationVisit(outrance, 0)]

        self.customerK1 = Customer(
            "K1-1", stationVisitsK1, customerK1StartTime, customerK1SpawnTime, self.eventQueue.push, self.eventQueue.pop)

        self.customerK2 = Customer("K2-1", stationVisitsK2, customerK2StartTime,
                                   customerK2SpawnTime, self.eventQueue.push, self.eventQueue.pop)

    def run(self, stopAt=(30*60)):
        self.customerK1.startShopping(stopAt)
        self.customerK2.startShopping(stopAt)
        self.eventQueue.work()
        l = list(self.eventQueue.queue)
        l.sort()

        for i in l:
            print(i)
        print(l)

        print("station statistics:")
        for s in self.listOfStations:
            print(s.name + ": ")
            print("last customer visited: " + str(s.lastCustomer))
            print("number of served customers: " + str(s.servedCustomers))
            print("customeres that left: " + str(s.customerThatLeft))


supermarket = Supermarket()
supermarket.run()