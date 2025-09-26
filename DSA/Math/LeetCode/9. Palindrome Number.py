class Solution:
    def isPalindrome(self, x: int) -> bool:
        # my idea is to just rev the num and check if they are equal 
        # as there are negative num i shoould take care of the sign because % and // work diff in neg range
        # no matter waht negative num is never palindrome 
        if x < 0:
            return False
        rev = 0
        val = x
        while x:
            rev = rev * 10 + (x%10)
            x = x // 10
        return rev == val

        #BRUTE FORCE SOL WOULD BE TO CONVERT THE NUM INTO STRING AND USE TWO POINTERS 
        