"""Definition for singly-linked list """

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_numbers(self, l1,l2):
        dummy = ListNode(0)
        current = dummy
        print(current)


    def push(self, new_data):
        new_node = Node(new_data)
	new_node.next = self.head
	self.head = new_node


test = Solution()
test.push(1)
test.push(2)
test.push(3)
print(test)




            
