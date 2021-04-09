import event
import event_queue
import time

class Station:
    def __init__(self, name, servingTime = 0):
        self.name = name
        self.servingTime = servingTime
        # TODO: Use queue structure
        self.customerQueue = []

    def queueCustomer(self, customer, maxWait):
        if len(self.customerQueue) <= maxWait:
            self.customerQueue.append(customer)
        return
        
    def serveCustomer(self, servings):
        #self.work(servings)
        self.customerQueue.pop()
        return

    def work(self, servings):
        time.sleep(self.servingTime * servings)

    def queuedCustomers(self):
        return len(self.customerQueue)

    def isNotEmpty(self):
        return len(self.customerQueue) > 1