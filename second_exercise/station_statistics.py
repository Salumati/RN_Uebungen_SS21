class StationStatistics():
    def __init__(self):
        self.lastCustomer = None
        self.totalServedCustomers = 0
        self.totalLeapCustomers = 0

    def setLastCustomer(self, customer):
        self.lastCustomer = customer

    def addTotalServedCustomer(self):
        self.totalServedCustomers += 1

    def addTotalLeapCustomer(self):
        self.totalLeapCustomers += 1