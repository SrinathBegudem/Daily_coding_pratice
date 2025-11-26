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

            

#attempt 2 code

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        The key point is 
        - for s to be subseq its len should be less than or eq to t
        -we have 2 pointer i and j which traverse both the strs
        - if the i == len(s) then we return true as it is subseq else false
        """
        # edge case: bigger len can never be subseq
        if len(s) > len(t): return False

        #for loop soution
        i = 0
        for j in range(len(t)):
            #break once we reached the len of s other wise we get index out of error
            if i == len(s):
                return True
            elif s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

        






        # i = 0 
        # j = 0 
        # # if i >= len(s) means s is sub str
        # while i < len(s) and j < len(t):
        #     # check for matching char , if any move i += 1
        #     if s[i] == t[j]:
        #         i += 1
        #     #if no match just increase j pointer
        #     j += 1
        # #once after loop breaks see if i == len(s) if yes true
        # return i == len(s)


       
        