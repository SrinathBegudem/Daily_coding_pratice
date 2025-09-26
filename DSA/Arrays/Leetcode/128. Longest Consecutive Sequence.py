class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.linear_time_sol(nums)
    
    def n_sqaure_sol(self,nums):
        seen = set()
        result = 0
        for num in nums:
            seen.add(num)
        for i in range(len(nums)):
            # if result > len(nums)// 2 + 1:
            #     return result
            cur_result = 0
            num = nums[i]
            while num in seen:
                cur_result += 1
                num = num - 1
            result = max(result, cur_result)
        return result
    def sorting_sol(self,nums):
        # solve again 
            
    def linear_time_sol(self,nums):

        seen = set(nums)
        longest = 0
        for num in seen:
            if num-1 not in seen:
                current = num
                streak = 1

                while current+1 in seen:
                    current += 1
                    streak += 1
                longest = max(streak,longest)
        return longest









            



                
        