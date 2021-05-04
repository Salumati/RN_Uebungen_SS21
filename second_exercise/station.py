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

    def queueCustomer(self, customer, maxWait):
        if len(self.customerQueue) <= maxWait:
            self.lock.acquire()
            self.customerQueue.append(customer)
            self.lock.release()
        return
        
    def serveCustomer(self, servings):
        self.work(servings)
        self.customerQueue.pop()
        return

    def work(self, servings):
        print("serving ", self.name)
        time.sleep(self.servingTime * servings * sleepFactor)

    def queuedCustomers(self):
        return len(self.customerQueue)

    def isNotEmpty(self):
        return len(self.customerQueue) > 1
