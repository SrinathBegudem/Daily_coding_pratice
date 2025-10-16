# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #classic binary search both left, right are inclusive 
        #Use INCLUSIVE template: right = n, while left <= right
        left = 1 
        right = n 
        while left <= right: #inlcusive or we can also do till output == 0 
            mid = (left + right)//2 # this is my guess 
            output = guess(mid) # the output can be -1, 0 , 1 # checking is it acutal pick 
            if output == -1:
                right = mid - 1
            elif output == 1:
                left = mid + 1
            else:
                return mid
        return "not found" # this never executes as sol gauranteed to give output 

        