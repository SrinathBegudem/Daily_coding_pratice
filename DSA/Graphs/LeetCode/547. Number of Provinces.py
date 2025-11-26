from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        pattern : bfs/dfs of diconnected graphs 
        The key idea:
        - start with each vertex and traverse the whole graphs increase 
        - increase count for every new disconneted graphs
        - return the count, that is eq to num of provinces
        So simple intuition 
        - increase count when ever dfs/bfs function is called, just makes sure to increase if and only if the vertex is not invisited set

        The key prblm
        - i solve it using grid methiod but this is not grid problem we 
        are given an ajacency matrix where r,c = (1,2) = (2,1)
        You treated the input isConnected as if it were a grid/maze, so you did:

        (i, j)  → treat as a cell position
        neighbors = (i±1, j±1)


        But this problem is NOT a grid traversal problem.

        ✔️ isConnected is an adjacency matrix of a graph, where:

        Each row i represents city i

        Each column j represents if city i is directly connected to j

        isConnected[i][j] = 1 means city i and city j are neighbors

        isConnected[i][j] = isConnected[j][i] because it’s undirected



Correct BFS/DFS logic:
- For each city `i`:
    - If it's not visited:
        - Run BFS/DFS on that node
        - Traverse all cities `j` where `isConnected[i][j] == 1`
        - Mark them visited
        - Increment province count

Important:
❌ Do NOT treat (i, j) as a grid cell.
❌ Do NOT use directions like (±1, 0) or (0, ±1).

You must:
✔️ Traverse neighbors based on row entries in the adjacency matrix.
✔️ Use either adjacency list or directly BFS on the matrix row.
        """

        def bfs(city):
            q = deque([city])
            while q:
                cur = q.popleft()
                for nei in range(n):
                    if isConnected[cur][nei] == 1 and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        
        def dfs(city):
            for nei in range(n):
                 if isConnected[city][nei] == 1 and nei not in visited:
                        visited.add(nei)
                        dfs(nei)




        #key idea is rows = cities and cols = conenctions
        n = len(isConnected) #no of cities
        visited = set() # to add the cities we already visited
        provinces = 0 # res 
        for city in range(n):
            # if city is not visited visit the city and its neighbours 
            if city not in visited:
                provinces += 1
                visited.add(city)
                # bfs(city)
                dfs(city)
        return provinces































        # wrong sol 
        # def bfs(r,c):
        #     directions = [(-1,0),(1,0),(0,-1),(0,1)]
        #     q = deque([(r,c)])
        #     for dr,dc in directions:
        #         nr,nc = (r+dr,c+dc)
        #         # if out of bounds continue
        #         if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        #             continue
        #         # if cur cell is not eq 1 
        #         if isConnected[i][j] == 0:
        #             continue
        #         if (nr,nc) not in visited:
        #             visited.add((nr,nc))
        #             q.append((nr,nc))
                

        

        # visited = set()
        # rows = len(isConnected)
        # cols = len(isConnected)
        # count = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         if (i,j) not in visited and isConnected[i][j] == 1:
        #             #increase count when ever a new disconnected graph is found               
        #             count += 1
        #             visited.add((i,j))
        #             bfs(i,j)
        # return count


        