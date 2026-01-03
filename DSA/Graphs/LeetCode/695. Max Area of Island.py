class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Pattern: disconnected graphs find the max area 
        we can etiher solve this usign a visited set or we can directily change the input without visited set
        - if using visited set make sure you chek the cur state doesnt be in the visited set.
        -  will proceed with modifying the input 
        """

        def bfs(row,col):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            q = deque([(row,col)])
            grid[row][col] = 0 # just like maeking visited in a set
            area = 0

            while q:
                r,c = q.popleft()
                area += 1

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    #out of bound, skip 
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    # if water, skip
                    if grid[nr][nc] == 0:
                        continue
                    
                    #else we are in the land add it to the queue
                    q.append((nr,nc))
                    grid[nr][nc] = 0 # marks that cur cell as visited 
            return area
        def dfs(r,c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] == 0:
                return 0
            

            grid[r][c] = 0
            area = 1
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                area += dfs(nr,nc)
        
            return area

            

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur_area = dfs(r,c)
                    max_area = max(max_area,cur_area)

        return max_area

    
        