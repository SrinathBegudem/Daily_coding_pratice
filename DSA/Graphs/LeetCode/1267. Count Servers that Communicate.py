class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        the key idea is have 
        - the preprocessing step would be to traverse and build below arrs
        - row_cnt which stores no of server present in particular row
        - col_cnt which store no of serer in that particular col 
        
        - once we have row count and col count arr 
        - we traverse the arr again and check 
        - if the crct grid is a server, if yes 
        - check the for that particular row servers > 1 if yes they can comunicate even if they are not adjacent
        - or check if col have server great than 1 
        - if any of above condition is true we can add +1 to res
        """
        rows = len(grid)
        cols = len(grid[0])
        row_cnt = [0] * rows 
        col_cnt = [0] * cols 

        # preprocessing 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_cnt[r] += 1 #increase the row count
                    col_cnt[c] += 1 #increase the col count
        #once the array is build we traverse again to check and count res
        res = 0 
        for r in range(rows):
            for c in range(cols):
                # check if is server and Two servers are said to communicate if they are on the same row or on the same column.
                if grid[r][c] and (row_cnt[r]>1 or col_cnt[c]>1):
                    res += 1
        return res