class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        The intution here is 
        - have max_var to count max 
        - have cur_max to keep track of the cur_max
        - increase count of cur_max when ever we encounter a consective one 
        - if the streak break set the max_val to max(max_val,cur_val)
        - And set the cur_max to zero
        - the key point here is in second snippet if we udpate the max insde the first if loop it throws error and misses the last index one to update to max. so always update max after both if else statement.
        -time = o(n)
        -space = o(1)
        """
        max_val = 0
        cur_max = 0
        for num in nums:
            if num == 1:
                cur_max += 1
                max_val = max(max_val,cur_max)
            else:
                cur_max = 0
        return max_val

        #second snippet 
        # for num in nums:
        #     if num == 0:
        #         cur_max = 0
        #         max_val = max(max_val,cur_max) # wrong misses also index max update 
        #     else:
        #         cur_max += 1
        #     max_val = max(max_val,cur_max)
        # return max_val

        