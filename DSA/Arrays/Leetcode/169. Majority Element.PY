class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
Boyer-Moore Majority Vote Algorithm (Classic version)
✅ What it guarantees:
It guarantees to find the correct majority element only if one exists (i.e., an element appears more than ⌊n/2⌋ times).

That’s why LeetCode Problem 169 (Majority Element I) explicitly states:

"The majority element always exists in the array."

❗ If the majority element is not guaranteed:
Boyer-Moore might return a wrong candidate.

So, you must do a verification step after finding the candidate:
if nums.count(candidate) > n // 2:
    return candidate
else:
    return -1  # or some indication that no majority exists

        """
        return self.optimal_sol(nums)
    
    def hashmap_sol(self,nums):
    # time = space = o(n)
        numSeen = dict()
        n = len(nums)
        # this edge case is hard to find so check proerly if usign hash map 
        if n == 1:
            return nums[0]
        for num in nums:
            if num in numSeen:
                numSeen[num] += 1
                if numSeen[num] > n//2:
                    return num
            else:
                numSeen[num] = 1
            
    def optimal_sol(self,nums):
        # time = o(n), space = o(1)
        candidate = nums[0]
        count = 0
        for num in nums:
            # the key here is to update the candidate once the count == 0 
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        # so here the boyer mayor algorithm works. because it expilcity given that there must exsits an mojority element
        # remember boyer major doesnt directly return majority element. if there are no condition that says there "exisit majority element" then it can return wrong elements ex [1,1,2,3,3] ---> algo returns 3 and 3 is not majority that is >n/2 so we need to always perform checks in interview byt adding below part of code and before better understanding solve leetcode 229.
        #code:
        # if nums.count(candiate) > n//2:
        #     return candidate
        # else:
        #     return -1
        # you can also use for loop tp count the no of times candidate appears, by any way it will take o(n) time complexity
        # solve majority element 2 for sure 
        
        
        