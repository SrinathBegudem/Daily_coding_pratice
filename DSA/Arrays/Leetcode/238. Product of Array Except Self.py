class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.optimal_sol(nums)
    def optimal_sol(self,nums):# time = o(n) and space = o(1)
        """
        The goal of this sum is to place the prefix multiplication on the cur indx of the result arr so we can skip mutiplying the cur_indx and when we mutiply postfix we can do it with one single variable mutilplying it in opp direction to get the product from right to left and in prefix multi we store the product from left to right in indx +1 position so in that way we can skip the mutiplication of self and preserve the previously mutiplied num in the right position.
        """
        n = len(nums)
        result = [1]*n
        # here i am doing prefix mutilplication and storing it in the result variable (prefix from left to right of the array)
        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1] # we want the result[0] == 1 so we start from indx 1 and we dont care about n-1 ind
        # the above return for ex 1 [1,1,2,6] we store the prefix mult till indx n-1
        # now lets mutiply it with postfix
        postfix = 1 # that means the last indx + 1 should always be one by logic coz there is no more num to right side of it 
        # we need to traverse reverse and mutiply it with the prefix result arr and parellely modify the array \
        for i in range(n-1,-1,-1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
        return result
    
    def good_sol(self,nums):# time = space = o(n)
        """
        This is just optimal sol but in less complex way by using the space to store both post and prefix multiplications
        """
        # the key is to keep the prefix[0] == 1 and postfix[n-1] ==1, we need to keep prefix 0 th indx and postfix n-1 indx ==1
        n = len(nums)
        result = [1]*n
        prefix_multi = [1] * n
        for i in range(1,n):
            prefix_multi[i] = prefix_multi[i-1] * nums[i-1]
        postfix_multi = [1] * n
        for i in range(n-2,-1,-1):
            postfix_multi[i] = postfix_multi[i+1] * nums[i+1]
        for i in range(n):
            result[i] = prefix_multi[i] * postfix_multi[i]
        return result
# dry run 
# lets take ex1 nums = [1,2,3,4]
# our prefix_multi = [1,1,2,6]
# our postfix_multi = [24,12,4,1]
#our result  = [24,12,8,6] pre*post





        
        

            
        