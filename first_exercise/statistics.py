class Statistics:
    _servedCustomers = []
    customers = []
    droppedStationCustomers = {}
    _completeShoppingTimes = {}

    @staticmethod
    def addCustomer(customer):
        Statistics.customers.append(customer)

    @staticmethod
    def setLastCustomerTime(customer, time):
        Statistics._lastCustomerTime = {customer: time}

    @staticmethod
    def addServedCustomer(customer):
        Statistics._servedCustomers.append(customer)

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
    def servedCustomers():
        return Statistics._servedCustomers

    @staticmethod
    def completeShoppingTimes():
        return Statistics._completeShoppingTimes

    @staticmethod
    def averageCompleteShoppingTime(customerType):
        shoppingTimes = []
        totalTime = 0
        for k, v in Statistics._completeShoppingTimes.items():
            if k.split('-')[0] == customerType:
                shoppingTimes.append(v)
                totalTime += v
        return totalTime / len(shoppingTimes)

    @staticmethod
    def droppedStationCustomerPercentages(station):
        return Statistics.droppedStationCustomers[station] / Statistics.customers