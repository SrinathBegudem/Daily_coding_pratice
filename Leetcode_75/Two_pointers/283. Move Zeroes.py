class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this problem can be solved by two pointers
        # i pointer starts with 0 index 
        # this swaps the existing zeros to the end
        i = 0
        for j in range(len(nums)):
            #when ever we encoutner a num which is non zero we swap with i and icnrease i
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        
            


        