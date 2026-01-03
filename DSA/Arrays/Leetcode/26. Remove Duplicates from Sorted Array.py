class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    # remove dulicates pattern
    # def removeDuplicates(nums, k):
    # index = 0
    
    # for num in nums:
    #     if index < k or num != nums[index - k]:
    #         nums[index] = num
    #         index += 1
    
    # return index
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
        
            


