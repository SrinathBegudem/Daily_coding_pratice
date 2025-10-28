class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # so we can skip duplicates and dotn start a branch, After sorting, duplicates are adjacent.
        res = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return 
            # not used think at high level and depth zero if [1,1,2] if 1 started branch at depth zero all are [f,f,f], so if index 0 started branhc idnex 1 at depth zero should not start a branhc as it will give repated purmutations so not False is true so we skip it, so to summarise used[i-1] is to check if we are in same lvel then we skip duplciates if diff level then we proceed to use the duplciates as it will result in diff permutations
            for i in range(len(nums)):
                # indx which is already consider in the path is ignored 
                # for ex if indx 0 is already in path we skip it dont include it again in the path 
                #as the for loop always starts from beggining we dont want same num to include in the path(depth first)
                if used[i]:
                    continue
                # duplicates are skipped at the same level to remove same end results (node level not path)
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:# IF YOU REMOVE USED[I-1] AFTER DEPTH 0 IN DEPTH 1 YOU WILL ALWAYS SKIP THE SECOND DUPLCIATE EVEN IN DIFF DEPTHS SO USED[I-1] MAKE SURE THAT DUPLCIATES AT SAME LEVEL ARE IGNORED AND DUPLICATES AT DIFF LEVEL ARE ACCEPTED SO, INTUTITON IS AFTER EVERY LEVEL ONE FLAG TURNS TRUE IT INDICATES WE ARE IN NEXT LEVEL SO IF NOT TRUE MEANS FALSE THEN WE ADD THE DUPKICATE IF NOT FALSE MEANS WE ARE IN THE SAME DEPTH THAT IS WHY THE DUPLICATES ALL HAVE FALSE SO NOT FALSE TRUE SKIP IT 
                    continue 
                used[i] = True
                #append
                path.append(nums[i])
                #recurse 
                dfs()
                #backtrack
                path.pop()
                used[i] = False
        dfs()
        return res


        