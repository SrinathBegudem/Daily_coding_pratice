class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        The intuition here is to zip all (pos,speed) and then sort with respective to pos ( for clarity draw a 1D line 
        and put all points on it and dry run) so now we start from right most as it is close to target and start merging
        before car if they reach before the cur and imp note is if a particular car doesnt meet the next car before target 
        the left side of those will never meet the cur next car because the speed of left side no matter how much will be 
        reduced to the cur car speed which will never meet the next ( its just an example) so we dont need while loop here as we 
        from right
        ex1 : zip (pos,s) and sort by pos 
        pairs = (0,1).  (3,3). (5,1). (8,4). (10,2).    |target 12
                -12-------3------7------1------1--------|time 
        stack = [] # we put the time into the stack 
        time = distance/ speed --> (tar-pos)/s
        -for (10,2) -> t = 1
        stack = [1]
        -for (8,4) -> t = 1
        stack = [1,1] check if stack has more than 2 elements and if incoming car reaches the target faster than the cur if yes pop it
        stack = [1] since the prev car and cur car meets at target they for fleet
        -for (5,1) -> t = 7 
        stack = [1,7]  # check if the con stack[-1] <= stack[-2] if yes pop if not continue 
        -for (3,3) - > t = 3
        stack = [1,7,3] yes stakc [-1] <= stack[-2] that means it is faster and forms fleet with 7 so pop it and now the case even though the 3,3 car is faster it will be slowed and formed fleet with the (5,1) car and this (5,1) car never fleets with (8,1) so thus (3,3) never meets with (8,1) therefore we dont really neeed a while loop an if loops would do the work here
        stack = [1,7]
        -for (0,1) --> t = 12
        stack = [1,7,12] condition doesnt pass 
        so now we retrun stack that is the num of fleets formed until all cars reach the target.
        """
        
        pairs = [[pos,s] for pos,s in zip(position,speed)]
        # we can direcly use sort which does lexigraphical sorting starting with pos or else use lamba function and sort with pos 
        pairs.sort(key=lambda x: x[0])
        stack = []

        for pos, s in pairs[::-1]: # we can also do for pos,s in sorted(pairs)[::-1]
            t = (target - pos)/s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        