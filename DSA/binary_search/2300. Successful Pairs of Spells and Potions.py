class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Time = nlogn (sorting) + n log  m (we apply binary search n times that is len of spells), space = o(n), the brute force approch will be using 2 nested loops and mutiplying spells with portion one by one and do a linear scan on portions so time complexity is o(n*m)
        """
        res = []
        potions.sort()
        n = len(potions)
        for s in spells:
            if s*potions[-1] < success: # micro optimization if the product of s * potions last val is less than success then no point of doing lower bound binary search for that arr as the potions is sorted all the rest will also be less.
                res.append(0)
                continue
            else:
                # i used lower bound binary search is we need to find the left most or insert position for sucess var and minus it with len(potions)
                lo = 0
                hi = n
                while lo < hi:
                    mid = (lo+hi)//2
                    cur = s*potions[mid]
                    if cur < success:
                        lo = mid + 1
                    else:
                        hi = mid 
                res.append(n-lo)
        return res 


        