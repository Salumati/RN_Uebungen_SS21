class Statistic:
    _completeCustomers = []
    customers = []
    stations = {}
    droppedStationCustomers = {}
    _completeShoppingTimes = {}

    @staticmethod
    def addCustomer(customer):
        Statistic.customers.append(customer)

    @staticmethod
    def showStatistics():
        Statistic.showCustomerStatistc()
        Statistic.showStationStatistic()

    @staticmethod
    def showStationStatistic():
        print("\nStation statistic:")
        for k in Statistic.stations:
            print(" " + Statistic.stations[k].name)
            print(" last served customer: " + str(Statistic.stations[k].lastCustomer.name) + " at " + str(
                Statistic.stations[k].lastCustomer.totalTimeInMarket) + "s")
            print(" number of served customers: " + str(Statistic.stations[k].totalServedCustomers))
            print(" customer that left  out the Station: " + str(
                Statistic.stations[k].totalLeapCustomers / Statistic.stations[k].totalServedCustomers) + "%")
            # prozentsatz an Kunden die die station auslassen

    @staticmethod
    def showCustomerStatistc():
        print("\nCustomer Statistic:")
        for c in Statistic.customers:
            if c.didCompleteShopping:
                Statistic.addCompleteCustomer(c)
        # amount of complete customers:
        print("amount of complete customers: " + str(len(Statistic._completeCustomers)))
        # average time complete visit
        print("average visit  of K1: " + str(Statistic.averageCompleteShoppingTime("K1")) + "s")
        print("average visit time of K2: " + str(Statistic.averageCompleteShoppingTime("K2")) + "s")
        # print("average visit time in general: " + Statistics.averageCompleteShoppingTime())
        # time last customer left:
        # print("last costumer left at: " + str(Statistics.stations["out"].lastCustomer.totalTimeInMarket) + "s")

    def fullyServedCustomers(self):
        return

    @staticmethod
    def setLastCustomerTime(customer, time):
        Statistic._lastCustomerTime = {customer: time}

    @staticmethod
    def addCompleteCustomer(customer):
        Statistic._completeCustomers.append(customer)

    @staticmethod
    def setCompleteShoppingTime(customer, time):
        Statistic._completeShoppingTimes[customer] = time

    @staticmethod
    def addDroppedStationCustomers(station, droppedCustomers):
        Statistic.droppedStationCustomers[station] = droppedCustomers

    @staticmethod
    def lastCustomerTime():
        return Statistic._lastCustomerTime

    @staticmethod
    def servedCustomers():
        return Statistic._servedCustomers

    @staticmethod
    def completeShoppingTimes():
        return Statistic._completeShoppingTimes

    @staticmethod
    def averageCompleteShoppingTime(customerType):
        shoppingTimes = []
        totalTime = 0
        for k in Statistic._completeCustomers:
            if k.name.split('-')[0] == customerType:
                shoppingTimes.append(k)
                totalTime += k.totalTimeInMarket
        if(totalTime > 0):
            totalTime = totalTime / len(shoppingTimes)

        return totalTime

    @staticmethod
    def droppedStationCustomerPercentages(station):
        return Statistic.droppedStationCustomers[station] / Statistic.customers
