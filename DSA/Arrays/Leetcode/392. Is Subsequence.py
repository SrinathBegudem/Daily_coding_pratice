class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        The intution here is to use the pointers 
        - one pointer to traverse s str 
        - one pointer to traverse t str 
        - we will check if the order is preseverd by advancing the s pointer if and if it found in the t pointer 
        - so if there is no proper order we will be not adancing the s str pointer 
        -time = o(len(t)
        -space = o(1)
        """
        p1 = 0
        p2 = 0
        #ege case empty str is always subseq
        if not s:
            return True
        while p1 < len(s) and p2 < len(t):
            # move the s pointer if and only if there is a match with t pointer
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        #edge case the s string can be empty and empty string is always a substring 
        return p1 == len(s)      #if s else True better write this edge case at the top 

            

        