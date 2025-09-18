class Solution:
    def check(self, nums: List[int]) -> bool:
        return self.optimal_case_1(nums)

    def my_first_try(self,nums):
        """
        the rotate array hit me so bad that every time i see rotate array i apply it to the problem 
        """
        # count = 1 
        n = len(nums)
        indx = None 
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                indx = i
                break
        if indx is None:
            return True
        nums[:i] = nums[:i][::-1]
        nums[i:] = nums[i:][::-1]
        nums.reverse()
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                return False
        return True

    def optimal_case_1(self,nums):
        """
        coommnly what we do is to cal drops if there are 2 drops then the array is not sorted and rotated 
        but the edge case here is to compare the last adn first element the circular thing.
        """
        drops = 1
        n = len(nums)
        for i in range(n):
            if nums[i-1] > nums[i]: # THIS WORKS BECAUSE WHEN I =0 WE CHECK I-1 = -1 IF -1 IS GREATER THAN 0 INDEX VAL THEN ONE DROPS
                drops -= 1
        #edegc ase last and first (last > first then drops -1)
        # if nums[-1] > nums[0]:
        #     drops -= 1 

        return False if drops < 0 else True





    def optimal_cal_2(self,nums):
        #chatgpt way of checking circular array
        drops = 1
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drops -= 1
        return False if drops < 0 else True
