class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def optimal_sol():
            """
            Key diff btw permutation and combination
            Permutations (order matters)
            - In permutations we use boolean "used" to check
            - check same indx var in the path is ignored 
                - if used[i]: continue
            - check the duplicates at same level is avoided 
                - if i > 0 and nums[i] == nums[i-1] and not used[i]: continue
            - have core backtrack algo 
            - set used[i] = False ( this helps skip duplicates at same level and also skip using the same index in path(diff levels))
            combinations (order doesnt matter)
            - we have start index 
            - this start says once one indx is consider and we explore all the possible sol we never go back to that index 
            - so we start with 0 index and as we procedd we add + 1 so this allows us to never go back to indx 0.
            two var 
            combination (with reuse) 
            - start index is i 
            combiantion (withour reuse)
            -start index is i + 1
            """
            # lets sort so we can skip vals more than target which can never give valid answes 
            candidates.sort()
            res = []
            path = []
            # we have 2 args start_indx and cur_sum 
            def backtrack(start,total):
                if total == target:
                    res.append(path[:])
                    return 
                for i in range(start,len(candidates)):
                    cur_sum = total + candidates[i]
                    if total > target:
                        break # dont explore future
                    #core backtrack
                    # add the choice 
                    path.append(candidates[i])
                    #explore the choice 
                    backtrack(i,cur_sum)
                    #backtrack
                    path.pop()
            backtrack(0,0)
            return res
        return optimal_sol()



        def brute_force():
            """
            The inuition here is 
            - we are not pruning anything means we are eploring solution that are already explored duplicated branchs 
            - we check if sum (path) == target then append that tuple sorted list to res (to remove duplicate in res)
            - if path sum is more than target we just return wont explore that branhc any more 
            - this is brute force solution 
            """
            nums = candidates # just reassigned so i can do loop like num in nums 
            res = set()
            path = []
            def backtrack():
                # base case 
                if sum(path) == target:
                    res.add(tuple(sorted(path[:])))
                    return 
                
                if sum(path) > target:
                    return 
                
                for num in nums:
                    #append (select the choice)
                    path.append(num)
                    #recurse
                    backtrack()
                    #backtrack(remove the prev choosen choice and proceed to add new choices)
                    path.pop()
            backtrack()
            return list(res)



            