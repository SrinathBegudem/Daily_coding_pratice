from collections import deque

"""
═══════════════════════════════════════════════════════════════════════════════
                    COMPLETE DFS PATTERNS GUIDE
═══════════════════════════════════════════════════════════════════════════════

DFS (Depth-First Search):
- Goes as DEEP as possible before backtracking
- Uses Stack (or recursion call stack)
- Space: O(height) - better for deep graphs
- Good for: cycles, paths, backtracking, tree problems

9 ESSENTIAL DFS PATTERNS:
1. Basic DFS (Recursive) - traverse all nodes
2. Basic DFS (Iterative) - using explicit stack
3. DFS for All Paths (Backtracking) - find all possible paths
4. DFS with Path Sum (Tree Paths) - track path with conditions
5. DFS for Disconnected Graph - handle multiple components
6. DFS with Visited (Path Finding) - find single path
7. DFS for Grid/Matrix - 2D traversal (VERY COMMON!)
8. DFS with Return Value - calculate values (depth, diameter)
9. DFS with Parent Tracking (LCA) - lowest common ancestor

═══════════════════════════════════════════════════════════════════════════════
"""


class DFSPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: BASIC DFS (Recursive) ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def dfs_recursive(self, graph, start):
        """
        Standard DFS using recursion
        
        WHEN TO USE:
        - Simple graph traversal
        - Need to visit all nodes
        - Graph has no cycles or use visited set
        
        KEY POINTS:
        1. Mark visited BEFORE recursive calls
        2. Visit all neighbors recursively
        3. Simpler than iterative (uses call stack)
        
        TIME: O(V + E), SPACE: O(V) for visited + O(H) recursion stack
        
        LEETCODE PROBLEMS:
        - 133: Clone Graph
        - 547: Number of Provinces
        - 841: Keys and Rooms
        """
        visited = set()
        res = []
        
        def dfs(node):
            visited.add(node)
            res.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(start)
        return res
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: BASIC DFS (Iterative) ⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def dfs_iterative(self, graph, start):
        """
        DFS using explicit stack (iterative)
        
        WHEN TO USE:
        - Want to avoid recursion (stack overflow risk)
        - Need explicit control over traversal
        
        KEY POINTS:
        1. Use stack instead of queue (LIFO)
        2. Pop from stack end
        3. Same logic as BFS but with stack
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - Same as recursive DFS
        - Useful when recursion depth is concern
        """
        stack = [start]
        visited = set()
        visited.add(start)
        res = []
        
        while stack:
            node = stack.pop()  # Pop from end (LIFO)
            res.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return res
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: DFS FOR ALL PATHS (BACKTRACKING) ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    def all_paths_universal(graph, start, target):
        """
        Find ALL paths from start to target
        Works for BOTH DAG and graphs with cycles!
        
        WHEN TO USE:
        - Find ALL possible paths (not just shortest)
        - Need to explore every route
        - Combination of paths
        
        KEY DIFFERENCE FROM DAG-ONLY:
        ┌─────────────────────────────────────────────────┐
        │ DAG (No Cycles):                                │
        │   - No visited tracking needed                  │
        │   - Just backtrack path                         │
        │                                                 │
        │ Graph WITH Cycles:                              │
        │   - MUST track visited IN CURRENT PATH          │
        │   - Add to visited when entering                │
        │   - Remove from visited when backtracking       │
        └─────────────────────────────────────────────────┘
        
        UNIVERSAL SOLUTION:
        Always use visited set that tracks CURRENT PATH only!
        This works for both DAG and cyclic graphs.
        
        TIME: O(2^V * V) - exponential
        SPACE: O(V) for recursion + path
        
        LEETCODE PROBLEMS:
        - 797: All Paths From Source to Target (DAG)
        - 1059: All Paths from Source Lead to Destination
        - Custom problems with cycles
        """
        result = []
        path = []
        visited = set()  # Track CURRENT PATH only (prevents cycles)
        
        def dfs(node):
            # Add to current path
            path.append(node)
            visited.add(node)  # Mark as visited IN CURRENT PATH
            
            # Found target - save this path
            if node == target:
                result.append(path[:])  # MUST copy path!
            else:
                # Explore all neighbors
                for neighbor in graph[node]:
                    if neighbor not in visited:  # Avoid cycles!
                        dfs(neighbor)
            
            # BACKTRACK
            path.pop()           # Remove from path
            visited.remove(node) # Remove from visited (allow other paths to use this node)
        
        dfs(start)
        return result

    # the above is universal sol and the below is only for DAG (no visited is need)
    def all_paths_source_to_target(self, graph, start, target):
        """
        Find ALL paths from start to target using backtracking
        
        WHEN TO USE:
        - Need ALL possible paths (not just one)
        - Combinations/permutations of paths
        - DAG (Directed Acyclic Graph) problems
        
        KEY POINTS:
        1. Track current PATH (not visited set!)
        2. Add to result when reach target
        3. BACKTRACK after exploring (path.pop())
        4. NO visited set - need to revisit nodes in different paths
        
        TIME: O(2^V * V) - exponential, SPACE: O(V) for recursion
        
        LEETCODE PROBLEMS:
        - 797: All Paths From Source to Target ⭐⭐⭐ (MUST DO)
        - 988: Smallest String Starting From Leaf
        """
        result = []
        path = []
        
        def dfs(node):
            path.append(node)  # Choose
            
            if node == target:
                result.append(path[:])  # Add COPY of path
            else:
                for neighbor in graph[node]:
                    dfs(neighbor)
            
            path.pop()  # Unchoose (Backtrack)
        
        dfs(start)
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: DFS WITH PATH SUM (Tree Paths) ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def all_root_to_leaf_paths(self, root):
        """
        Find all paths from root to leaf in binary tree
        
        WHEN TO USE:
        - Tree path problems
        - Need to collect all root-to-leaf paths
        - Path with conditions (sum, max, etc.)
        
        KEY POINTS:
        1. Track path as we go down
        2. Add to result at LEAF nodes only
        3. Backtrack when returning
        
        TIME: O(N), SPACE: O(H) where H is height
        
        LEETCODE PROBLEMS:
        - 257: Binary Tree Paths ⭐⭐⭐ (MUST DO)
        - 112: Path Sum
        - 113: Path Sum II ⭐⭐⭐ (MUST DO)
        - 437: Path Sum III
        - 129: Sum Root to Leaf Numbers
        """
        result = []
        path = []
        
        def dfs(node):
            if not node:
                return
            
            path.append(node.val)
            
            # LEAF node - add path to result
            if not node.left and not node.right:
                result.append(path[:])
            
            # Recurse on children
            dfs(node.left)
            dfs(node.right)
            
            path.pop()  # Backtrack
        
        dfs(root)
        return result
    
    
    def path_sum_all_paths(self, root, targetSum):
        """
        Find all root-to-leaf paths where sum equals targetSum
        
        LEETCODE: 113 - Path Sum II
        """
        result = []
        path = []
        
        def dfs(node, current_sum):
            if not node:
                return
            
            path.append(node.val)
            current_sum += node.val
            
            # Leaf node with target sum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:])
            
            # Recurse
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            path.pop()  # Backtrack
        
        dfs(root, 0)
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: DFS FOR DISCONNECTED GRAPH ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def dfs_disconnected(self, graph, n):
        """
        DFS that handles disconnected graphs (multiple components)
        
        WHEN TO USE:
        - Graph may have multiple components
        - Need to count/process all components
        - "Number of Islands" type problems
        
        KEY POINTS:
        1. Loop through ALL vertices
        2. Start DFS from unvisited vertices
        3. Shared visited set across all DFS calls
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 200: Number of Islands ⭐⭐⭐ (MUST DO)
        - 547: Number of Provinces ⭐⭐⭐ (MUST DO)
        - 323: Number of Connected Components (Premium)
        - 695: Max Area of Island
        - 1254: Number of Closed Islands
        """
        visited = set()
        components = []
        
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        # Try DFS from every vertex
        for vertex in range(n):
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)
        
        return components
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: DFS WITH VISITED (Path Finding) ⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def has_path_with_visited(self, graph, start, target):
        """
        Check if path exists from start to target
        
        WHEN TO USE:
        - Just need to find ONE path (not all)
        - Graph may have cycles
        - Early termination possible
        
        KEY POINTS:
        1. Use visited set to avoid infinite loops
        2. Return True as soon as target found
        3. Different from "all paths" - stops early
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 1971: Find if Path Exists in Graph
        - 797: All Paths From Source to Target (can optimize)
        """
        visited = set()
        
        def dfs(node):
            if node == target:
                return True
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            return False
        
        return dfs(start)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: DFS FOR GRID/MATRIX ⭐⭐⭐ (VERY IMPORTANT!)
    # ═══════════════════════════════════════════════════════════════════════
    
    def dfs_grid(self, grid, r, c, visited):
        """
        DFS for 2D grid/matrix traversal
        
        WHEN TO USE:
        - 2D grid problems (islands, flood fill)
        - Matrix traversal with constraints
        - Connected components in 2D
        
        KEY POINTS:
        1. Check boundaries (row, col limits)
        2. Check if already visited
        3. Check cell validity (not water, not wall, etc.)
        4. Visit 4 directions (or 8 if diagonal allowed)
        
        TIME: O(rows * cols), SPACE: O(rows * cols) for visited
        
        LEETCODE PROBLEMS:
        - 200: Number of Islands ⭐⭐⭐ (MUST DO FIRST)
        - 733: Flood Fill ⭐⭐ (Easiest grid problem)
        - 695: Max Area of Island ⭐⭐
        - 130: Surrounded Regions
        - 417: Pacific Atlantic Water Flow ⭐⭐
        - 1020: Number of Enclaves
        - 1905: Count Sub Islands
        """
        rows, cols = len(grid), len(grid[0])
        
        # Base cases: out of bounds, visited, or invalid cell
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or grid[r][c] == '0'):
            return
        
        visited.add((r, c))
        
        # Visit 4 directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            self.dfs_grid(grid, r + dr, c + dc, visited)
    
    
    def num_islands(self, grid):
        """
        Complete implementation: Count number of islands
        
        LEETCODE: 200 - Number of Islands
        
        Example:
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 3
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or grid[r][c] == '0'):
                return
            
            visited.add((r, c))
            
            # Visit all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Try DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: DFS WITH RETURN VALUE ⭐⭐⭐ (VERY IMPORTANT!)
    # ═══════════════════════════════════════════════════════════════════════
    
    def max_depth(self, root):
        """
        DFS that returns a calculated value
        
        WHEN TO USE:
        - Need to calculate depth, height, diameter
        - Aggregate values from subtrees
        - Bottom-up calculation
        
        KEY POINTS:
        1. Return value from each recursive call
        2. Combine results from left and right
        3. Use global variable if needed for diameter/path sum
        
        TIME: O(N), SPACE: O(H) for recursion
        
        LEETCODE PROBLEMS:
        - 104: Maximum Depth of Binary Tree ⭐⭐⭐ (MUST DO)
        - 111: Minimum Depth of Binary Tree
        - 110: Balanced Binary Tree
        - 543: Diameter of Binary Tree ⭐⭐⭐
        - 124: Binary Tree Maximum Path Sum ⭐⭐⭐ (Hard)
        """
        if not root:
            return 0
        
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        
        return 1 + max(left_depth, right_depth)
    
    
    def diameter_of_binary_tree(self, root):
        """
        DFS with global variable to track maximum
        
        LEETCODE: 543 - Diameter of Binary Tree
        
        Key: Diameter at each node = left_height + right_height
        """
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update global diameter
            self.max_diameter = max(self.max_diameter, 
                                   left_height + right_height)
            
            # Return height of this subtree
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter
    
    
    def is_balanced(self, root):
        """
        Check if tree is balanced (height-balanced)
        
        LEETCODE: 110 - Balanced Binary Tree
        
        Balanced: left and right subtree heights differ by at most 1
        """
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # If any subtree is unbalanced, return -1
            if (left_height == -1 or right_height == -1 or
                abs(left_height - right_height) > 1):
                return -1
            
            return 1 + max(left_height, right_height)
        
        return dfs(root) != -1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: DFS WITH PARENT TRACKING (LCA) ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def lowest_common_ancestor(self, root, p, q):
        """
        Find Lowest Common Ancestor of two nodes
        
        WHEN TO USE:
        - Need to find LCA of two nodes
        - Path between two nodes
        - Distance between nodes in tree
        
        KEY POINTS:
        1. Return node if it matches p or q
        2. Check both left and right subtrees
        3. If both return non-null, current is LCA
        4. Otherwise return the non-null one
        
        TIME: O(N), SPACE: O(H)
        
        LEETCODE PROBLEMS:
        - 236: Lowest Common Ancestor of Binary Tree ⭐⭐⭐ (MUST DO)
        - 235: Lowest Common Ancestor of BST
        - 1644: Lowest Common Ancestor II (Premium)
        - 1650: Lowest Common Ancestor III (Premium)
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        
        # Both found in different subtrees -> current is LCA
        if left and right:
            return root
        
        # Return whichever is not null
        return left if left else right
    
    
    def distance_between_nodes(self, root, p, q):
        """
        Find distance between two nodes in binary tree
        
        Steps:
        1. Find LCA of p and q
        2. Find distance from LCA to p
        3. Find distance from LCA to q
        4. Return sum of distances
        """
        # Find LCA
        lca = self.lowest_common_ancestor(root, p, q)
        
        def find_distance(node, target, dist):
            if not node:
                return -1
            if node == target:
                return dist
            
            left = find_distance(node.left, target, dist + 1)
            if left != -1:
                return left
            
            return find_distance(node.right, target, dist + 1)
        
        dist_p = find_distance(lca, p, 0)
        dist_q = find_distance(lca, q, 0)
        
        return dist_p + dist_q


# ═══════════════════════════════════════════════════════════════════════
# COMPLETE LEETCODE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

class Solution:
    
    def allPathsSourceTarget(self, graph):
        """
        LeetCode 797: All Paths From Source to Target
        
        Graph is DAG (Directed Acyclic Graph)
        Find all paths from 0 to n-1
        
        Example:
        graph = [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
        
        Difficulty: Medium
        Pattern: DFS with Backtracking (Pattern 3)
        """
        n = len(graph)
        target = n - 1
        result = []
        path = []
        
        def dfs(node):
            path.append(node)
            
            if node == target:
                result.append(path[:])
            else:
                for neighbor in graph[node]:
                    dfs(neighbor)
            
            path.pop()
        
        dfs(0)
        return result
    
    
    def binaryTreePaths(self, root):
        """
        LeetCode 257: Binary Tree Paths
        
        Return all root-to-leaf paths as strings
        
        Example:
        Input: [1,2,3,null,5]
        Output: ["1->2->5","1->3"]
        
        Difficulty: Easy
        Pattern: DFS with Path (Pattern 4)
        """
        if not root:
            return []
        
        result = []
        path = []
        
        def dfs(node):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                result.append("->".join(path))
            
            dfs(node.left)
            dfs(node.right)
            
            path.pop()
        
        dfs(root)
        return result
    
    
    def pathSum(self, root, targetSum):
        """
        LeetCode 113: Path Sum II
        
        Find all root-to-leaf paths where sum equals targetSum
        
        Example:
        root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
        Output: [[5,4,11,2],[5,8,4,5]]
        
        Difficulty: Medium
        Pattern: DFS with Path Sum (Pattern 4)
        """
        result = []
        path = []
        
        def dfs(node, current_sum):
            if not node:
                return
            
            path.append(node.val)
            current_sum += node.val
            
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:])
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            path.pop()
        
        dfs(root, 0)
        return result
    
    
    def numIslands(self, grid):
        """
        LeetCode 200: Number of Islands
        
        Count connected components of '1's in 2D grid
        
        Example:
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 3
        
        Difficulty: Medium
        Pattern: Grid DFS (Pattern 7)
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or grid[r][c] == '0'):
                return
            
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands
    
    
    def floodFill(self, image, sr, sc, color):
        """
        LeetCode 733: Flood Fill
        
        Change color of connected pixels starting from (sr, sc)
        
        Example:
        image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
        Output: [[2,2,2],[2,2,0],[2,0,1]]
        
        Difficulty: Easy
        Pattern: Grid DFS (Pattern 7)
        """
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                image[r][c] != original_color):
                return
            
            image[r][c] = color
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
    
    
    def maxDepth(self, root):
        """
        LeetCode 104: Maximum Depth of Binary Tree
        
        Find the maximum depth (height) of binary tree
        
        Example:
        Input: [3,9,20,null,null,15,7]
        Output: 3
        
        Difficulty: Easy
        Pattern: DFS with Return Value (Pattern 8)
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
    
    
    def diameterOfBinaryTree(self, root):
        """
        LeetCode 543: Diameter of Binary Tree
        
        Find longest path between any two nodes
        
        Example:
        Input: [1,2,3,4,5]
        Output: 3 (path: [4,2,1,3] or [5,2,1,3])
        
        Difficulty: Easy
        Pattern: DFS with Return Value + Global Variable (Pattern 8)
        """
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.max_diameter = max(self.max_diameter, left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return self.max_diameter
    
    
    def lowestCommonAncestor(self, root, p, q):
        """
        LeetCode 236: Lowest Common Ancestor of Binary Tree
        
        Find the LCA of two nodes p and q
        
        Example:
        root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3 (LCA of nodes 5 and 1 is node 3)
        
        Difficulty: Medium
        Pattern: DFS with Parent Tracking (Pattern 9)
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right
    
    
    def findCircleNum(self, isConnected):
        """
        LeetCode 547: Number of Provinces
        
        Count number of connected components (provinces)
        
        Example:
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2 (two provinces: {0,1} and {2})
        
        Difficulty: Medium
        Pattern: DFS for Disconnected Graph (Pattern 5)
        """
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        
        return provinces
    
    
    def maxAreaOfIsland(self, grid):
        """
        LeetCode 695: Max Area of Island
        
        Find maximum area of island (connected 1's)
        
        Example:
        grid = [[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,1]]
        Output: 4
        
        Difficulty: Medium
        Pattern: Grid DFS with Return Value (Pattern 7 + 8)
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            
            # Count current cell + all connected cells
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area


# ═══════════════════════════════════════════════════════════════════════
# QUICK REFERENCE - PATTERN SELECTION GUIDE
# ═══════════════════════════════════════════════════════════════════════

"""
┌─────────────────────────────────────────────────────────────────────────┐
│ DFS PATTERN SELECTION GUIDE                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│ QUESTION TYPE                           → USE PATTERN                    │
│ ─────────────────────────────────────────────────────────────────────── │
│                                                                           │
│ "Find ALL paths"                        → Pattern 3 (Backtracking)       │
│ "Count paths", "All combinations"                                        │
│                                                                           │
│ "Root to leaf paths"                    → Pattern 4 (Tree Paths)         │
│ "Path sum", "Path with condition"                                        │
│                                                                           │
│ "Number of islands"                     → Pattern 7 (Grid DFS)           │
│ "Flood fill", "Connected in 2D"                                          │
│                                                                           │
│ "Max/min depth"                         → Pattern 8 (Return Value)       │
│ "Height", "Diameter", "Balanced"                                         │
│                                                                           │
│ "Lowest common ancestor"                → Pattern 9 (LCA)                │
│ "Distance between nodes"                                                 │
│                                                                           │
│ "Count components"                      → Pattern 5 (Disconnected)       │
│ "Number of provinces"                                                    │
│                                                                           │
│ "Path exists?"                          → Pattern 6 (Path Finding)       │
│ "Can reach from A to B?"                                                 │
│                                                                           │
│ Basic traversal                         → Pattern 1 or 2                 │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘

KEY DECISION POINTS:

1. ALL paths vs ONE path?
   ALL   → No visited set, use backtracking
   ONE   → Use visited set, return early

2. Tree or Graph?
   TREE  → No visited set (no cycles)
   GRAPH → Need visited set (may have cycles)

3. Need return value?
   YES   → Pattern 8 (return from recursive calls)
   NO    → Pattern 1, 3, 4, 7

4. 2D Grid?
   YES   → Pattern 7 (check boundaries + 4 directions)
   NO    → Other patterns

5. Disconnected?
   YES   → Pattern 5 (loop through all vertices)
   NO    → Single DFS call

BACKTRACKING TEMPLATE (Pattern 3):
───────────────────────────────────────
def backtrack(node, path, result):
    path.append(node)           # Choose
    
    if is_target(node):
        result.append(path[:])  # Add COPY!
    else:
        for neighbor in get_neighbors(node):
            backtrack(neighbor, path, result)
    
    path.pop()                  # Unchoose (Backtrack)

GRID DFS TEMPLATE (Pattern 7):
───────────────────────────────────────
def dfs_grid(grid, r, c, visited):
    # Check boundaries and validity
    if (r < 0 or r >= rows or c < 0 or c >= cols or
        (r, c) in visited or grid[r][c] == invalid):
        return
    
    visited.add((r, c))
    
    # Visit 4 directions
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        dfs_grid(grid, r + dr, c + dc, visited)

RETURN VALUE TEMPLATE (Pattern 8):
───────────────────────────────────────
def dfs_with_return(node):
    if not node:
        return base_value
    
    left = dfs_with_return(node.left)
    right = dfs_with_return(node.right)
    
    # Optional: update global variable
    self.result = update(self.result, left, right)
    
    # Return calculated value
    return calculate(left, right)
"""


# ═══════════════════════════════════════════════════════════════════════
# PRACTICE PROBLEMS BY PATTERN
# ═══════════════════════════════════════════════════════════════════════

"""
PATTERN 3: ALL PATHS (BACKTRACKING)
═══════════════════════════════════════
Easy:
- 257: Binary Tree Paths

Medium:
- 797: All Paths From Source to Target ⭐⭐⭐ (START HERE)
- 113: Path Sum II ⭐⭐⭐
- 988: Smallest String Starting From Leaf

Hard:
- 124: Binary Tree Maximum Path Sum ⭐⭐⭐


PATTERN 4: TREE PATHS
═══════════════════════════════════════
Easy:
- 112: Path Sum
- 257: Binary Tree Paths ⭐⭐⭐

Medium:
- 113: Path Sum II ⭐⭐⭐
- 437: Path Sum III ⭐⭐
- 129: Sum Root to Leaf Numbers


PATTERN 5: DISCONNECTED GRAPH
═══════════════════════════════════════
Medium:
- 200: Number of Islands ⭐⭐⭐ (MUST DO)
- 547: Number of Provinces ⭐⭐⭐ (MUST DO)
- 695: Max Area of Island ⭐⭐
- 323: Number of Connected Components (Premium)
- 1254: Number of Closed Islands


PATTERN 7: GRID DFS
═══════════════════════════════════════
Easy:
- 733: Flood Fill ⭐⭐⭐ (START HERE - easiest grid)

Medium:
- 200: Number of Islands ⭐⭐⭐ (MUST DO)
- 695: Max Area of Island ⭐⭐
- 130: Surrounded Regions
- 417: Pacific Atlantic Water Flow ⭐⭐
- 1020: Number of Enclaves
- 1905: Count Sub Islands

Hard:
- 827: Making A Large Island


PATTERN 8: RETURN VALUE
═══════════════════════════════════════
Easy:
- 104: Maximum Depth of Binary Tree ⭐⭐⭐ (START HERE)
- 111: Minimum Depth
- 110: Balanced Binary Tree

Medium:
- 543: Diameter of Binary Tree ⭐⭐⭐ (MUST DO)
- 124: Binary Tree Maximum Path Sum (Hard but important)


PATTERN 9: LCA (PARENT TRACKING)
═══════════════════════════════════════
Easy:
- 235: Lowest Common Ancestor of BST

Medium:
- 236: Lowest Common Ancestor of Binary Tree ⭐⭐⭐ (MUST DO)


PRIORITY ORDER (DO THESE FIRST):
═══════════════════════════════════════
1. 733: Flood Fill (easiest grid)
2. 104: Maximum Depth (easiest return value)
3. 797: All Paths Source to Target (easiest backtracking)
4. 200: Number of Islands (most important grid)
5. 257: Binary Tree Paths (tree paths)
6. 113: Path Sum II (all paths with condition)
7. 547: Number of Provinces (disconnected)
8. 543: Diameter of Binary Tree (return value with global)
9. 236: Lowest Common Ancestor (LCA pattern)
10. 695: Max Area of Island (grid + return value)
"""


# ═══════════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════════

def test_dfs_patterns():
    """Test all DFS patterns"""
    
    print("Testing DFS Patterns...\n")
    
    # Test Pattern 1: Basic DFS
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2]
    }
    patterns = DFSPatterns()
    result = patterns.dfs_recursive(graph, 0)
    print(f"Pattern 1 - Basic DFS: {result}")
    assert len(result) == 5
    print("✅ Pattern 1 passed\n")
    
    # Test Pattern 3: All Paths
    dag = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    all_paths = patterns.all_paths_source_to_target(dag, 0, 3)
    print(f"Pattern 3 - All Paths: {all_paths}")
    assert len(all_paths) == 2
    print("✅ Pattern 3 passed\n")
    
    # Test Pattern 7: Grid DFS (Number of Islands)
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    sol = Solution()
    islands = sol.numIslands(grid)
    print(f"Pattern 7 - Number of Islands: {islands}")
    assert islands == 3
    print("✅ Pattern 7 passed\n")
    
    print("🎉 All tests passed!")


if __name__ == "__main__":
    test_dfs_patterns()