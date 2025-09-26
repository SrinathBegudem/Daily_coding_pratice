class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.optimal_sol(intervals,newInterval)


    def optimal_sol(self,intervals,newInterval):
        res = []
        i = 0
        n = len(intervals)
        s,e = newInterval

        #enter all the values before the start of the new intervals 
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1
        
        #merge 
        while i < n and intervals[i][0] <= e:
            s = min(s,intervals[i][0])
            e = max(e,intervals[i][1])
            i += 1
        res.append([s,e])
        #append the rest 
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


    def brute_force_sol(self,intervals,newInterval):
        res = []

        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        prev_s,prev_e = intervals[0]
        for cur_s,cur_e in intervals[1:]:
            if cur_s <= prev_e:#then there is overlapping
                prev_e = max(cur_e,prev_e)
            else: #simply append the non overlapping to res 
                res.append([prev_s,prev_e])
                prev_s,prev_e = cur_s,cur_e
        res.append([prev_s,prev_e])
        return res
        