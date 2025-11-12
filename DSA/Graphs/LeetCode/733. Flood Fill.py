from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        def iter_sol():
            rows = len(image) 
            cols = len(image[0])
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            initial_color = image[sr][sc]
            q = deque([(sr,sc)]) 
            
            # important and base case: if you miss this case in recur or iter it will loop infinetly
            if initial_color == color: return image # if start col and given col is same return
            while q:
                r,c = q.popleft() 
                if r < 0 or r >= rows or c < 0 or c >= cols: # if out of boundaries skip to next loop
                    continue 
                if image[r][c] != initial_color:# if not eq to the start col skip to next iteration
                    continue
                image[r][c] = color # once found change the colot 
                for dr,dc in directions: # add all the aja sides to the queue bfs
                    nr,nc = (r+dr,c+dc)
                    q.append((nr,nc))
            return image
        return iter_sol()
                

        def recur_sol():

            rows = len(image) 
            cols = len(image[0])
            directions = [(1,0),(-1,0),(0,1),(0,-1)] #R L U D 
            # visited = set() we dont need this because once we change the val of cur cell we will never visit it again because of base condition.
            intial_col = image[sr][sc] # this is to store intial colour 

            #mandatory base condition to avoid infinite recursion 
            if intial_col == color:
                return image
            def dfs(r,c):

                if r < 0 or r >= rows or  c < 0 or c >= cols or image[r][c] != intial_col: # here we check if the cur cell is not eq to intial color we return so this is how we never visit the already changed color cell so we dont need visited set 
                    return
                image[r][c] = color # Change the cur cell color to given color 
                for dr,dc in directions:
                    nr,nc = (r+dr,c+dc)
                    # if (nr,nc) not in visited:
                        # visited.add((nr,nc))
                    dfs(nr,nc)
            dfs(sr,sc)
            return image


            