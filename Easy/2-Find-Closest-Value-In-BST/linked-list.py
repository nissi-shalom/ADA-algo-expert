class Node:
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.nextvalue = None

class SLinkedList:
    def __init__(self):
        self.headvalue = None
        
    # Print the linked list
    def listprint(self):
        printvalue = self.headvalue

        while printvalue is not None:
            print (printvalue.datavalue)
            printvalue = printvalue.nextvalue
            
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next value to existing node
        NewNode.nextvalue = self.headvalue
        self.headvalue = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        # If there no nodes
        if self.headvalue is None:
            self.headvalue = NewNode
            return
        # Find the last element
        laste = self.headvalue
        while (laste.nextvalue):
            laste = laste.nextvalue
        laste.nextvalue = NewNode

    def InBetween(self, middle_node, newdata):
        found = False
        foundAt = None
        head = self.headvalue
        while (head.nextvalue):
            if head.datavalue == middle_node:
                found = True
                foundAt = head
                break
            head = head.nextvalue
        if found:
            NewNode = Node(newdata)
            NewNode.nextvalue = head.nextvalue
            head.nextvalue = NewNode

    def Remove(self, remove_node):
        found = False
        foundAt = Node
        
        head = self.headvalue
        if head.datavalue == middle_node:
            
        while (head.nextvalue):
                found = True
                foundAt = head
                break
        if found:
            

list = SLinkedList()

# Add values
list.headvalue = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headvalue.nextvalue = e2

# Link second Node to third node
e2.nextvalue = e3

list.AtBegining("Sun")
list.AtEnd("Fri")
list.InBetween("Wed", "Thu")
list.listprint()
