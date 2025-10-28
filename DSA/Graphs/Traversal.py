from collections import deque
"""
There are two main graph traversals 
1) breadth for search (bfs) (a.k.a graphs level order traversal)
    - Traverse/search the neighbours first
2)

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
"""

class GraphTraversal:
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: CLASSIC BFS (Level-by-Level Traversal)
    # ═══════════════════════════════════════════════════════════════════════

    def bfs(self,graph, start):
        """
        key points
        - have a deque (queue) to do bfs
        - have a set to check if then node is already visited
        - res var to print out the order
        -include nieghbours loop check if its not already visit 
        - then immediately add the node to visited and append its neighbours to q
        Key points:
        1. Mark as visited WHEN ADDING to queue (not when processing)
        2. No need for visited check after popleft
        3. Check if neighbor visited before adding
        """
        #variable intialization 
        q = deque([start]) # add the first node to the queue
        visited = set() #to keep track of node that are already visited
        visited.add([start]) # mark the start node as already visited
        res = [] # to hold the order of the bfs

        while q: #run the while loop until no elements left inside the q
            node = q.popleft() # pop the starting indx of q
            res.append(node) # immediately add it to the res

            #add neighbours
            for neighbour in graph[node]:
                #check if the nieghbour is not already visited 
                if neighbour not in visited:
                    visited.add(neighbour) # add the neighbour to visited set
                    q.append(neighbour) # add it to the queue 
        return res 
    

    def bfs_with_level(self,graph,start):
        """
        bfs to track levels, useful when you want to work with levels
        """
        q = deque([start])
        visited = set()
        visited.add(start)
        levels = []
        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append[node]
                for nieghbour in graph[node]:
                    if nieghbour not in visited:
                        visited.add(nieghbour)
                        q.append(nieghbour)
            levels.append(level)
        return levels






