class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        """
        Key idea: Ans will be in the range of 1 to len(nums) -> [1,len(nums)+1]
        but we mark all the [1,n] and if all this are negative at the end we return len(nums) + 1 as answer
        """
        # Traversal 1:
        #first mark all negative number to zeros, because they can never be the output 
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        #traversal 2:
        #now traverse the arr to mark all indexs that that exisis in the arr, for ex if there is num 3 then jump to index -1 position and mark that num to negative of that number, so when we make one final traversal we know that this numebr exsisted.
        for i in range(n):
            val = abs(nums[i]) # becasue there might be change we might changed this to negative before reaching to this index so take abs 
            if 1 <= val <= n: # if num is in index range then procedd else skip
                if nums[val-1] < 0:
                    continue 
                elif nums[val-1] > 0:
                    nums[val-1] = - nums[val-1] # change the sign to mark as visited
                elif nums[val-1] == 0:
                    nums[val-1] = -(n+1) # if that position is negative then we would have turned it into zero, so , we assign a val outside the len of arr so it wont really distrub our desired output 
        
        # traversal 3: 
        #now travese from the num 1 to n to find out the first missing positive number 
        for i in range(1,n+1):
            if nums[i-1] >= 0: #make sure the index starts from zero but we ass as 1
                return i
        return n + 1 # if didnot return anything that means the last num is missing
        




#non optimal sorting sol 
        # nums.sort()
        # want = 1
        # for num in nums:
        #     if num < want:
        #         continue
        #     if num == want:
        #         want += 1
        # return want


# non optimal set solution 

        # seen = set(nums)
        # max_num = max(nums) if max(nums) > 0 else 1 we dont need max _num 
        # ans will be in the range of 1, len(a)
        # for i in range(1,max_num+2):
        #     if i not in seen:
        #         return i
        