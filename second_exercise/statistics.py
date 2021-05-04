class Statistics:
    _completeCustomers = []
    customers = []
    stations = {}
    droppedStationCustomers = {}
    _completeShoppingTimes = {}


    @staticmethod
    def addCustomer(customer):
        Statistics.customers.append(customer)

    @staticmethod
    def showStatistics():
        Statistics.showCustomerStatistc()
        Statistics.showStationStatistic()


    @staticmethod
    def showStationStatistic():
        print("\nStation statistic:")
        for k in Statistics.stations:
            print(" " + Statistics.stations[k].name)
            print(" last served customer: " + str(Statistics.stations[k].lastCustomer.name) + " at " + str(Statistics.stations[k].lastCustomer.totalTime()) + "s")
            print(" number of served customers: " + str(Statistics.stations[k].totalServedCustomers))
            print(" customer that left  out the Station: " + str(Statistics.stations[k].totalLeapCustomers/Statistics.stations[k].totalServedCustomers) + "%")
            # prozentsatz an Kunden die die station auslassen

    @staticmethod
    def showCustomerStatistc():
        print("\nCustomer Statistic:")
        print("Statistics.customers ", Statistics.customers)
        for c in Statistics.customers:
            print("didCompleteShopping", c.didCompleteShopping)
            if c.didCompleteShopping:
                Statistics.addCompleteCustomer(c)
        # amount of complete customers:
        print("amount of complete customers: " + str(len(Statistics._completeCustomers)))
        # average time complete visit
        print("average visit  of K1: " + str(Statistics.averageCompleteShoppingTime("K1")) + "s")
        print("average visit time of K2: " + str(Statistics.averageCompleteShoppingTime("K2")) + "s")
        # print("average visit time in general: " + Statistics.averageCompleteShoppingTime())
        # time last customer left:
        print("last costumer left at: " + str(Statistics.stations["out"].lastCustomer.totalTime()) + "s")


    def fullyServedCustomers(self):
        return

    @staticmethod
    def setLastCustomerTime(customer, time):
        Statistics._lastCustomerTime = {customer: time}

    @staticmethod
    def addCompleteCustomer(customer):
        Statistics._completeCustomers.append(customer)

    @staticmethod
    def setCompleteShoppingTime(customer, time):
        Statistics._completeShoppingTimes[customer] = time

    @staticmethod
    def addDroppedStationCustomers(station, droppedCustomers):
        Statistics.droppedStationCustomers[station] = droppedCustomers

    @staticmethod
    def lastCustomerTime():
        return Statistics._lastCustomerTime

    @staticmethod
    def completeShoppingTimes():
        return Statistics._completeShoppingTimes

    @staticmethod
    def averageCompleteShoppingTime(customerType):
        shoppingTimes = []
        totalTime = 0
        print("Statistics._completeCustomers ", Statistics._completeCustomers)
        for k in Statistics._completeCustomers:
            if k.name.split('-')[0] == customerType:
                shoppingTimes.append(k)
                totalTime += k.totalTime()
        if len(shoppingTimes) > 0:
            return totalTime / len(shoppingTimes)
        return 0
    
    @staticmethod
    def droppedStationCustomerPercentages(station):
        return Statistics.droppedStationCustomers[station] / Statistics.customers
