class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the main imp point here is it start from i = j = 0 so if num is not zero both the i and j swap with the same places so the relative order stays the same, the mistake i was doing is start j from 1 which swaps the non zeros and distorts the relative order.
        # code for while loop 
        # i = 0 
        # j = 0
        n = len(nums)
        # while j < n:
        #     if nums[j] != 0:
        #         nums[j],nums[i] = nums[i],nums[j]
        #         i += 1
        #     j += 1
        
        # code for for loop 
        k = 0 
        for l in range(n):
           if nums[l] != 0:
                nums[k],nums[l] = nums[l],nums[k]
                k += 1
        
        