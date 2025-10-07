class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.medium_sol_fixed(nums)
        
    def brute_force(self,nums):
        """
        This code is just using 3 for loops and finding the sum and ading it to the list
        questions?
        do we need hash_map or hash_set or can it be done in constant space?
        answer : hash_set is needed, kep concpets about return type while using sorting
        time = o(n**3) obv TLE 
        space = o(n) 
        """
        n = len(nums)
        # result = []
        interim_result = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    three_sum = nums[i] + nums[j] + nums[k]
                    if three_sum == 0:
                        # sorting? because if you add the list in any order i mean
                        # lemme explain so [-1,1,0] and [1,-1,0] may not be hashed into #same bucket so sorting ensures they do certainly add towards the same hashbucket
                        #one more key concept sorted regarless of the iterable type will always return list
                        interim_result.add(tuple(sorted((nums[i],nums[j],nums[k]))))
        return [list(lst) for lst in interim_result]
            
    
    def medium_sol(self,nums):
        """
        Here we optimise our time complexity to reducing it to o(n**2) 
        for that we will use hash_map for quick lookups 
        hash_set for eliminating duplicated 
        we will use 2 for loops to get 2 vals and other val we will get by quick lookups 
        Time = o(n**2) suprisingly this also giving TLE
        Space = o(n)
        """
        n = len(nums)
        interim_result = set()
        # always try using list or dict comprehension to show how pythonic your code can look
        nums_map = {value:index for index,value in enumerate(nums)}
        # the above is wrong 
            #If a number appears multiple times, only the last index is stored.

            #So you may miss valid triplets or get wrong ones if i, j, or k overlap. use a set 
        for i in range(n):
            for j in range(i+1, n):
                complement = -(nums[i]+nums[j])
                if complement in nums_map:
                    k = nums_map[complement]
                    if i != k and j != k:
                        interim_result.add(tuple(sorted([nums[i],nums[j],complement])))
        return [list(lst) for lst in interim_result] # using list comprehension

    def medium_sol_fixed(self, nums): #still TLE
        n = len(nums)
        result = set()
        
        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(triplet)
                seen.add(nums[j])
        
        return [list(t) for t in result]


    def optimal_sol(self,nums):
        """
        Now we gonna optimise it more future using one for loop and two sum II solution i.e sorting and using left and right pointers
        time = o(n**2)
        space = o(1) if result is not counted and if they count result memory too then its gonna be o(n)
        wonder why this excecutes and the medium_sol doesn't even after having same time complexity if is skipping the duplicates vals is the key and lemme show you how that is achieved.
        I think this is the only way to escape from TLE we need to sort it in the begging to skip the repeated nums 
        """
        n = len(nums)
        result = []
        # we are going to sort the entire arr in place
        nums.sort()

        for i in range(n):
            # edge cases 
            if nums[i] > 0: # nums[i] > 0 means if the first sorted arr has positive val then there will not be any sol
                break 
            if n < 3: # if there are not enough nums to form triplets we simply return empty list 
                break
            if i > 0 and nums[i] == nums[i-1]: # skipping the repeated numbers 
                continue
            left = i+1
            right = n-1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    # found the triplets 
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    # skip the duplicates both left and right and to be hoenst you only need to take care of left and the 
                    # above if else statements gonna take care of right 
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
        return result


                
            



