class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        The intuition here is 
        - we main res, inc, dec var to track
        - if the order is inc we inc the count of inc and dec will be reset 1
        - simialr for dec 
        - when both num are eq its not inc and not dec so we rset both counters to 1
        """
        res = 1
        inc = 1
        dec = 1
        for i in range(1,len(nums)):
            # count the inc subarray
            if nums[i-1] < nums[i]:
                inc += 1
                dec = 1
            # count the dec subarray
            elif nums[i-1] > nums[i]:
                dec += 1
                inc = 1
            #when both nums ar eeq reset the vars
            else:
                inc = dec = 1
            res = max(res,inc,dec)
        return res


    


                

                
        