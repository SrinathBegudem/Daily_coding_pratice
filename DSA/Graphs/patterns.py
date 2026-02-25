"""
═══════════════════════════════════════════════════════════════════════════════
                    GRAPH TRAVERSAL MASTERY GUIDE - COMPLETE
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. WHAT IS A GRAPH?
   - Collection of nodes (vertices) connected by edges
   - Can be directed or undirected
   - Can be weighted or unweighted
   - Can have cycles or be acyclic (trees are special acyclic graphs)

2. GRAPH REPRESENTATIONS:
   
   Adjacency List (Most Common):
   graph = {
       0: [1, 2],
       1: [0, 3],
       2: [0, 3],
       3: [1, 2]
   }
   
   Adjacency Matrix:
   graph = [
       [0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]
   ]
   
   Edge List:
   edges = [(0,1), (0,2), (1,3), (2,3)]

3. BFS vs DFS - WHEN TO USE WHAT?
   
   USE BFS WHEN:
   ✅ Finding shortest path (unweighted graphs)
   ✅ Level-order traversal needed
   ✅ Finding nodes at exact distance k
   ✅ Testing bipartiteness
   ✅ Finding connected components (either works, but BFS more intuitive)
   
   USE DFS WHEN:
   ✅ Detecting cycles
   ✅ Topological sorting
   ✅ Finding strongly connected components
   ✅ Path finding (any path, not necessarily shortest)
   ✅ Backtracking problems
   ✅ Maze solving

4. KEY DIFFERENCES:
   
   BFS (Breadth-First Search):
   - Uses Queue (FIFO)
   - Explores level by level
   - Space: O(width) - can be large for wide graphs
   - Guarantees shortest path in unweighted graphs
   
   DFS (Depth-First Search):
   - Uses Stack (LIFO) or recursion
   - Explores as deep as possible first
   - Space: O(height) - better for deep, narrow graphs
   - Doesn't guarantee shortest path

5. 13 ESSENTIAL PATTERNS COVERED:
   ✅ Pattern 1: Classic BFS (Level-by-Level)
   ✅ Pattern 2: Classic DFS (Recursive & Iterative)
   ✅ Pattern 3: Shortest Path (Unweighted Graph)
   ✅ Pattern 4: Connected Components
   ✅ Pattern 5: Cycle Detection (Directed & Undirected)
   ✅ Pattern 6: Topological Sort (DFS & Kahn's)
   ✅ Pattern 7: Bipartite Graph Check
   ✅ Pattern 8: Island Problems (Grid DFS/BFS) ⭐⭐⭐
   ✅ Pattern 9: Clone Graph (DFS with HashMap) ⭐⭐⭐
   ✅ Pattern 10: Word Ladder (BFS Transformation) ⭐⭐⭐
   ✅ Pattern 11: Multi-source BFS (Rotting Oranges) ⭐⭐
   ✅ Pattern 12: Dijkstra's Algorithm (Weighted Shortest Path) ⭐⭐
   ✅ Pattern 13: Union Find (Disjoint Set Union) ⭐⭐

Missing patterns 
    MST: Kruskal (Union Find) and Prim (heap). 
    This shows up as “minimum cost to connect…”
    0-1 BFS: only when weights are 0 or 1. 
    It’s a common trick upgrade over Dijkstra.

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import deque, defaultdict
import heapq


class GraphTraversalPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: CLASSIC BFS (Level-by-Level Traversal)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Traverse graph level by level, shortest path in unweighted graph
    
    🔑 KEY CONCEPT:
    - Use Queue (FIFO)
    - Process nodes level by level
    - Track visited to avoid cycles
    - Mark as visited WHEN ADDING to queue (not when processing)
    
    ⏱️  Time: O(V + E) | Space: O(V) where V=vertices, E=edges
    
    📝 DRY RUN EXAMPLE:
    Graph:    0
            / | \
           1  2  3
          /
         4
    
    Adjacency List: {0: [1,2,3], 1: [4], 2: [], 3: [], 4: []}
    
    Initial: queue = [0], visited = {0}
    
    Step 1: Process 0
            Add neighbors 1, 2, 3 to queue
            queue = [1, 2, 3]
            visited = {0, 1, 2, 3}
            Output: 0
    
    Step 2: Process 1
            Add neighbor 4 to queue
            queue = [2, 3, 4]
            visited = {0, 1, 2, 3, 4}
            Output: 0, 1
    
    Step 3: Process 2 (no unvisited neighbors)
            queue = [3, 4]
            Output: 0, 1, 2
    
    Step 4: Process 3 (no unvisited neighbors)
            queue = [4]
            Output: 0, 1, 2, 3
    
    Step 5: Process 4 (no unvisited neighbors)
            queue = []
            Output: 0, 1, 2, 3, 4
    
    Final BFS Order: [0, 1, 2, 3, 4] ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 102: Binary Tree Level Order Traversal (easy) ⭐
    - LeetCode 107: Binary Tree Level Order Traversal II (medium)
    - LeetCode 103: Binary Tree Zigzag Level Order (medium)
    - LeetCode 111: Minimum Depth of Binary Tree (easy)
    - LeetCode 127: Word Ladder (hard) ⭐⭐⭐
    """
    
    def bfs_classic(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Classic BFS traversal
        
        Args:
            graph: Adjacency list representation
            start: Starting node
        
        Returns:
            List of nodes in BFS order
        """
        if not graph or start not in graph:
            return []
        
        visited = set()
        queue = deque([start])
        visited.add(start)  # ✅ Mark visited when adding!
        result = []
        
        while queue:
            # Dequeue node
            node = queue.popleft()
            result.append(node)
            
            # Process all neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)  # ✅ Mark before adding to queue
                    queue.append(neighbor)
        
        return result
    
    
    def bfs_with_levels(self, graph: Dict[int, List[int]], start: int) -> List[List[int]]:
        """
        BFS that tracks levels separately
        Useful for problems requiring level information
        
        📝 DRY RUN:
        Graph: 0 -> [1,2], 1 -> [3,4], 2 -> [5]
        
        Level 0: [0]
        Level 1: [1, 2]
        Level 2: [3, 4, 5]
        
        Result: [[0], [1, 2], [3, 4, 5]]
        """
        if not graph or start not in graph:
            return []
        
        visited = set()
        queue = deque([start])
        visited.add(start)
        levels = []
        
        while queue:
            level_size = len(queue)  # ✅ Key: process entire level
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                
                # Add unvisited neighbors for next level
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            levels.append(current_level)
        
        return levels
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: CLASSIC DFS (Recursive & Iterative)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Explore graph depth-first, find paths, detect cycles
    
    🔑 KEY CONCEPT:
    - Use Stack (LIFO) or recursion
    - Go as deep as possible before backtracking
    - Two approaches: recursive (cleaner) or iterative (explicit stack)
    
    ⏱️  Time: O(V + E) | Space: O(V) for visited + O(h) for recursion stack
    
    📝 DRY RUN EXAMPLE (Recursive):
    Graph:    0
            / | \
           1  2  3
          /
         4
    
    Call dfs(0):
        Visit 0 → Output: 0
        Call dfs(1):
            Visit 1 → Output: 0, 1
            Call dfs(4):
                Visit 4 → Output: 0, 1, 4
                Return (no neighbors)
            Return
        Call dfs(2):
            Visit 2 → Output: 0, 1, 4, 2
            Return (no neighbors)
        Call dfs(3):
            Visit 3 → Output: 0, 1, 4, 2, 3
            Return (no neighbors)
        Return
    
    Final DFS Order: [0, 1, 4, 2, 3] ✓
    (Note: Goes deep first - visits 4 before 2 and 3)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 200: Number of Islands (medium) ⭐⭐⭐
    - LeetCode 133: Clone Graph (medium) ⭐⭐
    - LeetCode 207: Course Schedule (medium) ⭐⭐⭐
    - LeetCode 210: Course Schedule II (medium) ⭐⭐
    - LeetCode 417: Pacific Atlantic Water Flow (medium)
    """
    
    def dfs_recursive(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        DFS using recursion (most common and cleanest)
        """
        result = []
        visited = set() 

        def dfs(node):
            # Mark as visited
            visited.add(node)# we add visited at the top because this is the edge
        #case if we add it in for loop like bfs we will miss to add the start node to the set
        #casuing problem to recount it failing some problems. so in recursion add to set at the top
        
            result.append(node)
            
            # Visit all unvisited neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
        
        if start in graph:
            dfs(start)
        
        return result
    
    
    def dfs_iterative(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        use this code if and only if they want us to match recursion traversal order
        other wise use this below code.
        "
        The below (this code does the thin its same to same as bfs just uses stack and pop instead of popleft)
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
        
        ex :graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [], 4: [], 5: []
        }
        start = 0
        Recursive DFS (natural neighbor order)

        It goes to the first neighbor as soon as it sees it:
        visit 0
        go to 1
        go to 3
        then 4
        then go back and go to 2
        then 5
        Output:
        [0, 1, 3, 4, 2, 5]

        Your iterative DFS (push neighbors in normal order)
        Your loop does:
        At node 0: push 1 then 2 → stack becomes [1, 2]
        Pop gives 2 first → so it goes to 2 before 1.
        Then from 2 push 5, etc.
        Output:
        [0, 2, 5, 1, 4, 3] (it can differ like this)

        How to fix the order to match recursive DFS
        When using a stack, if you want the same order as recursion, 
        you must push neighbors in reverse:
        "
        stack = [start]
        visited = {start}
        res = []

        while stack:
            node = stack.pop()
            res.append(node)

            for neighbor in reversed(graph.get(node, [])):  # ✅ reverse here
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return res
        " 
        The above gives the output exactly as recursive dfs





        DFS using explicit stack (iterative)
        Useful when recursion depth is a concern
        
        📝 DRY RUN:
        Graph: 0 -> [1,2], 1 -> [3], 2 -> [4]
        
        Initial: stack = [0], visited = set()
        
        Step 1: Pop 0, visit it
                Push neighbors 2, 1 (reverse order for same order as recursive)
                stack = [2, 1], visited = {0}
                Output: 0
        
        Step 2: Pop 1, visit it
                Push neighbor 3
                stack = [2, 3], visited = {0, 1}
                Output: 0, 1
        
        Step 3: Pop 3, visit it
                No neighbors
                stack = [2], visited = {0, 1, 3}
                Output: 0, 1, 3
        
        Step 4: Pop 2, visit it
                Push neighbor 4
                stack = [4], visited = {0, 1, 3, 2}
                Output: 0, 1, 3, 2
        
        Step 5: Pop 4, visit it
                stack = [], visited = {0, 1, 3, 2, 4}
                Output: 0, 1, 3, 2, 4
        """
        if not graph or start not in graph:
            return []
        
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            # Pop from stack
            node = stack.pop()
            
            # Skip if already visited
            if node in visited:
                continue
            
            # Visit node
            visited.add(node)
            result.append(node)
            
            # Push unvisited neighbors (in reverse to match recursive order)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: SHORTEST PATH (Unweighted Graph)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find shortest path between two nodes in unweighted graph
    
    🔑 KEY CONCEPT:
    - BFS guarantees shortest path in unweighted graphs
    - Track parent/predecessor to reconstruct path
    - First time we reach target is the shortest path
    
    ⏱️  Time: O(V + E) | Space: O(V)
    
    📝 DRY RUN:
    Graph: 0 -> [1,2], 1 -> [3], 2 -> [3,4], 3 -> [5], 4 -> [5]
    Find shortest path from 0 to 5
    
    Initial: queue = [0], parent = {0: None}, visited = {0}
    
    Step 1: Process 0
            Add 1 (parent=0), 2 (parent=0)
            queue = [1, 2]
            parent = {0: None, 1: 0, 2: 0}
    
    Step 2: Process 1
            Add 3 (parent=1)
            queue = [2, 3]
            parent = {0: None, 1: 0, 2: 0, 3: 1}
    
    Step 3: Process 2
            3 already visited, add 4 (parent=2)
            queue = [3, 4]
            parent = {0: None, 1: 0, 2: 0, 3: 1, 4: 2}
    
    Step 4: Process 3
            Add 5 (parent=3) → TARGET FOUND!
            queue = [4, 5]
            parent = {0: None, 1: 0, 2: 0, 3: 1, 4: 2, 5: 3}
    
    Reconstruct path from parent:
    5 <- 3 <- 1 <- 0
    Path: [0, 1, 3, 5] ✓
    Length: 3
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 1091: Shortest Path in Binary Matrix (medium) ⭐⭐
    - LeetCode 752: Open the Lock (medium)
    - LeetCode 1926 – Nearest Exit from Entrance in Maze (grid BFS shortest exit)
    - LeetCode 127: Word Ladder (hard) ⭐⭐⭐
    - LeetCode 773 – Sliding Puzzle
    - LeetCode 433: Minimum Genetic Mutation (medium)
    """
    
    def shortest_path_bfs(self, graph: Dict[int, List[int]], 
                          start: int, target: int) -> List[int]:
        """
        Find shortest path using BFS
        
        Returns:
            List representing shortest path, or empty if no path exists
        """
        if start not in graph:
            return []
        
        if start == target:
            return [start]
        
        visited = set()
        queue = deque([start])
        visited.add(start)
        parent = {start: None}
        
        while queue:
            node = queue.popleft()
            
            # Found target - reconstruct path
            if node == target:
                path = []
                current = target
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]  # Reverse to get start -> target
            
            # Explore neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        return []  # No path found
    
    
    def shortest_path_length(self, graph: Dict[int, List[int]], 
                            start: int, target: int) -> int:
        """
        Find shortest path LENGTH (number of edges)
        
        Often asked: "What's the minimum distance?"
        """
        if start not in graph:
            return -1
        
        if start == target:
            return 0
        
        visited = set()
        queue = deque([(start, 0)])  # (node, distance)
        visited.add(start)
        
        while queue:
            node, dist = queue.popleft()
            
            for neighbor in graph.get(node, []):
                if neighbor == target:
                    return dist + 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return -1  # No path found
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: CONNECTED COMPONENTS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Count number of separate graphs (islands, friend groups, etc.)
    
    🔑 KEY CONCEPT:
    - Start DFS/BFS from unvisited node
    - Each complete traversal = one component
    - Count how many times we start new traversal
    
    ⏱️  Time: O(V + E) | Space: O(V)
    
    📝 DRY RUN:
    Graph: {0: [1], 1: [0], 2: [3], 3: [2], 4: [], 5: [6], 6: [5]}
    
    Visualized:
    Component 1: 0 -- 1
    Component 2: 2 -- 3
    Component 3: 4 (isolated)
    Component 4: 5 -- 6
    
    Initial: visited = set(), count = 0
    
    Step 1: Visit 0 (unvisited)
            DFS from 0: visit 0, 1
            visited = {0, 1}, count = 1
    
    Step 2: Check 1 (already visited, skip)
    
    Step 3: Visit 2 (unvisited)
            DFS from 2: visit 2, 3
            visited = {0, 1, 2, 3}, count = 2
    
    Step 4: Check 3 (already visited, skip)
    
    Step 5: Visit 4 (unvisited)
            DFS from 4: visit 4 only
            visited = {0, 1, 2, 3, 4}, count = 3
    
    Step 6: Visit 5 (unvisited)
            DFS from 5: visit 5, 6
            visited = {0, 1, 2, 3, 4, 5, 6}, count = 4
    
    Result: 4 connected components ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 200: Number of Islands (medium) ⭐⭐⭐ (MOST ASKED!)
    - LeetCode 323: Number of Connected Components (medium)
    - LeetCode 547: Number of Provinces (medium) ⭐⭐
    - LeetCode 684: Redundant Connection (medium)
    - LeetCode 695: Max Area of Island (medium) ⭐
    """
    
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        """
        Count connected components given n nodes and edge list
        
        Example: n = 5, edges = [[0,1], [1,2], [3,4]]
        Result: 2 components ([0,1,2] and [3,4])
        """
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Try to start DFS from each node
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
    
    
    def find_component_sizes(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Find size of each connected component
        
        Returns: List of component sizes
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        component_sizes = []
        
        def dfs(node):
            visited.add(node)
            size = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    size += dfs(neighbor)
            return size
        
        for node in range(n):
            if node not in visited:
                size = dfs(node)
                component_sizes.append(size)
        
        return component_sizes
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: CYCLE DETECTION
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Detect if graph contains a cycle
    
    🔑 KEY CONCEPTS:
    
    UNDIRECTED GRAPH:
    - If we visit a node that's already visited AND it's not our parent → CYCLE!
    - Use DFS with parent tracking
    
    DIRECTED GRAPH:
    - Use "recursion stack" or "visiting" state
    - Three states: UNVISITED, VISITING, VISITED
    - If we reach a VISITING node → CYCLE (back edge)!
    
    ⏱️  Time: O(V + E) | Space: O(V)
    
    📝 DRY RUN (Undirected with Cycle):
    Graph: 0 -- 1 -- 2
           |         |
           +----3----+
    
    Edges: [[0,1], [1,2], [2,3], [3,0]]
    
    DFS from 0 (parent=None):
        Visit 0
        DFS(1, parent=0):
            Visit 1
            DFS(2, parent=1):
                Visit 2
                DFS(3, parent=2):
                    Visit 3
                    Check neighbor 0:
                        0 is visited AND 0 != parent(2)
                        → CYCLE DETECTED! ✓
    
    📝 DRY RUN (Directed with Cycle):
    Graph: 0 → 1 → 2
           ↑       ↓
           +---3←--+
    
    State tracking:
    Initial: all UNVISITED
    
    DFS(0):
        0: VISITING
        DFS(1):
            1: VISITING
            DFS(2):
                2: VISITING
                DFS(3):
                    3: VISITING
                    Check neighbor 0:
                        0 is VISITING → CYCLE! ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 207: Course Schedule (medium) ⭐⭐⭐
    - LeetCode 210: Course Schedule II (medium) ⭐⭐
    - LeetCode 261: Graph Valid Tree (medium) ⭐
    - LeetCode 684: Redundant Connection (medium)
    """
    # for undirect cycle detection the back edge is detect by parent tracking
    # for every nei there are 2 case 
    # case 1: it is unvisted ( visit it )
    # case 2 : it is visited 
        #subcase 1 : if visited and its the parent node then no cycle its normal 
        #subcase 2: if visited but not parent case then there is cycle and that is back edge 
    
    def has_cycle_undirected_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        Detect cycle in undirected graph using DFS
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                # If visited and not parent → cycle found!
                elif neighbor != parent:
                    return True
            
            return False
        
        # Check all components
        for node in range(n):
            if node not in visited:
                if dfs(node, -1):
                    return True
        
        return False
    def has_cycle_undirected_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        Detect cycle in undirected graph using BFS
        """
        # Build adjacency list. Time: O(E)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()

        def bfs(start: int) -> bool:
            q = deque([start])
            visited.add(start)

            parent = {start: -1}   # parent[node] = node that discovered it

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        parent[nei] = node
                        q.append(nei)
                    else:
                        # nei is already visited
                        # If nei is NOT the parent of node -> cycle
                        if nei != parent[node]:
                            return True
            return False
        
        # this is also valid we dont really need a hash map to track parent
        # def bfs(start: int) -> bool:
        #     q = deque([(start, -1)])  # (node, parent)
        #     visited.add(start)

        #     while q:
        #         node, parent = q.popleft()
        #         for nei in graph[node]:
        #             if nei not in visited:
        #                 visited.add(nei)
        #                 q.append((nei, node))
        #             elif nei != parent:
        #                 return True
        #     return False

        # Handle disconnected components
        for node in range(n):
            if node not in visited:
                if bfs(node,-1):
                    return True

        return False
    
    """
    Because that “undirected trick” is based on a fact that is only true for undirected graphs:

        In an undirected DFS/BFS tree, the only already-visited neighbor you should see is your parent.
        If you see a visited neighbor that is not your parent, you must have a cycle.

        That statement breaks in directed graphs.
        1) Directed graphs can have “visited neighbor” without any cycle (false positive)

        Example (this graph is a DAG, no cycle):
        0 → 1
        0 → 2
        1 → 2
        If you start DFS/BFS at 0:
        you visit 2 from 0 first (so 2 becomes visited)
        later when you are at node 1, you see edge 1 → 2
        2 is already visited, and 2 is not the “parent” of 1
        Undirected rule would scream “cycle”, but there is no cycle. That edge is just a cross edge in a directed acyclic graph.

        2) Directed graphs can have a real cycle that goes back to the parent (false negative)

        Example (this has a cycle):
        0 → 1
        1 → 2
        2 → 1
        If your “undirected” logic says “ignore visited neighbor if it equals parent”, then at node 2 you see neighbor 1:
        1 is visited
        1 is also the node that discovered 2 (the parent)
        undirected logic would ignore it
        but 2 → 1 is exactly the cycle edge
        So in directed graphs, “visited and not parent” is not the right test.
        What works for directed cycle detection
        You need to detect a back edge to a node that is still in the current DFS path, not just “visited sometime in the past”.

        That’s why we use 3 states (or recursion stack):
        0 = unvisited
        1 = visiting (currently in recursion stack / current path)
        2 = visited (fully done)
        If you ever see an edge to a node in state 1, that is a cycle.
    """
        
    
    def has_cycle_directed_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        Detect cycle in directed graph using DFS with recursion stack
        
        Three states:
        - 0: UNVISITED (white)
        - 1: VISITING (gray - in recursion stack)
        - 2: VISITED (black - done)
        The “3 states” is just a label you store for each node.
        It is not some special Python feature, it’s just a normal array or dict.
        Think of it like a status badge on every node while DFS is running.
        The 3 states (per node)
        We store one of these values for every node:
        0 = unvisited
        We have not started DFS from this node yet.
        1 = visiting
        We are currently inside DFS for this node, meaning it is on the current recursion path (call stack).
        2 = visited
        We finished DFS for this node completely, we have returned from it.
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * n
        
        def dfs(node):
            # If in current recursion stack → cycle!
            if state[node] == 1:
                return True
            
            # Already processed
            if state[node] == 2:
                return False
            
            # Mark as visiting (in recursion stack)
            state[node] = 1
            
            # Check all neighbors
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            
            # Mark as visited (done processing)
            state[node] = 2
            return False
        
        # Check all nodes
        for node in range(n):
            if state[node] == 0:
                if dfs(node):
                    return True
        
        return False
    
# CODE WITH 2 sets a bit easier to understand (this is what we use)
    def has_cycle_directed_two_sets(self, n: int, edges: List[List[int]]) -> bool:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited: Set[int] = set()   # fully processed nodes
        path: Set[int] = set()      # nodes in current recursion stack (current DFS path)

        def dfs(node: int) -> bool:
            # If node is in current path, we found a back edge -> cycle
            # Am I revisiting a node in the same DFS path?
            # If yes → cycle
            if node in path:
                return True

#Nodes that are completely explored, All descendants checked, and no cycle found from them
            # If already fully processed, no cycle from here
            # “Have I already proven this node is safe?
            # If yes → no need to explore again
            # we explored this nodes and its descendants and marked this as safe no need to
            #explore again and do the same repeated work we marked this safe which recursion unwinding

            if node in visited:
                return False

            # Start exploring this node
            path.add(node)

            for nei in graph[node]:
                if dfs(nei):
                    return True

            # Done exploring this node
            path.remove(node)
            visited.add(node) 
            return False

        # Handle disconnected components
        for node in range(n):
            if dfs(node):
                return True

        return False
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: TOPOLOGICAL SORT
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Order tasks with dependencies (DAG only!)
    
    🔑 KEY CONCEPT:
    - Only works on Directed Acyclic Graphs (DAG)
    - Two methods: DFS (postorder) or Kahn's Algorithm (BFS with in-degree)
    - Result: Linear ordering where all edges go from left to right
    
    ⏱️  Time: O(V + E) | Space: O(V)
    
    📝 DRY RUN (Kahn's Algorithm - BFS):
    Graph: 0 → 1 → 3
           ↓       ↑
           2 ------+
    
    Calculate in-degrees:
    In-degree: {0: 0, 1: 1, 2: 1, 3: 2}
    
    Initial: queue = [0] (nodes with in-degree 0)
             result = []
    
    Step 1: Process 0
            Remove edges 0→1, 0→2
            Decrease in-degrees: {1: 0, 2: 0, 3: 2}
            Add 1, 2 to queue
            result = [0]
    
    Step 2: Process 1
            Remove edge 1→3
            Decrease in-degree: {3: 1}
            result = [0, 1]
    
    Step 3: Process 2
            Remove edge 2→3
            Decrease in-degree: {3: 0}
            Add 3 to queue
            result = [0, 1, 2]
    
    Step 4: Process 3
            No neighbors
            result = [0, 1, 2, 3] ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 207: Course Schedule (medium) ⭐⭐⭐
    - LeetCode 210: Course Schedule II (medium) ⭐⭐⭐
    - LeetCode 269: Alien Dictionary (hard) ⭐⭐
    - LeetCode 444: Sequence Reconstruction (hard)
    """
    
    def topological_sort_dfs(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Topological sort using DFS (postorder)
        
        Returns empty list if cycle detected

        Topological sort (DFS version) is:

        Directed cycle detection with DFS states (unvisited, visiting, visited)
        If you ever reach a visiting node again, that’s a cycle, so topo order is impossible.
        One extra thing: when a node is fully done (all its outgoing neighbors are processed), you append it to result (postorder).
        At the end you reverse result to get the topological order.

        Nothing else “new” is happening. The cycle detection part is the same as directed cycle detection, and the topo order is just the postorder list.

        Tiny intuition:
        Edge is u -> v (u must come before v).
        DFS finishes v before u (because u depends on v).
        So you append u after v (postorder), then reverse to make u appear before v.
        
        JUST ADD RES OR STACK VAR AT THE END AFTER MARKING FULL VISITED AND REVERSE IT
        THATS IT FOR TOPO SORT
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        state = [0] * n  # 0: unvisited, 1: visiting, 2: visited
        result = []
        
        def dfs(node):
            if state[node] == 1:  # Cycle detected
                return True
            if state[node] == 2:  # Already processed
                return False
            
            state[node] = 1  # Mark as visiting
            
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            
            state[node] = 2  # Mark as visited
            result.append(node)  # Add in postorder
            return False
        
        # Process all nodes
        for node in range(n):
            if state[node] == 0:
                if dfs(node):
                    return []  # Cycle found
        
        return result[::-1]  # Reverse postorder
    

    # topo sort with dfs and 2 sets 
    def topo_sort_two_sets(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v) 
            # here make sure you follow u = preq(comes_first), v = course(comes after)

        visited: Set[int] = set()  # done
        path: Set[int] = set()     # in current recursion stack
        order: List[int] = []

        def dfs(node):
            if node in path:
                return True          # cycle found
            if node in visited:
                return False         # no cycle from here

            path.add(node)
            for nei in graph[node]:
                if dfs(nei):         # cycle in neighbor
                    return True
            path.remove(node)

            visited.add(node)
            order.append(node)       # postorder
            return False             # no cycle

        for node in range(n):
            if node not in visited:
                if dfs(node):        # cycle detected
                    return []
        return order[::-1]
    
    def topological_sort_kahn(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Topological sort using Kahn's Algorithm (BFS with in-degree)
        
        More intuitive for beginners!
        DOnt confuse btw u and v while building graph 
        Meaning:
        u = Prerequisite / Dependency / Must come first
        v = Course / Task / Comes after
        u must be completed BEFORE

        universal remeber 
        graph[prerequisite].append(course)
        in_degree[course] += 1

        or more genrally 
    
        graph[comes_first].append(comes_after)
        in_degree[comes_after] += 1
        """
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Build graph and calculate in-degrees
        for u, v in edges:
            graph[u].append(v) # u → v (u comes BEFORE v)
            in_degree[v] += 1  # v depends on u
        
        # Start with nodes having no dependencies
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Remove this node's edges
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                # If no more dependencies, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If result has all nodes → valid topological order
        # If not → cycle exists
        return result if len(result) == n else []
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: BIPARTITE GRAPH CHECK
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Check if graph can be colored with 2 colors (no adjacent same color)
    
    🔑 KEY CONCEPT:
    - Try to color graph with 2 colors using BFS/DFS
    - If two adjacent nodes must have same color → NOT bipartite
    - Applications: Matching problems, scheduling with conflicts
    
    ⏱️  Time: O(V + E) | Space: O(V)
    
    📝 DRY RUN (Bipartite):
    Graph: 0 -- 1
           |    |
           3 -- 2
    
    Try coloring:
    Color 0 with Red
    Color 1 with Blue (neighbor of 0)
    Color 2 with Red (neighbor of 1)
    Color 3 with Blue (neighbor of 0)
    Check: 3-2 edge → Blue-Red ✓ (different colors)
    
    Result: IS bipartite! ✓
    
    📝 DRY RUN (Not Bipartite):
    Graph: 0 -- 1
           |  X |  (triangle)
           +-- 2
    
    Try coloring:
    Color 0 with Red
    Color 1 with Blue (neighbor of 0)
    Color 2 with Red (neighbor of 1)
    Check: 0-2 edge → Red-Red ✗ (same color!)
    
    Result: NOT bipartite! ✗
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 785: Is Graph Bipartite? (medium) ⭐⭐
    - LeetCode 886: Possible Bipartition (medium) ⭐
    """
    
    def is_bipartite_bfs(self, graph: Dict[int, List[int]]) -> bool:
        """
        Check if graph is bipartite using BFS
        
        Returns True if can be 2-colored, False otherwise
        """
        if not graph:
            return True
        
        # -1: uncolored, 0: color A, 1: color B
        color = {}
        
        # Check each component
        for start_node in graph:
            if start_node in color:
                continue
            
            # BFS to color this component
            queue = deque([start_node])
            color[start_node] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color  # Flip color
                
                for neighbor in graph[node]:
                    if neighbor not in color:
                        # Color with opposite color
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        # Conflict! Same color as current node
                        return False
        
        return True
    
    
    def is_bipartite_dfs(self, graph: Dict[int, List[int]]) -> bool:
        """
        Check if graph is bipartite using DFS
        """
        color = {}
        
        def dfs(node, c):
            color[node] = c
            
            for neighbor in graph[node]:
                if neighbor not in color:
                    # Color with opposite color
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    # Conflict!
                    return False
            
            return True
        
        # Check each component
        for node in graph:
            if node not in color:
                if not dfs(node, 0):
                    return False
        
        return True
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: ISLAND PROBLEMS (Grid DFS/BFS) ⭐⭐⭐ MOST ASKED!
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Count islands, find areas, flood fill, grid traversal
    
    🔑 KEY CONCEPTS:
    - Treat 2D grid as graph (4 or 8 directional neighbors)
    - Each cell is a node, edges to adjacent cells
    - Use DFS/BFS to explore connected components
    - Mark visited to avoid revisiting
    
    ⏱️  Time: O(rows × cols) | Space: O(rows × cols) worst case
    
    📝 DRY RUN - Number of Islands:
    Grid:
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    
    Where 1 = land, 0 = water
    
    Initial: count = 0, visited = empty
    
    Step 1: Visit (0,0) - it's 1!
            DFS from (0,0): visit (0,0), (0,1), (1,0), (1,1)
            Mark all as visited
            count = 1 (found island 1)
    
    Step 2: Continue scanning, find (2,2) - it's 1!
            DFS from (2,2): visit only (2,2)
            count = 2 (found island 2)
    
    Step 3: Find (3,3) - it's 1!
            DFS from (3,3): visit (3,3), (3,4)
            count = 3 (found island 3)
    
    Result: 3 islands ✓
    
    💡 LEETCODE PROBLEMS (CRITICAL!):
    - LeetCode 200: Number of Islands (medium) ⭐⭐⭐ #1 MOST ASKED!
    - LeetCode 695: Max Area of Island (medium) ⭐⭐⭐
    - LeetCode 733: Flood Fill (easy) ⭐
    - LeetCode 130: Surrounded Regions (medium) ⭐⭐
    - LeetCode 994: Rotting Oranges (medium) ⭐⭐⭐
    - LeetCode 1020: Number of Enclaves (medium)
    - LeetCode 1254: Number of Closed Islands (medium)
    """
    
    def num_islands(self, grid: List[List[str]]) -> int:
        """
        LeetCode 200: Number of Islands
        
        Count connected components of '1's in grid
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def dfs(r, c):
            # Check bounds and validity
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or grid[r][c] == '0'):
                return
            
            visited.add((r, c))
            
            # Explore 4 directions (up, down, left, right)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Scan every cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    count += 1  # Found a new island!
        
        return count
    
    
    def max_area_island(self, grid: List[List[int]]) -> int:
        """
        LeetCode 695: Max Area of Island
        
        Find the largest connected component of 1's
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            area = 1  # Current cell counts as 1
            
            # Add areas from all 4 directions
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
    
    
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, 
                   color: int) -> List[List[int]]:
        """
        LeetCode 733: Flood Fill
        
        Change all connected pixels of same color to new color
        """
        if not image or image[sr][sc] == color:
            return image
        
        original_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                image[r][c] != original_color):
                return
            
            image[r][c] = color
            
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: CLONE GRAPH (DFS with HashMap) ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Deep copy a graph, copy linked structures
    
    🔑 KEY CONCEPT:
    - Use HashMap to map original nodes to cloned nodes
    - DFS through graph, creating clones as we go
    - For each neighbor, recursively clone if not already cloned
    
    ⏱️  Time: O(V + E) | Space: O(V) for hashmap
    
    📝 DRY RUN:
    Original Graph:
    1 -- 2
    |    |
    4 -- 3
    
    Node structure: class Node { val, neighbors[] }
    
    Clone Process:
    old_to_new = {}
    
    Step 1: Clone node 1
            new_1 = Node(1)
            old_to_new[1] = new_1
            Clone neighbors [2, 4]
    
    Step 2: Clone node 2
            new_2 = Node(2)
            old_to_new[2] = new_2
            Clone neighbors [1, 3]
            1 already cloned, reuse
    
    Step 3: Clone node 3
            new_3 = Node(3)
            old_to_new[3] = new_3
            Clone neighbors [2, 4]
    
    Step 4: Clone node 4
            new_4 = Node(4)
            old_to_new[4] = new_4
            Clone neighbors [1, 3]
            Both already cloned, reuse
    
    Connect all neighbors using old_to_new mapping
    Result: Complete cloned graph ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 133: Clone Graph (medium) ⭐⭐⭐ VERY COMMON!
    - LeetCode 138: Copy List with Random Pointer (medium) ⭐⭐
    """
    
    def clone_graph_dfs(self, node):
        """
        LeetCode 133: Clone Graph (DFS approach)
        
        Node definition:
        class Node:
            def __init__(self, val=0, neighbors=None):
                self.val = val
                self.neighbors = neighbors if neighbors else []
        """
        if not node:
            return None
        
        # Map original node -> cloned node
        old_to_new = {}
        
        def dfs(node):
            # If already cloned, return the clone
            if node in old_to_new:
                return old_to_new[node]
            
            # Create clone (assuming Node class exists)
            # clone = Node(node.val)
            # old_to_new[node] = clone
            
            # Recursively clone neighbors
            # for neighbor in node.neighbors:
            #     clone.neighbors.append(dfs(neighbor))
            
            # return clone
            pass  # Placeholder since we don't have Node class
        
        return dfs(node)
    
    
    def clone_graph_bfs(self, node):
        """
        LeetCode 133: Clone Graph (BFS approach)
        """
        if not node:
            return None
        
        # old_to_new = {node: Node(node.val)}
        # queue = deque([node])
        
        # while queue:
        #     curr = queue.popleft()
            
        #     for neighbor in curr.neighbors:
        #         if neighbor not in old_to_new:
        #             old_to_new[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)
                
        #         old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
        # return old_to_new[node]
        pass  # Placeholder
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 10: WORD LADDER (BFS Transformation) ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Shortest transformation sequence, state space search
    
    🔑 KEY CONCEPT:
    - Treat each word as a node
    - Edge exists if words differ by exactly 1 letter
    - Use BFS to find shortest path
    - Generate neighbors by trying all letter substitutions
    
    ⏱️  Time: O(N × L² × 26) where N=words, L=word length
          Space: O(N × L)
    
    📝 DRY RUN:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    Build graph of transformations:
    hit -> hot (change i->o)
    hot -> dot, lot (change h->d or h->l)
    dot -> dog (change t->g)
    lot -> log (change t->g)
    dog -> cog (change d->c)
    log -> cog (change l->c)
    
    BFS:
    Level 0: [hit]
    Level 1: [hot] (distance 1)
    Level 2: [dot, lot] (distance 2)
    Level 3: [dog, log] (distance 3)
    Level 4: [cog] (distance 4) → Found target!
    
    Shortest path: hit -> hot -> dot -> dog -> cog
    Length: 5 words ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 127: Word Ladder (hard) ⭐⭐⭐ TOP INTERVIEW!
    - LeetCode 126: Word Ladder II (hard) ⭐⭐
    - LeetCode 433: Minimum Genetic Mutation (medium)
    """
    
    def ladder_length(self, beginWord: str, endWord: str, 
                     wordList: List[str]) -> int:
        """
        LeetCode 127: Word Ladder
        
        Find shortest transformation sequence length
        """
        if endWord not in wordList:
            return 0
        
        word_set = set(wordList)
        queue = deque([(beginWord, 1)])  # (word, level)
        visited = {beginWord}
        
        while queue:
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            # Try changing each position
            for i in range(len(word)):
                # Try all 26 letters
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        
        return 0  # No path found
    
    
    def ladder_length_optimized(self, beginWord: str, endWord: str, 
                               wordList: List[str]) -> int:
        """
        Optimized with bidirectional BFS (search from both ends)
        """
        if endWord not in wordList:
            return 0
        
        word_set = set(wordList)
        
        # Two sets: search from both directions
        begin_set = {beginWord}
        end_set = {endWord}
        visited = set()
        length = 1
        
        while begin_set and end_set:
            # Always expand the smaller set (optimization!)
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_level = set()
            
            for word in begin_set:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        
                        # If found in other direction, done!
                        if next_word in end_set:
                            return length + 1
                        
                        if next_word in word_set and next_word not in visited:
                            visited.add(next_word)
                            next_level.add(next_word)
            
            begin_set = next_level
            length += 1
        
        return 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 11: MULTI-SOURCE BFS (Rotting Oranges) ⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Spread from multiple starting points simultaneously
    
    🔑 KEY CONCEPT:
    - Start BFS from ALL sources at once
    - Track time/distance level by level
    - All sources spread simultaneously each minute/step
    
    ⏱️  Time: O(rows × cols) | Space: O(rows × cols)
    
    📝 DRY RUN - Rotting Oranges:
    Grid: 2 = rotten, 1 = fresh, 0 = empty
    
    Initial:
    2 1 1
    1 1 0
    0 1 1
    
    Minute 0: Queue = [(0,0)]
              Fresh count = 6
    
    Minute 1: (0,0) rots (0,1) and (1,0)
              Grid:
              2 2 1
              2 1 0
              0 1 1
              Queue = [(0,1), (1,0)]
              Fresh count = 4
    
    Minute 2: (0,1) rots (0,2)
              (1,0) rots (1,1)
              Grid:
              2 2 2
              2 2 0
              0 1 1
              Queue = [(0,2), (1,1)]
              Fresh count = 2
    
    Minute 3: (1,1) rots (2,1)
              Grid:
              2 2 2
              2 2 0
              0 2 1
              Queue = [(2,1)]
              Fresh count = 1
    
    Minute 4: (2,1) rots (2,2)
              Grid:
              2 2 2
              2 2 0
              0 2 2
              Fresh count = 0 ✓
    
    Result: 4 minutes
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 994: Rotting Oranges (medium) ⭐⭐⭐
    - LeetCode 286: Walls and Gates (medium) ⭐⭐
    - LeetCode 542: 01 Matrix (medium) ⭐⭐
    - LeetCode 1162: As Far from Land as Possible (medium)
    """
    
    def oranges_rotting(self, grid: List[List[int]]) -> int:
        """
        LeetCode 994: Rotting Oranges
        
        Find time for all oranges to rot (multi-source BFS)
        """
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Find all initial rotten oranges and count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0  # Already all rotten/empty
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        minutes = 0
        
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)
            
            # Spread to 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == 1):
                    # Rot this orange
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))
        
        return minutes if fresh_count == 0 else -1
    
    
    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        """
        LeetCode 286: Walls and Gates
        
        Fill each empty room with distance to nearest gate
        Multi-source BFS from all gates
        """
        if not rooms or not rooms[0]:
            return
        
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        INF = 2147483647
        
        # Find all gates (multi-source!)
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:  # Gate
                    queue.append((r, c))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    rooms[nr][nc] == INF):
                    # Update distance
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 12: DIJKSTRA'S ALGORITHM (Weighted Shortest Path) ⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Shortest path in WEIGHTED graphs (positive weights)
    
    🔑 KEY CONCEPT:
    - Use min-heap (priority queue) instead of regular queue
    - Always process node with smallest distance first
    - Update distances when shorter path found (relaxation)
    - Greedy algorithm - once processed, distance is final
    
    ⏱️  Time: O((V + E) log V) | Space: O(V)
    
    📝 DRY RUN:
    Graph (weighted):
    0 --1-- 1
    |       |
    4       2
    |       |
    2 --1-- 3
    
    Find shortest path from 0 to 3:
    
    Initial: heap = [(0, 0)]  # (distance, node)
             distances = {0:0, others:∞}
    
    Step 1: Process (0, 0)
            Update neighbors:
            - Node 1: dist = 0+1 = 1
            - Node 2: dist = 0+4 = 4
            heap = [(1,1), (4,2)]
            distances = {0:0, 1:1, 2:4}
    
    Step 2: Process (1, 1) - smallest distance
            Update neighbor 3:
            - Node 3: dist = 1+2 = 3
            heap = [(3,3), (4,2)]
            distances = {0:0, 1:1, 2:4, 3:3}
    
    Step 3: Process (3, 3)
            Update neighbor 2:
            - Node 2: new dist = 3+1 = 4 (not better)
            heap = [(4,2)]
    
    Step 4: Process (4, 2) - done!
    
    Final distances: {0:0, 1:1, 2:4, 3:3}
    Shortest path to 3: 0 -> 1 -> 3 with distance 3 ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 743: Network Delay Time (medium) ⭐⭐
    - LeetCode 787: Cheapest Flights Within K Stops (medium) ⭐⭐
    - LeetCode 1514: Path with Maximum Probability (medium)
    - LeetCode 1631: Path With Minimum Effort (medium) ⭐
    """
    
    def dijkstra(self, graph: Dict[int, List[Tuple[int, int]]], 
                 start: int) -> Dict[int, int]:
        """
        Classic Dijkstra's Algorithm
        
        Args:
            graph: Adjacency list {node: [(neighbor, weight), ...]}
            start: Starting node
        
        Returns:
            Dictionary of shortest distances from start to all nodes
        """
        # Min heap: (distance, node)
        heap = [(0, start)]
        distances = {start: 0}
        visited = set()
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            # Skip if already processed
            if node in visited:
                continue
            
            visited.add(node)
            
            # Relax edges to neighbors
            for neighbor, weight in graph.get(node, []):
                if neighbor in visited:
                    continue
                
                new_dist = dist + weight
                
                # If found shorter path, update
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        
        return distances
    
    
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        """
        LeetCode 743: Network Delay Time
        
        Find time for signal to reach all nodes
        times[i] = [u, v, w] means edge from u to v with weight w
        """
        # Build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Run Dijkstra from node k
        distances = self.dijkstra(graph, k)
        
        # Check if all nodes reachable
        if len(distances) != n:
            return -1
        
        # Return max distance (time for last node to receive)
        return max(distances.values())
    
    
    def min_effort_path(self, heights: List[List[int]]) -> int:
        """
        LeetCode 1631: Path With Minimum Effort
        
        Find path with minimum effort (max absolute difference)
        Uses Dijkstra on grid
        """
        if not heights or not heights[0]:
            return 0
        
        rows, cols = len(heights), len(heights[0])
        
        # Min heap: (effort, row, col)
        heap = [(0, 0, 0)]
        efforts = {(0, 0): 0}
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)
            
            # Reached destination
            if r == rows - 1 and c == cols - 1:
                return effort
            
            # Skip if we've found better path
            if effort > efforts.get((r, c), float('inf')):
                continue
            
            # Try all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Effort is max diff on path
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    
                    if new_effort < efforts.get((nr, nc), float('inf')):
                        efforts[(nr, nc)] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        
        return 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 13: UNION FIND (Disjoint Set Union) ⭐⭐ BONUS!
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Dynamic connectivity, grouping elements, cycle detection
    
    🔑 KEY CONCEPT:
    - Track connected components efficiently
    - Two main operations: Find (which set?) and Union (merge sets)
    - Path compression: flatten tree during find
    - Union by rank: attach smaller tree to larger
    
    ⏱️  Time: O(α(n)) ≈ O(1) amortized | Space: O(n)
    
    📝 DRY RUN:
    Elements: 0, 1, 2, 3, 4
    Operations: union(0,1), union(2,3), union(0,2), find(1,3)
    
    Initial: Each element is its own parent
    parent = [0, 1, 2, 3, 4]
    rank = [0, 0, 0, 0, 0]
    
    union(0, 1):
        find(0) = 0, find(1) = 1 (different sets)
        Merge: make 1 child of 0
        parent = [0, 0, 2, 3, 4]
        Group: {0,1}, {2}, {3}, {4}
    
    union(2, 3):
        find(2) = 2, find(3) = 3 (different sets)
        Merge: make 3 child of 2
        parent = [0, 0, 2, 2, 4]
        Group: {0,1}, {2,3}, {4}
    
    union(0, 2):
        find(0) = 0, find(2) = 2 (different sets)
        Merge: make 2 child of 0
        parent = [0, 0, 0, 2, 4]
        Group: {0,1,2,3}, {4}
    
    find(1) and find(3) both return 0
    → Same component! ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 323: Number of Connected Components (medium) ⭐⭐
    - LeetCode 684: Redundant Connection (medium) ⭐⭐
    - LeetCode 547: Number of Provinces (medium) ⭐
    - LeetCode 990: Satisfiability of Equality Equations (medium)
    - LeetCode 1319: Number of Operations (medium)
    """
    
    class UnionFind:
        """
        Union Find / Disjoint Set Union data structure
        
        With path compression and union by rank
        """
        def __init__(self, n: int):
            # Initially, each element is its own parent
            self.parent = list(range(n))
            # Rank for union by rank optimization
            self.rank = [0] * n
            # Track number of components
            self.components = n
        
        def find(self, x: int) -> int:
            """
            Find root of x with path compression
            
            Path compression: make every node point directly to root
            """
            if self.parent[x] != x:
                # Recursively find root and compress path
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x: int, y: int) -> bool:
            """
            Union two sets containing x and y
            
            Returns True if they were in different sets (union happened)
            """
            root_x = self.find(x)
            root_y = self.find(y)
            
            if root_x == root_y:
                return False  # Already in same set
            
            # Union by rank: attach smaller tree to larger
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            self.components -= 1
            return True
        
        def connected(self, x: int, y: int) -> bool:
            """Check if x and y are in same component"""
            return self.find(x) == self.find(y)
        
        def get_components(self) -> int:
            """Get number of connected components"""
            return self.components
    
    
    def count_components_uf(self, n: int, edges: List[List[int]]) -> int:
        """
        LeetCode 323: Number of Connected Components
        Using Union Find
        """
        uf = self.UnionFind(n)
        
        for u, v in edges:
            uf.union(u, v)
        
        return uf.get_components()
    
    
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        """
        LeetCode 684: Redundant Connection
        
        Find edge that creates cycle (last redundant edge)
        """
        n = len(edges)
        uf = self.UnionFind(n + 1)  # 1-indexed
        
        for u, v in edges:
            # If already connected, this edge creates cycle!
            if not uf.union(u, v):
                return [u, v]
        
        return []


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 COMPLETE TOP 25 PROBLEMS (BY IMPORTANCE)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 ABSOLUTE MUST-KNOW (Top 5):
═══════════════════════════════════════════════════════════════════════════
1. ⭐⭐⭐ LC 200: Number of Islands (Pattern 8)
   - Why: #1 most asked graph problem at ALL companies
   - Pattern: Grid DFS/BFS, Connected Components
   - Companies: Amazon, Microsoft, Google, Facebook, Apple

2. ⭐⭐⭐ LC 207: Course Schedule (Pattern 5+6)
   - Why: Classic cycle detection + topological sort
   - Pattern: Cycle Detection, Topological Sort
   - Companies: Amazon, Microsoft, Google, Facebook

3. ⭐⭐⭐ LC 133: Clone Graph (Pattern 9)
   - Why: Tests deep understanding of graph traversal + HashMap
   - Pattern: DFS with HashMap
   - Companies: Facebook, Amazon, Microsoft

4. ⭐⭐⭐ LC 127: Word Ladder (Pattern 10)
   - Why: Complex BFS, very popular hard problem
   - Pattern: BFS Transformation, State Space Search
   - Companies: Amazon, Google, Microsoft, LinkedIn

5. ⭐⭐⭐ LC 994: Rotting Oranges (Pattern 11)
   - Why: Multi-source BFS is very common pattern
   - Pattern: Multi-source BFS
   - Companies: Amazon, Bloomberg, Microsoft


🔥🔥 VERY IMPORTANT (Next 10):
═══════════════════════════════════════════════════════════════════════════
6. ⭐⭐ LC 695: Max Area of Island (Pattern 8)
7. ⭐⭐ LC 210: Course Schedule II (Pattern 6)
8. ⭐⭐ LC 785: Is Graph Bipartite? (Pattern 7)
9. ⭐⭐ LC 323: Number of Connected Components (Pattern 4)
10. ⭐⭐ LC 1091: Shortest Path in Binary Matrix (Pattern 3)
11. ⭐⭐ LC 547: Number of Provinces (Pattern 4)
12. ⭐⭐ LC 286: Walls and Gates (Pattern 11)
13. ⭐⭐ LC 417: Pacific Atlantic Water Flow (Pattern 8)
14. ⭐⭐ LC 743: Network Delay Time (Pattern 12)
15. ⭐⭐ LC 684: Redundant Connection (Pattern 13)


🔥 IMPORTANT (Complete Foundation):
═══════════════════════════════════════════════════════════════════════════
16. ⭐ LC 733: Flood Fill (Pattern 8)
17. ⭐ LC 130: Surrounded Regions (Pattern 8)
18. ⭐ LC 752: Open the Lock (Pattern 3)
19. ⭐ LC 261: Graph Valid Tree (Pattern 5)
20. ⭐ LC 1631: Path With Minimum Effort (Pattern 12)
21. ⭐ LC 542: 01 Matrix (Pattern 11)
22. ⭐ LC 1162: As Far from Land as Possible (Pattern 11)
23. ⭐ LC 1020: Number of Enclaves (Pattern 8)
24. ⭐ LC 1254: Number of Closed Islands (Pattern 8)
25. ⭐ LC 990: Satisfiability of Equality Equations (Pattern 13)


═══════════════════════════════════════════════════════════════════════════
📊 4-WEEK STUDY PLAN:
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - Master BFS & DFS Basics:
Day 1-2: Implement BFS and DFS from scratch (both recursive and iterative)
Day 3: LC 200 (Number of Islands) - Do 3+ times! ⚠️
Day 4: LC 695 (Max Area of Island)
Day 5: LC 733 (Flood Fill) + LC 130 (Surrounded Regions)
Day 6: LC 133 (Clone Graph)
Day 7: LC 547 (Number of Provinces) + Review

WEEK 2 - Shortest Path & Topological Sort:
Day 1-2: LC 127 (Word Ladder) ⚠️ Challenging! Spend time here
Day 3: LC 1091 (Shortest Path in Binary Matrix)
Day 4: LC 752 (Open the Lock)
Day 5: LC 207 (Course Schedule) - Learn both DFS and Kahn's
Day 6: LC 210 (Course Schedule II)
Day 7: Review + Practice variations

WEEK 3 - Advanced Patterns:
Day 1: LC 785 (Is Graph Bipartite?)
Day 2: LC 994 (Rotting Oranges) - Multi-source BFS
Day 3: LC 286 (Walls and Gates) + LC 542 (01 Matrix)
Day 4: LC 417 (Pacific Atlantic)
Day 5: LC 261 (Graph Valid Tree)
Day 6: LC 323 (Connected Components) + LC 684 (Redundant Connection)
Day 7: Review + Practice

WEEK 4 - Dijkstra, Union Find & Mock Interviews:
Day 1: LC 743 (Network Delay Time) - Learn Dijkstra
Day 2: LC 1631 (Path With Minimum Effort)
Day 3: Implement Union Find from scratch
Day 4: LC 684, LC 990, LC 323 using Union Find
Day 5-6: Timed practice (45 min per problem, no hints)
Day 7: Mock interview with all patterns


═══════════════════════════════════════════════════════════════════════════
💡 INTERVIEW TIPS & COMMON MISTAKES:
═══════════════════════════════════════════════════════════════════════════

✅ ALWAYS DO THESE:
1. Ask clarifying questions:
   - Directed or undirected?
   - Weighted or unweighted?
   - Can there be cycles?
   - Are there disconnected components?
   - What's the size? (helps choose algorithm)

2. State your approach clearly:
   - "I'll use BFS because we need shortest path"
   - "I'll use DFS because we're detecting cycles"
   - "I'll use Union Find for dynamic connectivity"

3. Handle edge cases:
   - Empty graph
   - Single node
   - Disconnected components
   - All nodes visited already

4. Explain complexity:
   - Time: O(V + E) for most traversals
   - Space: O(V) for visited set
   - Be ready to justify!


❌ NEVER DO THESE:
1. Forget to mark as visited WHEN ADDING to queue (BFS)
2. Not check bounds in grid problems
3. Modify input without permission
4. Use DFS when BFS is clearly better (shortest path)
5. Forget to handle disconnected components
6. Not initialize visited set
7. Mix up directed vs undirected cycle detection


🎯 PATTERN SELECTION CHEAT SHEET:
═══════════════════════════════════════════════════════════════════════════
Problem Type                    → Pattern to Use
──────────────────────────────────────────────────────────────────────────
Shortest path (unweighted)      → BFS (Pattern 3)
Shortest path (weighted)        → Dijkstra (Pattern 12)
Find any path                   → DFS (Pattern 2)
Count components                → DFS/BFS (Pattern 4) or Union Find (Pattern 13)
Detect cycle (undirected)       → DFS with parent (Pattern 5)
Detect cycle (directed)         → DFS with states (Pattern 5)
Order with dependencies         → Topological Sort (Pattern 6)
2-coloring possible?            → Bipartite Check (Pattern 7)
Grid islands/areas              → Grid DFS/BFS (Pattern 8)
Copy graph structure            → DFS + HashMap (Pattern 9)
Transform strings minimally     → BFS state space (Pattern 10)
Spread from multiple sources    → Multi-source BFS (Pattern 11)
Dynamic connectivity            → Union Find (Pattern 13)


═══════════════════════════════════════════════════════════════════════════
🎓 FINAL TIPS FOR SUCCESS:
═══════════════════════════════════════════════════════════════════════════

1. Master the fundamentals first (Patterns 1-4)
2. Do LC 200 (Number of Islands) until you can code it in 10 minutes
3. Learn when to use each pattern (don't force patterns!)
4. Practice explaining your approach out loud
5. Time yourself - aim for 30-40 minutes per medium problem
6. Review mistakes and understand WHY you made them
7. Don't just memorize - understand the WHY behind each pattern

Good luck with your interviews! 🚀
"""