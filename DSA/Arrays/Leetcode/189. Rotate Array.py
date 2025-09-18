class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #edge case: k can go over the len of nums so stop it we mod the k by le nof nums 
        def reverse_arr(arr):
            """
            In place reverse of given arr 
            """
            # i = 0 
            # j = len(arr) -1 
            # while i < j:
            #     arr[i],arr[j] = arr[j],arr[i]
            #     i += 1
            #     j -= 1
            # return arr

        # n = len(nums)
        # k = (n-k) % n # its because of how we intialize the k 

        # nums[:k] = reverse_arr(nums[:k]) # reverse first k
        # nums[k:] = reverse_arr(nums[k:]) # REVERSE THE REST
        # reverse_arr(nums)      #reverse all 

        #chatgpt sol v:: this is completey diff from abve
        def rev(arr,i,j):
            while i < j:
                arr[i],arr[j] = arr[j],arr[i]
                i +=1
                j -=1 
        n = len(nums)
        k = k % n
        rev(nums,0,n-1) # reverse all 
        rev(nums,0,k-1) # reverse first k 
        rev(nums,k,n-1) # reverse the rest
