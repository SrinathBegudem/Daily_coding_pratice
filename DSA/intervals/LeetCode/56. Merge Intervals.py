class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        i will sort the intervals based on the first index and and have two pointer cur_start and cur_end and check if next element start is less than or eq to prev element end then we have common intervals so we take max of both ends and append the merge results.
        """
        intervals.sort(key = lambda x : x[0]) # or you can use .sort it will sort lexigraphically sorts the first element and then next 
        prev_s,prev_e = intervals[0] # i.e [1,3]
        merge = []

        for cur_s,cur_e in intervals[1:]:
            #check if the start <= the prev element end if yes then we need to merge as they are overlapping\
            if cur_s <= prev_e: # if cur start < = prev end then we have to merge there is overlapping 
                prev_e = max(prev_e,cur_e)
            else: #no overlapping add to the res
                merge.append([prev_s,prev_e])
                prev_s,prev_e = cur_s,cur_e
        # last element append 
        merge.append([prev_s,prev_e])
        return merge







