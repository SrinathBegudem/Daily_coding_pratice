class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        We are going to solve this with recursive backtracking, so we take processed and unprocessd and for every node we have 2 choices ( so if we have more than 2 choices then its permutation sum because there we use for loop for all choices just for inution)
        in that 2 choices either to take the num or skip it. if you take it then backtrack and pop it.
        """
        n = len(nums)
        res = []
        sol = []

        # def backtrack(i):
        #     if i == n:
        #         res.append(sol[:])
        #         return
            
        #     #we skip the num 
        #     backtrack(i+1)

        #     #we keep the number
        #     sol.append(nums[i]) 
        #     backtrack(i+1)
        #     sol.pop()
        # backtrack(0)
        # return res

        # do this first we consider num and then we skip it, because it will be easy for the subset 2 duplciate problem
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            #we keep the number
            sol.append(nums[i]) 
            backtrack(i+1)
            sol.pop()

            #we skip the num 
            backtrack(i+1)
        backtrack(0)
        return res
        