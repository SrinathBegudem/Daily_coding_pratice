class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        its very simple idea
        we have 2 arrays 
        trusts arr is the coutn of particular index who trusts some one ( for judge this arr indx will be 0)
        for ex if 1 trust 2,3 then the count of indx 1 will be 2
        trusted_by arr is that stores the count of people a particular indx is trusted by ( for judge to exists index of particular arr should be eq to the n-1 since judge wont trust him self and everyone trusts him)
        """

        if n == 1:  # Edge case
            return 1
        trusts = [0] * (n+1)
        trusted_by = [0] * (n+1)

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1
        
        for i in range(n+1):
            if trusts[i] == 0 and trusted_by[i] == n-1:
                return i
        return -1









        # this code was my first try was optimal but not interview frndly
        # adj_list = {val:[] for val in range(1,n+1)}
        # judge_count = {}

        # if n == 1:
        #     return n
        # for val in trust:
        #     person = val[0]
        #     trusts = val[1]
        #     adj_list[person].append(trusts)
        #     if trusts in judge_count:
        #         judge_count[trusts] += 1
        #     else:
        #         judge_count[trusts] = 1
        # print(adj_list)
        # print(judge_count)
        # for k,val in judge_count.items():
        #     if val == n-1 and adj_list[k] == []: 
        #         return k 
        # return -1



            