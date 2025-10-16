class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Intuition for insertion and finding left most occurence we do lower bound binary search 
        becasue take a look at example 3 if we use classical binary search then the l,r = [0,n-1] but there is a chance of n so we need to take that into consideration, there is a chance that we go out of bound just liek for ex 3 
        charteristics of lower bound 
        lo = 0, hi = n
        while lo < hi: 
        if nums[m] < target: lo = m + 1
        else:#nums[m] >= target hi = mid # we move mid to the first index of occurence or insert posiiton 
        🔵 INCLUSIVE [left, right] - "Both boundaries are IN the range"
        "Inclusive" means: We can check nums[right] - it's a valid index we're searching!
        🔴 EXCLUSIVE [left, right) - "Right boundary is NOT in the range"
        "Exclusive" means: right is a boundary marker, NOT something we access. It's outside the valid range!
        """
        # we use exclusive [l,r) closed on left end and open on right (half open) and in while loop we do l < r (exclusive)
        l = 0 
        r = len(nums) # see we put the right pointer to n not n - 1( in classic)
        while l < r: #we dont do l <= r that will throw out of bond error as we trying to access n ( exclusive) we never acess r
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1 # we try to move till we reach the target 
            else: #nums[m] >= target 
                r = m
        return l # or r 

