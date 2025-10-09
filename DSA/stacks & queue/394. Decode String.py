class Solution:
    def decodeString(self, s: str) -> str:
        """
        we will append to stack until we find a closing bracket and then once we find a closing bracket then we pop till the open brack and pop once to remove the open bracket and then comes the umber we extract that number and then push into stack that num times the text and repeat this till we process everything once done we will join the stack and output it 
        """
        #stack to store the string 
        stack = []
        for char in s:
            # we append all the char until we find the first closing brakcet 
            if char != ']':
                stack.append(char)
            # now when we find the first closing bracket
            else:
            # we pop till we find the respective opening bracket 
                str_lst = []
                digit_lst = [] # cna be single diigt double and triple we can directly do str concat but its not efficent 
                while stack[-1] != '[':
                    str_lst.append(stack.pop())
                #once we found the opening bracket break the loop and pop it out and dont add to temp_lst
                stack.pop() #poping the opening bracket 
                while stack and stack[-1].isdigit(): # there is a chnance that there is no num so we should check if stack
                    digit_lst.append(stack.pop())
                #adding to get complete str from lst 
                strN = "".join(str_lst[::-1]) # join in reverse dir as we are appending if we do concat we can ingore this as append send the last char to first and first will be on top of stack 
                #getting the int type of digit from digitlist
                digit = int("".join(digit_lst[::-1])) # same goes to digits reverse adn join 
                #now we push all the digit * str_lst to stack again 
                #we can use for loop or simple can do this stack.append(digit*strN) or we can use for loop to do it ut its better to do the append as it will concat and push it to the stack as one element than for loop which pushes digits times 
                stack.append(digit*strN)
        #retrun the str format of stack
        return "".join(stack)


        #or str concat solution easier but not efficient 
        # stack = []
        # for char in s:
        #     if char != ']':
        #         stack.append(char)
        #     else:
        #         strN = ""
        #         digit = ""
        #         while stack[-1] != '[':
        #             strN = stack.pop() + strN # for str too we need to add the pop index in the begg
        #         stack.pop()
        #         while stack and stack[-1].isdigit():
        #             digit = stack.pop() + digit
        #         stack.append(int(digit)*strN)
        # return "".join(stack)



        