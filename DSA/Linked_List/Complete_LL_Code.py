"""
This script has all main functionalities of single linkedlist
built from scratch.
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for val in iterable:
                self.append(val)

    #-------core ops-----------
    def append(self,val):
        """
        append an element if linked list exist or it is 
        also used to create a fresh LL when the iterable is 
        given, time = o(1) and purpose is either to create new ll
        or append the new_node to the end of LL
        """
        # create a New node using List node class
        new_node = ListNode(val)
        # check if the linkedlist is empty if yes, create new LL
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if LL already exists then add the new node to the end.
        else:
            self.tail.next = new_node
            self.tail = new_node
        #increase the size of ll to reflect the true len of ll
        self.size += 1
    
    def prepend(self,val):
        """
        add the new_node at the beggining of the LL, time o(1)
        """
        # creates a new node with val 
        # and the new_node.next being self.head 
        # i.e new node next pointer is set to the cur head of the lst 
        new_node = ListNode(val, self.head)
        #now we need to update the old head to point to the new node as it is the frst element
        self.head = new_node 
        # edge case if the LL is empty 
        if self.tail is None:
            self.tail = new_node # both head and tail should point to new_node
        self.size += 1 # increase the size of ll








