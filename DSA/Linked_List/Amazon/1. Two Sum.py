class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def brute_sol(nums,target):
            n = len(nums)
            for i in range(n):
                for j in range(i+1,n):
                    if nums[i]+nums[j] == target:
                        return [i,j]
        #     return False
        # return brute_sol(nums,target)

        def optimal_sol(nums,target):
            hash_map = {}
            for i,num in enumerate(nums):
                check = target-num
                if check in hash_map:
                    return [i,hash_map[check]]
                hash_map[num] = i 
            return False
        return optimal_sol(nums,target)

# [2,7,11,15]
# -> {}, i = 0, num=2, check = 9-2=7 ,{2:0}
# -> {2:0}, i = 1, num=7, check = 9-7=2,found , return [1,0] 

# [2,-7,11,15] , target = 4
# {2:0}
# {2:0,7:1}




        