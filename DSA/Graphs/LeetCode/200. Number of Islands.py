class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Pattern: traversal of disconnected components, they are just asking total num of disconnected componenets.
        """

        def bfs(row,col):

            q = deque([(row,col)])
            visited.add((row,col))
            directions  = [(1,0),(-1,0),(0,1),(0,-1)] # R L T B 
            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc

                    # if its is out of boundary, if yes skip to next dir
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue 
                    
                    # if its a water then also continue, skip it
                    if grid[nr][nc] == "0":
                        continue
                    
                    #else we on the land we add it to queue and also check ifs prev not visited:
                    if (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                
        def dfs(r,c):
            grid[r][c] = "0"

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                #out of bounds
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                
                # if its a water then also continue, skip it
                if grid[nr][nc] == "0":
                    continue
                
                # else that means we are on land so we do dfs, here no need to check visited
                dfs(nr,nc)

        #methid 2 modifying the input
        rows = len(grid)
        cols = len(grid[0])
        directions  = [(1,0),(-1,0),(0,1),(0,-1)] # R L T B 
        # visited = set() no need of set
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        return islands


     
    #  #methiod 1 using set 
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     visited = set()
    #     islands = 0
    #     for r in range(rows):
    #         for c in range(cols):
    #             if (r,c) not in visited and grid[r][c] == "1":
    #                 islands += 1
    #                 # bfs(r,c)
    #     return islands
        
 
