class Solution:
    def maxDifference(self, s: str) -> int:
        """
        The inuition here is 
        - we need to find max diff 
        - given a str of char we need to find max diff such that frq(a1) id odd and freq(a2) is even
        - from logic to have max diff we need to select the var which has max_odd freq and min_even freq
        TIme and space:
        time = o(N)
        space = o(26) which is o(1)
        """
        count = dict()
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        max_odd = 0
        min_even = float('inf')
        for val in count.values():
            if val % 2 != 0:
                max_odd = max(max_odd,val)
            else:
                min_even = min(min_even,val)
        return max_odd - min_even 



        