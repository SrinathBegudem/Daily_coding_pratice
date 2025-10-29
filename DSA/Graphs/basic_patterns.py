from collections import deque, defaultdict

"""
═══════════════════════════════════════════════════════════════════════════════
                    COMPLETE BASIC GRAPH PATTERNS GUIDE
═══════════════════════════════════════════════════════════════════════════════

After mastering BFS and DFS, these are the ESSENTIAL graph patterns:

5 CORE PATTERNS:
1. Cycle Detection (Undirected & Directed)
2. Topological Sort (DFS & Kahn's Algorithm)
3. Union-Find (Disjoint Set Union)
4. Bipartite Graph Check
5. Connected Components

LEARNING ORDER:
Week 1: Cycle Detection + Topological Sort (they're related!)
Week 2: Union-Find (critical for interviews)
Week 3: Bipartite + Review
Week 4: Practice mixed problems

═══════════════════════════════════════════════════════════════════════════════
"""


class GraphPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: CYCLE DETECTION ⭐⭐⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def has_cycle_undirected(self, n, edges):
        """
        Detect cycle in UNDIRECTED graph using DFS
        
        WHEN TO USE:
        - Undirected graph
        - Check if adding edge creates cycle
        - Validate tree structure
        
        KEY POINTS:
        1. Track parent to avoid going back to where we came from
        2. If we visit a node that's already visited (and not parent) → cycle!
        3. Use DFS with parent tracking
        
        TIME: O(V + E), SPACE: O(V)
        
        INTUITION:
        In undirected graph, if we reach a visited node (that's not our parent),
        it means there's another path to that node → cycle!
        
        Example:
        A --- B     If at B we see A, that's ok (A is parent)
        |     |     But if at C we see A → cycle! (A not parent of C)
        C --- D
        
        LEETCODE PROBLEMS:
        - 684: Redundant Connection ⭐⭐⭐
        - 261: Graph Valid Tree ⭐⭐
        - 1059: All Paths from Source Lead to Destination
        """
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):  # Found cycle in subtree
                        return True
                elif neighbor != parent:  # Visited and not parent → cycle!
                    return True
            
            return False
        
        # Check all components
        for i in range(n):
            if i not in visited:
                if dfs(i, -1):
                    return True
        
        return False
    
    
    def has_cycle_directed(self, n, edges):
        """
        Detect cycle in DIRECTED graph using DFS with states
        
        WHEN TO USE:
        - Directed graph (arrows have direction!)
        - Detect circular dependencies
        - Check if topological sort possible
        
        KEY POINTS:
        1. Use THREE states: UNVISITED, VISITING, VISITED
        2. VISITING = currently in DFS path (recursion stack)
        3. If we reach a VISITING node → cycle!
        
        THREE STATES:
        - WHITE (0): Unvisited
        - GRAY (1): Visiting (in current DFS path)
        - BLACK (2): Visited (completed)
        
        INTUITION:
        If during DFS we encounter a node that's GRAY (currently being processed),
        it means we've found a back edge → cycle!
        
        Example:
        A → B → C
        ↑       ↓
        └───────┘
        When at C, if we see A (which is GRAY), cycle detected!
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 207: Course Schedule ⭐⭐⭐ (MUST DO)
        - 210: Course Schedule II
        - 802: Find Eventual Safe States
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # 0 = WHITE (unvisited), 1 = GRAY (visiting), 2 = BLACK (visited)
        state = [0] * n
        
        def dfs(node):
            if state[node] == 1:  # GRAY = cycle!
                return True
            if state[node] == 2:  # BLACK = already processed
                return False
            
            state[node] = 1  # Mark as GRAY (visiting)
            
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            
            state[node] = 2  # Mark as BLACK (visited)
            return False
        
        # Check all nodes
        for i in range(n):
            if state[i] == 0:  # Unvisited
                if dfs(i):
                    return True
        
        return False
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: TOPOLOGICAL SORT ⭐⭐⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def topological_sort_dfs(self, n, edges):
        """
        Topological Sort using DFS (Post-order)
        
        WHEN TO USE:
        - Order tasks with dependencies
        - Course prerequisites
        - Build order
        - Directed Acyclic Graph (DAG) ordering
        
        WHAT IS TOPOLOGICAL SORT?
        For every edge A → B, A appears before B in the ordering
        
        Example:
        Courses:
        Math → Physics → Advanced Physics
        Math → Chemistry
        
        Valid orders:
        [Math, Physics, Chemistry, Advanced Physics]
        [Math, Chemistry, Physics, Advanced Physics]
        
        KEY POINTS:
        1. Only works on DAG (Directed Acyclic Graph)
        2. DFS + add to result in POST-ORDER
        3. Reverse the result at end
        4. Check for cycles first!
        
        INTUITION:
        Process deepest dependencies first, then work backwards
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 210: Course Schedule II ⭐⭐⭐
        - 269: Alien Dictionary (Premium) ⭐⭐⭐
        - 310: Minimum Height Trees
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        visited = set()
        result = []
        
        # First check for cycle
        state = [0] * n
        
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False
        
        for i in range(n):
            if has_cycle(i):
                return []  # Cycle exists, no valid order
        
        # DFS for topological sort
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor)
            
            result.append(node)  # POST-ORDER: add after processing children
        
        for i in range(n):
            if i not in visited:
                dfs(i)
        
        return result[::-1]  # Reverse!
    
    
    def topological_sort_kahns(self, n, edges):
        """
        Topological Sort using Kahn's Algorithm (BFS-based)
        
        RECOMMENDED APPROACH! Easier to understand than DFS version.
        
        ALGORITHM:
        1. Count in-degree (number of incoming edges) for each node
        2. Add all nodes with in-degree 0 to queue (no dependencies)
        3. Process queue:
           - Remove node, add to result
           - Decrease in-degree of neighbors
           - If neighbor's in-degree becomes 0, add to queue
        4. If result has all nodes → valid topo sort
           Otherwise → cycle exists!
        
        INTUITION:
        Start with nodes that have no prerequisites (in-degree 0)
        Remove them one by one, "freeing up" their dependents
        
        Example:
        A → B → D
        A → C → D
        
        In-degrees: A=0, B=1, C=1, D=2
        
        Step 1: Process A (in-degree 0)
        Step 2: B and C now have in-degree 0
        Step 3: Process B and C
        Step 4: D now has in-degree 0
        Step 5: Process D
        
        Result: [A, B, C, D] or [A, C, B, D]
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 207: Course Schedule ⭐⭐⭐
        - 210: Course Schedule II ⭐⭐⭐
        - 269: Alien Dictionary (Premium)
        """
        # Build graph and count in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Add all nodes with in-degree 0 to queue
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Reduce in-degree of neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                
                # If in-degree becomes 0, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all nodes processed → cycle exists
        if len(result) != n:
            return []  # Cycle detected
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: UNION-FIND (Disjoint Set Union) ⭐⭐⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    class UnionFind:
        """
        Union-Find (Disjoint Set Union) Data Structure
        
        WHEN TO USE:
        - Dynamic connectivity queries
        - Detect cycles in undirected graphs
        - Group elements into sets
        - Kruskal's MST algorithm
        - Network connectivity
        
        OPERATIONS:
        - find(x): Which set does x belong to?
        - union(x, y): Merge sets containing x and y
        - connected(x, y): Are x and y in same set?
        
        INTUITION:
        Each set has a "representative" (root/parent)
        All elements in same set point to same root
        
        Example:
        Initial: {1} {2} {3} {4} {5}
        
        union(1, 2): {1,2} {3} {4} {5}
        union(3, 4): {1,2} {3,4} {5}
        union(2, 3): {1,2,3,4} {5}
        
        find(1) == find(4)? YES (same root)
        find(1) == find(5)? NO (different roots)
        
        OPTIMIZATIONS:
        1. Path Compression: Make tree flat during find
        2. Union by Rank: Attach smaller tree under larger tree
        
        TIME: O(α(n)) ≈ O(1) amortized with optimizations
        SPACE: O(n)
        
        LEETCODE PROBLEMS:
        - 684: Redundant Connection ⭐⭐⭐
        - 547: Number of Provinces ⭐⭐
        - 721: Accounts Merge ⭐⭐
        - 200: Number of Islands (can use UF)
        - 323: Number of Connected Components (Premium)
        - 1319: Number of Operations to Make Network Connected
        """
        
        def __init__(self, n):
            """Initialize n disjoint sets"""
            self.parent = list(range(n))  # Each node is its own parent initially
            self.rank = [0] * n  # Rank for union by rank optimization
            self.count = n  # Number of separate components
        
        def find(self, x):
            """
            Find root of x with PATH COMPRESSION
            
            Path compression: Make all nodes point directly to root
            
            Before:     After find(4):
            1           1
            |           |\ \
            2           2 3 4
            |           
            3           
            |           
            4           
            """
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression!
            return self.parent[x]
        
        def union(self, x, y):
            """
            Union sets containing x and y with UNION BY RANK
            
            Union by rank: Attach smaller tree under root of larger tree
            Keeps tree flat → faster operations
            """
            root_x = self.find(x)
            root_y = self.find(y)
            
            if root_x == root_y:
                return False  # Already in same set
            
            # Union by rank: attach smaller tree under larger tree
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            self.count -= 1  # One less component
            return True
        
        def connected(self, x, y):
            """Check if x and y are in same set"""
            return self.find(x) == self.find(y)
        
        def get_count(self):
            """Get number of separate components"""
            return self.count
    
    
    def find_redundant_connection(self, edges):
        """
        LeetCode 684: Redundant Connection
        
        Find edge that creates cycle in undirected graph
        
        Example:
        edges = [[1,2],[1,3],[2,3]]
        Output: [2,3] (this edge creates cycle)
        
        APPROACH:
        Use Union-Find. When union returns False, that edge creates cycle!
        """
        n = len(edges)
        uf = self.UnionFind(n + 1)
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]  # This edge creates cycle!
        
        return []
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: BIPARTITE GRAPH ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def is_bipartite_bfs(self, graph):
        """
        Check if graph is bipartite using BFS with 2-coloring
        
        WHAT IS BIPARTITE?
        Graph where nodes can be split into 2 groups such that
        all edges go between groups (no edges within a group)
        
        EQUIVALENT TO:
        Can we color graph with 2 colors such that no adjacent nodes
        have the same color?
        
        Example - BIPARTITE:
        A --- B        Color: A=Red, B=Blue, C=Blue, D=Red
        |     |        All edges connect different colors ✓
        C --- D
        
        Example - NOT BIPARTITE:
        A --- B        A-B-C forms triangle
        |   / |        Cannot 2-color a triangle! ✗
        | /   |
        C     
        
        PROPERTIES:
        - Bipartite ↔ No odd-length cycles
        - Trees are always bipartite
        - Even-length cycle graphs are bipartite
        
        WHEN TO USE:
        - Matching problems
        - Conflict detection
        - Scheduling (2 groups)
        
        ALGORITHM:
        1. Try to color graph with 2 colors (0 and 1)
        2. Use BFS, color neighbors with opposite color
        3. If we try to color a node that's already colored differently → not bipartite
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 785: Is Graph Bipartite? ⭐⭐⭐
        - 886: Possible Bipartition ⭐⭐
        """
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0 = color 0, 1 = color 1
        
        def bfs(start):
            queue = deque([start])
            color[start] = 0  # Color with 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Uncolored: color with opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Already colored with SAME color → not bipartite!
                        return False
            
            return True
        
        # Check all components (graph might be disconnected)
        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
    
    
    def is_bipartite_dfs(self, graph):
        """
        Check if graph is bipartite using DFS with 2-coloring
        
        Same idea as BFS, but using DFS
        """
        n = len(graph)
        color = [-1] * n
        
        def dfs(node, c):
            color[node] = c
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    # Uncolored: color with opposite color
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == color[node]:
                    # Same color → not bipartite!
                    return False
            
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: CONNECTED COMPONENTS (Review)
    # ═══════════════════════════════════════════════════════════════════════
    
    def count_components_dfs(self, n, edges):
        """
        Count connected components using DFS
        
        WHEN TO USE:
        - Count separate groups/islands
        - Find number of networks
        
        TIME: O(V + E), SPACE: O(V)
        """
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
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
    
    
    def count_components_union_find(self, n, edges):
        """
        Count connected components using Union-Find
        
        APPROACH:
        1. Start with n components (all separate)
        2. Union edges
        3. Count remaining components
        """
        uf = self.UnionFind(n)
        
        for u, v in edges:
            uf.union(u, v)
        
        return uf.get_count()


# ═══════════════════════════════════════════════════════════════════════
# COMPLETE LEETCODE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

class Solution:
    
    def canFinish(self, numCourses, prerequisites):
        """
        LeetCode 207: Course Schedule
        
        Detect if cycle exists in directed graph
        If cycle exists → impossible to finish all courses
        
        Example:
        numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: False (circular dependency: 0→1→0)
        
        numCourses = 2, prerequisites = [[1,0]]
        Output: True (can do: 0 then 1)
        
        Difficulty: Medium
        Pattern: Cycle Detection in Directed Graph
        
        APPROACHES:
        1. DFS with states (WHITE, GRAY, BLACK)
        2. Kahn's algorithm (BFS with in-degrees)
        """
        # Approach 1: DFS with states
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # 0=WHITE (unvisited), 1=GRAY (visiting), 2=BLACK (visited)
        state = [0] * numCourses
        
        def has_cycle(course):
            if state[course] == 1:  # GRAY = back edge = cycle!
                return True
            if state[course] == 2:  # BLACK = already processed
                return False
            
            state[course] = 1  # Mark GRAY
            
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
            
            state[course] = 2  # Mark BLACK
            return False
        
        for i in range(numCourses):
            if has_cycle(i):
                return False
        
        return True
    
    
    def findOrder(self, numCourses, prerequisites):
        """
        LeetCode 210: Course Schedule II
        
        Return topological sort order (valid course order)
        If cycle exists → return empty array
        
        Example:
        numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,1,2,3] or [0,2,1,3]
        
        Difficulty: Medium
        Pattern: Topological Sort (Kahn's Algorithm)
        """
        # Build graph and in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Kahn's algorithm
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If not all courses in result → cycle exists
        return result if len(result) == numCourses else []
    
    
    def findRedundantConnection(self, edges):
        """
        LeetCode 684: Redundant Connection
        
        Find edge that creates cycle in undirected graph
        Return last edge that creates cycle
        
        Example:
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4] (creates cycle 1-2-3-4-1)
        
        Difficulty: Medium
        Pattern: Union-Find
        """
        uf = UnionFind(len(edges) + 1)
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]  # This edge creates cycle!
        
        return []
    
    
    def findCircleNum(self, isConnected):
        """
        LeetCode 547: Number of Provinces
        
        Count number of connected components
        
        Example:
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2 (two separate groups)
        
        Difficulty: Medium
        Pattern: Union-Find or DFS
        """
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        return uf.get_count()
    
    
    def isBipartite(self, graph):
        """
        LeetCode 785: Is Graph Bipartite?
        
        Check if graph can be 2-colored
        
        Example:
        graph = [[1,3],[0,2],[1,3],[0,2]]
        Output: True (0=Red, 1=Blue, 2=Red, 3=Blue)
        
        graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        Output: False (node 0,1,2,3 form odd cycle)
        
        Difficulty: Medium
        Pattern: BFS/DFS with 2-coloring
        """
        n = len(graph)
        color = [-1] * n
        
        def bfs(start):
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
    
    
    def accountsMerge(self, accounts):
        """
        LeetCode 721: Accounts Merge
        
        Merge accounts with common emails
        
        Example:
        accounts = [
            ["John","john@mail.com","john_work@mail.com"],
            ["John","john_new@mail.com"],
            ["John","john@mail.com","john_new@mail.com"]
        ]
        Output: [
            ["John","john@mail.com","john_new@mail.com","john_work@mail.com"]
        ]
        
        Difficulty: Medium
        Pattern: Union-Find
        """
        uf = UnionFind(len(accounts))
        email_to_id = {}
        
        # Union accounts with common emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    uf.union(i, email_to_id[email])
                else:
                    email_to_id[email] = i
        
        # Group emails by account
        merged = defaultdict(set)
        for email, acc_id in email_to_id.items():
            root = uf.find(acc_id)
            merged[root].add(email)
        
        # Build result
        result = []
        for acc_id, emails in merged.items():
            name = accounts[acc_id][0]
            result.append([name] + sorted(emails))
        
        return result


# ═══════════════════════════════════════════════════════════════════════
# UNION-FIND STANDALONE (for easy import)
# ═══════════════════════════════════════════════════════════════════════

class UnionFind:
    """
    Standard Union-Find implementation with path compression and union by rank
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_count(self):
        return self.count


# ═══════════════════════════════════════════════════════════════════════
# QUICK REFERENCE - PATTERN SELECTION
# ═══════════════════════════════════════════════════════════════════════

"""
┌─────────────────────────────────────────────────────────────────────────┐
│ GRAPH PATTERN SELECTION GUIDE                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│ QUESTION TYPE                           → USE PATTERN                    │
│ ─────────────────────────────────────────────────────────────────────── │
│                                                                           │
│ "Detect cycle" (undirected)            → DFS with parent tracking        │
│ "Detect cycle" (directed)              → DFS with 3 states (W/G/B)      │
│                                                                           │
│ "Course schedule"                       → Cycle detection OR Topo sort   │
│ "Prerequisites", "Task order"          → Topological sort (Kahn's)      │
│                                                                           │
│ "Dynamic connectivity"                  → Union-Find                      │
│ "Redundant connection"                  → Union-Find (detect cycle)      │
│ "Group/merge by connection"            → Union-Find                      │
│                                                                           │
│ "2-coloring", "Bipartite"              → BFS/DFS with coloring           │
│ "Split into 2 groups"                  → Bipartite check                 │
│                                                                           │
│ "Count components/islands"             → DFS/BFS or Union-Find           │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘

ALGORITHM CHEAT SHEET:

CYCLE DETECTION:
────────────────────────────────────────
Undirected: DFS with parent
def dfs(node, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node): return True
        elif neighbor != parent:
            return True  # Cycle!
    return False

Directed: DFS with states
state = [0] * n  # 0=WHITE, 1=GRAY, 2=BLACK
def dfs(node):
    if state[node] == 1: return True  # Cycle!
    if state[node] == 2: return False
    state[node] = 1
    for neighbor in graph[node]:
        if dfs(neighbor): return True
    state[node] = 2
    return False

TOPOLOGICAL SORT:
────────────────────────────────────────
Kahn's Algorithm (RECOMMENDED):
in_degree = [0] * n
queue = deque([nodes with in_degree 0])
result = []

while queue:
    node = queue.popleft()
    result.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(result) != n: return []  # Cycle!
return result

UNION-FIND:
────────────────────────────────────────
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

BIPARTITE:
────────────────────────────────────────
BFS with 2-coloring:
color = [-1] * n
queue = deque([start])
color[start] = 0

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if color[neighbor] == -1:
            color[neighbor] = 1 - color[node]
            queue.append(neighbor)
        elif color[neighbor] == color[node]:
            return False  # Not bipartite!
return True
"""


# ═══════════════════════════════════════════════════════════════════════
# PRACTICE PROBLEMS BY PATTERN
# ═══════════════════════════════════════════════════════════════════════

"""
WEEK 1: CYCLE DETECTION + TOPOLOGICAL SORT
═══════════════════════════════════════════════════════════════════════════
Day 1-2: Cycle Detection
- 207: Course Schedule ⭐⭐⭐ (MUST DO FIRST)
- 684: Redundant Connection ⭐⭐
- 261: Graph Valid Tree

Day 3-4: Topological Sort
- 210: Course Schedule II ⭐⭐⭐ (MUST DO)
- 802: Find Eventual Safe States
- 310: Minimum Height Trees (harder)

Day 5-7: Practice both
- Review and combine concepts
- Try medium/hard problems


WEEK 2: UNION-FIND
═══════════════════════════════════════════════════════════════════════════
Day 1-2: Basic Union-Find
- 547: Number of Provinces ⭐⭐⭐ (MUST DO FIRST)
- 684: Redundant Connection ⭐⭐
- 323: Number of Connected Components (Premium)

Day 3-4: Advanced Union-Find
- 721: Accounts Merge ⭐⭐⭐
- 1319: Number of Operations to Make Network Connected
- 1202: Smallest String With Swaps

Day 5-7: Practice
- 959: Regions Cut By Slashes (harder)
- Review all UF problems


WEEK 3: BIPARTITE + REVIEW
═══════════════════════════════════════════════════════════════════════════
Day 1-2: Bipartite
- 785: Is Graph Bipartite? ⭐⭐⭐ (MUST DO)
- 886: Possible Bipartition ⭐⭐

Day 3-7: Mixed practice
- Random problems from all patterns
- Mock interviews
- Review weak areas


WEEK 4: COMPREHENSIVE PRACTICE
═══════════════════════════════════════════════════════════════════════════
Mix all patterns:
- Do 2-3 problems daily
- Focus on recognizing which pattern to use
- Time yourself
- Explain solution out loud


═══════════════════════════════════════════════════════════════════════════
TOP 15 MUST-DO PROBLEMS (PRIORITY ORDER):
═══════════════════════════════════════════════════════════════════════════

ESSENTIAL (DO THESE FIRST):
1. 207: Course Schedule (Cycle Detection)
2. 210: Course Schedule II (Topological Sort)
3. 547: Number of Provinces (Union-Find)
4. 684: Redundant Connection (Union-Find)
5. 785: Is Graph Bipartite? (Bipartite Check)

IMPORTANT:
6. 721: Accounts Merge (Union-Find)
7. 261: Graph Valid Tree (Cycle Detection)
8. 886: Possible Bipartition (Bipartite)
9. 802: Find Eventual Safe States (Cycle + Topo)
10. 1319: Network Operations (Union-Find)

PRACTICE:
11. 310: Minimum Height Trees (Topo Sort variant)
12. 323: Connected Components (Union-Find) (Premium)
13. 269: Alien Dictionary (Topo Sort) (Premium)
14. 1202: Smallest String With Swaps (Union-Find)
15. Review and random selection

Master these 15 and you'll handle 95% of graph interviews! 🚀
"""


# ═══════════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════════

def test_all_patterns():
    """Test all graph patterns"""
    
    print("Testing Graph Patterns...\n")
    patterns = GraphPatterns()
    
    # Test 1: Cycle Detection (Undirected)
    edges = [[0, 1], [1, 2], [2, 0]]
    result = patterns.has_cycle_undirected(3, edges)
    print(f"Cycle Detection (Undirected): {result}")
    assert result == True
    print("✅ Test 1 passed\n")
    
    # Test 2: Cycle Detection (Directed)
    edges = [[0, 1], [1, 2], [2, 0]]
    result = patterns.has_cycle_directed(3, edges)
    print(f"Cycle Detection (Directed): {result}")
    assert result == True
    print("✅ Test 2 passed\n")
    
    # Test 3: Topological Sort
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    result = patterns.topological_sort_kahns(4, edges)
    print(f"Topological Sort: {result}")
    assert len(result) == 4
    print("✅ Test 3 passed\n")
    
    # Test 4: Union-Find
    uf = patterns.UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    print(f"0 and 1 connected: {uf.connected(0, 1)}")
    print(f"0 and 2 connected: {uf.connected(0, 2)}")
    print(f"Number of components: {uf.get_count()}")
    assert uf.connected(0, 1) == True
    assert uf.connected(0, 2) == False
    print("✅ Test 4 passed\n")
    
    # Test 5: Bipartite
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    result = patterns.is_bipartite_bfs(graph)
    print(f"Is Bipartite: {result}")
    assert result == True
    print("✅ Test 5 passed\n")
    
    print("🎉 All tests passed!")


if __name__ == "__main__":
    test_all_patterns()
```

---

## **How to Use This Guide** 📖

1. **Copy entire code** to `basic_graph_patterns.py`
2. **Follow week-by-week schedule** in comments
3. **Do problems in order** (marked with ⭐)
4. **Run test cases** to verify understanding
5. **Review Quick Reference** section often

---

## **Study Plan** 📅
```
Week 1: Cycle + Topo (hardest)
Week 2: Union-Find (most useful)
Week 3: Bipartite + Review
Week 4: Mixed practice

Daily: 2-3 hours, 2-3 problems