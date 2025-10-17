"""
═══════════════════════════════════════════════════════════════════════════════
                    LINKEDLIST MASTERY GUIDE
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. LINKEDLIST NODE STRUCTURE:
   class ListNode:
       def __init__(self, val=0, next=None):
           self.val = val
           self.next = next

2. WHY LINKEDLIST IS DIFFERENT FROM ARRAYS:
   - No random access (can't do arr[5])
   - Must traverse from head
   - Easy insertion/deletion (just change pointers)
   - No memory reallocation needed

3. KEY LINKEDLIST OPERATIONS:
   - Traversal: O(n)
   - Insert at head: O(1)
   - Insert at tail: O(n) without tail pointer
   - Delete: O(n) to find, O(1) to delete
   - Search: O(n)

4. COMMON PITFALLS:
   - Losing reference to head
   - Not handling None/null pointers
   - Off-by-one errors
   - Forgetting to update next pointers

5. 9 ESSENTIAL PATTERNS COVERED:
   ✅ Pattern 1: Two Pointers (Fast & Slow) - Cycles, Middle, Nth from end
   ✅ Pattern 2: Reverse LinkedList - Iterative, Recursive, Between positions
   ✅ Pattern 3: Merge Operations - Two lists, K lists, Merge sort
   ✅ Pattern 4: Dummy Node Technique - Simplify edge cases
   ✅ Pattern 5: Two Pointers (General) - Reorder, Partition, Odd-Even
   ✅ Pattern 6: Intersection & Rotation - Find intersection, Rotate, Add numbers
   ✅ Pattern 7: LinkedList + HashMap - Copy random pointer, Complex structures
   ✅ Pattern 8: LRU Cache - Doubly LinkedList + HashMap (TOP INTERVIEW!)
   ✅ Pattern 9: Sort LinkedList - Merge sort implementation

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: TWO POINTERS (FAST & SLOW) - TORTOISE & HARE
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find middle element
    2. Detect cycle
    3. Find cycle start
    4. Check if palindrome
    5. Find kth element from end
    
    🔑 KEY CONCEPT:
    - Slow pointer moves 1 step
    - Fast pointer moves 2 steps
    - When fast reaches end, slow is at middle
    - If there's a cycle, they'll meet
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 DRY RUN - FIND MIDDLE:
    List: 1 → 2 → 3 → 4 → 5 → None
    
    Initial: slow = 1, fast = 1
    
    Step 1: slow = 2, fast = 3
            1 → 2 → 3 → 4 → 5
                ↑       ↑
              slow    fast
    
    Step 2: slow = 3, fast = 5
            1 → 2 → 3 → 4 → 5
                    ↑           ↑
                  slow        fast
    
    Step 3: fast.next = None → STOP
            Return slow = 3 (middle) ✓
    
    📝 DRY RUN - DETECT CYCLE:
    List: 1 → 2 → 3 → 4 → 5
                  ↑_________|  (cycle)
    
    Step 1: slow=2, fast=3
    Step 2: slow=3, fast=5
    Step 3: slow=4, fast=3 (wrapped around)
    Step 4: slow=5, fast=5 → MEET! Cycle detected ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 876: Middle of the Linked List (easy) ⭐
    - LeetCode 141: Linked List Cycle (easy) ⭐
    - LeetCode 142: Linked List Cycle II (medium) ⭐⭐
    - LeetCode 234: Palindrome Linked List (easy)
    - LeetCode 19: Remove Nth Node From End (medium)
    """
    
    def find_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of linked list
        If even length, return second middle
        """
        # Edge case: empty or single node
        if not head or not head.next:
            return head
        
        slow = fast = head
        
        # Move slow by 1, fast by 2
        # When fast reaches end, slow is at middle
        while fast and fast.next:
            slow = slow.next      # Move 1 step
            fast = fast.next.next # Move 2 steps
        
        return slow  # Middle node
    
    
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if linked list has a cycle
        Using Floyd's Cycle Detection (Tortoise & Hare)
        """
        if not head or not head.next:
            return False
        
        slow = fast = head
        
        # If there's a cycle, they'll eventually meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True  # Cycle detected!
        
        return False  # Reached end, no cycle
    
    
    def detect_cycle_start(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the node where cycle begins
        
        🔑 ALGORITHM:
        1. Use fast/slow to detect cycle and find meeting point
        2. Move one pointer to head
        3. Move both by 1 step until they meet
        4. Meeting point is cycle start!
        
        📝 DRY RUN:
        List: 1 → 2 → 3 → 4 → 5
                      ↑_________|
        
        Phase 1: Detect cycle (they meet at node 4)
        Phase 2: ptr1 = head (node 1), ptr2 = meeting point (node 4)
                 Move both by 1 step:
                 ptr1: 1 → 2 → 3
                 ptr2: 4 → 5 → 3
                 They meet at 3! (cycle start) ✓
        """
        if not head or not head.next:
            return None
        
        # Phase 1: Detect cycle and find meeting point
        slow = fast = head
        has_cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                has_cycle = True
                break
        
        if not has_cycle:
            return None
        
        # Phase 2: Find cycle start
        # Move one pointer to head, keep other at meeting point
        ptr1 = head
        ptr2 = slow  # Meeting point
        
        # Move both by 1 step until they meet
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1  # Cycle start node
    
    
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove nth node from end of list
        
        🔑 TRICK: Use two pointers with gap of n
        
        📝 DRY RUN:
        List: 1 → 2 → 3 → 4 → 5, n = 2 (remove 4)
        
        Step 1: Create dummy → 0 → 1 → 2 → 3 → 4 → 5
                Move fast n steps: fast at node 2
                
        Step 2: Move both until fast reaches end:
                slow = 0 → 1 → 2 → 3
                fast = 2 → 3 → 4 → 5 → None
                
        Step 3: slow.next = slow.next.next (skip node 4)
                Result: 1 → 2 → 3 → 5 ✓
        """
        # Dummy node to handle edge cases (removing head)
        dummy = ListNode(0)
        dummy.next = head
        
        slow = fast = dummy
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches end
        # This creates gap of n between slow and fast
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the node (slow.next is the node to remove)
        slow.next = slow.next.next
        
        return dummy.next
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: REVERSE LINKED LIST
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Reverse entire list
    2. Reverse sublist (between positions)
    3. Reverse in k-groups
    4. Check palindrome (reverse second half)
    
    🔑 KEY CONCEPT:
    Change direction of all next pointers
    
    ⏱️  Time: O(n) | Space: O(1) iterative, O(n) recursive
    
    📝 DRY RUN - ITERATIVE REVERSE:
    Original: 1 → 2 → 3 → 4 → 5 → None
    
    Initial: prev = None, curr = 1
    
    Step 1: Save next = 2
            curr.next = None (reverse pointer)
            prev = 1, curr = 2
            
            None ← 1    2 → 3 → 4 → 5
            ↑      ↑    ↑
          prev   was   curr
                curr
    
    Step 2: Save next = 3
            curr.next = 1 (reverse pointer)
            prev = 2, curr = 3
            
            None ← 1 ← 2    3 → 4 → 5
                       ↑    ↑
                     prev  curr
    
    Step 3: Continue until curr = None
    
    Final: None ← 1 ← 2 ← 3 ← 4 ← 5
                                  ↑
                                prev
    
    Return prev (new head = 5) ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 206: Reverse Linked List (easy) ⭐⭐⭐
    - LeetCode 92: Reverse Linked List II (medium) ⭐⭐
    - LeetCode 25: Reverse Nodes in k-Group (hard) ⭐⭐⭐
    - LeetCode 24: Swap Nodes in Pairs (medium)
    """
    
    def reverse_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse linked list iteratively
        
        Core idea: Change each node's next to point backwards
        """
        prev = None
        curr = head
        
        while curr:
            # Save next node before changing pointer
            next_node = curr.next
            
            # Reverse the pointer
            curr.next = prev
            
            # Move prev and curr one step forward
            prev = curr
            curr = next_node
        
        return prev  # New head (was the tail)
    
    
    def reverse_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse linked list recursively
        
        🔑 RECURSIVE THINKING:
        - Base case: empty or single node
        - Recursive case: reverse rest, then attach current
        
        📝 RECURSION TRACE:
        reverse(1 → 2 → 3 → None)
        ├─ reverse(2 → 3 → None)
        │  ├─ reverse(3 → None)
        │  │  └─ return 3 (base case)
        │  └─ Make 3 point to 2: 3 → 2
        │     Make 2.next = None: 3 → 2 → None
        └─ Make 2 point to 1: 3 → 2 → 1
           Make 1.next = None: 3 → 2 → 1 → None ✓
        """
        # Base case: empty or single node
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        new_head = self.reverse_recursive(head.next)
        
        # Make next node point back to current
        head.next.next = head
        
        # Current node becomes tail
        head.next = None
        
        return new_head
    
    
    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse nodes from position left to right
        
        📝 DRY RUN:
        List: 1 → 2 → 3 → 4 → 5, left=2, right=4
        
        Step 1: Find node before left (node 1)
        Step 2: Reverse nodes 2→3→4
        Step 3: Reconnect: 1 → 4 → 3 → 2 → 5 ✓
        """
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        # Find node before left position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the sublist
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: MERGE OPERATIONS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Merge two sorted lists
    2. Merge k sorted lists
    3. Merge sort on linked list
    
    🔑 KEY CONCEPT:
    Compare values and build new list by choosing smaller
    
    ⏱️  Time: O(n+m) for 2 lists, O(nk log k) for k lists
    
    📝 DRY RUN - MERGE TWO SORTED:
    list1: 1 → 3 → 5
    list2: 2 → 4 → 6
    
    Initial: dummy → None
    
    Step 1: Compare 1 vs 2, take 1
            dummy → 1
            
    Step 2: Compare 3 vs 2, take 2
            dummy → 1 → 2
            
    Step 3: Compare 3 vs 4, take 3
            dummy → 1 → 2 → 3
            
    Continue...
    Result: 1 → 2 → 3 → 4 → 5 → 6 ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 21: Merge Two Sorted Lists (easy) ⭐⭐
    - LeetCode 23: Merge k Sorted Lists (hard) ⭐⭐⭐
    - LeetCode 148: Sort List (medium) ⭐⭐
    """
    
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists
        """
        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Compare and merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (one list is exhausted)
        current.next = list1 if list1 else list2
        
        return dummy.next
    
    
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists
        
        🔑 APPROACH: Divide and conquer (merge pairs)
        
        Example: [1→4, 2→5, 3→6, 7→8]
        
        Round 1: Merge pairs
        [1→2→4→5, 3→6→7→8]
        
        Round 2: Merge pairs
        [1→2→3→4→5→6→7→8] ✓
        """
        if not lists or len(lists) == 0:
            return None
        
        # Divide and conquer approach
        while len(lists) > 1:
            merged_lists = []
            
            # Merge pairs of lists
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge_two_lists(list1, list2))
            
            lists = merged_lists
        
        return lists[0]
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: DUMMY NODE TECHNIQUE
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. When head might change (deletion, insertion)
    2. Building new list from scratch
    3. Simplifying edge case handling
    
    🔑 KEY CONCEPT:
    Create dummy node before head to avoid special cases
    
    📝 WHY DUMMY NODE?
    
    WITHOUT dummy (removing first node):
    if head.val == target:
        return head.next  # Special case!
    curr = head
    while curr.next:
        if curr.next.val == target:
            curr.next = curr.next.next
    
    WITH dummy:
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == target:
            curr.next = curr.next.next
    return dummy.next  # No special case needed!
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 203: Remove Linked List Elements (easy) ⭐
    - LeetCode 83: Remove Duplicates from Sorted List (easy)
    - LeetCode 82: Remove Duplicates from Sorted List II (medium)
    """
    
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Remove all nodes with value = val
        """
        # Dummy node simplifies removing head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # Skip the node
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
    
    
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicate values from sorted list
        Keep one occurrence of each value
        
        📝 DRY RUN:
        Input: 1 → 1 → 2 → 3 → 3
        
        Step 1: curr=1, curr.next=1 (duplicate!)
                curr.next = curr.next.next
                Result: 1 → 2 → 3 → 3
                
        Step 2: curr=1, curr.next=2 (different)
                Move curr to 2
                
        Step 3: curr=2, curr.next=3 (different)
                Move curr to 3
                
        Step 4: curr=3, curr.next=3 (duplicate!)
                curr.next = curr.next.next
                Result: 1 → 2 → 3 ✓
        """
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Remove duplicate
                current.next = current.next.next
            else:
                current = current.next
        
        return head
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: LINKEDLIST + TWO POINTERS (GENERAL)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Reorder list
    2. Partition list
    3. Odd-even list
    
    🔑 KEY CONCEPT:
    Use multiple pointers to reorganize list in one pass
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 143: Reorder List (medium) ⭐⭐
    - LeetCode 86: Partition List (medium)
    - LeetCode 328: Odd Even Linked List (medium)
    """
    
    def reorder_list(self, head: Optional[ListNode]) -> None:
        """
        Reorder list: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        
        🔑 ALGORITHM:
        1. Find middle using fast/slow
        2. Reverse second half
        3. Merge two halves alternately
        
        📝 DRY RUN:
        Input: 1 → 2 → 3 → 4 → 5
        
        Step 1: Find middle: slow = 3
        
        Step 2: Reverse second half: 5 → 4 → 3
        
        Step 3: Merge alternately:
                1 → 5 → 2 → 4 → 3 ✓
        """
        if not head or not head.next:
            return
        
        # Step 1: Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        second = slow.next
        slow.next = None  # Split the list
        second = self.reverse_iterative(second)
        
        # Step 3: Merge alternately
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
    
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Partition list: nodes < x before nodes >= x
        
        📝 EXAMPLE:
        Input: 1 → 4 → 3 → 2 → 5 → 2, x = 3
        Output: 1 → 2 → 2 → 4 → 3 → 5
        """
        # Two dummy nodes for two partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        # Partition into two lists
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # Connect two lists
        greater.next = None  # Important: avoid cycle!
        less.next = greater_head.next
        
        return less_head.next
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: LINKEDLIST INTERSECTION & ROTATION
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find intersection of two lists
    2. Rotate list
    3. Add two numbers represented as lists
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 160: Intersection of Two Linked Lists (easy) ⭐⭐
    - LeetCode 61: Rotate List (medium)
    - LeetCode 2: Add Two Numbers (medium) ⭐⭐
    - LeetCode 445: Add Two Numbers II (medium)
    """
    
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Find intersection point of two linked lists
        
        🔑 BRILLIANT TRICK:
        When pointer reaches end, redirect to other list's head
        They'll meet at intersection (or both reach None)
        
        📝 DRY RUN:
        ListA: 1 → 2 → 3 ↘
                          6 → 7 → None
        ListB: 4 → 5 ↗
        
        ptrA: 1→2→3→6→7→None→4→5→6 (meets at 6)
        ptrB: 4→5→6→7→None→1→2→3→6 (meets at 6)
        
        They travel same total distance and meet at intersection!
        """
        if not headA or not headB:
            return None
        
        ptrA, ptrB = headA, headB
        
        # They'll meet at intersection or both become None
        while ptrA != ptrB:
            # When reaching end, redirect to other list
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        
        return ptrA  # Intersection or None
    
    
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate list to the right by k places
        
        📝 DRY RUN:
        Input: 1 → 2 → 3 → 4 → 5, k = 2
        Output: 4 → 5 → 1 → 2 → 3
        
        🔑 ALGORITHM:
        1. Connect tail to head (make circular)
        2. Find new tail (length - k - 1 steps from head)
        3. Break the circle
        """
        if not head or not head.next or k == 0:
            return head
        
        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Optimize k
        k = k % length
        if k == 0:
            return head
        
        # Find new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # Rotate
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head


    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: LINKEDLIST + HASHMAP (Most Important Missing Pattern!)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Copy list with random pointers
    2. LRU Cache (TOP 5 interview question!) ⭐⭐⭐
    3. Clone complex structures
    
    🔑 KEY CONCEPT:
    Use HashMap to track relationships between old and new nodes
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - COPY LIST WITH RANDOM POINTER:
    
    Original List:
    Node 1 (val=7) → Node 2 (val=13) → Node 3 (val=11) → None
      ↓ random          ↓ random          ↓ random
    Node 3            None              Node 1
    
    Step 1: First pass - Create nodes without random
            HashMap: {old_node1: new_node1, old_node2: new_node2, ...}
    
    Step 2: Second pass - Set random pointers
            new_node.random = hashmap[old_node.random]
    
    Result: Exact copy with all pointers intact ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 138: Copy List with Random Pointer (medium) ⭐⭐⭐
    - LeetCode 146: LRU Cache (medium) ⭐⭐⭐ (TOP 5 most asked!)
    - LeetCode 1472: Design Browser History (medium)
    """
    
    def copy_random_list(self, head):
        """
        Copy linked list with random pointer
        Each node has next and random pointer
        
        🔑 ALGORITHM:
        1. Create all new nodes and map old → new
        2. Set next and random using the map
        
        Node definition:
        class Node:
            def __init__(self, val, next=None, random=None):
                self.val = val
                self.next = next
                self.random = random
        """
        if not head:
            return None
        
        # HashMap to store old → new node mapping
        old_to_new = {}
        
        # First pass: Create all nodes
        curr = head
        while curr:
            old_to_new[curr] = ListNode(curr.val)  # Using ListNode as placeholder
            curr = curr.next
        
        # Second pass: Set next and random pointers
        curr = head
        while curr:
            # Set next pointer
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            
            # Set random pointer
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            
            curr = curr.next
        
        return old_to_new[head]
    
    
    def copy_random_list_optimized(self, head):
        """
        SPACE-OPTIMIZED: O(1) space (excluding output)
        
        🔑 BRILLIANT TRICK: Interweave old and new nodes!
        
        📝 ALGORITHM:
        Step 1: Insert copy after each node
                A → A' → B → B' → C → C'
        
        Step 2: Set random pointers
                A'.random = A.random.next
        
        Step 3: Separate the lists
                A → B → C  and  A' → B' → C'
        """
        if not head:
            return None
        
        # Step 1: Create interweaved list
        curr = head
        while curr:
            copy = ListNode(curr.val)  # Using ListNode as placeholder
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        
        # Step 2: Set random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate lists
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        
        return new_head


    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: LRU CACHE (Doubly LinkedList + HashMap)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 THE MOST IMPORTANT PATTERN FOR INTERVIEWS!
    
    Asked by: Google, Amazon, Facebook, Microsoft, Apple, Netflix
    
    🔑 KEY CONCEPT:
    - HashMap: O(1) key → node lookup
    - Doubly LinkedList: O(1) move to front (most recent)
    
    Structure:
    HashMap: {key: Node}
    
    Doubly List: Dummy Head ↔ [Most Recent] ↔ ... ↔ [Least Recent] ↔ Dummy Tail
    
    Operations:
    - get(key): Move accessed node to front (most recent)
    - put(key, val): Add to front, evict from tail if capacity exceeded
    
    ⏱️  Time: O(1) for both get and put | Space: O(capacity)
    
    📝 DRY RUN:
    Capacity = 2
    
    Operation 1: put(1, 1)
    Cache: [1]
    List: Head ↔ (1,1) ↔ Tail
    
    Operation 2: put(2, 2)
    Cache: [1, 2]
    List: Head ↔ (2,2) ↔ (1,1) ↔ Tail
    
    Operation 3: get(1)
    Move (1,1) to front (most recent)
    List: Head ↔ (1,1) ↔ (2,2) ↔ Tail
    Return: 1
    
    Operation 4: put(3, 3)
    Capacity exceeded! Evict (2,2) from tail
    Add (3,3) to front
    List: Head ↔ (3,3) ↔ (1,1) ↔ Tail
    Cache: [1, 3]
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 146: LRU Cache (medium) ⭐⭐⭐ MUST KNOW!
    - LeetCode 460: LFU Cache (hard)
    """
    
    class DListNode:
        """Doubly Linked List Node for LRU Cache"""
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    
    class LRUCache:
        """
        LRU Cache using Doubly LinkedList + HashMap
        
        🔑 CORE OPERATIONS:
        1. _add_to_front(node): Add node right after head (most recent)
        2. _remove(node): Remove node from current position
        3. _move_to_front(node): Remove + Add to front
        4. _evict_lru(): Remove node before tail (least recent)
        """
        
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = {}  # key → DListNode
            
            # Dummy head and tail for easy operations
            self.head = self.DListNode()
            self.tail = self.DListNode()
            self.head.next = self.tail
            self.tail.prev = self.head
        
        
        def _add_to_front(self, node):
            """Add node right after head (most recently used)"""
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
        
        
        def _remove(self, node):
            """Remove node from its current position"""
            node.prev.next = node.next
            node.next.prev = node.prev
        
        
        def _move_to_front(self, node):
            """Move existing node to front (mark as recently used)"""
            self._remove(node)
            self._add_to_front(node)
        
        
        def _evict_lru(self):
            """Remove least recently used (node before tail)"""
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        
        
        def get(self, key: int) -> int:
            """
            Get value by key, mark as recently used
            Return -1 if not found
            """
            if key not in self.cache:
                return -1
            
            node = self.cache[key]
            self._move_to_front(node)  # Mark as recently used
            return node.val
        
        
        def put(self, key: int, value: int) -> None:
            """
            Put key-value pair
            If key exists: update value and move to front
            If new key: add to front, evict LRU if capacity exceeded
            """
            if key in self.cache:
                # Update existing key
                node = self.cache[key]
                node.val = value
                self._move_to_front(node)
            else:
                # Add new key
                if len(self.cache) >= self.capacity:
                    self._evict_lru()  # Make space
                
                new_node = self.DListNode(key, value)
                self.cache[key] = new_node
                self._add_to_front(new_node)
        
        # Nested class reference
        DListNode = DListNode


    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: SORT LINKED LIST (Merge Sort)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Sort linked list in O(n log n) time, O(1) space
    
    🔑 KEY CONCEPT:
    Merge Sort is perfect for linked lists!
    - No random access needed
    - Efficient in-place merging
    
    📝 ALGORITHM:
    1. Find middle using fast/slow pointers
    2. Split into two halves
    3. Recursively sort both halves
    4. Merge sorted halves
    
    ⏱️  Time: O(n log n) | Space: O(log n) for recursion stack
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 148: Sort List (medium) ⭐⭐
    - LeetCode 147: Insertion Sort List (medium)
    """
    
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort linked list using merge sort
        
        📝 DRY RUN:
        Input: 4 → 2 → 1 → 3
        
        Split: [4, 2] and [1, 3]
        
        Recursively sort:
        [4, 2] → [2, 4]
        [1, 3] → [1, 3]
        
        Merge: [1, 2, 3, 4] ✓
        """
        # Base case: empty or single node
        if not head or not head.next:
            return head
        
        # Step 1: Find middle and split
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split at middle
        mid = slow.next
        slow.next = None
        
        # Step 2: Recursively sort both halves
        left = self.sort_list(head)
        right = self.sort_list(mid)
        
        # Step 3: Merge sorted halves
        return self.merge_two_lists(left, right)


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 15 MUST-KNOW PROBLEMS (RANKED BY IMPORTANCE)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 ABSOLUTE MUST-KNOW (Do These First!):
═══════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LeetCode 206: Reverse Linked List (easy)
   - Pattern: Reverse
   - Why: Foundation for many problems, asked EVERYWHERE
   - Difficulty: 8/10 importance
   
2. ⭐⭐⭐ LeetCode 146: LRU Cache (medium)
   - Pattern: Doubly LinkedList + HashMap
   - Why: Top 5 most asked, tests multiple concepts
   - Asked by: Google, Amazon, Facebook, Microsoft, Apple
   - Difficulty: 10/10 importance
   
3. ⭐⭐⭐ LeetCode 141: Linked List Cycle (easy)
   - Pattern: Two Pointers (Fast & Slow)
   - Why: Classic algorithm, very common
   - Difficulty: 9/10 importance

4. ⭐⭐⭐ LeetCode 21: Merge Two Sorted Lists (easy)
   - Pattern: Merge
   - Why: Foundation for merge sort, very common
   - Difficulty: 8/10 importance

5. ⭐⭐⭐ LeetCode 138: Copy List with Random Pointer (medium)
   - Pattern: HashMap
   - Why: Tests deep understanding of pointers
   - Asked by: Amazon, Microsoft, Facebook
   - Difficulty: 9/10 importance


🔥🔥 VERY IMPORTANT (Must Practice):
═══════════════════════════════════════════════════════════════════════════

6. ⭐⭐ LeetCode 19: Remove Nth Node From End (medium)
   - Pattern: Two Pointers
   - Why: Common follow-up question
   - Difficulty: 7/10 importance

7. ⭐⭐ LeetCode 2: Add Two Numbers (medium)
   - Pattern: Basic Operations
   - Why: Tests digit manipulation, very common
   - Difficulty: 7/10 importance

8. ⭐⭐ LeetCode 142: Linked List Cycle II (medium)
   - Pattern: Two Pointers (Advanced)
   - Why: Follow-up to cycle detection
   - Difficulty: 8/10 importance

9. ⭐⭐ LeetCode 143: Reorder List (medium)
   - Pattern: Multiple techniques combined
   - Why: Tests ability to combine patterns
   - Difficulty: 7/10 importance

10. ⭐⭐ LeetCode 160: Intersection of Two Linked Lists (easy)
    - Pattern: Two Pointers (Clever trick)
    - Why: Tests logical thinking
    - Difficulty: 6/10 importance


🔥 IMPORTANT (Complete the Foundation):
═══════════════════════════════════════════════════════════════════════════

11. ⭐⭐ LeetCode 148: Sort List (medium)
    - Pattern: Merge Sort
    - Why: Tests O(n log n) understanding
    - Difficulty: 7/10 importance

12. ⭐ LeetCode 876: Middle of the Linked List (easy)
    - Pattern: Two Pointers
    - Why: Building block for other problems
    - Difficulty: 5/10 importance

13. ⭐⭐ LeetCode 234: Palindrome Linked List (easy)
    - Pattern: Two Pointers + Reverse
    - Why: Combines multiple patterns
    - Difficulty: 6/10 importance

14. ⭐⭐⭐ LeetCode 23: Merge k Sorted Lists (hard)
    - Pattern: Merge + Divide & Conquer
    - Why: Advanced version of merge two lists
    - Asked by: Google, Amazon, Facebook
    - Difficulty: 8/10 importance

15. ⭐⭐⭐ LeetCode 25: Reverse Nodes in k-Group (hard)
    - Pattern: Reverse (Advanced)
    - Why: Most difficult reverse problem
    - Asked by: Facebook, Microsoft
    - Difficulty: 7/10 importance


═══════════════════════════════════════════════════════════════════════════
📊 PROBLEM DIFFICULTY DISTRIBUTION:
═══════════════════════════════════════════════════════════════════════════

Easy: 5 problems (206, 141, 21, 876, 234, 160)
Medium: 8 problems (146, 138, 19, 2, 142, 143, 148, 23)
Hard: 2 problems (23, 25)

Total: 15 problems covering ALL patterns


═══════════════════════════════════════════════════════════════════════════
🎯 STUDY PLAN (4 WEEKS):
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - Foundation:
Day 1-2: 206 (Reverse), 876 (Middle)
Day 3-4: 141 (Cycle), 142 (Cycle II)
Day 5-6: 21 (Merge Two), 19 (Remove Nth)
Day 7: Review + Practice

WEEK 2 - Core Patterns:
Day 1-2: 138 (Copy Random Pointer) ⚠️ Challenging!
Day 3-5: 146 (LRU Cache) ⚠️ SPEND TIME HERE!
Day 6: 2 (Add Two Numbers)
Day 7: Review + Practice

WEEK 3 - Advanced Patterns:
Day 1-2: 143 (Reorder List)
Day 3-4: 148 (Sort List)
Day 5: 234 (Palindrome)
Day 6: 160 (Intersection)
Day 7: Review + Practice

WEEK 4 - Hard Problems + Review:
Day 1-3: 23 (Merge k Lists)
Day 4-5: 25 (Reverse k-Group)
Day 6-7: Review ALL 15 problems, redo the ones you struggled with


═══════════════════════════════════════════════════════════════════════════
💡 PRO TIPS FOR INTERVIEWS:
═══════════════════════════════════════════════════════════════════════════

1. ALWAYS use dummy node when:
   - Head might be deleted
   - Building new list
   - Unsure about edge cases

2. Check for None/null BEFORE accessing:
   - curr.next (check if curr exists first!)
   - Always handle empty list edge case

3. Draw it out:
   - Visualize with 3-4 nodes
   - Test with 1 node, 2 nodes

4. Common edge cases:
   - Empty list (head = None)
   - Single node
   - Two nodes
   - All same values
   - Cycles

5. Space complexity:
   - Iterative: O(1)
   - Recursive: O(n) for call stack

6. Practice the "verbal walk-through":
   - Explain your approach before coding
   - "I'll use two pointers, slow and fast..."


═══════════════════════════════════════════════════════════════════════════
🎓 COMPANY-SPECIFIC FOCUS:
═══════════════════════════════════════════════════════════════════════════

Google: 146 (LRU), 138 (Copy Random), 23 (Merge k)
Amazon: 206 (Reverse), 21 (Merge), 2 (Add Two)
Facebook: 146 (LRU), 25 (Reverse k), 138 (Copy Random)
Microsoft: 206 (Reverse), 141 (Cycle), 19 (Remove Nth)
Apple: 206 (Reverse), 234 (Palindrome), 2 (Add Two)

If targeting FAANG: Master problems 1-5 + 14-15 (the ⭐⭐⭐ ones)


═══════════════════════════════════════════════════════════════════════════
✅ COMPLETION CHECKLIST:
═══════════════════════════════════════════════════════════════════════════

Basic Patterns (Week 1):
□ 206: Reverse Linked List
□ 876: Middle of Linked List
□ 141: Linked List Cycle
□ 142: Linked List Cycle II
□ 21: Merge Two Sorted Lists
□ 19: Remove Nth Node From End

Advanced Patterns (Week 2-3):
□ 138: Copy List with Random Pointer ⚠️
□ 146: LRU Cache ⚠️⚠️
□ 2: Add Two Numbers
□ 143: Reorder List
□ 148: Sort List
□ 234: Palindrome Linked List
□ 160: Intersection of Two Lists

Hard Problems (Week 4):
□ 23: Merge k Sorted Lists
□ 25: Reverse Nodes in k-Group

🎉 Completed all 15? You're interview-ready!
"""
