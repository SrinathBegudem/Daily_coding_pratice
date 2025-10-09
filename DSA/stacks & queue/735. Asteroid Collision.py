class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    
        stack = []
         # check if the stack[-1] > 0 and asteriod a < 0 then and onlu then we can have a collision and we use while as collision can pass on
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0: # this a will also serve as flag which we can use to break the loop 
                diff  = stack[-1] + a
                # case 1 check if a the negative val destroys the last element in stack if yes we pop the last element 
                if diff < 0:
                    stack.pop()
                #case 2 check if the diff > 0 that means the negative ast is destroyed and we break the loop 
                elif diff > 0:
                    a = 0 
                #case 3 if both a and stack[-1] is same we destory both 
                else:
                    a = 0 
                    stack.pop()
            # there might be a case where the negative destroys all the ast in stack then we add it to stack and also if the above while loop is not exceuted then we add the element to stack so if a is set to zero then it will not be added as 0 is treated as falsy and if a is neg or pos it will be added so perfect if the neg destorys all the elements in stack or else if the while loop fails to excute for positive vals 
            if a:
                stack.append(a)
        return stack 
                

        
                    
        