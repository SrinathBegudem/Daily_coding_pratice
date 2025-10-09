class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ahh when ever we see combination its 99 percent gonna be a backtracking sum because we have to build varies output cases which only possible by backtracking and also n = 3 hints us there are 3 open and 3 close total 6 that is 3 pairs 
        so here the intution is clear we use stack ( or we can also call it as path ) + backtracking. this is classic backtracking question nothing to do with stack we can also call it path var 
        conditions 
        we have open and clased brackets so the basic concept is closed < open that means if there is 1 open bracket then and only then we have possiblity for closed bracket 
        """
        #3 step code 
        # step 1: base case if open = close = n we snapshot or build the result and return 
        # step 2: if open < n add open parentheses ( , increase the open += 1 call backtrack and undo 
        # step 3 : if close < open then added close parentheses ) , increase close += 1 call bactrack and undo 

        path = [] # or stack 
        res = []

        def backtrack(openN,closeN):
            # step1: base case 
            if openN == n and closeN == n:
                res.append("".join(path))
                return 
            # step2 : if open < n 
            if openN < n:
                # add the choice (append)
                path.append("(")
                # recurvise backtrack (recurse)
                backtrack(openN+1,closeN)
                #backtrack (undo)
                path.pop()
            
            if closeN < openN:
                #add the choice(append)
                path.append(")")
                #recurse 
                backtrack(openN,closeN+1)
                #backtrack(undo)
                path.pop()
        backtrack(0,0)
        return res 


            