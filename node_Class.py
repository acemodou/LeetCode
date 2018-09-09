class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n


    """ getters and setters linked list has only one attribute
    head by default. this will point to none if head point to none
    it means linked list is empty """

    def set_next(self):
        self.next_node = n
        
    def get_next(self):
        return self.next_node
    
    def set_data(self):
        self.data = d
        
    def get_data(self):
        return self.data


 
class singleLinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def printNode(self):
        curr = self.root
        while curr:
            print(curr.data)
            curr = curr.get_next()

            


myList = singleLinkedList()
myList.add(5)
myList.add(8)
myList.add(11)
myList.printNode()
        
