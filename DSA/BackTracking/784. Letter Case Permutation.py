class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        The intuition here is 
        - Order matters ( dont think its permuation) in permutation we go back and front and in permu char position can change which is not the case here, so its combination 
        - we have 2 choice at every stage use lower case or use upper case and once we pass that index we dont always loop through it.
        - exactly as combination where we pass start index. 
        for a char we either take the lower case or upper case 
        """
        res = []
        path = []
        def backtrack(start_index):
            if len(path) == len(s):
                res.append("".join(path))
                return 
            # if the char is alpha 
            if s[start_index].isalpha():
                # we add lower case 
                path.append(s[start_index].lower())
                backtrack(start_index+1)
                path.pop()
                # wee add upper case 
                path.append(s[start_index].upper())
                backtrack(start_index+1)
                path.pop()
            else:
                path.append(s[start_index])
                backtrack(start_index+1)
                path.pop()
        backtrack(0)
        return res





        