class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                #edge case : if there are char at the start of the string direct pop ca lead to error but this sum gauntree that there will be left element before the star
                if stack: stack.pop()
            else:
                stack.append(char)
        return "".join(stack)



#my first try worked but very complciated not suggested
        
        # res = []
        # stars = []
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] == '*':
        #         stars.append(s[i])
        #     else:
        #         res.append(s[i])
        #         if res and stars:
        #             res.pop()
        #             stars.pop()
        # res.reverse()
        # return "".join(res)
