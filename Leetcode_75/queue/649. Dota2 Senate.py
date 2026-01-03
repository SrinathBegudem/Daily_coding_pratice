class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # watch need code video not at all inutite at all this question
        r_q = deque()
        d_q = deque()
        n = len(senate)
        # add the indexs to the queues 
        for i,c in enumerate(senate):
            if c == "R":
                r_q.append(i)
            else:
                d_q.append(i)

        while r_q and d_q:
            r = r_q.popleft()
            q = d_q.popleft()
            if r < q:
                #r bans d and add the r to next round of votes by adding offset
                r_q.append(r+n)
                continue
            else:
                #q bans r add the d to next round of votes by adding offset
                d_q.append(r+n)
                continue
        return "Radiant" if r_q else "Dire"
    

            
