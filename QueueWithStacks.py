class QueueWithStacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.in_stack = []
        self.out_stack = []
     
    def enqueue(self, element):
        self.in_stack.append(element)
    
    def dequeue(self):
        
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()