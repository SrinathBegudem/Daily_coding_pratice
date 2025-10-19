class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        def optimal_sol():
            """
            The inutition here to move from right to left instead of left to right
            - we intially can have max_val = - 1
            - loop in reverse order
            - store the cur val 
            - and update that index with max_val
            - put if cond to check if the max_val can be update or stays same
            - time = o(n)
            -space = o(1)
            """
            max_val = -1 # since there is no negative val in arr -1 serves as min poss val
            for i in range(len(arr)-1,-1,-1):
                cur_val = arr[i]
                arr[i] = max_val
                if cur_val > max_val:
                    max_val = cur_val
            return arr

        def brute_force():
            """
            - the intuition here is to use nested loops and updated max_val = -1 for ever outer loop and find the max_val in right part with inner loop and then update the cur arr positio 
            - have outter for loop till n-1 
            - in outer for loop we have a max_val set to -1 after every iteration 
            - in inner for loop we traverse whole arr to find the max_val and update the max_val and exit the inner loop and update the arr at that cur index with max_val
            -at the end we update the last element of the arr with -1 
            -time - o(n^2) 
            -space - o(1)

            """
            n = len(arr)
            for i in range(n-1): # we traverse till last second elemnt so we dont have any out of bound index issues in inner loop
                max_val = -1
                for j in range(i+1,n):
                    max_val = max(max_val,arr[j])
                    #at the end of this loop we will have max val of right part of arr
                #UPDATE THE CUR POSITION INDEX to max_val
                arr[i] = max_val
            #set the last index to -1 
            arr[-1] = -1
            return arr
        return optimal_sol()
