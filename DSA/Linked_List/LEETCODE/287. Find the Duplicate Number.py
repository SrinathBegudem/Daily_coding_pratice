class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.optimal_sol(nums)


    def optimal_sol(self,nums):
        """
        There is no way this could be solved optimally which proper practice of this question
        Concept:
        undertsand the question they said n+1 integers lets assume n = 5 so there will be 6 intergers and the interger range is from 1 to 5, so by this we can udnertsand that definetly there is one or more number that should be repated to fill out the whole spots in array 
        Now we use fast and slow pointer to detect the cycle
        so if fast and slow pointers meet then we proved that there is cycle and the purpose of this is not to prove the cycle bcz we already know there is a cycle.
        but the concept is once both slow and fast pointer meet then when we intialize slow pointer at the begging and move fast pointer from the same position they will meet exactly that the number where cycle start i.e where we have duplicates (we have a mathematical proof for this)
        ex : [1,2,3,4,5,6,3]
index:  0 → 1 → 2 → 3 → 4 → 5 → 6
value:  1 ->  2 ->  3 ->  4 ->  5 ->  6 ->  3
                      ↑                     │
                      └─────────----------──┘
        assume len from 1-3 = l1 
        len from 3-5(cycle start point to where the fast and slow pointers meet for the first time)  = l2 
        len from 5-3(From the point where s and f meet for the first time to the cycle start point) = k 
        we know slow = l1+l2 
                fast = l1 + 2l2 + k 
        we also know that fast = 2slow
        equating both the equations 
        2l1 + 2l2 = l1 + 2l2 + k 
        l1 = k 
        thats why when we re assign the slow pointer to the start and traverse both slow and fast one step at a time they meet exactly at cycle start point that is the num that is duplicate.
        """
        #phrase one detect cycle or more like intro to prhase 2 
        slow = nums[0]
        fast = nums[0]
        while True:
            # increament slow by one indx 
            slow = nums[slow]
            # fast by 2
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #once we found the cycle point, we intialize the slwo to start and move one step at a time and they meet
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        # you can return slow or fast anythign works 
        return fast #or slow

    
    def brute_force(self,nums): 
        #time = o(n**2)
        #space = o(1)
        # we use to for loops and it is accepeted but in follow up they asked to do in o(1) which is goign to be the optimal solution, # Time Limit Exceed.
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
    
    def sort_sol(self,nums):#not allowed
    #time = o(nlogn)
    # space = o(1)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]

    def set_sol(self,nums): #not allowed
    # time = space = o(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
    def list_sol(self,nums): # because num are in the range of index and list lookup is faster when you know index than set
    # time = space = o(n)
        seen = [0] * len(nums) # still not accepted
        for num in nums:
            if seen[num] != 0:
                return num 
            seen[num] = num


        
        
        
        