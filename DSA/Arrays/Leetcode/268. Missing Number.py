class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        XOR is associative, commutative, and self-canceling (x ^ x = 0), you can reorder and cancel pairs.
        even if you do sequentially the end ans will be same as arrange all of them together reordering and canceling 
        properties :
        x^x = 0
        x^y = cal binary of x and y and then add the binary and then convert it into digits 
        0^0 =0
        1^1 = 0
        1^0 = 1
        0^1 = 1
        """

#-----------my first try-----------------------
        #space = time = o(N)
        # n = len(nums)
        # seen = [-1]*(n+1)
        # for num in nums:
        #     seen[num] = num
        # for i in range(len(seen)):
        #     if seen[i] == -1:
        #         return i 
#-------------optimal_sol_by_me-------------------------------
        n = len(nums) #o(1)
        max_val = max(max(nums),n) #o(n) # why i did this because sometimes max num from nums can be missing so we find len so the len can be the max num 
        sum_val = sum(nums) #o(n)
        total = max_val*(max_val + 1)//2 #o(1)
        return total - sum_val #o(1)

#-------------optimal_sol_by_me-------------------------------
        n = len(nums) #o(1)
        max_val = n #o(1) # or simply you coukd do is to but the len as max num
        sum_val = sum(nums) #o(n)
        total = max_val*(max_val + 1)//2 #o(1)
        return total - sum_val #o(1)
        
#-------------chatgpt suggest ------
#xor
    res = n # because we need to xor every num in that arr the for loops takes care of 0 - (n-1) the n is only missing so we assign n, because the idnex start from o and go all the way till n-1, so its is logical and that what question want us to do. assign res = n
    for i,v in enumerate(nums):
        res ^= i ^ v
    return res 