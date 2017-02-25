

class Node:

    def __init__(self,val):
        self.value = val
        self.nextNode = None

    def getValue(self):
        return self.value

    def getNextNode(self):
        return self.nextNode

    def setValue(self,val):
        self.value = val

    def setNextNode(self,nxtNode):
        self.nextNode = nxtNode

"""
Linked List (LL)

Following are the basic operations supported by a list :-

1. Add − Adds an element at the beginning of the list.
2. Deletion − Deletes an element at the beginning of the list.
3. Display − Displays the complete list.
4. Search − Searches an element using the given key.

"""
class LinkedList:

    def __init__(self):
        self.head = None

#Returns 'True' or 'False' depending on the size of the LL
    def isEmpty(self):

        if(self.head == None):
            return True

        else:
            return False

# Add a node to the head of the LL
    def add(self,value):

        temp = Node(value)
        temp.setNextNode(self.head)
        self.head = temp

# gives the total number of elements
    def size(self):
        temp = self.head
        count = 0

        if(temp != None):
            count = 1
            while(temp.getNextNode() != None):
                count += 1
                temp = temp.getNextNode()

        return count

# prints the elemnts in the List
    def printList(self):
            temp = self.head

            while(temp != None):
                print (temp.getValue())
                temp = temp.getNextNode()

    def deleteNode(self,key):
        temp = self.head

        while(temp != None):
            nextNode = temp.getNextNode()
            if(nextNode != None):
                if(nextNode.getValue() == key):
                    temp = temp.setNextNode(nextNode.getNextNode())

                else:
                    temp = temp.getNextNode()




if __name__ == "__main__":

#Create a new linked list
    myList = LinkedList()

# Add elements to the list
    myList.add(1)
    myList.add(2)
    myList.add(3)
    myList.add(4)
    myList.add(5)
    myList.add(6)
    myList.add(3)
    myList.add(7)

# Perform operations on the list
    print ("List Size : " + str(myList.size()))
    myList.printList()

    print ("---------------------")

    myList.deleteNode(3)
    print ("List Size : " + str(myList.size()))
    myList.printList()
