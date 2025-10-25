class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        The inuition here is 
        - intially i used input_arr but lately realised that we can use indexs and can save inpur_arr space
        - we cannot reuse the same num so its backtrack(i+1)
        - and rest is the core backtracking algorithm 
        edge case
        - start with index 1 and go till n+1
            - explore 
            - recurse (until res is found)
            - undo 
        """
        # input_arr = [num for num in range(1,n+1)] #o(n)
        res = []
        path = []
        def backtrack(start_indx):
            if len(path) == k:
                res.append(path[:])
                return 
            for i in range(start_indx, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return res
        # i think we can optimise the space too remove the input_arr
        # input_arr = [num for num in range(1,n+1)] #o(n)
        # res = []
        # path = []
        # def backtrack(start_indx):
        #     if len(path) == k:
        #         res.append(path[:])
        #         return 
        #     for i in range(start_indx, n):
        #         path.append(input_arr[i])
        #         backtrack(i+1)
        #         path.pop()
        # backtrack(0)
        # return res
"""
[1,2,3,4]
res = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
-> level 0 (0...4)
    -> i = 0 , path =[1],backtrack(1) 
    -> i = 1 , path = [2],backtrack(2)
    - i = 2, path = [3],backtrack(3)

-> level 1 
 -> branch for path =[1,.]
    -> i = 1 , path = [1,2],backtrack(2) | after retun in level 2 , path = [1]
    -> i = 2 , path = [1,3],backtrack(3) | after return in lvl 2 , path = [1]
    -> i = 3, path = [1,4], backtrack(3) | after return in lvl 2 , path = [1]
    backtrack to lvl 0 to explore other choices by popping 1 , path = []
 -> branch for path =[2,.]
    -> i = 2 , path = [2,3],backtrack(3) | after return in lvl 2 , path = [2]
    -> i = 3 , path = [2,4],backtrack(4) |after return in lvl 2 , path = [2]
    backtrack to lvl 0 to explore other choices by popping 1 , path = []
 -> branch for path =[3,.]
    -> i = 3, path = [3,4],backtrack(4) | after return in lvl 2 , path = [3]

-> level 2 
 -> branch for path =[1,.]
    -> i = 2,base case len(path) == k , return and path.pop and go back one level ,path =[1]
    -> i = 3 , base case len(path) == k , retrun and path.pop() and go back 1 lvl,path =[1]
    -> i = 4 , base case len(path) == k , retrun and path.pop() and go back 1 lvl,path =[1]
 -> branch for path =[2,.]
    -> i = 3 , base case len(path) == k , return and path.pop and go back one level ,path =[2]
    -> i = 4 , base case len(path) == k , return and path.pop and go back one level ,path =[2] 
 -> branch for path =[3,.]
    -> i = 4 , base case len(path) == k , return and path.pop and go back one level ,path =[3] 

"""