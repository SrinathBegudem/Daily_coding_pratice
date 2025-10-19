class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        THe code is straight forward just have to know how to convert char to int using ord('a')(its unnessary) you can use the raw code.
        time - o(n)
        space - o(1)
        """
        #chatgpt said the ord convretion of a is unncessary and i thinks its right 
        # res = 0 
        # for i in range(1,len(s)):
        #     a = ord(s[i-1]) - ord('a')
        #     b = ord(s[i]) - ord('a')
        #     res = res + abs(a - b)
        # return res 
        res = 0
        for i in range(1,len(s)):
            res += abs(ord(s[i-1]) - ord(s[i]))
        return res 
        