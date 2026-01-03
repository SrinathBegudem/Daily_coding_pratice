class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Pattern: knapsack
        The intuition here is we are not given something like capcity here like knapscap
        - we have to derive it 
        - given if sum(subset1) == sum(subset2) : return true # cond1 
        - the above can ne written as sum(subset1) + sum(subset2) = sum(total) ( because if there exisit ans then the whole arr is divided into 2 parts and both parts sum should = sum(total)) cond2
        - from cond1 and cond2 2(subset) = total - > subset = total/2 
        - now we just have to find if there is any subset that will be equal to total/2, if yes then we found out the 2 equal partition subsets
        """
        # cal the total sum
        total = sum(nums)
        # if the total is odd return false never possible 
        if total % 2 != 0:
            return False
        
        #if its even there is a chance there exists and answer
        target = total//2
        n = len(nums)

        def recursive_sol(i,rem):

            #base cases1: if target is found return true
            if rem == 0:
                return True
            #base case2: after checking the whole arr res not found
            if i == 0:
                return False
            
            #skip: if num is greater than target or skipping this res might give ans 
            if recursive_sol(i-1,rem):
                return True
            
            #take: if conisder the num might lead to the res
            # if cur num is less than or eq  rem 
            if nums[i-1] <= rem:
                #check if considering it might give ans 
                if recursive_sol(i-1,rem-nums[i-1]):
                    return True
            
            #after evaluting both conditions ans is not found then probably its not there and not possible
            return False
            
            # other way of writing the above code.
            # #base cases1: if target is found return true
            # if rem == 0:
            #     return True
            # #base case2: after checking the whole arr res not found
            # if i == 0:
            #     return False

            # #skip or take 
            # return recursive_sol(i-1,target) or (nums[i-1] <= rem and recursive_sol(i-1,rem-nums[i-1]))
        # return recursive_sol(n,target)



        def memo_dp():
            """
            From rules of memoization, the state which is overlapping or repeating should be the key of the memo.
            - so what are variables are changing ?? 
            - the no of items are changing and the rem is changing 
            - so our key should be (i,rem), in recursion depths this calls may be overlapping or being cal again and again 
            strucutre 
            - base cases 
            - check in cache 
            - recursion 
            - store in cache 
            - return 
            Memo stores whether it is possible to form sum rem using first i elements.
            It does NOT store paths. It stores truth of existence.
            """
            memo = dict()

            def solve(i,rem):
                #base cases 
                if rem == 0: return True #found subsets
                if i == 0: return False #if there are no elements return false

                #check in cache
                if (i,rem) in memo:
                    return memo[(i,rem)]
                
                if solve(i-1,rem):
                    #store in memo before any return statement
                    memo[(i, rem)] = True
                    return True
                
                if nums[i-1] <= rem:
                    if solve(i-1,rem-nums[i-1]):
                        #store in memo before any return statements 
                        memo[(i, rem)] = True
                        return True
                #store in memo before any retrun statements 
                memo[(i, rem)] = False
                return False
            return solve(n,target)
        # return memo_dp()

        def tabular_dp():

            # intialise dp table
            # dp[i][s] = True if we can form sum s using first i numbers 
            dp = [[False] *(target+1) for _ in range(n+1)]
            #base case sum 0 is always possible (cols is target s0 cols 0 which is target 0 should be true)
            for i in range(n+1):
                dp[i][0] = True


            for i in range(1,n+1):
                for rem in range(1,target+1):

                    #skip it
                    dp[i][rem] = dp[i-1][rem]

                    #take it if it fits
                    if nums[i-1] <= rem:
                        dp[i][rem] = dp[i][rem] or dp[i-1][rem-nums[i-1]]
                    
            # final answer = original problem state
            return dp[n][target]
        return tabular_dp()

                    

                


