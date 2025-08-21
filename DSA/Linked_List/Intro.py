"""bulding linked list from scratch. 
 most of the times leetcode gives us the already built 
 linked list, so we can directly use .val for value and .next
 for the next node but here we are going to build ll from s
 scratch.(array -> ll)
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next

values = [1,2,3,4]
head = None
tail = None

for val in values:
    new_node = ListNode(val)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

cur = head
print("1) Standard way to create a linked list and print it")
while cur:
    print(cur.val, end=" -> " if cur.next else "\n")
    cur = cur.next

