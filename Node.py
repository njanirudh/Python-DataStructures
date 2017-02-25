# Python class to create a simple Node class that can be used to create data structures like Linked Lists and Trees

"""
Node class requirements :
    1. Save some data
    2. Returns the next node
"""


class Node:

    def __init__(self,val):
        self.value = val    # Data stored in an individual node
        self.nextNode = None # Pointer to the next Node

    def getValue(self):
        return self.value

    def getNext(self):
        return self.nextNode

if __name__ == "__main__":

    #Creating a new node and assignina a value to it
    firstNode = Node(20)
    firstNode.nextNode = None

    print (firstNode.getValue())