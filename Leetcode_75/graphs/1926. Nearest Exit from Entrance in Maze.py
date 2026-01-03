class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        The intuition here is simple 
        we used bfs and traverse level by level and add the distance
        key rule: bfs give the shortest possible distance as we traverse level by level
        - + is a wall so we dont append to queue 
        - - is a empty space we onl yadd this cells to the queue
        - so when we are in row start row or end row or in first col or last col we are at the borders then we need to return our steps 
        key edge case:
        entrance doesnt count as an exit
        """
        rows,cols = len(maze),len(maze[0])
        # create a queue and add the start point 
        q = deque([tuple(entrance)]) #deque expects a iterable so alwasy have those sqaure brackets
        start_element = True # to check the edge case for start != exit
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        steps = 0
        #mark the entrace as visited so it can never be bother us about the edge case where start == end then no exit
        maze[entrance[0]][entrance[1]] = "+"
        while q:
            #increase the steps at each level
            steps += 1
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r + dr, c + dc

                    #case1: if the nr,nc is out of bounds skip 
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    #case2: if there is a wall you cannot move that side so no adding to queue
                    if maze[nr][nc] == "+":
                        continue
                    
                    #case3:if its at the border returns steps, it's a valid exit (and not entrance, because entrance was marked '+')
                    if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1 ):
                        return steps 
                    
                    #now we covered all the cases if we still have the block(empty space) then its empty and need to added queue 
                    #cover the tracks either used visited set or put + on path you can so you wont traverse back
                    maze[nr][nc] = "+"
                    q.append((nr,nc))
                
        return -1




