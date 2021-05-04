import event
import event_queue
import time
from threading import Lock
from config import sleepFactor

class Station():
    def __init__(self, name, servingTime = 0):
        self.name = name
        self.lock = Lock()
        self.servingTime = servingTime
        self.customerQueue = []
        self.lastCustomer = None
        self.totalServedCustomers = 0
        self.totalLeapCustomers = 0

    def queueCustomer(self, customer, maxWait):
        if len(self.customerQueue) <= maxWait:
            self.lock.acquire()
            print(self.name + " queued customer: " + customer.name)
            self.customerQueue.append(customer)
            self.lock.release()
        else:
            self.totalLeapCustomers = self.totalLeapCustomers + 1
        return
        
    def serveCustomer(self, servings):
        self.lock.acquire()
        self.work(servings)
        customer = self.customerQueue.pop()
        print(self.name + " just served: " + customer.name)
        self.totalServedCustomers = self.totalServedCustomers + 1
        self.lastCustomer = customer
        self.lock.release()
        return

    def work(self, servings):
        print("serving ", self.name)
        time.sleep(self.servingTime * servings * sleepFactor)

    def queuedCustomers(self):
        return len(self.customerQueue)

    def isNotEmpty(self):
        return len(self.customerQueue) > 1