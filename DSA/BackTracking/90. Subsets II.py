class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        We will do the same subset 78 problem but in this we have duplciated, so remeber to be easy for this problem we should alsways do keep it first and then skip it next.
        """ 
        # for both permutations and subset duplciates we need to sort at the begging 
        nums.sort()
        n = len(nums)
        res = []
        path = []

        def backtrack(i):
            if i == n:
                res.append(path[:])
                return 
            
            # case 1 keep the nums[i]
            path.append(nums[i])
            backtrack(i+1)
            path.pop()

            #skip the nums[i] and skip the duplicates
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            # case 2 after skipping duplicates we skip the num
            backtrack(i+1)
        backtrack(0)
        return res

        