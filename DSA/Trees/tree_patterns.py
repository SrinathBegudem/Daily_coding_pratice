"""
═══════════════════════════════════════════════════════════════════════════════
                    TREE PATTERNS MASTERY GUIDE
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. TREE NODE STRUCTURE:
   class TreeNode:
       def __init__(self, val=0, left=None, right=None):
           self.val = val
           self.left = left
           self.right = right

2. WHY TREES ARE SPECIAL:
   - Hierarchical structure (parent-child relationships)
   - Recursive by nature (left and right subtrees are trees)
   - Many problems have elegant recursive solutions
   - Can represent various real-world data (file systems, org charts, etc.)

3. KEY TREE PROPERTIES:
   - Height: Longest path from root to leaf
   - Depth: Distance from root to a node
   - Level: Same as depth (root is level 0)
   - Balanced: Height difference between subtrees ≤ 1
   - Complete: All levels filled except possibly last (filled left to right)
   - Full: Every node has 0 or 2 children
   - Perfect: All leaves at same level, all internal nodes have 2 children

4. TIME COMPLEXITIES (for Binary Tree with n nodes):
   - DFS Traversal: O(n)
   - BFS Traversal: O(n)
   - Space for recursion: O(h) where h = height
   - Space for BFS queue: O(w) where w = max width

5. 15 ESSENTIAL PATTERNS COVERED:
   ✅ Pattern 1: DFS - Preorder Traversal (Root → Left → Right)
   ✅ Pattern 2: DFS - Inorder Traversal (Left → Root → Right) - BST sorted!
   ✅ Pattern 3: DFS - Postorder Traversal (Left → Right → Root)
   ✅ Pattern 4: BFS - Level Order Traversal (Queue-based)
   ✅ Pattern 5: Path Sum Problems (Root to Leaf paths)
   ✅ Pattern 6: Tree Construction (From traversals/arrays)
   ✅ Pattern 7: Lowest Common Ancestor (LCA)
   ✅ Pattern 8: Tree Views (Left/Right/Top/Bottom)
   ✅ Pattern 9: Serialize & Deserialize
   ✅ Pattern 10: BST Specific Operations
   ✅ Pattern 11: Tree Diameter & Distances
   ✅ Pattern 12: Validate & Convert Trees
   ✅ Pattern 13: Vertical/Diagonal Traversal
   ✅ Pattern 14: Morris Traversal (O(1) space)
   ✅ Pattern 15: Trie Operations (Prefix Tree)

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import Optional, List, Dict
from collections import deque, defaultdict

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreePatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: DFS - PREORDER TRAVERSAL (Root → Left → Right)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Copy/clone a tree (process node before children)
    2. Tree serialization
    3. Prefix expression evaluation
    4. Creating a copy of tree structure
    5. Path from root problems
    
    🔑 KEY CONCEPT:
    Process ROOT first, then LEFT subtree, then RIGHT subtree
    
    ⏱️  Time: O(n) | Space: O(h) recursive, O(n) iterative
    
    📝 DRY RUN - PREORDER:
    Tree:        1
               /   \
              2     3
             / \
            4   5
    
    Preorder: Process Root → Left → Right
    
    Step 1: Visit 1 (root) → output [1]
    Step 2: Go left to 2 → output [1, 2]
    Step 3: Go left to 4 → output [1, 2, 4]
    Step 4: 4 has no children, backtrack
    Step 5: Go right to 5 → output [1, 2, 4, 5]
    Step 6: Backtrack to 1, go right to 3 → output [1, 2, 4, 5, 3]
    
    Result: [1, 2, 4, 5, 3] ✓
    
    🆚 WHEN TO USE PREORDER:
    - Need to process parent before children
    - Creating a copy of tree
    - Prefix notation
    - Tree serialization
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 144: Binary Tree Preorder Traversal (easy) ⭐⭐
    - LeetCode 589: N-ary Tree Preorder Traversal (easy)
    - LeetCode 297: Serialize and Deserialize Binary Tree (hard) ⭐⭐⭐
    - LeetCode 114: Flatten Binary Tree to Linked List (medium) ⭐⭐
    """
    
    def preorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder traversal using recursion
        Most intuitive and clean
        memory trick: process node , then add right to stack and then left
        because stack follows LIFO (So left is processed first)
        for postorder : the order is LRN, we first fo reverse NRL
        That means we do N first then, visit R next that means append LEFT first
        and then we visit L at the end that means push that first to stack
        """
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # Process root first
            result.append(node.val)
            
            # Then left subtree
            dfs(node.left)
            
            # Then right subtree
            dfs(node.right)
        
        dfs(root)
        return result
    
    
    def preorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder using stack (iterative)
        
        🔑 TRICK: Use stack, push right child first (so left is processed first)
        
        📝 ALGORITHM:
        1. Push root to stack
        2. Pop node, process it
        3. Push right child (if exists)
        4. Push left child (if exists)
        5. Repeat until stack empty
        
        Why push right first? Stack is LIFO, so left will be popped first!
        """
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            #process the node
            node = stack.pop()
            result.append(node.val)
            
            # Push right first (will be processed later)
            if node.right:
                stack.append(node.right)
            
            # Push left second (will be processed first)
            if node.left:
                stack.append(node.left)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: DFS - INORDER TRAVERSAL (Left → Root → Right)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Get BST elements in sorted order ⭐⭐⭐ (MOST IMPORTANT!)
    2. Validate BST
    3. Find kth smallest in BST
    4. BST iterator
    5. Infix expression evaluation
    
    🔑 KEY CONCEPT:
    Process LEFT subtree first, then ROOT, then RIGHT subtree
    
    ⏱️  Time: O(n) | Space: O(h)
    
    📝 DRY RUN - INORDER:
    Tree (BST):  4
               /   \
              2     6
             / \   / \
            1   3 5   7
    
    Inorder: Left → Root → Right
    
    Step 1: Go all the way left to 1 → output [1]
    Step 2: Visit parent 2 → output [1, 2]
    Step 3: Go right to 3 → output [1, 2, 3]
    Step 4: Visit root 4 → output [1, 2, 3, 4]
    Step 5: Go left to 5 → output [1, 2, 3, 4, 5]
    Step 6: Visit 6 → output [1, 2, 3, 4, 5, 6]
    Step 7: Go right to 7 → output [1, 2, 3, 4, 5, 6, 7]
    
    Result: [1, 2, 3, 4, 5, 6, 7] - SORTED! ✓
    
    🆚 WHEN TO USE INORDER:
    - Working with BST (gives sorted order!)
    - Need ascending order
    - Validate BST property
    - Find kth element in BST
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 94: Binary Tree Inorder Traversal (easy) ⭐⭐
    - LeetCode 98: Validate Binary Search Tree (medium) ⭐⭐⭐
    - LeetCode 230: Kth Smallest Element in a BST (medium) ⭐⭐⭐
    - LeetCode 173: Binary Search Tree Iterator (medium) ⭐⭐
    - LeetCode 99: Recover Binary Search Tree (medium)
    """
    
    def inorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder traversal using recursion
        For BST: gives sorted order!
        """
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # First left subtree
            dfs(node.left)
            
            # Then process root
            result.append(node.val)
            
            # Then right subtree
            dfs(node.right)
        
        dfs(root)
        return result
    
    
    def inorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder using stack (iterative)
        
        🔑 ALGORITHM:
        1. Go all the way left, pushing nodes to stack
        2. Pop node, process it
        3. Go to right child and repeat
        
        📝 DRY RUN:
        Tree:    1
                  \
                   2
                  /
                 3
        
        curr = 1, stack = []
        Step 1: 1 has no left, push 1 → stack = [1]
        Step 2: Pop 1, process → result = [1], curr = 1.right = 2
        Step 3: 2 has no left, push 2 → stack = [2]
        Step 4: Pop 2... wait, 2 has left child 3!
        
        Let me redo:
        Step 1: curr = 1, push 1, go left (None) → stack = [1]
        Step 2: curr = None, pop 1, process, curr = 1.right = 2 → result = [1]
        Step 3: curr = 2, has left, go left to 3
        Step 4: curr = 3, push 3, go left (None) → stack = [3]
        Step 5: curr = None, pop 3, process, curr = 3.right = None → result = [1,3]
        Step 6: curr = None, stack not empty, pop 2, process → result = [1,3,2]
        
        Wait, that's wrong. Let me think again...
        
        The correct algorithm for iterative inorder:
        - Keep going left and pushing all nodes
        - When can't go left anymore, pop and process
        - Then go right once and repeat
        """
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Go all the way left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the node
            curr = stack.pop()
            result.append(curr.val)
            
            # Go right
            curr = curr.right
        
        return result
    
    
    def kth_smallest_bst(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find kth smallest element in BST
        
        🔑 KEY: Inorder traversal of BST gives sorted order!
        
        📝 EXAMPLE:
        Tree (BST):  5
                   /   \
                  3     6
                 / \
                2   4
               /
              1
        
        Inorder: [1, 2, 3, 4, 5, 6]
        k=3 → return 3 (3rd smallest)
        
        OPTIMIZATION: Can stop early when count reaches k!
        """
        count = 0
        result = None
        
        def inorder(node):
            nonlocal count, result
            if not node or result is not None:
                return
            
            # Left
            inorder(node.left)
            
            # Process root
            count += 1
            if count == k:
                result = node.val
                return
            
            # Right
            inorder(node.right)
        
        inorder(root)
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: DFS - POSTORDER TRAVERSAL (Left → Right → Root)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Delete tree (delete children before parent)
    2. Calculate tree height/depth
    3. Postfix expression evaluation
    4. Bottom-up calculations (diameter, max path sum)
    5. Tree cleanup operations
    
    🔑 KEY CONCEPT:
    Process LEFT subtree, then RIGHT subtree, then ROOT
    Process children before parent!
    
    ⏱️  Time: O(n) | Space: O(h)
    
    📝 DRY RUN - POSTORDER:
    Tree:        1
               /   \
              2     3
             / \
            4   5
    
    Postorder: Left → Right → Root
    
    Step 1: Go all the way left to 4 → output [4]
    Step 2: 4's parent 2 has right child, go to 5 → output [4, 5]
    Step 3: Both children of 2 done, visit 2 → output [4, 5, 2]
    Step 4: Root 1's right child is 3 (leaf) → output [4, 5, 2, 3]
    Step 5: Both children of 1 done, visit 1 → output [4, 5, 2, 3, 1]
    
    Result: [4, 5, 2, 3, 1] ✓
    
    🆚 WHEN TO USE POSTORDER:
    - Need to process children before parent
    - Deleting/freeing tree nodes
    - Calculating heights, depths
    - Bottom-up aggregation (max path sum, diameter)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 145: Binary Tree Postorder Traversal (easy) ⭐⭐
    - LeetCode 543: Diameter of Binary Tree (easy) ⭐⭐⭐
    - LeetCode 124: Binary Tree Maximum Path Sum (hard) ⭐⭐⭐
    - LeetCode 104: Maximum Depth of Binary Tree (easy) ⭐⭐
    - LeetCode 110: Balanced Binary Tree (easy) ⭐⭐
    """
    
    def postorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Postorder traversal using recursion
        Children before parent
        """
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # First left subtree
            dfs(node.left)
            
            # Then right subtree
            dfs(node.right)
            
            # Finally process root
            result.append(node.val)
        
        dfs(root)
        return result
    
    
    def postorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Postorder using stack (iterative)
        
        🔑 TRICK: Use two stacks OR reverse preorder!
        Postorder is L R N. If you do N R L and then reverse, you get L R N.
        Method 1: Reverse Preorder
        - Preorder: Root → Left → Right
        - Modified: Root → Right → Left (swap left/right)
        - Reverse result: Left → Right → Root (Postorder!)
        for postorder : the order is LRN, we first fo reverse NRL
        That means we do N first then, visit R next that means append LEFT first
        and then we visit L at the end that means push that first to stack
        """
        #Postorder is L R N. If you do N R L and then reverse, you get L R N.
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push left first (opposite of preorder)
            if node.left:
                stack.append(node.left)
            
            # Push right second
            if node.right:
                stack.append(node.right)
        
        # Reverse to get postorder
        return result[::-1]
    
    
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Maximum depth of binary tree
        Classic postorder problem!
        
        🔑 KEY: Need children's depths before calculating parent's
        
        📝 EXAMPLE:
        Tree:    3
               /   \
              9    20
                  /  \
                15    7
        
        Postorder calculation:
        - depth(9) = 1
        - depth(15) = 1
        - depth(7) = 1
        - depth(20) = max(depth(15), depth(7)) + 1 = 2
        - depth(3) = max(depth(9), depth(20)) + 1 = 3 ✓
        """
        if not root:
            return 0
        
        # Get left subtree depth
        left_depth = self.max_depth(root.left)
        
        # Get right subtree depth
        right_depth = self.max_depth(root.right)
        
        # Current depth = max of subtrees + 1
        return max(left_depth, right_depth) + 1
    
    
    def diameter_of_tree(self, root: Optional[TreeNode]) -> int:
        """
        Diameter of binary tree (longest path between any two nodes)
        
        🔑 KEY: At each node, diameter = left_height + right_height
        But the actual diameter might pass through a lower node!
        So track maximum while calculating heights (postorder)
        
        📝 EXAMPLE:
        Tree:    1
               /   \
              2     3
             / \
            4   5
        
        At node 2:
        - left_height (from 4) = 0
        - right_height (from 5) = 0
        - diameter through 2 = 0 + 0 = 0
        
        At node 1:
        - left_height (from 2) = 1
        - right_height (from 3) = 0
        - diameter through 1 = 1 + 0 = 1... wait that's not right
        
        Let me recalculate:
        At node 4 (leaf): height = 0
        At node 5 (leaf): height = 0
        At node 2: 
          - left_height = 1 (from 4)
          - right_height = 1 (from 5)
          - diameter = 1 + 1 = 2
          - return height = max(1,1) + 1 = 2
        At node 3 (leaf): height = 0
        At node 1:
          - left_height = 2 (from 2)
          - right_height = 1 (from 3)
          - diameter = 2 + 1 = 3 ✓
        
        💡 LEETCODE PROBLEMS:
        - LeetCode 543: Diameter of Binary Tree (easy) ⭐⭐⭐
        """
        max_diameter = 0
        
        def height(node):
            nonlocal max_diameter
            if not node:
                return 0
            
            # Get heights of subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update max diameter
            max_diameter = max(max_diameter, left_height + right_height)
            
            # Return height of this subtree
            return max(left_height, right_height) + 1
        
        height(root)
        return max_diameter
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: BFS - LEVEL ORDER TRAVERSAL (Queue-based)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Level-by-level processing
    2. Find level with maximum sum
    3. Right side view / Left side view
    4. Zigzag level order
    5. Connect nodes at same level
    6. Find minimum depth (shortest path to leaf)
    
    🔑 KEY CONCEPT:
    Use QUEUE (FIFO) to process nodes level by level
    
    ⏱️  Time: O(n) | Space: O(w) where w = max width
    
    📝 DRY RUN - BFS:
    Tree:        3
               /   \
              9    20
                  /  \
                15    7
    
    Level order: Process each level left to right
    
    Initial: queue = [3]
    
    Level 0:
    - Dequeue 3, add to result → [[3]]
    - Enqueue children 9, 20 → queue = [9, 20]
    
    Level 1:
    - Dequeue 9, add to level → level = [9]
    - Dequeue 20, add to level → level = [9, 20]
    - Enqueue children 15, 7 → queue = [15, 7]
    - Add level to result → [[3], [9, 20]]
    
    Level 2:
    - Dequeue 15, add to level → level = [15]
    - Dequeue 7, add to level → level = [15, 7]
    - No children
    - Add level to result → [[3], [9, 20], [15, 7]] ✓
    
    🆚 DFS vs BFS:
    Use BFS when:
    - Need level information
    - Shortest path (unweighted)
    - Process by levels
    
    Use DFS when:
    - Path from root to leaf
    - Tree height/depth
    - Pre/In/Post order needed
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 102: Binary Tree Level Order Traversal (medium) ⭐⭐⭐
    - LeetCode 103: Binary Tree Zigzag Level Order (medium) ⭐⭐
    - LeetCode 107: Binary Tree Level Order Traversal II (medium)
    - LeetCode 199: Binary Tree Right Side View (medium) ⭐⭐⭐
    - LeetCode 637: Average of Levels (easy)
    - LeetCode 111: Minimum Depth of Binary Tree (easy) ⭐
    """
    
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Level order traversal using queue
        
        🔑 TEMPLATE for level-by-level:
        1. Queue with root
        2. For each level: process all nodes in current queue size
        3. Add children to queue for next level
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # Current level's node count
            level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
    
    
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Right side view of binary tree
        Return rightmost node at each level
        
        🔑 KEY: BFS, take last node of each level
        OR: DFS going right first, track level
        
        📝 EXAMPLE:
        Tree:    1
               /   \
              2     3
               \     \
                5     4
        
        Right side view: [1, 3, 4]
        - Level 0: rightmost = 1
        - Level 1: rightmost = 3
        - Level 2: rightmost = 4
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Last node of this level? Add to result
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
    
    
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Zigzag level order traversal
        Level 0: left to right
        Level 1: right to left
        Level 2: left to right
        ...and so on
        
        🔑 KEY: Normal BFS, but reverse odd-numbered levels
        
        📝 EXAMPLE:
        Tree:    3
               /   \
              9    20
                  /  \
                15    7
        
        Zigzag: [[3], [20,9], [15,7]]
        - Level 0: [3] (left to right)
        - Level 1: [20,9] (right to left - reversed!)
        - Level 2: [15,7] (left to right)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse if going right to left
            if not left_to_right:
                level.reverse()
            
            result.append(level)
            left_to_right = not left_to_right
        
        return result
    
    
    def min_depth(self, root: Optional[TreeNode]) -> int:
        """
        Minimum depth (shortest path to a leaf)
        
        🔑 KEY: BFS finds shortest path! (level of first leaf)
        DFS would need to check ALL leaves
        
        📝 WHY BFS IS BETTER:
        Tree:        1
                   /
                  2
                 /
                3
               /
              4
        
        BFS: checks level by level, would need to go to level 3
        DFS: might go deep first, but then needs to check all paths
        
        For minimum, BFS stops at first leaf! Efficient!
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # First leaf found = minimum depth!
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: PATH SUM PROBLEMS (Root to Leaf Paths)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Path with target sum
    2. All paths from root to leaf
    3. Maximum/minimum path sum
    4. Binary tree paths
    5. Sum of all left leaves
    
    🔑 KEY CONCEPT:
    DFS with path tracking (backtracking)
    Maintain current path/sum as you traverse
    
    ⏱️  Time: O(n) | Space: O(h)
    
    📝 DRY RUN - PATH SUM:
    Tree:        5
               /   \
              4     8
             /     / \
            11    13  4
           /  \        \
          7    2        1
    
    Target sum = 22
    
    Path exploration:
    1. 5 → 4 → 11 → 7: sum = 5+4+11+7 = 27 ✗
    2. 5 → 4 → 11 → 2: sum = 5+4+11+2 = 22 ✓ FOUND!
    
    🆚 WHEN TO USE:
    - Any problem mentioning "path from root to leaf"
    - "Sum of nodes on path"
    - "All paths in tree"
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 112: Path Sum (easy) ⭐⭐
    - LeetCode 113: Path Sum II (medium) ⭐⭐
    - LeetCode 437: Path Sum III (medium) ⭐⭐⭐
    - LeetCode 257: Binary Tree Paths (easy) ⭐
    - LeetCode 129: Sum Root to Leaf Numbers (medium) ⭐⭐
    - LeetCode 404: Sum of Left Leaves (easy)
    """
    
    def has_path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Check if there exists root-to-leaf path with given sum
        
        🔑 KEY: DFS, subtract node value from target
        When reach leaf, check if remaining == 0
        """
        if not root:
            return False
        
        # Leaf node? Check if this completes the sum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursive: check left and right subtrees
        # Subtract current node's value from target
        remaining = targetSum - root.val
        return (self.has_path_sum(root.left, remaining) or 
                self.has_path_sum(root.right, remaining))
    
    
    def path_sum_all_paths(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Find ALL paths with target sum
        
        🔑 KEY: Backtracking! 
        - Add node to path
        - Recurse
        - Remove node from path (backtrack)
        """
        result = []
        
        def dfs(node, remaining, path):
            if not node:
                return
            
            # Add current node to path
            path.append(node.val)
            
            # Leaf node with correct sum?
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])  # Copy the path!
            
            # Recurse on children
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)
            
            # Backtrack: remove current node
            path.pop()
        
        dfs(root, targetSum, [])
        return result
    
    
    def sum_numbers(self, root: Optional[TreeNode]) -> int:
        """
        Sum of all root-to-leaf numbers
        
        📝 EXAMPLE:
        Tree:    1
               /   \
              2     3
        
        Paths:
        - 1 → 2 = 12
        - 1 → 3 = 13
        Total = 12 + 13 = 25
        
        🔑 KEY: Pass down the number formed so far
        number = number * 10 + node.val
        """
        def dfs(node, current_num):
            if not node:
                return 0
            
            # Form number: previous * 10 + current digit
            current_num = current_num * 10 + node.val
            
            # Leaf? Return the number
            if not node.left and not node.right:
                return current_num
            
            # Sum from both subtrees
            return dfs(node.left, current_num) + dfs(node.right, current_num)
        
        return dfs(root, 0)
    
    
    def binary_tree_paths(self, root: Optional[TreeNode]) -> List[str]:
        """
        All root-to-leaf paths as strings
        
        📝 EXAMPLE:
        Tree:    1
               /   \
              2     3
               \
                5
        
        Output: ["1->2->5", "1->3"]
        """
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Add current node
            path += str(node.val)
            
            # Leaf? Add path to result
            if not node.left and not node.right:
                result.append(path)
                return
            
            # Continue with arrow
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: TREE CONSTRUCTION (From Traversals/Arrays)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Build tree from preorder + inorder
    2. Build tree from postorder + inorder
    3. Build tree from array representation
    4. Convert sorted array to BST
    5. Construct from parent array
    
    🔑 KEY CONCEPT:
    - Preorder: First element is root
    - Postorder: Last element is root
    - Inorder: Elements left of root are in left subtree
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - BUILD FROM PREORDER + INORDER:
    Preorder: [3, 9, 20, 15, 7]
    Inorder:  [9, 3, 15, 20, 7]
    
    Step 1: Preorder[0] = 3 is root
    Step 2: Find 3 in inorder → index 1
    Step 3: Inorder left of 3: [9] → left subtree
            Inorder right of 3: [15, 20, 7] → right subtree
    Step 4: Recursively build left with preorder[1:2] and inorder[0:1]
            → node with value 9
    Step 5: Recursively build right with preorder[2:5] and inorder[2:5]
            → preorder[0] = 20 is root of right subtree
            → find 20 in [15, 20, 7] → index 1
            → left = 15, right = 7
    
    Result tree:     3
                   /   \
                  9    20
                      /  \
                    15    7  ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 105: Construct Binary Tree from Preorder and Inorder (medium) ⭐⭐⭐
    - LeetCode 106: Construct Binary Tree from Postorder and Inorder (medium) ⭐⭐
    - LeetCode 108: Convert Sorted Array to BST (easy) ⭐⭐⭐
    - LeetCode 889: Construct Binary Tree from Preorder and Postorder (medium)
    """
    
    def build_tree_pre_in(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build tree from preorder and inorder
        
        🔑 KEY INSIGHTS:
        - Preorder: Root is first
        - Inorder: Root splits left and right subtrees
        - Use hashmap for O(1) root lookup in inorder
        """
        if not preorder:
            return None
        
        # Map value → index in inorder for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            # Root is first in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root in inorder
            root_idx = inorder_map[root_val]
            
            # Size of left subtree
            left_size = root_idx - in_start
            
            # Build left subtree
            root.left = build(
                pre_start + 1,           # Next in preorder
                pre_start + left_size,   # End of left subtree in preorder
                in_start,                # Start in inorder
                root_idx - 1             # Before root in inorder
            )
            
            # Build right subtree
            root.right = build(
                pre_start + left_size + 1,  # After left subtree in preorder
                pre_end,                     # End in preorder
                root_idx + 1,                # After root in inorder
                in_end                       # End in inorder
            )
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
    
    
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Convert sorted array to height-balanced BST
        
        🔑 KEY: Middle element as root ensures balance!
        
        📝 EXAMPLE:
        nums = [-10, -3, 0, 5, 9]
        
        Step 1: mid = 0 (index 2) → root
        Step 2: left = [-10, -3] → mid = -3 → left subtree root
        Step 3: right = [5, 9] → mid = 5 or 9 → right subtree root
        
        Result:      0
                   /   \
                 -3     9
                /      /
              -10     5  ✓
        
        Height balanced: each node's subtrees differ by ≤ 1 in height
        """
        def build(left, right):
            if left > right:
                return None
            
            # Middle as root for balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: LOWEST COMMON ANCESTOR (LCA)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find LCA of two nodes
    2. Distance between two nodes
    3. Check if node is ancestor of another
    4. Find path between two nodes
    
    🔑 KEY CONCEPT:
    LCA is the lowest (deepest) node that has both p and q as descendants
    
    ⏱️  Time: O(n) | Space: O(h)
    
    📝 DRY RUN - LCA:
    Tree:        3
               /   \
              5     1
             / \   / \
            6   2 0   8
               / \
              7   4
    
    Find LCA(5, 1):
    
    At node 3:
    - left search finds 5 in left subtree
    - right search finds 1 in right subtree
    - Both found → 3 is LCA ✓
    
    Find LCA(5, 4):
    
    At node 3:
    - left search goes into left subtree
      At node 5:
      - node == 5, found one!
      - right search finds 4
      - Both found in left subtree → 5 is LCA ✓
    
    🆚 VARIATIONS:
    - Binary Tree: Any tree, need to search both sides
    - BST: Can use values to decide which side to search!
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 236: Lowest Common Ancestor of Binary Tree (medium) ⭐⭐⭐
    - LeetCode 235: Lowest Common Ancestor of BST (easy) ⭐⭐
    - LeetCode 1644: LCA II (nodes might not exist) (medium)
    - LeetCode 1650: LCA III (with parent pointers) (medium)

    The Key diff for lca(236) and lca 2(1644) is that 
    lca 1 :
    - the check condition comes before exploring children 
    - as it is gaurenteed that both p and q exists we return once p or q is found this is premature return 
    - and this works for only lca 1
    lca 2:
    - here your not gauntreed to have p and q 
    - so you should check all nodes before returning 
    - so check should come after the recurse ( visitng both children)
    - this gauntree to visit all the nodes in the tree and checking if node exists 

    """
    
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        LCA in binary tree
        
        🔑 ALGORITHM:
        1. If current node is p or q, return it
        2. Search left and right
        3. If both found in different subtrees, current is LCA
        4. If only one found, return that (LCA is above)
        
        📝 RETURN VALUES:
        - None: neither p nor q found
        - p or q: one of them found (or their LCA)
        - When both found in different subtrees: current node is LCA
        """
        # Base case
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        
        # Both found in different subtrees → current is LCA
        if left and right:
            return root
        
        # Only one found → return that
        return left if left else right
    
    
    def lca_bst(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        LCA in Binary Search Tree
        
        🔑 KEY: Use BST property!
        - If both < root: LCA in left
        - If both > root: LCA in right
        - Otherwise: root is LCA (split point)
        
        📝 EXAMPLE:
        BST:        6
                  /   \
                 2     8
                / \   / \
               0   4 7   9
                  / \
                 3   5
        
        LCA(2, 8):
        At 6: 2 < 6 and 8 > 6 → split! LCA = 6 ✓
        
        LCA(2, 4):
        At 6: both < 6 → go left
        At 2: 2 == 2 → LCA = 2 ✓
        """
        while root:
            # Both in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Both in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # Split point or one equals root
            else:
                return root
        
        return None
    

    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: TREE VIEWS (Left/Right/Top/Bottom)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Right side view (rightmost node per level)
    2. Left side view (leftmost node per level)
    3. Top view (first node at each horizontal distance)
    4. Bottom view (last node at each horizontal distance)
    5. Boundary traversal
    
    🔑 KEY CONCEPT:
    - Right/Left view: BFS, take first/last per level
    - Top/Bottom view: Track horizontal distance, use map
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - TOP VIEW:
    Tree:        1
               /   \
              2     3
             / \   / \
            4   5 6   7
    
    Top view (looking from above):
    
    Horizontal distances (hd):
    - Node 1: hd = 0
    - Node 2: hd = -1, Node 3: hd = +1
    - Node 4: hd = -2, Node 5: hd = 0, Node 6: hd = 0, Node 7: hd = +2
    
    Top view = first node at each hd:
    hd=-2: 4
    hd=-1: 2
    hd=0:  1 (first at hd=0, not 5 or 6)
    hd=+1: 3
    hd=+2: 7
    
    Result: [4, 2, 1, 3, 7] ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 199: Binary Tree Right Side View (medium) ⭐⭐⭐
    - LeetCode 987: Vertical Order Traversal (hard) ⭐⭐
    - LeetCode 314: Binary Tree Vertical Order Traversal (medium)
    - LeetCode 545: Boundary of Binary Tree (medium)
    """
    
    def vertical_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Vertical order traversal (top view / bottom view component)
        
        🔑 KEY: Use horizontal distance (column)
        - Left child: column - 1
        - Right child: column + 1
        - BFS with (node, column) pairs
        """
        if not root:
            return []
        
        # Map: column → list of values
        column_table = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            node, col = queue.popleft()
            column_table[col].append(node.val)
            
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        # Sort by column and return
        return [column_table[col] for col in sorted(column_table.keys())]
    
    
    def top_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Top view: first node at each horizontal distance
        
        🔑 KEY: Use BFS with (node, hd)
        Store only FIRST node per hd (top view)
        """
        if not root:
            return []
        
        # Map: hd → first node value at that hd
        top_view_map = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Only store if this hd not seen before (first = top)
            if hd not in top_view_map:
                top_view_map[hd] = node.val
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Return in left to right order
        return [top_view_map[hd] for hd in sorted(top_view_map.keys())]
    
    
    def bottom_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Bottom view: last node at each horizontal distance
        
        🔑 KEY: Similar to top view, but ALWAYS update (last = bottom)
        """
        if not root:
            return []
        
        bottom_view_map = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Always update (last node at this hd)
            bottom_view_map[hd] = node.val
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        return [bottom_view_map[hd] for hd in sorted(bottom_view_map.keys())]
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: SERIALIZE & DESERIALIZE
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Save tree to file/database
    2. Transmit tree over network
    3. Clone tree
    4. Encode/decode tree structure
    
    🔑 KEY CONCEPT:
    Convert tree to string and back
    - Preorder with null markers
    - Level order with null markers
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - SERIALIZE:
    Tree:    1
           /   \
          2     3
               / \
              4   5
    
    Preorder with nulls:
    - Visit 1 → "1"
    - Visit 2 → "1,2"
    - 2.left = null → "1,2,null"
    - 2.right = null → "1,2,null,null"
    - Visit 3 → "1,2,null,null,3"
    - Visit 4 → "1,2,null,null,3,4"
    - 4.left = null → "1,2,null,null,3,4,null"
    - 4.right = null → "1,2,null,null,3,4,null,null"
    - Visit 5 → "1,2,null,null,3,4,null,null,5"
    - 5.left = null → "1,2,null,null,3,4,null,null,5,null"
    - 5.right = null → "1,2,null,null,3,4,null,null,5,null,null"
    
    Result: "1,2,null,null,3,4,null,null,5,null,null"
    
    DESERIALIZE: Use same preorder traversal, consume tokens
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 297: Serialize and Deserialize Binary Tree (hard) ⭐⭐⭐
    - LeetCode 449: Serialize and Deserialize BST (medium)
    - LeetCode 428: Serialize and Deserialize N-ary Tree (hard)
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Serialize tree to string using preorder
        
        🔑 KEY: Use "null" for None nodes
        This preserves structure!
        """
        def preorder(node):
            if not node:
                return "null"
            
            # Root, Left, Right
            return f"{node.val},{preorder(node.left)},{preorder(node.right)}"
        
        return preorder(root)
    
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Deserialize string to tree
        
        🔑 KEY: Use iterator to consume values in preorder
        """
        def build(vals):
            val = next(vals)
            
            if val == "null":
                return None
            
            # Build root, then left, then right (preorder)
            node = TreeNode(int(val))
            node.left = build(vals)
            node.right = build(vals)
            
            return node
        
        vals = iter(data.split(','))
        return build(vals)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 10: BST SPECIFIC OPERATIONS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Insert into BST
    2. Delete from BST
    3. Search in BST
    4. Find min/max in BST
    5. Kth smallest/largest
    6. Range sum
    
    🔑 KEY CONCEPT:
    BST Property: Left < Root < Right
    - Use this for efficient O(h) operations
    
    ⏱️  Time: O(h) average, O(n) worst | Space: O(h)
    
    📝 DRY RUN - INSERT INTO BST:
    BST:     4
           /   \
          2     7
         / \
        1   3
    
    Insert 5:
    
    Start at 4:
    - 5 > 4 → go right to 7
    - 5 < 7 → go left
    - 7.left is null → insert 5 here!
    
    Result:  4
           /   \
          2     7
         / \   /
        1   3 5  ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 700: Search in a BST (easy) ⭐
    - LeetCode 701: Insert into a BST (medium) ⭐⭐
    - LeetCode 450: Delete Node in a BST (medium) ⭐⭐⭐
    - LeetCode 98: Validate Binary Search Tree (medium) ⭐⭐⭐
    - LeetCode 230: Kth Smallest Element in BST (medium) ⭐⭐⭐
    - LeetCode 538: Convert BST to Greater Tree (medium)
    """
    
    def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Search in BST
        
        🔑 KEY: Use BST property for O(h) search
        """
        if not root or root.val == val:
            return root
        
        # Use BST property to decide direction
        if val < root.val:
            return self.search_bst(root.left, val)
        else:
            return self.search_bst(root.right, val)
    
    
    def insert_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Insert into BST
        
        🔑 KEY: Find correct position using BST property
        """
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert_bst(root.left, val)
        else:
            root.right = self.insert_bst(root.right, val)
        
        return root
    
    
    def delete_bst(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Delete from BST
        
        🔑 THREE CASES:
        1. Node has no children → remove it
        2. Node has one child → replace with that child
        3. Node has two children → replace with inorder successor
           (smallest in right subtree)
        
        📝 EXAMPLE - DELETE 3:
        BST:     5
               /   \
              3     7
             / \
            2   4
        
        Node 3 has two children:
        - Find successor = min of right subtree = 4
        - Replace 3's value with 4
        - Delete 4 from right subtree
        
        Result:  5
               /   \
              4     7
             /
            2  ✓
        """
        if not root:
            return None
        
        # Find node to delete
        if key < root.val:
            root.left = self.delete_bst(root.left, key)
        elif key > root.val:
            root.right = self.delete_bst(root.right, key)
        else:
            # Found the node to delete!
            
            # Case 1 & 2: 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: 2 children
            # Find inorder successor (min in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace value with successor
            root.val = successor.val
            
            # Delete successor from right subtree
            root.right = self.delete_bst(root.right, successor.val)
        
        return root
    
    
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """
        Validate if tree is a valid BST
        
        🔑 KEY: Each node must satisfy:
        - All left descendants < node
        - All right descendants > node
        
        Use min/max bounds!
        
        📝 COMMON MISTAKE:
        Tree:    5
               /   \
              1     4
                   / \
                  3   6
        
        Just checking 4 > 5? NO! Because 3 < 5 too (invalid)
        Must check ALL descendants!
        """
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Current node must be in range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Validate left (all must be < node.val)
            # Validate right (all must be > node.val)
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 11: TREE DIAMETER & DISTANCES
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Diameter of tree (longest path)
    2. Maximum path sum
    3. Distance between two nodes
    4. Width of tree
    
    🔑 KEY CONCEPT:
    At each node: answer = left_height + right_height
    Track global maximum while calculating heights
    
    ⏱️  Time: O(n) | Space: O(h)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 543: Diameter of Binary Tree (easy) ⭐⭐⭐
    - LeetCode 124: Binary Tree Maximum Path Sum (hard) ⭐⭐⭐
    - LeetCode 687: Longest Univalue Path (medium)
    """
    
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Maximum path sum (any node to any node)
        
        🔑 KEY: At each node:
        - max_path_through_node = left_gain + right_gain + node.val
        - return to parent: max(left_gain, right_gain) + node.val
        
        📝 EXAMPLE:
        Tree:    -10
                /   \
               9    20
                   /  \
                 15    7
        
        At node 15: max_sum = 15, return 15
        At node 7: max_sum = 7, return 7
        At node 20:
          - left_gain = 15, right_gain = 7
          - path_through = 15 + 20 + 7 = 42 ✓ (max!)
          - return max(15,7) + 20 = 35 to parent
        At node -10:
          - path_through = 0 + (-10) + 35 = 25 (not better than 42)
        
        Result: 42
        """
        max_sum = float('-inf')
        
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Get max gains from subtrees (ignore negative)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Path sum through this node
            path_sum = left_gain + right_gain + node.val
            
            # Update global max
            max_sum = max(max_sum, path_sum)
            
            # Return max gain from this subtree to parent
            return max(left_gain, right_gain) + node.val
        
        max_gain(root)
        return max_sum


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 30 MUST-KNOW TREE PROBLEMS (RANKED BY IMPORTANCE)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 ABSOLUTE MUST-KNOW (Master These First!):
═══════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LeetCode 94: Binary Tree Inorder Traversal (easy)
   - Pattern: DFS - Inorder
   - Why: Foundation, used in many BST problems
   - Difficulty: 9/10 importance
   - Company: Google, Amazon, Microsoft, Apple

2. ⭐⭐⭐ LeetCode 102: Binary Tree Level Order Traversal (medium)
   - Pattern: BFS
   - Why: Most common tree pattern, used everywhere
   - Difficulty: 10/10 importance
   - Company: Amazon, Microsoft, Facebook, Apple

3. ⭐⭐⭐ LeetCode 236: Lowest Common Ancestor (medium)
   - Pattern: LCA
   - Why: Top 10 most asked tree problem
   - Difficulty: 10/10 importance
   - Company: Facebook, Amazon, Google, LinkedIn

4. ⭐⭐⭐ LeetCode 297: Serialize and Deserialize Binary Tree (hard)
   - Pattern: Serialize/Deserialize
   - Why: Tests deep understanding of trees
   - Difficulty: 9/10 importance
   - Company: Amazon, Google, Facebook, Microsoft

5. ⭐⭐⭐ LeetCode 98: Validate Binary Search Tree (medium)
   - Pattern: BST + DFS
   - Why: Classic BST problem, very common
   - Difficulty: 10/10 importance
   - Company: Amazon, Facebook, Bloomberg, Microsoft

6. ⭐⭐⭐ LeetCode 105: Construct Tree from Preorder and Inorder (medium)
   - Pattern: Tree Construction
   - Why: Tests traversal understanding
   - Difficulty: 8/10 importance
   - Company: Microsoft, Amazon, Facebook

7. ⭐⭐⭐ LeetCode 124: Binary Tree Maximum Path Sum (hard)
   - Pattern: Path Sum + Postorder
   - Why: Hard but very common in top companies
   - Difficulty: 9/10 importance
   - Company: Facebook, Amazon, Google, Microsoft

8. ⭐⭐⭐ LeetCode 230: Kth Smallest Element in BST (medium)
   - Pattern: BST + Inorder
   - Why: Tests BST property understanding
   - Difficulty: 8/10 importance
   - Company: Google, Amazon, Bloomberg, Uber


🔥🔥 VERY IMPORTANT (Must Practice):
═══════════════════════════════════════════════════════════════════════════

9. ⭐⭐ LeetCode 104: Maximum Depth of Binary Tree (easy)
   - Pattern: DFS/BFS
   - Why: Foundation for many problems
   - Difficulty: 7/10 importance

10. ⭐⭐ LeetCode 543: Diameter of Binary Tree (easy)
    - Pattern: Postorder + Diameter
    - Why: Common diameter pattern
    - Difficulty: 8/10 importance

11. ⭐⭐ LeetCode 199: Binary Tree Right Side View (medium)
    - Pattern: BFS + Views
    - Why: Common view problem
    - Difficulty: 7/10 importance

12. ⭐⭐ LeetCode 112: Path Sum (easy)
    - Pattern: Path Sum
    - Why: Foundation for path problems
    - Difficulty: 6/10 importance

13. ⭐⭐ LeetCode 113: Path Sum II (medium)
    - Pattern: Path Sum + Backtracking
    - Why: Backtracking in trees
    - Difficulty: 7/10 importance

14. ⭐⭐ LeetCode 450: Delete Node in a BST (medium)
    - Pattern: BST Operations
    - Why: Tests BST modification
    - Difficulty: 7/10 importance

15. ⭐⭐ LeetCode 108: Convert Sorted Array to BST (easy)
    - Pattern: Tree Construction
    - Why: Common construction problem
    - Difficulty: 7/10 importance


🔥 IMPORTANT (Complete the Foundation):
═══════════════════════════════════════════════════════════════════════════

16. ⭐ LeetCode 226: Invert Binary Tree (easy)
    - Pattern: DFS/BFS
    - Why: Classic simple tree problem
    - Difficulty: 5/10 importance

17. ⭐⭐ LeetCode 110: Balanced Binary Tree (easy)
    - Pattern: Postorder
    - Why: Height calculation
    - Difficulty: 6/10 importance

18. ⭐⭐ LeetCode 111: Minimum Depth of Binary Tree (easy)
    - Pattern: BFS
    - Why: BFS for shortest path
    - Difficulty: 6/10 importance

19. ⭐⭐ LeetCode 144: Binary Tree Preorder Traversal (easy)
    - Pattern: DFS - Preorder
    - Why: Traversal foundation
    - Difficulty: 5/10 importance

20. ⭐⭐ LeetCode 145: Binary Tree Postorder Traversal (easy)
    - Pattern: DFS - Postorder
    - Why: Traversal foundation
    - Difficulty: 5/10 importance

21. ⭐⭐ LeetCode 103: Binary Tree Zigzag Level Order (medium)
    - Pattern: BFS + Zigzag
    - Why: Level order variation
    - Difficulty: 6/10 importance

22. ⭐⭐ LeetCode 235: Lowest Common Ancestor of BST (easy)
    - Pattern: LCA + BST
    - Why: LCA with BST optimization
    - Difficulty: 7/10 importance

23. ⭐⭐ LeetCode 437: Path Sum III (medium)
    - Pattern: Path Sum + Prefix Sum
    - Why: Advanced path sum
    - Difficulty: 7/10 importance

24. ⭐⭐ LeetCode 114: Flatten Binary Tree to Linked List (medium)
    - Pattern: Preorder + Modification
    - Why: Tree modification
    - Difficulty: 6/10 importance

25. ⭐⭐ LeetCode 222: Count Complete Tree Nodes (medium)
    - Pattern: Binary Search + Tree
    - Why: Complete tree optimization
    - Difficulty: 6/10 importance

26. ⭐⭐ LeetCode 572: Subtree of Another Tree (easy)
    - Pattern: DFS + Tree Comparison
    - Why: Tree matching
    - Difficulty: 6/10 importance

27. ⭐⭐ LeetCode 700: Search in a BST (easy)
    - Pattern: BST Operations
    - Why: BST basics
    - Difficulty: 5/10 importance

28. ⭐⭐ LeetCode 701: Insert into a BST (medium)
    - Pattern: BST Operations
    - Why: BST modification
    - Difficulty: 6/10 importance

29. ⭐⭐ LeetCode 129: Sum Root to Leaf Numbers (medium)
    - Pattern: Path Sum
    - Why: Number formation in paths
    - Difficulty: 6/10 importance

30. ⭐⭐ LeetCode 337: House Robber III (medium)
    - Pattern: DFS + DP
    - Why: DP on trees
    - Difficulty: 7/10 importance


═══════════════════════════════════════════════════════════════════════════
📊 PROBLEM DIFFICULTY DISTRIBUTION:
═══════════════════════════════════════════════════════════════════════════

Easy: 12 problems
Medium: 15 problems
Hard: 3 problems

By Pattern:
- DFS Traversals: 8 problems
- BFS: 6 problems
- Path Sum: 5 problems
- BST Operations: 6 problems
- Tree Construction: 3 problems
- LCA: 2 problems
- Other: 5 problems


═══════════════════════════════════════════════════════════════════════════
🎯 STUDY PLAN (4 WEEKS):
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - Traversals & Basics:
Day 1-2: 94 (Inorder), 144 (Preorder), 145 (Postorder)
Day 3-4: 102 (Level Order), 104 (Max Depth), 226 (Invert)
Day 5-6: 112 (Path Sum), 113 (Path Sum II)
Day 7: Review all traversals

WEEK 2 - BST & Construction:
Day 1-2: 98 (Validate BST), 700 (Search BST), 701 (Insert BST)
Day 3-4: 230 (Kth Smallest), 450 (Delete BST)
Day 5-6: 105 (Build Tree), 108 (Array to BST)
Day 7: Review BST operations

WEEK 3 - Advanced Patterns:
Day 1-2: 236 (LCA), 235 (LCA BST)
Day 3-4: 543 (Diameter), 110 (Balanced)
Day 5-6: 199 (Right View), 103 (Zigzag)
Day 7: Review advanced patterns

WEEK 4 - Hard Problems + Review:
Day 1-2: 297 (Serialize/Deserialize) ⚠️ SPEND TIME!
Day 3-4: 124 (Max Path Sum) ⚠️ HARD!
Day 5: 437 (Path Sum III)
Day 6-7: Review ALL 30 problems, redo struggles


═══════════════════════════════════════════════════════════════════════════
💡 HOW TO IDENTIFY WHICH PATTERN TO USE:
═══════════════════════════════════════════════════════════════════════════

KEYWORDS IN PROBLEM → PATTERN:

"inorder" / "sorted order" / "BST"
→ Use Inorder Traversal (Left → Root → Right)

"level" / "level by level" / "each level"
→ Use BFS (Level Order Traversal)

"path from root to leaf" / "root to leaf sum"
→ Use DFS Path Sum Pattern

"height" / "depth" / "balanced"
→ Use Postorder (need children info first)

"diameter" / "longest path" / "maximum path sum"
→ Use Postorder + Track Maximum

"view" / "boundary" / "vertical"
→ Use BFS with coordinates OR DFS with tracking

"construct" / "build tree from"
→ Use Tree Construction Pattern

"common ancestor" / "LCA"
→ Use LCA Pattern

"serialize" / "encode" / "save tree"
→ Use Serialize/Deserialize Pattern

"validate BST" / "search in BST" / "kth element"
→ Use BST Properties


═══════════════════════════════════════════════════════════════════════════
🎓 COMPANY-SPECIFIC FOCUS:
═══════════════════════════════════════════════════════════════════════════

Amazon: 102, 297, 236, 98, 105, 124
Microsoft: 102, 236, 98, 105, 297
Facebook: 236, 124, 297, 98, 102
Google: 98, 230, 236, 297, 124
Apple: 94, 102, 104, 226, 112

If targeting FAANG: Master problems 1-8 + practice company-specific


═══════════════════════════════════════════════════════════════════════════
🚀 PRO TIPS FOR TREE INTERVIEWS:
═══════════════════════════════════════════════════════════════════════════

1. ALWAYS ask about:
   - Is it a BST or regular binary tree?
   - Can there be duplicate values?
   - Can the tree be empty?
   - What's the expected size?

2. DRAW the tree on paper:
   - Visualize with 3-4 nodes
   - Draw your traversal path
   - Mark what you're tracking

3. Identify the pattern:
   - Need sorted order? → Inorder
   - Need level info? → BFS
   - Need height info? → Postorder
   - Process before children? → Preorder

4. Common mistakes to avoid:
   - Not handling None/null pointers
   - Confusing left/right in recursion
   - Forgetting to return node in recursive calls
   - Not considering edge cases (empty tree, single node)

5. BFS vs DFS decision:
   - Shortest path → BFS
   - All paths → DFS
   - Level information → BFS
   - Tree properties (height, diameter) → DFS

6. BST optimization:
   - Always use BST property when given BST!
   - Inorder gives sorted order
   - Can eliminate half the tree with comparisons

7. Space complexity:
   - Recursive DFS: O(h) call stack
   - Iterative DFS: O(h) explicit stack
   - BFS: O(w) queue, where w = max width

8. Time complexity:
   - Almost always O(n) for visiting all nodes
   - BST operations can be O(h) if not visiting all


═══════════════════════════════════════════════════════════════════════════
✅ COMPLETION CHECKLIST:
═══════════════════════════════════════════════════════════════════════════

Fundamentals (Week 1):
□ 94: Inorder Traversal
□ 144: Preorder Traversal
□ 145: Postorder Traversal
□ 102: Level Order Traversal
□ 104: Maximum Depth
□ 226: Invert Tree
□ 112: Path Sum
□ 113: Path Sum II

BST & Construction (Week 2):
□ 98: Validate BST ⚠️
□ 700: Search BST
□ 701: Insert BST
□ 230: Kth Smallest ⚠️
□ 450: Delete BST
□ 105: Build from Traversals ⚠️
□ 108: Array to BST

Advanced (Week 3):
□ 236: LCA ⚠️⚠️
□ 235: LCA BST
□ 543: Diameter
□ 110: Balanced Tree
□ 199: Right Side View
□ 103: Zigzag Level Order

Hard Problems (Week 4):
□ 297: Serialize/Deserialize ⚠️⚠️⚠️
□ 124: Maximum Path Sum ⚠️⚠️⚠️
□ 437: Path Sum III

🎉 Completed all 30? You're a Tree Master! Ready for any tree interview!


═══════════════════════════════════════════════════════════════════════════
🔑 FINAL REMINDERS:
═══════════════════════════════════════════════════════════════════════════

1. Trees are RECURSIVE by nature - embrace recursion!
2. Draw before coding - visualize the tree and your approach
3. Master the 4 traversals - everything builds on these
4. BFS for levels, DFS for paths
5. Postorder for bottom-up calculations
6. BST property is your friend - use it!
7. Track global variables for max/min problems
8. Test with: empty tree, single node, skewed tree
9. Most problems are O(n) time, O(h) space
10. Practice until patterns become second nature!

Remember: Trees might seem hard at first, but they follow clear patterns.
Master these 15 patterns and 30 problems, and you'll be unstoppable! 🚀
"""


def test_tree_patterns():
    """Test all tree patterns"""
    tp = TreePatterns()
    
    # Build test tree:     1
    #                    /   \
    #                   2     3
    #                  / \
    #                 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("🧪 Testing Tree Patterns...\n")
    
    # Test Preorder
    assert tp.preorder_recursive(root) == [1, 2, 4, 5, 3]
    assert tp.preorder_iterative(root) == [1, 2, 4, 5, 3]
    print("✅ Preorder: Passed")
    
    # Test Inorder
    assert tp.inorder_recursive(root) == [4, 2, 5, 1, 3]
    assert tp.inorder_iterative(root) == [4, 2, 5, 1, 3]
    print("✅ Inorder: Passed")
    
    # Test Postorder
    assert tp.postorder_recursive(root) == [4, 5, 2, 3, 1]
    print("✅ Postorder: Passed")
    
    # Test Level Order
    assert tp.level_order(root) == [[1], [2, 3], [4, 5]]
    print("✅ Level Order: Passed")
    
    # Test Max Depth
    assert tp.max_depth(root) == 3
    print("✅ Max Depth: Passed")
    
    # Test Path Sum
    assert tp.has_path_sum(root, 7) == True  # 1 -> 2 -> 4
    assert tp.has_path_sum(root, 10) == False
    print("✅ Path Sum: Passed")
    
    print("\n🎉 All tests passed! Tree patterns mastered!")


if __name__ == "__main__":
    test_tree_patterns()