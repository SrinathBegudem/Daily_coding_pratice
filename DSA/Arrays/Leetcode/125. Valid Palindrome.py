class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.optimised_code(s)


    def my_first_code(self,s): #takes time = o(n) = space 
        result_string = "" # space = o(n)
        for char in s: # time = o(n)
            if char.isalnum():
                result_string += char.lower() # or we can also write  result_string += "".join(char)
        
        i=0
        j=len(result_string) - 1
        while i<=j: 
            if result_string[i] != result_string[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def optimised_code(self,s):# imp sol , time = o(n) loops are not mutiplying they are only traversing once they are just getting added to the whole array and space is constant time operation o (1)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left+= 1 
            right-= 1
        return True
             
        



        