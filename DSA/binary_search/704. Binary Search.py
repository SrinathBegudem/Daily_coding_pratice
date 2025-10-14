class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Classic binary search sum:
        have left and right pointer and cal the mid point and check with the target and move either side based on the target val
        """
        n = len(nums)
        def iter_sol():
            #time , space = o(logn), o(1)
            # start with left with 0 
            left = 0
            #right with end of the arr
            right = n-1 
            
            #egde case we need to check each and every element if we do left < right we might skip right and that might be the target
            while left <= right:
                # this cal of mid usally helps in other lang where there might be an interger overflow large int error but python automatically handles this 
                mid = left + (right-left)//2
                #target found 
                if nums[mid] == target:
                    return mid
                #target is in right part of arr
                elif nums[mid] < target:
                    left = mid + 1
                #target is in left part of arr
                else:
                    right = mid - 1
            #no index found 
            return -1 
        # return iter_sol()
        def recur_sol(left,right):
            #time = space = o(logn)
            #base case if left index crosses right index return number not found 
            if left > right:
                return -1
            # cal the mid val 
            mid = (left+right)//2
            # if target found 
            if nums[mid] == target:
                return mid
            #recurusive cases 
            if nums[mid] < target:
                return recur_sol(mid+1,right)
            else:
                return recur_sol(left,mid-1)
        # return recur_sol(0,n-1)

        #so the above two works for no duplicates(unquie numbers), if there are duplciates and require you to return the left most index 
        # for duplciates like [1,2,2,3] there might be question in interview asking to return the left most index of duplicate or right most index of target if target is 2, so calssic binary search doesnt gaurantee this we need to modify to either return left index which is 1 or right index which is 0.

        # to get the left most index lower bound 
        def left_most_occurrence():
            left = 0
            right = n-1
            while left < right: # we should set left < right so if left = right we will either found the target or return -1 
                mid = (left+right)//2
                if nums[mid] < target: # target is in right side of the arr 
                    left = mid + 1
                else: # else nums[mid] >= target we change right to mid since there is change that mid can be the only one target
                    right = mid 
            # thsi returns the left most 
            return left if left < n and nums[left] == target else - 1 # you can also return hi 
        #dry run [1,2,2,3] target = 2 get me left most idnex 
        #l = 0, r = 3, mid = 1 # nums[mid] is not less than target its eq so else statement executed r = mid = 1
        #l = 0 , r = 1 , mid = 0  if statements exe l = 1
        #l=r=1 loop breaks we return l so we get the indx of first occurence 
        #--------
        #dry run 2 [1,2,2,,3,3] target = 2 get me left most idnex
        # l = 0, r = 4, mid = 2 
        # l = 0 , r = 2 , mid = 1 
        # l = 0, r = 1 # see how we move  left even we found the target thats the magic 
        # l = 0, r = 1 , mid = 0 
        # l = r = 1 loop breaks return l so the first elft occurence 

        # now lets return right most occurence, for this we need to find the target next val and then go back one index 
        def right_most_occurence():
            left = 0
            right = n-1
            while left < right:
                mid = (left+right)//2
                if nums[mid] <= target: # we changed < from <= , even if we found target we move left index to target next 
                    left = mid + 1  # discard left includign mid 
                else: #nums[mid] > target
                    right = mid  # once we move the mid over target then we lower the right and eventually break the loop,so the left index now is in target next index 
            j = left - 1 # we do -1 to get to the right most index of target num 
            return j if j >=0 and nums[j] == target else -1 
            
        #dry run [1,2,2,,3,3] target = 2 get me left most idnex 
        # l = 0 , r = 4, mid = 2 , nums[mid] == target yet we move to next index left = mid + 1, this is done to get the right most
        # l = 3, r =4 ,mid = 3 , nums[mid]> target we bring down right its obv right once we cross the left = mid + 1 we continously decrse right so the loop breaks 
        # l = 3 , r = 3 , break the loop and return l - 1 index make sure to check edge case if its start of arr and if the l-1 == target 










