class Queue(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, e):
        self.items.insert(0, e)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)