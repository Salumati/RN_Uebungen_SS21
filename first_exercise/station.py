import event
import event_queue

class Station:
    def __init__(self, name, servingTime):
        self.name = name
        self.servingTime = servingTime
        self.customerQueue = []  # todo: queue

    def queueCustomer(self, customer):
        self.customerQueue.append(customer)
        return
        
    def serveCustomer(self, func):
        # calculate time customer needs (servingTime * customerObjects)
        customer = self.customerQueue.pop()
        timeNeeded = self.servingTime * customer.productsForStation(self.name)

        # create "customer serve" event
        func(timeNeeded)
        return