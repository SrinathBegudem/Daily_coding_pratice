class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        looking at the question the idea pops up is the right most occurence or the upper boundary binary search , becuase it gives us the target next element which is exactly what the code wants and they gave us chars i think we need to use ord to convert them into numerical to do some should of comaprision.
        key points of upper bound 
        - lo,hi =0,n (exclusive)
        - where lo < hi 
        - if nums[mid] >= target: lo = mid + 1
        - else: hi = mid 
        - last occurence = lo - 1 
        """
        #lets convert the target char into number 
        tar = ord(target) - ord('a') # now a = 0, b = 1 ......
        n = len(letters)
        lo = 0 
        hi = n 
        while lo < hi:
            mid = (lo+hi)//2
            num_char = ord(letters[mid]) - ord('a')
            if num_char <= tar:
                lo = mid + 1
            else:
                hi = mid 
        last_occurence = lo - 1
        return letters[lo] if lo < n else letters[0]

        