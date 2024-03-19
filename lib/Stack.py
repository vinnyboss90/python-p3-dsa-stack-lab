class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if not self.items:
            return True
        return False

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)
        # else: raise ValueError("Stack full")

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return (self.size() >= self.limit)

    def search(self, target):
        l = len(self.items)
        for i in range(l):
            if self.items[i] == target:
                return l - (i + 1)
            
        return -1