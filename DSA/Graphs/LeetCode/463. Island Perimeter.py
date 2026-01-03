from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


        def iter_sol():
            """
            bfs
            - find the first r,c of land 
            - from there if there is a land on any side enqueue it to the queuue and add it to visited set
            - if its water or boundary we found our permiter add 1 
            its as simple as it is for bfs 
            -Time - o(rows*cols)
            -space - o(rows*cols)
            """
            def bfs(start_r,start_c):

                rows,cols = len(grid),len(grid[0])
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                q = deque([(start_r,start_c)])
                visited = set()
                visited.add((start_r,start_c))
                res = 0
                while q:
                    r,c = q.popleft()
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc

                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc]==0:
                            res += 1 

                        elif (nr,nc) not in visited:
                            visited.add((r+dr,c+dc))
                            q.append((r+dr,c+dc))
                return res 

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return bfs(i,j)
        return iter_sol()
                        
                    
                




        def recur_sol():
            """
            dfs
            The intuition here is 
            - If we reach the grid boundaries, we return 1 as its water outside
            - or if we reach the water inside the grid we return 1 
            - so the above is how we get the perimeter
            - if we reach land which we already visited simply retrun 0 
            key points 
            -find the firs land r,c because it doesnt make sense to travel all the r,c as the land is one 
            - and dont make a mistake of calling dfs(0,0) by looking example 1
            - because imagine a situition where if all 4 side including the (0,0) is water we never move to next grid
            - and if we use for loop and call on each r,c thats highly inefficeint and not needed
            - so find the first r,c with land and start dfs 
            - and perimeter is not global its local, we pass the values above 
            - think it through thats how we do cal inside recursion 
            - permimeter is intilised to 0 for every new land block found and build the val and return to top.

            Time and Space
            -Time - o(rows*cols)
            -space - o(rows*cols)
            """

            rows,cols = len(grid),len(grid[0])
            directions = [(0,-1),(0,1),(-1,0),(1,0)]
            visited = set()
            res = 0
            def dfs(r,c):
                #base conditions
                # if boundaries,outside the grid (its also water)
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    return 1
                # if water ( inside the grid)
                if grid[r][c] == 0: 
                    return 1
                #if already visited land
                if (r,c) in visited:
                    return 0

                visited.add((r,c))
                perimeter = 0

                for dr,dc in directions:
                        perimeter += dfs(dr+r,dc+c)
                
                return perimeter


            #find the first land cell and call the dfs
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return dfs(i,j)
            
                    
                    
                
            

# attempt 2 
# bfs 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # bfs(0,1)
        def bfs(row,col):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]  # R L U D 
            q = deque([(row,col)])
            visited = set()
            visited.add((row,col))
            perimeter = 0

            while q:

                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    # case 1: let me check if the nr, nc are out of bounds
                    if nr >= rows or nr < 0 or nc >= cols or nc < 0:
                        # from our concept we will add it to permiter if its out of bounds or water, that imples we are at the edge of the land that should be used for perimeter calculations
                        perimeter += 1
                        continue # skip to next iter 
                    
                    # case 2: if we encounter a water shore, we are at the edge of the lands we increase the perimeter
                    if grid[nr][nc] == 0:
                        perimeter += 1
                        continue # skip to next iter 

                    # check if the nr nc is not laready visited
                    if (nr,nc) not in visited:
                        # once both the above cases faield that means we encountered a land, we add it to the queue and dont increase the perimter
                        q.append((nr,nc))
                        #as add it to visited set
                        visited.add((nr,nc))
            return perimeter
                    






        
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                   return bfs(r,c)
                
        