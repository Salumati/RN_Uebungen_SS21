import event
import event_queue
import time

class Station:

    def __init__(self, name, servingTime = 0):
        self.name = name
        self.servingTime = servingTime
        # TODO: Use queue structure
        self.customerQueue = []
        self.lastCustomer = None
        self.totalServedCustomers = 0
        self.totalLeapCustomers = 0

    def queueCustomer(self, customer, maxWait):
        if len(self.customerQueue) <= maxWait:
            self.customerQueue.append(customer)
            print(customer + " got queued in station " + self.name)
        return
        
    def serveCustomer(self, servings):
        #self.work(servings)
        customer = self.customerQueue.pop()
        print(customer + "was served in" + self.name)
        self.lastCustomer = customer
        self.totalServedCustomers = 1
        return

    def work(self, servings):
        self.serveCustomer()

    def queuedCustomers(self):
        return len(self.customerQueue)

    def isNotEmpty(self):
        return len(self.customerQueue) > 1