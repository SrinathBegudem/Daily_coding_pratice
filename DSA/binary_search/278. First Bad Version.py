# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        The intution is very clear, in the whole search range there will be one bad version  which starts and all the version after that are bad its something like half bad and half good so instead of doing linear search we can to binary search to find whther its bad or not, in the binary search too we dont use classic binary search because calssic only finds you wheather its bad or not, but we need the first version which is bad and which started all the next version to be bad, any idea ??? something like left most occurance ?? lower bound??? think it as an array of 0 and 1 o is good versions and 1 is bad [0,0,0,1,1,1,1] our goal is to find first 1 , which is left most occuurence.
        key points of left most occurence 
        - lo,hi = 1,n i.e [1,n) n is exclusive we dont include n but put our boundary as n 
        - while lo < hi 
        - if nums[mid] < target: lo = mid+1
        - else: hi = mid 
        - return lo 
        """
        #time = o(logn), space = o(1)
        #brute force would be we can also do linear search one by one until we get first bad version and return that num the time for that would be o(n)
        lo = 1
        hi = n + 1 #exclusive
        while lo < hi:
            mid = (lo+hi)//2
            #lets check the api call at mid point 
            check = isBadVersion(mid)
            if not check:
                lo = mid + 1
            else:
                hi = mid 
        return lo 
        