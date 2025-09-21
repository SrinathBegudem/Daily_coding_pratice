class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0 
        right = len(nums) - 1
        while left < right:
            # check if the cur num is in its right posiito 
            # check if even in left 
            if nums[left]%2 == 0:
                #then increase the pointer to +1 because it is in right positoon
                left += 1
            elif nums[right]%2 == 1:
            #the odd num is in coorect position 
                right -= 1
            else:
                #swap both num because both are in opp direction 
                nums[left],nums[right] = nums[right], nums[left]
        return nums
 
            
            

        