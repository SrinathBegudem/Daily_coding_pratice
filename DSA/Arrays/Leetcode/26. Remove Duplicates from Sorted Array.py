class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # i  = 1 
        # while i < n:
        #     while nums[i-1] 
        k = 1
        for i in range(1,n):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k
        
            


