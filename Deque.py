class Deque(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, e):
        self.items.insert(0, e)
    def add_rear(self, e):
        self.items.append(e)
    def remove_front(self):
        return self.items.pop(0)
    def remove_rear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    pass