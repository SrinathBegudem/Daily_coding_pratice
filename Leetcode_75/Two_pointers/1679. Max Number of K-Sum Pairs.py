class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = dict()
        ops = 0 

        for num in nums:
            comp = k - num 
            if comp in freq and freq[comp] > 0:
                freq[comp] -= 1
                ops += 1
            else:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        return ops



      

        