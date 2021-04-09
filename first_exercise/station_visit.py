from station import Station


class StationVisit:
    def __init__(self, station, arrivalTime, servings=0, maxWait=0):
        self.station = station
        self.arrivalTime = arrivalTime
        self.servings = servings
        self.maxWait = maxWait
        self.hasBeenVisited = False

    def do(self):
        self.hasBeenVisited = True
        return

    def visited(self):
        return self.hasBeenVisited

    def queue(self, customer):
        self.station.queueCustomer(customer, self.maxWait)

    def serve(self):
        self.station.serveCustomer(self.servings)

    def shouldNotSkip(self):
        return self.maxWait >= self.station.queuedCustomers()

    def servingTime(self):
        return self.servings * self.station.servingTime
