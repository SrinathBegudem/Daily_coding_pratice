class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        intuition for binary search we know that the num which appears one time or lets call it target, 
        -the num left side and right side of the target should be diff or more concisely we can say if index - 1 < 0 or nums[leftside] != target ( that means either the left is out of bound that is less than 0 or elft element is diff than target) and if index + 1 > len(nums) or nums[right] != target, then we found the target return it. 
        -now how do we decide to move left or right??? so lets assume we found a num 3 [1,1,2,3,3,4,4] we check left of the num and right of the num as 3 has duplciate it is not our target so we can remove both 3's, now if you see the right side it will be even and it is gaurantee to have duplciates and left side is odd that means our target is on left of the 3 

        """
        def modified_binary_search():
            lo = 0 
            hi = len(nums)-1
            while lo <= hi:
                mid = (lo+hi)//2
                #check if the mid is the target?? 
                if ((mid-1 < 0 or nums[mid] != nums[mid-1]) and 
                        (mid+1 >= len(nums) or nums[mid] != nums[mid+1])):
                    return nums[mid]
                leftSize = mid - 1 if nums[mid] == nums[mid-1] else mid
                #ex [1,1,2,3,3,4,4,8,8] mid = 4 and nums[mid] == nums[mid-1], so leftSize = 3 elements whic 1,1,2 so it is mid - 1 as the index is started from 0 we do mid - 1 ( seems like we are considering the first 3 but its not index its no of elements) so 3 elemtns == index 2, we need that to see which side is odd and which side is even 
                if leftSize%2:# if this true(any num except 0) that is leftSize%2 != 0 then its true we move left as its odd
                    hi = mid - 1 
                else:
                    lo = mid + 1
            # it will return the ans above so no return type is needed 
        return modified_binary_search()


        def brute_force():
            # use can also use xor opertor
            #linear time compelixty 
            res = 0
            for num in nums:
                res ^= num
            return res

        def brute_force2():
            total = nums[0]
            cur = nums[0]
            for i in range(1,len(nums)):

                if nums[i] != nums[i-1]:
                    cur += nums[i]
                total += nums[i]
            return cur*2 - total 
        # return brute_force()

            
                    
    


