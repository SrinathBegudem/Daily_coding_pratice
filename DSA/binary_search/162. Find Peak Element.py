class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def brute_force():
            """
            The brute force approch is to traverse each element and find its left and right, check them to see whether the current element is peak element or not, if yes return the first element encountered
            Time : o(n)
            space:o(1)
            """
            n = len(nums)
            for i in range(n):
                #lets check if the number left and right are less than cur and given cond that out of bound are always less
                if ((i - 1  < 0 or nums[i-1] < nums[i]) and 
                    (i+1 >= n or nums[i+1] < nums[i])):
                    return i
            return -1 # if no number is found 
        # return brute_force()
    
        def optimal_sol():
            """
            They want us to solve in logn time complexity clear hint of using a binary search, so now instead of doing linear pass lets simple do binary search, but how do we decide to move left or right???? 
            well the trick is upward slope and downward slope.
            so lets say we are at the mid and check left and right if the right side val is high by inutuion the peak element is on right side because
            case 1: if cur mid is less the right then right might be a peak elem if right next ele is less than right
            case 2 : if right next element is not less then that elem might be peak if we keep on going we will either be at the end of the list where the end of list is great and out of bound is always less so it is peak or we find the peak element. 
            similar logic for left too 
            so choose to move on side which is greater than cur mid and it works if monotically increase or non monotically incresaeing 
            """
            n = len(nums)
            lo = 0
            hi = len(nums) - 1
            while lo <= hi: # simple trick if we return inside the while loop then use the lo <= hi code or if we return outside liek return lo we use lo < hi in while loop, bcz you can dry run and see if lo < hi we meet at the result lo == hi == res so we return outside and if we also proceed with lo <= hi so we need to excplitily have return tatement inside the while loop other wise left and right crosses each otehr and creates a bug 
                m = (lo+hi)//2
                #condition if the cur mid is peak return 
                if ((m - 1  < 0 or nums[m-1] < nums[m]) and 
                        (m+1 >= n or nums[m+1] < nums[m])):
                        return m
                #if peak element is on right move right
                elif nums[m] < nums[m+1]:
                    lo = m+ 1
                # if peak is left move left
                else:
                    hi = m - 1
            return -1 #if ans not found 
        return optimal_sol()
            
                


        