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
        return
    
