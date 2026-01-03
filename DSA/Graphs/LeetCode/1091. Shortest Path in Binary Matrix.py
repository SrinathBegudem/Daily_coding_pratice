class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        The key idea here is to use bfs with dist calculation 
        - to do bfs for each node i will append all its nei in all 8 directions and track distance level by level
        - the target node will be on len(rows) - 1 and len(cols) - 1 
        """
        rows = len(grid)
        cols = len(grid[0])
        # key base case if the grid starting nodee is itself 1 there will not be any clear path and if the ending psoition is 1 then directly return the ans 
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1: return -1

        # R L T B Q1 Q2 Q3 Q4 
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1) , (-1,1), (-1,-1),(1,-1)]
        target = (rows-1,cols-1)
        # start = (0,0)
        # dist = 1
        q = deque([(0,0,1)])# 3 ele r,c,dist
        # visited = set()
        # visited.add()
        grid[0][0] = 1
        while q:
            r,c,d = q.popleft()
            # if target foudn return the distance 
            if (r,c) == target:
                return d
            for dr,dc in directions:
                nr,nc = r+dr, c+dc 

                # if they nr,nc is out of bound skip
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue 
                
                # if the nei is not 0 then also skip 
                if grid[nr][nc] == 1:
                    continue

                # if the nei is 0 then it can be shorest clear path
                q.append((nr,nc,d+1))
                # turn the visited cells to visited by changing its val to 1
                grid[nr][nc] = 1
        #if not found clear path return -1 
        return -1 


                