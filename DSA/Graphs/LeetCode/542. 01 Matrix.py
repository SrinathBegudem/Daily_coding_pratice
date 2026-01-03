class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        THe intuition here is just build a negative distance matrix
        - This sum is similar to rotten oranges 
        - we add all zeors to the source and start traverse and bfs outwards
        - the closest node will reach the 1 first and it will be updated first before any other large distancen node comes
        - -1 are used as visited set here 
        """
        rows,cols = len(mat),len(mat[0])
        #created a disatnce output matrix with all 0 so we can avoid set
        distance = [[-1]*cols for _ in range(rows)]

        #step1 : lets add all the zeros to queue and also parellely we can update the 0 posiiton in distance matrix to zeors 
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    # add the 0's to queue to bfs outwards
                    q.append((r,c))
                    distance[r][c] = 0 # udpate the distance matrix 0 node to zero so it servers as visited node
        

        #step2: do multi source bfs like rotten oranges outwards
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()

            for dr,dc in directions:
                nr,nc = r + dr, c + dc

                # #case 1: if out of bounds skip 
                # if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                #     continue
                # if distance[nr][nc] != -1 or distance[nr][nc] == 0 :
                #     continue # since its already visited 
                
                # #now if disstance[nr][nc] == -1 unvisted then we udpdate the distance
                # distance[nr][nc] = distance[r][c] + 1 #make sure of nr,nc in lhs and r,c in rhs. r,c is always visited since it is popped from queue
                # #now add nr nc to queue 
                # q.append((nr,nc))
                
                # or simply 
                # if in bounds and not visited then add distance
                if 0 <= nr < rows and 0 <= nc < cols and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1  #make sure of nr,nc in lhs and r,c in rhs. r,c is always visited since it is popped from queue
                # #now add nr nc to queue 
                    q.append((nr,nc))
        return distance
                
                
                



        
        




        