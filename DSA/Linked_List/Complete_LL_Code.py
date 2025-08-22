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
        self._size = 0
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
        #increase the _size of ll to reflect the true len of ll
        self._size += 1
    
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
        self._size += 1 # increase the _size of ll
    
    #-------internal--------
    def _node_at(self,index):
        """
        Return the node at index (0 based indexing)
        """
        cur = self.head
        for _ in index:
            cur = cur.next
        return cur 
    
    def insert_at(self, index, val):
        """
        To insert a val at given index, time is 0(n) coz of travsersal
        """
        #edge cases
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(val)
        if index == self._size:
            self.append(val)

        #traverse till index using _node_at function 
        prev = self._node_at(index-1)
        #create a new node and directly link it to the prev.nxt
        new_node = ListNode(val,prev.next)
        #now update prev.next to point towards the new node
        prev.next = new_node
        #increase the _size
        self._size += 1
    
    def pop_front(self):
        """
        Remove the first element in LL and return it, time is o(1)
        """
        #edge case 
        if not self.head :
            raise IndexError("Linked List is empty")
        node = self.head
        self.head = node.next
        # if we only have one node and we popped it then we do
        if self.head is None:
            self.tail = None
        self._size -= 1
        return node.val
    
    def pop_end(self):
        """
        The important point is that the singly linked list 
        thou it has the tail we cannot move backwards, 
        so to remove last element we need to move one step back and 
        set last before node pointing towards None, as i mention we 
        cannot move back therefore we need to travser from start 
        Time = O(1) and we usually have a single fucntion called 
        remove_at for poping the end element, but here for pratice 
        we are just calling remove_at function for _size - 1 for pop_end
        """
        return self.remove_at(self._size-1)
    
    def remove_at(self, index):
        """
        Removing the node at given index, time o(n) walk
        """
        if index < 0 or index >= self._size:
            raise IndexError("index out of bounds")
        if index == 0:
            return self.pop_front()
        prev = self._node_at(index - 1)
        node = prev.next
        prev.next = node.next
        node.next = None



    def remove_at(self, index, val):

    











