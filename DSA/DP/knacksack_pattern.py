"""
What 0/1 Knapsack is:

You are given a bag with limited capacity.
Each item has a weight and a value.
You can either take an item once or skip it.
You want the maximum total value without exceeding the capacity.

In this example:

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

The best choice is taking items with weights 3 and 4, giving value 9.
"""


class Knapsack_patterns:

    """pure recursion, not yet DP. when we optimse this recursion calls
      the with cache and aviod repeated calling of function with same args 
      then its called dp. for dp always write the recursive solution first.
    """
    def Forward_RecursiveSol(self,weights,values,capacity):
        #this misses direct link to Dp, to convert recursion into dp directly
        #use reverse recursion.

        """
        Key rules for recursion:
        - what is the function we are trying to solve: solve(i,cap) this is
        the function that gives the best val using the items from index i 
        onwards with capacity cap.
        - Find the base case : when to not do nothing 
            - when i reaches the end of the arr(No elements left to solve) or 
            - when the cap becomes zero, no more space to add items
        - what are the choices: think what choices are avaible at this state
            Always draw choice diagram
            - choice 1: we skip it,may be skipping this gives better val
            - choice 2: we skip it, because the wieght of the cur val is more 
              than our storage capacity
            - choice 3: we take it, becuase it is under the storage capacity and
             may be gives the better vals
            if you look properly chocie 1 and 2 can be coded with same line
        - combines: how result result from coices are used
        - return type: return the best val like max(chocies) or min(choices)
        which are future used to combine step
        """
        n = len(weights)
        #function solve(i,cap)
        def solve(i,cap): #here i is index and in reverse recursion i means no of items


            #base case: if we are at the end of the arr or capacity is 0
            if i == n or cap == 0:
                return 0 

            #choices

            #choice 1 and 2: skip it, because its over wie or may be skipping the cur val gives the bestval
            skip = solve(i+1,cap) # we skipped it so the cap remains unchanged

            #choice 3: takeit, may be  taking it give you the best val
            take = 0 # edge case dry run to see, skip excutes till return statement
            #and skip gets 0 as assigned and if the last index wei is great than over bag limit 
            #if you dont assign the take = 0 then return statement max will be eval 
            #max(0,None) which is errror.

            if weights[i] <= cap: # if its fits in the bag
                # add the val and solve for the next call with reduced wie
                take = values[i] + solve(i+1,cap-weights[i])
            
            return max(skip,take) # return the best val for the cur state
            

        return solve(0,capacity)
    

    def Memo_DP_Sol(self,weights,values,capacity):
        """
        DP State — What It Actually Means
        - A DP state is the minimum set of variables needed to uniquely 
          identify a subproblem such that any two recursive calls with 
          the same state will always return the same answer.
        Nothing more. Nothing less.
        State = a subproblem.
        Memoization = store the result of that subproblem.
        we store the state because we dont have to solve the same subproblem 
        again and agian which leads to the same best val.


        - State is not just parameters.
        - State represents a situation where the future outcome is fixed.
        - If you reach the same state again, no matter how you got there, 
        the best answer from that point onward will be the same.
        - So instead of recomputing, we reuse it.
        -A DP state represents a situation in the problem such that 
        once you are in that situation, the best answer from there 
        onward is fixed, regardless of the path taken to reach it.
        - That is why memoization works.
        - One-line intuition (very important)
        - Same state → same future → same best answer.

        - How to identify the state (most important rule)
            - Ask this question:
            If two recursive calls have the same values for these 
            variables, will they always return the same result?
                - If yes → those variables form the state
                - If no → you are missing something

        - State is NOT random parameters
            - State variables are only the variables that:
                -describe where you are in the problem
                -describe what resources are left
                -State variables directly affect the answer.

        -What is NOT part of the state
            Do NOT include:
            - current result or accumulated value
            - temporary variables
            - loop counters
            - paths or lists being built
            - helper variables
            - If it does not define the remaining problem, it is not state.

        - Mental shortcut (works for most DP problems)
            State = position + remaining resources
            Examples:
            index + capacity
            index + remaining sum
            row + column
            step + moves left

        template:
        def solve(state):
            # 1. base case
            if base_condition:
                return base_value

            # 2. memo check
            if state in memo:
                return memo[state]

            # 3. compute result from smaller states
            result = combine(
                solve(next_state_1),
                solve(next_state_2),
                # ...
            )

            # 4. store and return
            memo[state] = result
            return result

        Simple code
        for recursion you need to add 2 more lines thats it 
        - base case 
        - look into cache right after the base case, if ans is present return
        - compute result from smaller states, explore your choices
        - one exploring the chocie is done at the best choice to the memo
        - always store in cache/memo before return 
        - return the res
        """
        memo = dict() #key will be the state (i,cap) : val will be the best val for that state
        n = len(weights)
        def solve(i,cap):

            #base condition:
            if i == n or cap == 0:
                return 0

            #check in cache, if we already explored this path
            if (i,cap) in memo:
                return memo[(i,cap)]

            #explore chocies 

            skip = solve(i+1,cap)

            take = 0
            if weights[i] <= cap:
                take = values[i] + solve(i+1,cap-weights[i])

            best = max(take,skip)
            #store the best res for that state in memo 
            memo[(i,cap)] = best

            #return the best
            return best

        return solve(0,capacity)
    
    #follow this for all sums from here
    # reverse_recurison
    def reverse_memo_dp(weights,capacity,values):
        n = len(weights)
        memo = {}  # key = (i, cap), value = best value for that state

        def solve(i, cap):
            # base case
            if i == 0 or cap == 0:
                return 0

            # memo check
            if (i, cap) in memo:
                return memo[(i, cap)]

            # skip the i-th item
            skip = solve(i - 1, cap)

            # take the i-th item if it fits
            take = 0
            if weights[i - 1] <= cap:
                take = values[i - 1] + solve(i - 1, cap - weights[i - 1])

            # store result for current state
            memo[(i, cap)] = max(skip, take)
            return memo[(i, cap)]

        return solve(n, capacity)

    #reverse recursion has direct link to dp
    #notes: In forward recursion, we start from index 0 and move forward.
    #In reverse recursion, we start with all items and reduce the problem size.
    def Reverse_RecursiveSol(self,weights,values,capacity):
        n = len(weights)

        def solve(i,cap): #here i is not index, its no of items avaible (n)
            if i == 0 or cap == 0: #when there are no items, then we return 0
                return 0
            
            #divided the problem into smaller parts
            #recuding the no of items = no_items - 1
            # skip the i-th item
            skip = solve(i-1,cap)# see we never acess the last ele we did i-1
            
            # take the i-th item if it fits
            take = 0
            if weights[i-1] <= cap:
                take = values[i-1] + solve(i-1,cap-weights[i-1])
            
            return max(skip,take)
        return solve(n,capacity)
    
    #reverse recurison to dp dito dito literally line by line mapping
    """
        Step 1: What solve(i, cap) becomes in DP

            Direct mapping:
            solve(i, cap)  ⟶  dp[i][cap]

            So write this sentence first:
            dp[i][cap] = best value using first i items with capacity cap
            This is mandatory. If you can’t write this, you can’t do DP.
        Step 2: Base case mapping
            Reverse recursion
            if i == 0 or cap == 0:
                return 0

            Bottom-up DP equivalent
            dp[0][cap] = 0    # 0 items
            dp[i][0] = 0      # 0 capacity

            this is indirectly being set by this peice of code when we intia DP
            dp = [[0] * (capacity + 1) for _ in range(n + 1)] # exact mapping

            This is why we:
            create n+1 rows
            create capacity+1 columns
            initialize first row and first column with 0 
            No magic. This is the base case written into the table.

            Step 3: Recursive calls → DP table lookups
                Reverse recursion
                skip = solve(i-1, cap)

                Bottom-up DP
                skip = dp[i-1][cap]

                Reverse recursion
                take = values[i-1] + solve(i-1, cap - weights[i-1])

                Bottom-up DP
                take = values[i-1] + dp[i-1][cap - weights[i-1]]

                Same formula.
                Only solve → dp.
        
            Step 4: Return statement → DP assignment
                Reverse recursion
                return max(skip, take)

                Bottom-up DP
                dp[i][cap] = max(skip, take)

                This is the most important mapping:
                return value ⟶ store in table.

                Storing results is the memoization step.
                The only difference is where and how you store them.
                
                Here’s the clean, final way to remember it:

                Memoization (top-down):
                You store the result when a recursive call returns.
                Storage happens on demand.

                memo[state] = result

                Bottom-up (tabulation):
                You store the result while filling the table in loops.
                Storage happens systematically.

                dp[state] = result


                Same idea. Same stored value. Different control flow.
                            
            Step 5: Recursive call order → loop order
                Reverse recursion
                solve(n, capacity)

                Recursion ensures:
                smaller i is solved before bigger i

                Bottom-up DP
                You must force the same order with loops:

                for i in range(1, n+1):
                    for cap in range(1, capacity+1):

                Why?
                dp[i] depends on dp[i-1]
                so row i-1 must already be filled
                This replaces the call stack.

            Step 6: Final return mapping
                Reverse recursion
                return solve(n, capacity)

                Bottom-up DP
                return dp[n][capacity]

                Exact same meaning.

    """

    def tabular_DP_Sol(self,weights,values,capacity):
        """
        What bottom-up DP actually is

            Bottom-up DP solves the problem by first solving the smallest subproblems
            and then building up to the final answer using loops.
            No recursion.
            No call stack.
            No memo checks.

            You decide the order. The computer just follows it.

            Key difference (this is the core)
            Top-down (memoization)
            - You start with the final question
            - Recursion asks for smaller answers
            - Cache avoids recomputation
            - Order is decided by recursion

            Bottom-up (tabulation)
            - You start with the smallest possible problems
            - You compute everything step by step
            - No recursion at all
            - Order is fully controlled by you

            Important:
            Both solve the same DP recurrence.
            Only the direction of computation changes.

            Why bottom-up is considered “better” sometimes
            Not because of Big-O.
            - Time complexity is the same as memoization.
            - Bottom-up is preferred when:
            - recursion depth could be large
            - stack overflow is a risk 
            - interviewer asks for tabulation
            - space optimization is required 
            - DP table is clearly defined
            - Mental model (simple and correct)

            Top-down thinking:
            “To solve this, what smaller problems do I need?”

            Bottom-up thinking:
            “If I already know answers to all smaller problems, I can compute the bigger one.”

            Bottom-up always follows this structure
            - Define DP table
            - Fill base cases
            - Fill table in increasing problem size
            - Return final cell
            That’s it.

        """
        n = len(weights)
        #intiliase the dp table 
        dp = [[0] * (capacity + 1) for _ in range(n+1)] #automatically intialise base recurion case

        #recursive call order -> forcing it into loops
        for i in range(1,n+1):
            for cap in range(1,capacity+1):
                #recursion equivalent : skip = solve(i-1,cap)
                skip = dp[i-1][cap] 

                #recursion equivalent : 
                # take = 0
                # if weights[i-1] <= cap: take = values[i-1] + solve(i-1,cap-weights[i-1])

                take = 0
                if weights[i-1] <= cap:
                    take = values[i-1] + dp[i-1][cap-weights[i-1]]
                
                #store results is memoization step
                dp[i][cap] = max(skip,take)
        
        # “Best value using all items with full capacity”
        # The answer is always stored in the DP cell that represents the full original state.
        return dp[n][capacity]


    

"""
pratice problems for this pattern 
Concept	LeetCode
Subset Sum	LC 416
Equal Sum Partition	LC 416
Count of Subset Sum	LC 494
Min Subset Sum Diff	LC 1049
Target Sum	LC 494
Count-based 0/1 DP	LC 494, LC 474
"""