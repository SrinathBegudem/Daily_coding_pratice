class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.dutch_nation_flag(nums) # the optimal sol for this question (leet code expects to return none so no return)
    def insertion_sort(self,nums): #brute force solution o(n**2) and inplace algorithm
        """
        This is a fundamental soting algo which sorts the array in - place but takes 
        o(n**2) time complexity.so this is consider my easiest and brute force solution.
        insertion sort is like playing cards, we get a number and compare that with the 
        cards we have and put that new num in the correct place. this is the basic 
        concept. left part of array is the cards that we already have and in sorted
        order and when a new num( right part) arrives we compare it with the left part 
        and insert it in correct position thus the name insertion sort.
        """
        # lets traverse through the array to find the new num
        n = len(nums)
        for i in range(1,n): #we are starting from indx 1 because if we start with index zero there is no number to compare
            cur_element = nums[i] # store the current element 
            j = i - 1 # we should compare with the cards we already have and i is the newly arrived card 
            while j >= 0 and nums[j] > cur_element:
                nums[j+1] = nums[j] # move the elements to right
                j -= 1 
            nums[j+1] = cur_element # once found the right positon insert the cur_ele
        return nums # inplace sorting

    def bucket_sort(self,nums):# time = space = 0(n) and its not in place algorithm
        """
        In bucket sort we create buckets( in this case we create 3 buckets for 3 colours) and put the ball in those buckets and 
        merge the final output ( this is gonna take 2 passes but still takes better time compelxity o(n) compared to insertion)
        bucket sort takes time complexity = space complexity = o(n)
        """
        buckets = [[] for _ in range(3)] # o(n) space

        for indx in nums: #o(n) time 
            buckets[indx].append(indx)
        
        index = 0
        for bucket in buckets: # this is o(n) time bcz its a common misconception nested for loops means o(n*n) but here the loops are not multiplied but added or in order words the outer loops onlu runs 3 times and inner loop runs n/3 times so its n*n/3 = n
            for val in bucket:
                nums[index] = val
                index += 1
        return nums 


    def counting_sort(self,nums): # time =  0(n) and space = o(1)(constant space = 3) and its not in place algorithm
        """
        this is also called optimsed bucket sort instead of storing all the variables in bucket we store the counts which inturn svaes the memory 
        """
        counts = [0,0,0]

        for num in nums:
            counts[num] += 1
        
        indx = 0
        for color_value in range(3):
            for _ in range(counts[color_value]):
                nums[indx] = color_value
                indx += 1
        return nums 
        
    def dutch_nation_flag(self,nums): # optimal sol with time = o(n), space = 0(1) and inplace memory
        """
        This is the most optimal sol for this question which takes o(n) time and o(1) space and this is a three pointer/partion approch where we have left( that tracks num of zeros), right( that tracks the num of 2), i (variable to traverse throught the arr)
        the idea is that we start traversing with i adn when ever we encounter a 0 we swap that with left pointer and whenever we encounter 2 we swap it with right. the key point is we increment left and i pointer when we swap with left and only decrement right pointer and DONT increament i pointer, becasue we never know what the right swap val is so we keep the i pointer and verify and then increment and when in case of left pointer swap we know for sure it is gonna swap either 1 or 0 to itself so its safe.
        and whenever we encounter 1 we skip it so they are struck in btw the 0 and 2.
        """
        # intializing the pointers 
        left = i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0: # found zero, then lets swap it with the left pointer and incremenet both left and i
                nums[i],nums[left] = nums[left], nums[i] 
                left += 1 
                i += 1
            elif nums[i] == 2:
                nums[i],nums[right] = nums[right],nums[i]
                right -= 1 # dont increment i as we dont knw the swapped num this is the key concept of dutch nation algo
            else:
                i += 1 # if we encounter a 1 we simply skip it so that it can be struck in the middle of num 0 and 2 
        return nums

    

    



            t