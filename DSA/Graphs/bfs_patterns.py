from collections import deque

"""
═══════════════════════════════════════════════════════════════════════════════
                    COMPLETE BFS PATTERNS GUIDE
═══════════════════════════════════════════════════════════════════════════════

BFS (Breadth-First Search):
- Explores level by level (neighbors first)
- Uses Queue (FIFO - First In First Out)
- Space: O(width) - can be large for wide graphs
- BEST for: shortest path, level-order, minimum steps

WHY BFS OVER DFS?
✅ Shortest path in unweighted graphs (BFS guarantees it!)
✅ Level-order traversal
✅ Finding closest/nearest nodes
✅ Minimum number of steps/moves
✅ Testing bipartiteness

9 ESSENTIAL BFS PATTERNS:
1. Basic BFS - single source traversal
2. BFS with Level Tracking - process level by level
3. BFS for Disconnected Graph - multiple components
4. Multi-source BFS - multiple starting points
5. BFS for Grid/Matrix - 2D traversal
6. BFS for Shortest Path - minimum distance
7. BFS with State - track additional state info
8. Bidirectional BFS - meet in the middle (advanced)
9. 0-1 BFS - weighted graphs with 0/1 weights (advanced)

═══════════════════════════════════════════════════════════════════════════════
"""


class BFSPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: BASIC BFS ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def bfs_basic(self, graph, start):
        """
        Standard BFS traversal from single source
        
        WHEN TO USE:
        - Simple graph traversal
        - Visit all reachable nodes
        - Order matters (level by level)
        
        KEY POINTS:
        1. Use deque for O(1) popleft
        2. Mark visited WHEN ADDING to queue (not when processing)
        3. Add all neighbors to queue
        
        TIME: O(V + E), SPACE: O(V) for queue and visited
        
        LEETCODE PROBLEMS:
        - 1971: Find if Path Exists in Graph
        - 133: Clone Graph
        - 841: Keys and Rooms
        """
        queue = deque([start])
        visited = set([start])
        result = []
        
        while queue:
            node = queue.popleft()  # FIFO - First In First Out
            result.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: BFS WITH LEVEL TRACKING ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def bfs_with_levels(self, graph, start):
        """
        BFS that processes nodes level by level
        
        WHEN TO USE:
        - Need to know which level each node is at
        - Process all nodes at same distance together
        - Level-order traversal in trees
        - "Minimum steps" problems
        
        KEY POINTS:
        1. Take snapshot of queue size at each level
        2. Process exactly that many nodes
        3. Each level represents distance from start
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 102: Binary Tree Level Order Traversal ⭐⭐⭐ (MUST DO)
        - 103: Binary Tree Zigzag Level Order
        - 107: Binary Tree Level Order Traversal II
        - 199: Binary Tree Right Side View ⭐⭐
        - 515: Find Largest Value in Each Row
        - 637: Average of Levels
        - 1161: Maximum Level Sum
        """
        queue = deque([start])
        visited = set([start])
        levels = []  # List of lists, each inner list is one level
        
        while queue:
            level_size = len(queue)  # Snapshot current level size
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            levels.append(current_level)
        
        return levels
    
    
    def bfs_with_distance(self, graph, start):
        """
        BFS tracking distance/depth from start
        
        WHEN TO USE:
        - Need actual distance to each node
        - "How many steps away" problems
        """
        queue = deque([(start, 0)])  # (node, distance)
        visited = set([start])
        distances = {start: 0}
        
        while queue:
            node, dist = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distances[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1))
        
        return distances
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: BFS FOR DISCONNECTED GRAPH ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def bfs_disconnected(self, graph, n):
        """
        BFS that handles multiple disconnected components
        
        WHEN TO USE:
        - Graph may have separate components
        - Need to visit ALL nodes regardless of connectivity
        - Count number of components
        
        KEY POINTS:
        1. Loop through ALL vertices
        2. Start BFS from unvisited vertices
        3. Shared visited set across all BFS calls
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 547: Number of Provinces ⭐⭐⭐ (MUST DO)
        - 323: Number of Connected Components (Premium)
        - Can also do: 200 (Islands), 695 (Max Area)
        """
        visited = set()
        components = []
        
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            component = []
            
            while queue:
                node = queue.popleft()
                component.append(node)
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            return component
        
        # Try BFS from every vertex
        for vertex in range(n):
            if vertex not in visited:
                component = bfs(vertex)
                components.append(component)
        
        return components
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: MULTI-SOURCE BFS ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def multi_source_bfs(self, graph, sources):
        """
        BFS starting from MULTIPLE sources simultaneously
        
        WHEN TO USE:
        - Multiple starting points
        - "Distance from nearest X" problems
        - Spreading/propagation problems (fire, infection, etc.)
        
        KEY POINTS:
        1. Add ALL sources to queue initially
        2. They all start at distance 0
        3. BFS naturally finds minimum distance to any source
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 994: Rotting Oranges ⭐⭐⭐ (MUST DO - classic multi-source)
        - 542: 01 Matrix ⭐⭐
        - 1162: As Far from Land as Possible
        - 286: Walls and Gates (Premium)
        - 317: Shortest Distance from All Buildings (Hard)
        """
        queue = deque()
        visited = set()
        
        # Add ALL sources to queue
        for source in sources:
            queue.append((source, 0))  # (node, distance)
            visited.add(source)
        
        distances = {}
        
        while queue:
            node, dist = queue.popleft()
            distances[node] = dist
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return distances
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: BFS FOR GRID/MATRIX ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def bfs_grid(self, grid, start_r, start_c):
        """
        BFS for 2D grid/matrix
        
        WHEN TO USE:
        - 2D grid shortest path
        - Spreading in 2D (flood fill, rotting, etc.)
        - Finding nearest cell with property X
        
        KEY POINTS:
        1. Check boundaries for each cell
        2. Visit 4 directions (or 8 if diagonal allowed)
        3. Use (row, col) tuples for positions
        4. Track visited cells
        
        TIME: O(rows * cols), SPACE: O(rows * cols)
        
        LEETCODE PROBLEMS:
        - 1091: Shortest Path in Binary Matrix ⭐⭐⭐ (MUST DO)
        - 542: 01 Matrix ⭐⭐
        - 994: Rotting Oranges ⭐⭐⭐
        - 1162: As Far from Land as Possible
        - 1765: Map of Highest Peak
        - 286: Walls and Gates (Premium)
        - 317: Shortest Distance from All Buildings (Hard Premium)
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque([(start_r, start_c, 0)])  # (row, col, distance)
        visited = set([(start_r, start_c)])
        
        # 4 directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c, dist = queue.popleft()
            
            # Process current cell
            # (do whatever you need with grid[r][c])
            
            # Visit all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and validity
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    grid[nr][nc] != -1):  # Example: -1 is obstacle
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: BFS FOR SHORTEST PATH ⭐⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def shortest_path(self, graph, start, end):
        """
        Find shortest path from start to end
        
        WHEN TO USE:
        - Need SHORTEST path (BFS guarantees it!)
        - Minimum number of edges
        - Unweighted graphs only
        
        KEY POINTS:
        1. BFS finds shortest path in unweighted graphs
        2. First time you reach target = shortest path
        3. Can also reconstruct path using parent tracking
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 1091: Shortest Path in Binary Matrix ⭐⭐⭐
        - 752: Open the Lock ⭐⭐
        - 127: Word Ladder ⭐⭐⭐ (Hard but classic)
        - 1926: Nearest Exit from Entrance in Maze
        - 863: All Nodes Distance K in Binary Tree ⭐⭐
        """
        if start == end:
            return 0
        
        queue = deque([(start, 0)])  # (node, distance)
        visited = set([start])
        
        while queue:
            node, dist = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor == end:
                    return dist + 1  # Found shortest path!
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return -1  # No path exists
    
    
    def shortest_path_with_path(self, graph, start, end):
        """
        Find shortest path AND return the actual path
        
        Uses parent tracking to reconstruct path
        """
        if start == end:
            return [start]
        
        queue = deque([start])
        visited = set([start])
        parent = {start: None}
        
        while queue:
            node = queue.popleft()
            
            if node == end:
                # Reconstruct path
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]  # Reverse to get start -> end
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        return []  # No path
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: BFS WITH STATE ⭐⭐
    # ═══════════════════════════════════════════════════════════════════════
    
    def bfs_with_state(self, start_state):
        """
        BFS where each node has additional STATE information
        
        WHEN TO USE:
        - Need to track more than just position
        - State affects what moves are valid
        - Examples: keys collected, obstacles removed, direction facing
        
        KEY POINTS:
        1. State is part of visited check
        2. Queue contains (position, state, steps)
        3. Same position with different state = different node
        
        TIME: O(V * S) where S is state space
        SPACE: O(V * S)
        
        LEETCODE PROBLEMS:
        - 864: Shortest Path to Get All Keys ⭐⭐⭐ (Hard)
        - 1293: Shortest Path in Grid with Obstacles Elimination ⭐⭐
        - 847: Shortest Path Visiting All Nodes (Hard)
        - 1263: Minimum Moves to Move a Box (Hard)
        """
        # Example: position with keys collected
        # State = (row, col, keys_collected)
        queue = deque([start_state])
        visited = set([start_state])
        
        while queue:
            state = queue.popleft()
            # state could be: (r, c, keys, steps) or similar
            
            # Process state and generate next states
            for next_state in self.get_next_states(state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: BIDIRECTIONAL BFS ⭐⭐ (ADVANCED)
    # ═══════════════════════════════════════════════════════════════════════
    
    def bidirectional_bfs(self, graph, start, end):
        """
        BFS from both start and end simultaneously
        
        WHEN TO USE:
        - Very large search space
        - Know both start and end
        - Can reduce time complexity significantly
        
        KEY INSIGHT:
        Meet in the middle! Search from both ends.
        Time: O(b^(d/2)) instead of O(b^d) where b=branching factor, d=depth
        
        KEY POINTS:
        1. Two queues: one from start, one from end
        2. Two visited sets
        3. Stop when they meet
        4. Expand smaller frontier (optimization)
        
        LEETCODE PROBLEMS:
        - 127: Word Ladder (can optimize with bidirectional)
        - 752: Open the Lock
        """
        if start == end:
            return 0
        
        # Forward search from start
        queue_start = deque([(start, 0)])
        visited_start = {start: 0}
        
        # Backward search from end
        queue_end = deque([(end, 0)])
        visited_end = {end: 0}
        
        while queue_start and queue_end:
            # Expand from start
            node, dist = queue_start.popleft()
            
            for neighbor in graph[node]:
                if neighbor in visited_end:
                    # Met in the middle!
                    return dist + 1 + visited_end[neighbor]
                
                if neighbor not in visited_start:
                    visited_start[neighbor] = dist + 1
                    queue_start.append((neighbor, dist + 1))
            
            # Expand from end
            node, dist = queue_end.popleft()
            
            for neighbor in graph[node]:
                if neighbor in visited_start:
                    # Met in the middle!
                    return dist + 1 + visited_start[neighbor]
                
                if neighbor not in visited_end:
                    visited_end[neighbor] = dist + 1
                    queue_end.append((neighbor, dist + 1))
        
        return -1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: 0-1 BFS ⭐ (ADVANCED)
    # ═══════════════════════════════════════════════════════════════════════
    
    def zero_one_bfs(self, graph, start, end):
        """
        BFS for graphs with edge weights 0 or 1 only
        
        WHEN TO USE:
        - Weighted graph but weights are only 0 or 1
        - Faster than Dijkstra for this special case
        - Example: grid where some moves are free (0) others cost 1
        
        KEY POINTS:
        1. Use deque (not priority queue like Dijkstra)
        2. Weight 0 edges: add to FRONT of queue
        3. Weight 1 edges: add to BACK of queue
        4. This maintains sorted order by distance
        
        TIME: O(V + E), SPACE: O(V)
        
        LEETCODE PROBLEMS:
        - 1368: Minimum Cost to Make at Least One Valid Path ⭐⭐ (Hard)
        - 2290: Minimum Obstacle Removal to Reach Corner
        """
        queue = deque([(start, 0)])  # (node, distance)
        distances = {start: 0}
        
        while queue:
            node, dist = queue.popleft()
            
            if node == end:
                return dist
            
            if dist > distances.get(node, float('inf')):
                continue
            
            for neighbor, weight in graph[node]:  # (neighbor, weight)
                new_dist = dist + weight
                
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    
                    if weight == 0:
                        queue.appendleft((neighbor, new_dist))  # Add to FRONT
                    else:
                        queue.append((neighbor, new_dist))  # Add to BACK
        
        return distances.get(end, -1)


# ═══════════════════════════════════════════════════════════════════════
# COMPLETE LEETCODE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

class Solution:
    
    def levelOrder(self, root):
        """
        LeetCode 102: Binary Tree Level Order Traversal
        
        Return level order traversal as list of lists
        
        Example:
        Input: [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
        
        Difficulty: Medium
        Pattern: BFS with Level Tracking (Pattern 2)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
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
            
            result.append(level)
        
        return result
    
    
    def rightSideView(self, root):
        """
        LeetCode 199: Binary Tree Right Side View
        
        Return values visible from right side (last node in each level)
        
        Example:
        Input: [1,2,3,null,5,null,4]
        Output: [1,3,4]
        
        Difficulty: Medium
        Pattern: BFS with Level Tracking (Pattern 2)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Last node in this level
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
    
    
    def orangesRotting(self, grid):
        """
        LeetCode 994: Rotting Oranges
        
        Fresh oranges rot if adjacent to rotten (4-directional)
        Return minutes until all oranges rot, or -1 if impossible
        
        Example:
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4
        
        Difficulty: Medium
        Pattern: Multi-source BFS + Grid (Pattern 4 + 5)
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Find all rotten oranges (multiple sources) and count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == 1):
                    
                    grid[nr][nc] = 2  # Rot this orange
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))
        
        return minutes if fresh_count == 0 else -1
    
    
    def shortestPathBinaryMatrix(self, grid):
        """
        LeetCode 1091: Shortest Path in Binary Matrix
        
        Find shortest path from top-left to bottom-right
        Can move 8 directions (including diagonal)
        0 = empty, 1 = blocked
        
        Example:
        grid = [[0,0,0],[1,1,0],[1,1,0]]
        Output: 4 (path length)
        
        Difficulty: Medium
        Pattern: BFS Grid Shortest Path (Pattern 5 + 6)
        """
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # 8 directions (including diagonal)
        directions = [
            (0,1), (1,0), (0,-1), (-1,0),  # 4 cardinal
            (1,1), (1,-1), (-1,1), (-1,-1)  # 4 diagonal
        ]
        
        queue = deque([(0, 0, 1)])  # (row, col, distance)
        visited = set([(0, 0)])
        
        while queue:
            r, c, dist = queue.popleft()
            
            if r == n - 1 and c == n - 1:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < n and 0 <= nc < n and
                    (nr, nc) not in visited and
                    grid[nr][nc] == 0):
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        
        return -1
    
    
    def updateMatrix(self, mat):
        """
        LeetCode 542: 01 Matrix
        
        For each cell, find distance to nearest 0
        
        Example:
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        Output: [[0,0,0],[0,1,0],[1,2,1]]
        
        Difficulty: Medium
        Pattern: Multi-source BFS + Grid (Pattern 4 + 5)
        """
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        # Add all 0s as sources
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1  # Mark as unvisited
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and
                    mat[nr][nc] == -1):
                    
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat
    
    
    def findCircleNum(self, isConnected):
        """
        LeetCode 547: Number of Provinces
        
        Count number of connected components
        
        Example:
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2
        
        Difficulty: Medium
        Pattern: BFS for Disconnected Graph (Pattern 3)
        """
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            
            while queue:
                city = queue.popleft()
                
                for neighbor in range(n):
                    if (isConnected[city][neighbor] == 1 and
                        neighbor not in visited):
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        for city in range(n):
            if city not in visited:
                provinces += 1
                bfs(city)
        
        return provinces
    
    
    def openLock(self, deadends, target):
        """
        LeetCode 752: Open the Lock
        
        4-digit lock, each digit can be rotated up or down
        Find minimum rotations to reach target, avoiding deadends
        
        Example:
        deadends = ["0201","0101","0102","1212","2002"]
        target = "0202"
        Output: 6
        
        Difficulty: Medium
        Pattern: BFS Shortest Path (Pattern 6)
        """
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                digit = int(state[i])
                
                # Rotate up
                new_digit = (digit + 1) % 10
                neighbors.append(state[:i] + str(new_digit) + state[i+1:])
                
                # Rotate down
                new_digit = (digit - 1) % 10
                neighbors.append(state[:i] + str(new_digit) + state[i+1:])
            
            return neighbors
        
        while queue:
            state, steps = queue.popleft()
            
            for neighbor in get_neighbors(state):
                if neighbor == target:
                    return steps + 1
                
                if neighbor not in visited and neighbor not in dead:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1
    
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        LeetCode 127: Word Ladder
        
        Transform beginWord to endWord, changing one letter at a time
        Each intermediate word must be in wordList
        Return length of shortest transformation sequence
        
        Example:
        beginWord = "hit", endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
        
        Difficulty: Hard
        Pattern: BFS Shortest Path (Pattern 6)
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            
            # Try changing each character
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))
        
        return 0
    
    
    def minDepth(self, root):
        """
        LeetCode 111: Minimum Depth of Binary Tree
        
        Find shortest path from root to any leaf
        
        Example:
        Input: [3,9,20,null,null,15,7]
        Output: 2 (path: 3 -> 9)
        
        Difficulty: Easy
        Pattern: BFS Level Tracking (Pattern 2)
        
        NOTE: BFS is better than DFS for minimum depth!
        BFS stops as soon as it finds first leaf.
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # First leaf found = minimum depth
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0


# ═══════════════════════════════════════════════════════════════════════
# QUICK REFERENCE - PATTERN SELECTION GUIDE
# ═══════════════════════════════════════════════════════════════════════

"""
┌─────────────────────────────────────────────────────────────────────────┐
│ BFS PATTERN SELECTION GUIDE                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│ QUESTION TYPE                           → USE PATTERN                    │
│ ─────────────────────────────────────────────────────────────────────── │
│                                                                           │
│ "Shortest path"                         → Pattern 6 (Shortest Path)      │
│ "Minimum steps/moves"                   → BFS guarantees shortest!       │
│                                                                           │
│ "Level order traversal"                 → Pattern 2 (Level Tracking)     │
│ "Process by level"                      → Snapshot queue size            │
│                                                                           │
│ "Multiple sources"                      → Pattern 4 (Multi-source)       │
│ "Rotting oranges", "Distance to X"     → Add all sources to queue       │
│                                                                           │
│ "2D grid shortest path"                 → Pattern 5 (Grid BFS)           │
│ "Maze", "Islands with distance"        → Check 4 or 8 directions         │
│                                                                           │
│ "Count components"                      → Pattern 3 (Disconnected)       │
│ "Number of islands"                     → Loop through all cells         │
│                                                                           │
│ "With keys/obstacles"                   → Pattern 7 (BFS with State)     │
│ "Collect items while moving"            → Track state in queue           │
│                                                                           │
│ "Word Ladder", very large space         → Pattern 8 (Bidirectional)      │
│ "Meet in the middle"                    → Two BFS simultaneously         │
│                                                                           │
│ "0-1 weighted edges only"               → Pattern 9 (0-1 BFS)            │
│ "Free moves vs costly moves"            → Deque: front for 0, back for 1│
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘

CRITICAL DECISION POINTS:

1. Shortest Path?
   YES → ALWAYS use BFS (not DFS!)
   BFS guarantees shortest path in unweighted graphs

2. Need level information?
   YES → Pattern 2 (snapshot queue size per level)
   NO  → Pattern 1 (basic BFS)

3. Multiple starting points?
   YES → Pattern 4 (add all sources to queue initially)
   NO  → Single source BFS

4. 2D Grid?
   YES → Pattern 5 (check boundaries + directions)
   NO  → Regular graph BFS

5. Disconnected graph?
   YES → Pattern 3 (loop through all vertices)
   NO  → Single BFS call


BFS vs DFS - WHEN TO USE BFS:
─────────────────────────────────────
✅ Finding SHORTEST path (unweighted)
✅ Level-order traversal
✅ Minimum steps/moves
✅ "Nearest X" problems
✅ Spreading/propagation (fire, infection)

❌ Use DFS instead for:
- All paths (need backtracking)
- Deeper than wider graphs (save space)
- Detect cycles
- Topological sort


TEMPLATES:

═══════════════════════════════════════════════════════════════════
BASIC BFS (Pattern 1):
───────────────────────────────────────
queue = deque([start])
visited = set([start])

while queue:
    node = queue.popleft()
    # Process node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

═══════════════════════════════════════════════════════════════════
BFS WITH LEVELS (Pattern 2):
───────────────────────────────────────
queue = deque([start])
visited = set([start])

while queue:
    level_size = len(queue)  # Snapshot!
    
    for _ in range(level_size):
        node = queue.popleft()
        # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

═══════════════════════════════════════════════════════════════════
MULTI-SOURCE BFS (Pattern 4):
───────────────────────────────────────
queue = deque()
visited = set()

# Add ALL sources
for source in sources:
    queue.append(source)
    visited.add(source)

while queue:
    node = queue.popleft()
    # Process
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

═══════════════════════════════════════════════════════════════════
GRID BFS (Pattern 5):
───────────────────────────────────────
queue = deque([(start_r, start_c)])
visited = set([(start_r, start_c)])
directions = [(0,1), (1,0), (0,-1), (-1,0)]

while queue:
    r, c = queue.popleft()
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if (0 <= nr < rows and 0 <= nc < cols and
            (nr, nc) not in visited and
            grid[nr][nc] != obstacle):
            
            visited.add((nr, nc))
            queue.append((nr, nc))

═══════════════════════════════════════════════════════════════════
"""


# ═══════════════════════════════════════════════════════════════════════
# PRACTICE PROBLEMS BY PATTERN
# ═══════════════════════════════════════════════════════════════════════

"""
PATTERN 2: BFS WITH LEVEL TRACKING
═══════════════════════════════════════
Easy:
- 102: Binary Tree Level Order Traversal ⭐⭐⭐ (MUST DO FIRST)
- 107: Binary Tree Level Order Traversal II
- 637: Average of Levels in Binary Tree
- 111: Minimum Depth of Binary Tree ⭐⭐

Medium:
- 103: Binary Tree Zigzag Level Order ⭐⭐
- 199: Binary Tree Right Side View ⭐⭐⭐
- 515: Find Largest Value in Each Row
- 1161: Maximum Level Sum of Binary Tree
- 116: Populating Next Right Pointers ⭐⭐


PATTERN 4: MULTI-SOURCE BFS
═══════════════════════════════════════
Medium:
- 994: Rotting Oranges ⭐⭐⭐ (MUST DO - classic)
- 542: 01 Matrix ⭐⭐⭐ (MUST DO)
- 1162: As Far from Land as Possible
- 1765: Map of Highest Peak
- 286: Walls and Gates (Premium)


PATTERN 5: GRID BFS
═══════════════════════════════════════
Medium:
- 1091: Shortest Path in Binary Matrix ⭐⭐⭐ (MUST DO)
- 542: 01 Matrix (also multi-source)
- 994: Rotting Oranges (also multi-source)
- 1162: As Far from Land as Possible
- 1926: Nearest Exit from Entrance in Maze


PATTERN 6: SHORTEST PATH
═══════════════════════════════════════
Medium:
- 1091: Shortest Path in Binary Matrix ⭐⭐⭐
- 752: Open the Lock ⭐⭐⭐
- 863: All Nodes Distance K in Binary Tree ⭐⭐

Hard:
- 127: Word Ladder ⭐⭐⭐ (Classic, must know)
- 126: Word Ladder II
- 1293: Shortest Path with Obstacles Elimination


PATTERN 3: DISCONNECTED COMPONENTS
═══════════════════════════════════════
Medium:
- 547: Number of Provinces ⭐⭐⭐ (MUST DO)
- 323: Number of Connected Components (Premium)


COMBINED PATTERNS (Grid + Multi-source + Shortest Path)
═══════════════════════════════════════
These are the MOST important for interviews:
- 994: Rotting Oranges ⭐⭐⭐
- 542: 01 Matrix ⭐⭐⭐
- 1091: Shortest Path in Binary Matrix ⭐⭐⭐
- 1162: As Far from Land as Possible


═══════════════════════════════════════════════════════════════════
PRIORITY ORDER (DO THESE FIRST):
═══════════════════════════════════════════════════════════════════

WEEK 1 - FOUNDATIONS:
1. 102: Binary Tree Level Order Traversal (easiest BFS)
2. 111: Minimum Depth (BFS is better than DFS!)
3. 199: Binary Tree Right Side View (level tracking)
4. 547: Number of Provinces (disconnected)

WEEK 2 - GRID BFS:
5. 733: Flood Fill (start with DFS/BFS choice)
6. 994: Rotting Oranges ⭐⭐⭐ (CRITICAL - multi-source grid)
7. 542: 01 Matrix ⭐⭐⭐ (CRITICAL - multi-source)
8. 1091: Shortest Path in Binary Matrix ⭐⭐⭐ (CRITICAL)

WEEK 3 - SHORTEST PATH:
9. 752: Open the Lock (state space)
10. 127: Word Ladder (hard but classic)
11. 863: All Nodes Distance K (tree BFS)

WEEK 4 - ADVANCED:
12. 1293: Shortest Path with Obstacles (BFS with state)
13. Review all patterns
14. Mock interviews


TOP 10 MUST-DO BFS PROBLEMS:
═══════════════════════════════════════
1. 102: Binary Tree Level Order Traversal
2. 994: Rotting Oranges (multi-source + grid)
3. 542: 01 Matrix (multi-source + grid)
4. 1091: Shortest Path in Binary Matrix
5. 547: Number of Provinces
6. 199: Binary Tree Right Side View
7. 752: Open the Lock
8. 127: Word Ladder (hard but important)
9. 111: Minimum Depth
10. 863: All Nodes Distance K in Binary Tree

Master these 10 and you'll ace 90% of BFS interviews! 🚀
"""


# ═══════════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════════

def test_bfs_patterns():
    """Test all BFS patterns"""
    
    print("Testing BFS Patterns...\n")
    
    # Test Pattern 1: Basic BFS
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2]
    }
    patterns = BFSPatterns()
    result = patterns.bfs_basic(graph, 0)
    print(f"Pattern 1 - Basic BFS: {result}")
    assert len(result) == 5
    print("✅ Pattern 1 passed\n")
    
    # Test Pattern 2: BFS with levels
    levels = patterns.bfs_with_levels(graph, 0)
    print(f"Pattern 2 - BFS with Levels: {levels}")
    assert len(levels) == 3  # 3 levels
    print("✅ Pattern 2 passed\n")
    
    # Test Pattern 4: Multi-source BFS
    distances = patterns.multi_source_bfs(graph, [0, 4])
    print(f"Pattern 4 - Multi-source BFS: {distances}")
    print("✅ Pattern 4 passed\n")
    
    # Test Pattern 6: Shortest path
    dist = patterns.shortest_path(graph, 0, 4)
    print(f"Pattern 6 - Shortest Path (0 to 4): {dist}")
    assert dist == 2
    print("✅ Pattern 6 passed\n")
    
    # Test Solution: Rotting Oranges
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    sol = Solution()
    minutes = sol.orangesRotting(grid)
    print(f"Rotting Oranges: {minutes} minutes")
    assert minutes == 4
    print("✅ Rotting Oranges passed\n")
    
    print("🎉 All BFS tests passed!")


if __name__ == "__main__":
    test_bfs_patterns()