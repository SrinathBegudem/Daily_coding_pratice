class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)] #L, R, D, U
        q = deque()
        # This is multi source bfs problem find all the rotten oranges and enque them first
        #step1 : Add all the rotten oranges into q
        fresh = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while q and fresh > 0: # this get rids of flag and minutes now will only increase if there are any fresh oranges covers the edges cases which requires flag in below sol 
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    # case1 : if nr and nc is out of bounds then skip
                    if nr >= rows or nc >= cols or nr < 0 or nc < 0:
                        continue
                    #case 2: if its empty cell or already rotten skip
                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    #case 3 : if its a fresh cell then we rot it 
                    grid[nr][nc] = 2
                    fresh -= 1 # we rotted on fresh orange 
                    q.append((nr,nc))

            #makes sure to icnrease the minutes after completeting on one compelte leveL (multi source bfs)
            minutes += 1
        
        #return if and only if all fresh oranges are rotten else false
        #think of edge case which have one rotten and one fresh but they are not connected the above while loop increase the minutes to 1 but this return check conditions checks is the fresh is rotten if not we simply return -1 which coveres that edge case
        return minutes if fresh == 0 else -1 


















# # my first try was jsut redoing the work the flag approch was brave just track fresh oranges to in the step 1 it self to aviod step 3 
#         #step1 : Add all the rotten oranges into q
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 2:
#                     q.append((r,c))

#         minutes = 0
#         # step2: do multi soruce bfs (may be level by level)
#         while q:
#             q_len = len(q)
#             flag = False # this is kept here to icrease minutes only if there if any rotting happening the edge cases.
#             for _ in range(q_len):
#                 r,c = q.popleft()

#                 for dr,dc in directions:
#                     nr,nc = (r+dr,c+dc)
#                     if nr >= rows or nc >= cols or nr < 0 or nc < 0 or grid[nr][nc] == 0 or grid[nr][nc] == 2:
#                         continue
#                     grid[nr][nc] = 2 # rotting the orange by changing the val
#                     q.append((nr,nc)) # adding it to queue to traverse its nei
#                     flag = True
#             if flag: minutes += 1
        
#         # step3: check if all the the fresh oranges rotted or not 
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     return -1
#         return minutes


