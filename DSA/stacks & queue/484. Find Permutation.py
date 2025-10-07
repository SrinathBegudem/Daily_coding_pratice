class Solution:
    def findPermutation(self, s: str) -> List[int]:
        """
        There is no way we figure out this sum can be solved by all our own, even given an idea of stack it takes a lot to figure this question out.
        so the concpet is you push the num into stack until you find and "I" once you see a I you pop all the elements in the stack so simple if you see a "D" push elemenets into stack and if you see an "i" pop elemnts from stakc and add it to res. and make sure you add the last elements to stack after for loop and pop that, never make a mistake of directly added the last elements to the res because last place can be "D" fo this cases the last elem add to res fails dry run both of this cases to udnertsnad IDDI works if you directly add last element to res bcz the str ends with I that menas next element should be increasing and for IDDD the last elements append to res fails.
        """
        n = len(s)
        res = []
        stack = []        

        for i,char in enumerate(s):
            stack.append(i+1) # beacuse the index starts from 0 and the num starts from 1 
            if char == "I":
                while stack:
                    res.append(stack.pop())
        stack.append(n+1)
        while stack:
            res.append(stack.pop())
        return res
        
