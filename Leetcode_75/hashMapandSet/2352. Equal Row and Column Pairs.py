class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid) # len of rows
        m = len(grid[0]) # len of cols 
        col_count = dict()

        #extarct cols and store it in separate set
        for c in range(m):
            cur_col = list()
            for r in range(n):
                cur_col.append(grid[r][c])
            cur_col = tuple(cur_col)
            col_count[cur_col] = col_count.get(cur_col,0) + 1
        #traverse rows and check if they are prsent in cols set
        pairs = 0
        for r in range(n):
            if tuple(grid[r]) in col_count:
                pairs += col_count[tuple(grid[r])]
        
        return pairs



            

        