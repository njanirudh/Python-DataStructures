__author__ = 'ANIRUDH'


# FIFO  --> First in First out
# Used in OS scheduling processes.

class Queue:

    def __init__(self):
        self.items = []

# Checks if the given stack is empty or not. Returns True or False
    def isEmpty(self):
        return self.items == []

# Adds the data to the first index of the list
    def enqueue(self, item):
        self.items.insert(0,item)

# Removes the data with largest index from the queue
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
