import event
import event_queue
import time
from threading import Lock
from config import sleepFactor
from statistics import Statistics

class Station():
    def __init__(self, name, servingTime = 0):
        self.name = name
        self.lock = Lock()
        self.servingTime = servingTime
        self.customerQueue = []

    def queueCustomer(self, customer, maxWait):
        if len(self.customerQueue) < maxWait:
            self.lock.acquire()
            print(self.name + " queued customer: " + customer.name)
            self.customerQueue.append(customer)
            self.lock.release()
        else:
            Statistics.stations[self.name].addTotalLeapCustomer()
        return
        
    def serveCustomer(self, servings):
        self.work(servings)
        self.lock.acquire()
        print("popping at station ", self.name)
        if len(self.customerQueue) > 0:
            customer = self.customerQueue.pop()
            print(self.name + " just served: " + customer.name)
        Statistics.stations[self.name].addTotalServedCustomer()
        self.lock.release()
        return

    def work(self, servings):
        time.sleep(self.servingTime * servings * sleepFactor)

    def queuedCustomers(self):
        return len(self.customerQueue)

    def isNotEmpty(self):
        return len(self.customerQueue) > 1

    def copyShallow(self):
        return Station(self.name, self.servingTime)