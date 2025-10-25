class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Key diff btw comb 1 and comb2 
        comb1 
        - no duplicates (sorting optional but preffered for pruning)
        - can resue numbers therefore (we can backtrack(i,total)) same index
        -doesn't require skip duplicate logic 
        - next recursion call backtrack(i,total)
        comb2 
        - duplicates exists (sorting required to skip)
        - cannot reuse number (backtrack(i+1,total))
        - to skip duplicates at same level we have to use if i > start (not i > 0 which will skip all duplciates globally at diff recursion depths) and nums[i] == nums[i-1]
        """
        candidates.sort()
        print(candidates)
        res = []
        path = []
        def backtrack(start,total):
            if total == target:
                res.append(path[:])
                return
            for i in range(start,len(candidates)):
                #skip duplicates at same level
                if i > start and  candidates[i] == candidates[i-1]:
                    continue 
                # after that have local sum var
                cur_sum = total + candidates[i]
                # skip all indx which has vals > target pruning step
                if cur_sum > target:
                    break
                #core backtrack 
                #add choice
                path.append(candidates[i])
                #explore the option
                backtrack(i+1,cur_sum)
                #undo the chocie to explore other.
                path.pop()
        backtrack(0,0)
        return res