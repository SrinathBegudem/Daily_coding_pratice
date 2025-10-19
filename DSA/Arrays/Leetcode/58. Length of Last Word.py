class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        The intuition here is very clear
        - start with last index 
        - if the last index is not alpha (space) then move the index towards left until we find the alpha
        - once we encouter alpha start counting the len and when the next space comes break the loop 
        - return the res 
        - time = o(s)
        -space = o(1)
        """
        last_index = len(s) - 1
        while last_index >= 0 and not s[last_index].isalpha():
            last_index -=1 
        
        res_len = 0 
        while last_index >= 0 and s[last_index].isalpha():
            res_len += 1
            last_index -= 1
        return res_len

        
# or you can also do something like this if you dont remeber isalpha() synatx 
        # i = len(s) - 1                 # O(1) start from end

        # # 1) Skip trailing spaces                                # ≤ O(n)
        # while i >= 0 and s[i] == ' ':
        #     i -= 1

        # # 2) Count the last word's length                        # ≤ O(n)
        # length = 0
        # while i >= 0 and s[i] != ' ':
        #     length += 1
        #     i -= 1

        # return length   