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


       
        