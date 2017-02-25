
# LIFO --> Last in First out
# Example use is in Browser back button. Url stored in the form of a stack

class Stack:


    def __init__(self):
        self.items = []

#Checks if the given stack is empty or not. Returns True or False
    def isEmpty(self):
        return self.items == []

#Adds data to index 0
    def push(self, item):
        self.items.insert(0,item)

#Removes data having index 0 ie. First data
    def pop(self):
        return self.items.pop(0)

#Remove data from the top most part of the stack
    def peek(self):
        return self.items[0]

# Total number of items present in the stack
    def size(self):
        return len(self.items)


s = Stack()
s.push("1")
s.push("2")

print s.pop()
print s.peek()

