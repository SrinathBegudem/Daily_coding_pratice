class Solution:
    def decodeString(self, s: str) -> str:
        """
        This question have to many edge cases 
        edgecase 1 : when you pop and append to temp you will be appending in revrese order so you need to revrese it again back before adding to stack
        edgecase2: there can be mutiple char of digits so we need to use loop and isdigit()  to extarct all those num and perform operation
        """
        stack = []
        for char in s:
            temp = []
            # if there is closing sign 
            if char == "]":
                #while ther are elemnts and till we are not ar open bracket append to temp. just know that the append to temp will be in reverse order you need to reverse it or pop and add it back
                while stack and stack[-1] != "[":
                    temp.append(stack.pop())
                
                # removing the open bracket
                stack.pop() # to get rid of '['
                #extarcting the number, edge case make sure double and thriple digits
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)

                # temp = temp * num #this operation reasigns to new list 
                temp *= num # does inplace modification works for this question because it only have immutable type inside it 
                #if there are mutable then there would be issue use temp = temp * num, even this will cause the sharing of mutable items inside. 
                # If you don’t want inner lists to be shared, then you must create new inner lists, and that means using a loop or a comprehension. like in grpahs rows and cols creation
                # temp.reverse() # do the reverse and add it to stack with extend function
                # stack.extend(temp)
                #or pop  + for loop for auto reverse
                for _ in range(len(temp)):
                    stack.append(temp.pop()) # auto reverse
            else:
                stack.append(char)
        return "".join(stack)
            