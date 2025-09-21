class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = 0  
        odd = 1 
        while even < n and odd < n:
            # check if even index num is even, if move + 2 next even position and check 
            if nums[even] % 2 == 0:
                even += 2
            # check if odd index is odd, if yes move +2 for next odd positon we initalizes the odd from 1.
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                #both elements are in wrong positoon we swap
                nums[even],nums[odd] = nums[odd],nums[even]
        return nums


