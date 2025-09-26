# first solve (look below for num of times solved and also that sol when i solve mutiple times)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.optimal_sol(s)

    def my_first_code(self,s):#this code passed 470/490 cases this is not a sucesfull code and i coded this in my first try
        delete_char  = 1 
        i = 0 
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if delete_char == 0:
                    return False
                else:
                    delete_char -= 1
                    if s[i+1] == s[j]:
                        i += 1
                    else:
                        j-=1
                    continue
            i += 1
            j -= 1
        return True 
    
    def ispalindrome(self,s): # you can also write this as static method 
        """
        This is basic palindrome helper function that checks whether a given string is palindrome or not
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1 
        return True
            
    
    def brute_force(self,s): # this code passes 405/477 but gives tle and i guess but i am not sure this is o(n**2) time
    # logic correct but the time is o(n**2) and space is o(n) per slicing 

        # first let me check directly if given string is already a palndrome without deleteing anything
        if self.ispalindrome(s) == True:
            return True
        
        for i in range(len(s)):
            if self.ispalindrome(s[:i]+s[i+1:]) == True:
                return True
        return False

#-------------------optimal sol-----------------------------
    # time = o(n) and space = o(1)
    def palindrome_helper_for_optimal(self,s,left,right):
        # this is diff this is optimsed for space and doesnot need extra space for optimal sol, here we directly pass left and
        # right not string slicing which creates a new string and requries o(n) time
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1 
            right -= 1
        return True

    def optimal_sol(self,s):
        """
        here the idea is to just check if the left pointer and right pointer are not eq then we need to check one more cond
        in that condition we need to skip left once and check if the rest is palindrome if yes we return true and also there 
        is a possibility of having right skip and vice versa


✅ Instance Method
Works with an object of the class.

Uses self to access data stored in the object.

Example: Checking or updating a car’s color.

✅ Class Method
Works with the class itself, not a specific object.

Uses cls to access class-level stuff.

Example: Getting the number of wheels all cars have.

✅ Static Method
Just a helper function inside a class.

Doesn’t use self or cls.

Example: Checking if a car color is valid — doesn’t need to know the car.
use static for helper function next time onwards

        """
    # we are using the is palindorme(helper func) a standard function to check whther the indx we give are a panlindrome or not 
    # lets use 2 pointer approch to solve this sum 
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:# lets check if the left and right pointer are eq or not 
                # if the are not eq usually in standard plaindrome we return false but here they given us a condition of deleting
                #at most one char so we have freedom to delete one and recheck if the filtered string is palindrome or not 
                return self.palindrome_helper_for_optimal(s,left+1,right) or self.palindrome_helper_for_optimal(s,left,right-1)
            left +=1
            right -= 1
        return True

# next time use @static method for helper function @ static methos is used when your not manipluationg class or instance varible its doesnt belong to a class and is put inside of a class for logical relevance and self is not needed and only does some manuplication exactly like helper function 

#---------------------------------------Attempt 2 (completly own solved)--------------------------------------------
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.optimal_sol(s)

    @staticmethod
    def isPalindrome(s):
        left = 0 
        right = len(s) - 1 
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def optimal_sol(self,s):
        left = 0 
        right = len(s) - 1
        k = 1
        while left < right:
            if s[right] != s[left]:
                return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1])
            left += 1
            right -=1
        return True



        