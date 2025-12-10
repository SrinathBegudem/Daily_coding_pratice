class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        concept 
        ex:1
        [1,2,3,4]

        prefix =  [1, 2, 6, 24]
        postfix = [24, 24, 12, 4]

        build the prefix res arr
        and start from reverse and build the postfix and mutiple it to the prefix 
        res = [24,12,8,6]
        """
        n = len(nums)
        res = [1] * n 

        prefix = 1 
        # we are storing prefix up until that index in that index 
        # for ex prefix of index 0 will be ele left side no elemts so 1 
        #prefix of index 1 = left(1) and prefix[0](1) we store that in that index so we are skipping that particular index not mutiplying the num in that index
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        #res = [1,1,2,6]

        postfix = 1
        for i in range(n-1,-1,-1):
            # so for the last num we are just mutiplying it with 1 and prefix last index
            res[i] *= postfix
            postfix *= nums[i]
        return res

        









# # the below code first build the post fix and starts with prefix while traversing but they mention that in standard process we build prefix and mutiple it with postfix 

#         n = len(nums)
#         # bulding the res as postfix arr 
#         postfix = [1] * n
#         for i in range(n-1,-1,-1):
#             if i == n-1:
#                 postfix[i] = nums[i]
#             else:
#                 postfix[i] = postfix[i+1] * nums[i]
#         print(postfix)

#         prefix = 1 
#         n = len(nums) - 1
#         for i in range(len(nums)):
#             if i+1 == len(nums):
#                 postfix[i] = prefix
#                 return postfix
#             else:  
#                 postfix[i] = prefix * postfix[i+1]
#             prefix *= nums[i]
        

# # [1,2,3,4]

# # prefix =  [1, 2, 6, 24]
# # postfix = [24, 24, 12, 4]

# # if i == 0: res[i] = 1 * postfix[i+1]

# # if i >= len(nums): res[i] = prefix[i-1] * 1

# # res[i] = prefix[i-1] * postfix[i+1]

# # res = [24,12,8,6]

# # our approch will be we will build the res as postfix array