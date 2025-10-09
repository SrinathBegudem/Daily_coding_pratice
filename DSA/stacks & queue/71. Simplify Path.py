class Solution:
    def simplifyPath(self, path: str) -> str:
        # my inutiion is to split by slash and push them into stack and return the joined stack
        temp = path.split("/")
        print(temp)
        stack = []
        for char in temp:
            if char == "" or char == ".":
                continue
            # if char == ".":
            #     continue
            elif char == "..":
                if stack:
                    stack.pop()
                    stack.pop()
            else:
                stack.append('/')
                stack.append(char)
        return "".join(stack) if stack else '/'

        #second sol 
        # stack = []
        # parts = path.split('/')
        # # print(parts)
        # for i in parts:
        #     if i == '' or i == ".":
        #         continue 
        #     elif i == "..":
        #         if stack:
        #             stack.pop()
        #     else:
        #         stack.append(i)
        # return '/'+ '/'.join(stack)