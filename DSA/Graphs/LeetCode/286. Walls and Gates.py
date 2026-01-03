class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
       
       
       
        # i would be doign the shortest part multi source bfs, this solution dont really
        # need visitd set

        rows = len(rooms)
        cols = len(rooms[0])
        q = deque() #r,c,dist
        INF = 2147483647

        # add all gates to the queue 
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c,0))

        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # multu source bfs 
        while q:
            r,c,dist = q.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                #out of bounds, skip
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                #if obstacle, skip that cell
                if rooms[nr][nc] == -1:
                    continue
                
                # we dont need visited as this check acts visited and only updateds the inf block which are not visited
                if rooms[nr][nc] == INF:
                    # increase the distance + 1 and add it to the rooms
                    rooms[nr][nc] = dist + 1
                    q.append((nr,nc,dist+1))
        
       
       
       # non optimal
        # i would be doign the shortest part multi source bfs 

        rows = len(rooms)
        cols = len(rooms[0])
        q = deque() #r,c,dist
        visited = set()

        # add all gates to the queue 
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))

        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # multu source bfs 
        while q:
            r,c,dist = q.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                #out of bounds, skip
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                #if obstacle, skip that cell
                if rooms[nr][nc] == -1:
                    continue
                
                # check if the cur cell is not viisted, if not proceed, since we added all the gates to visited, we don need to explicity check the gate cond
                if (nr,nc) not in visited:
                    # increase the distance + 1 and add it to the rooms
                    rooms[nr][nc] = dist + 1
                    q.append((nr,nc,dist+1))
                    visited.add((nr,nc))
        
                



            
        


                
        

        
        