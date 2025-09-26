class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        #because % and // work diff in negative vals
        sign  = -1 if x < 0 else 1 
        x = abs(x)
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        while x:
            res = res * 10 + (x % 10)
            x = x // 10 
        res *= sign
        if INT_MIN <= res <= INT_MAX:
            return res
        else:
            return 0

        