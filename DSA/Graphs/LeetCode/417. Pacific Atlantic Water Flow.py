class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        We start from all edge rows and start our traversal inwards and find out all the possible cells that can reach the pacfic and alantic ocean and return the common elemtns. so now we once traverse twice for both the oceans bring down our time complexity to o(m*n)
        """
        def dfs(r,c,seen):
            seen.add((r,c))

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:

                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr,nc,seen)

        pac = set()
        atl = set() 
        rows = len(heights)
        cols = len(heights[0])    
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # Pacific borders: top row + left col
        for c in range(cols):
            dfs(0, c, pac)
        for r in range(rows):
            dfs(r, 0, pac)

        # Atlantic borders: bottom row + right col
        for c in range(cols):
            dfs(rows - 1, c, atl)
        for r in range(rows):
            dfs(r, cols - 1, atl)     

                
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res









        # #multi source bfs from all the edge rows for both pacific and atlantic
        # def bfs(starts):
        #     q = deque(starts)
        #     seen = set(starts)

        #     while q:
        #         r,c = q.popleft()
        #         for dr,dc in directions:
        #             nr,nc = r+dr,c+dc
        #             #in bounds 
        #             if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
        #                 #if reverse heigh check 
        #                 if heights[nr][nc] >= heights[r][c]:
        #                     q.append((nr,nc))
        #                     seen.add((nr,nc))
        #     return seen    

        # rows = len(heights)
        # cols = len(heights[0])
        # directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # pacific_rows = [(0,c) for c in range(cols)] + [(r,0) for r in range(rows)]
        # atlantic_rows = [(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(rows)]

        # pac = bfs(pacific_rows)
        # atl = bfs(atlantic_rows)

        # res = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r,c) in pac and (r,c) in atl:
        #             res.append([r,c])
        # return res










        # # non optimal solution time is o(n*m)^2 
        # def bfs(row,col):
        #     q = deque([(row,col)])
        #     visited = set()
        #     visited.add((row,col))
        #     directions = [(1,0),(-1,0),(0,1),(0,-1)]
        #     pacific = False
        #     atlantic = False
        #     while q:

        #         r,c = q.popleft()
        #         if pacific and atlantic: return True
                
        #         for dr,dc in directions:
        #             nr,nc = r+dr,c+dc

        #             #pacific cond
        #             if nr < 0 or nc < 0:
        #                 pacific = True
        #                 continue
        #             if nr >= rows or nc >= cols:
        #                 atlantic = True
        #                 continue
        #             if heights[nr][nc] <=  heights[r][c] and (nr,nc) not in visited:
        #                 q.append((nr,nc))
        #                 visited.add((nr,nc))
        #     return pacific and atlantic
                    
            
        
        # output = []
        # rows = len(heights)
        # cols = len(heights[0])
        # for r in range(rows):
        #     for c in range(cols):
        #         res = bfs(r,c)
        #         if res:
        #             output.append([r,c])
        # return output

        