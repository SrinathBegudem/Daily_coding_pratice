"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Good problem which uses concept of pointer and hashmap
        twoways to solve and its two pass algo 
        one : create a linked list copy with only next pointer and then use map to store old node info in key and new node info in val, so when ever we do new_node.random = map[old_node.random] so that paticular random take you towards the key that the old node pointing and as we are using map[key] = val so you will be given the val pointer of the new node.
        two: just create nodes and then in second pass join next and random with map help
        """
        return self.case2_sol(head)
    
    def case1_sol(self,head):
        #base case:
        if not head:
            return None
        #method1: lets create linkedlist with without random pointer and also store all the old -> new node in dict so we have the information for the next pass 
        # map old node -> new node; seed None so random=None works naturally
        # None:None mandatory and edge case because if the old.random points towards None
        #oldTonew[None] should be None. this is the most imp edge case 
        oldToNew = {None:None}

        # ---- PASS 1: build the new list with only next pointers ----
        cur_old = head
        new_head = Node(cur_old.val)
        oldToNew[cur_old] = new_head

        cur_new = new_head
        cur_old = cur_old.next
        while cur_old:
            cur_new.next = Node(cur_old.val)
            cur_new = cur_new.next
            oldToNew[cur_old] = cur_new
            cur_old = cur_old.next

        # ---- PASS 2: attach random pointers using the map ----
        cur_old = head
        cur_new = new_head
        while cur_old:
            cur_new.random = oldToNew[cur_old.random]
            cur_new = cur_new.next
            cur_old = cur_old.next
        return new_head
            


    def case2_sol(self,head):
        # this function is prefered to due its clean and easy code 
        #now we first pass we create nodes and in second pass we attach next and random 
        if not head:
            return None
        
        #dict to map old to new 
        oldToNew = {None:None}

        # pass 1 : create nodes and push old and new to map
        # so her we are creating nodes and storing them in map if not they will be created and lost as there is no pointer stiching them so imp point is we store this ndoes in map to sticht them later
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        #pass 2 : wireup the next pointer and random pointer
        cur = head
        while cur:
            clone = oldToNew[cur]
            clone.next = oldToNew[cur.next]
            clone.random = oldToNew[cur.random]
            cur = cur.next
        return oldToNew[head]
            