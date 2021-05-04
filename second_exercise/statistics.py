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
    def addCompletelyServedCustomer(customer):
        Statistics._servedCustomers.append(customer)

    @staticmethod
    def setCompleteShoppingTime(customer, time):
        Statistics._completeShoppingTimes[customer] = time

    @staticmethod
    def addDroppedStationCustomer(station, droppedCustomer):
        if station in Statistics.droppedStationCustomers:
            Statistics.droppedStationCustomers[station].append(droppedCustomer)
        else:
            Statistics.droppedStationCustomers[station] = []

    @staticmethod
    def lastCustomerTime(customer):
        if customer in Statistics._lastCustomerTime:
            return Statistics._lastCustomerTime[customer]
        return 0
    
    @staticmethod
    def servedCustomers():
        return len(Statistics._servedCustomers)

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
        if len(shoppingTimes) > 0:
            return totalTime / len(shoppingTimes)

        return 0
    
    @staticmethod
    def droppedStationCustomerPercentages(station):
        if station in Statistics.droppedStationCustomers:
            return len(Statistics.droppedStationCustomers[station]) / len(Statistics.customers)
        return 0
