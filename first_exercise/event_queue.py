import heapq
class EventQueue:
    def __init__(self):
        self.queue = []
        heapq.heapify(self.queue)
    
    def pop(self):
        return heapq.heappop(self.queue)

    def push(self, event):
        heapq.heappush(self.queue, event)
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
