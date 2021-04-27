import heapq
from threading import Lock

class EventQueue:
    def __init__(self):
        self.lock = Lock()
        self.queue = []
        heapq.heapify(self.queue)
    
    def pop(self):
        self.lock.acquire()
        ev = heapq.heappop(self.queue)
        self.lock.release()
        return ev

    def push(self, event):
        self.lock.acquire()
        heapq.heappush(self.queue, event)
        self.lock.release()
        return

    def work(self):
        for ev in self.queue:
            ev.execute()
            # TODO: calc stats
        return
    

    def isNotEmpty(self):
        return len(self.queue) > 0

    def __str__(self):
        res = ""
        while self.isNotEmpty():
            ev = self.queue.pop()
            res += str(ev) + "\n"
        return res
