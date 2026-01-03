class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Judge conditions

        Judge trusts nobody → out_degree[j] == 0

        Everyone else trusts judge → in_degree[j] == n - 1

        So we count:

        out[a] += 1 for a -> b

        in[b] += 1 for a -> b
        """
        
        trusts = [0]*(n+1) # this store who the villagers trust (outdegree)
        has_trusted = [0] * (n+1) # this stores the villager who trust (in_degree[j] == n - 1)

        for a,b in trust:
            has_trusted[a] += 1
            trusts[b] += 1

        for i in range(1,n+1):
            # jurdge never trust anyone and everyone trust jurdge
            if has_trusted[i] == 0 and trusts[i] == n-1:
                return i
        return -1

        
# trusts = [0,0,1] # this should be 1
# trusted_by = [0,1,0] # this should be zero for town jurdge 

# trusts = [0,1,0,1] # this should be 1
# trusted_by = [0,1,1,1] # this should be zero for town jurdge 

