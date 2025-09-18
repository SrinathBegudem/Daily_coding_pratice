class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def optimal_sol(s): #good work solved by my self
            seen = set() #at max 26 alphabets so o(1) space
            i=0
            j=0
            n = len(s)
            max_len = 0
            while i < n and j<n: #o(n)
                while s[j] in seen:
                    seen.discard(s[i]) #o(1) and can also use .remove()
                    i += 1 
                seen.add(s[j])
                j += 1 
                max_len = max(j-i,max_len)
            return max_len 
        
        def brute_force(s):
            """
            for every element i start another loop j until you found duplicates and update max_len
            """
            n  = len(s)
            max_len = 0
            for i in range(n):
                seen = set()
                for j in range(i,n):
                    if s[j] in seen:
                        break
                    seen.add(s[j])
                    max_len = max(j-i+1,max_len)
            return max_len
        return brute_force(s)

        