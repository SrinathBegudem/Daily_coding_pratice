class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def optimal_sol():
            """
            The intuition here is 
            this sum can be optimally solved by hashmap and stack (monotnically decreasing)
            - first we create a nums1 val to indx map dict 
            - then we push all the min val into the stack and once the large val arraives we pop and set all the num indx to the next greater element 
            - so to find the indx we use num as key 
            Time and space 
            - time = o(nums1)
            - space = o(nums2)
            """
            res = [-1] * len(nums1)
            indx_num1 = {val : i for i,val in enumerate(nums1)} # to store the index of nums 1 for quick look up and updates
            # once we mapped the num1 nums to indx 
            # we iterate over the nums2 array find the next greatest element
            # we use monotnic stack to store all the num until the 
            stack = [] # monotonically decreasing stack
            stack.append(nums2[0])
            i = 1
            while i < len(nums2):
                while stack and stack[-1] < nums2[i]:
                    last = stack.pop()
                    if last in indx_num1:
                        indx = indx_num1[last] 
                        res[indx] = nums2[i]
                stack.append(nums2[i])
                i += 1
            return res




        def brute_force(sol):
            """
            Key points 
            - order matters (so we cannot sort)
            - for ever num in nums 1 we need to find its eq num in nums2 and find the next greater element
            - so i think no matter what we need to have nested for loop to solve this
            - lets have res var to kee ptrack of next greater element
            Time and space :
            Time = o(n1*n2)
            space = o(n1)
            """
            res = []

            for n1 in nums1:
                max_num = -1
                i = 0 
                while n1 != nums2[i]: # traverse until we find a match in nums2
                    i += 1
                # once found traverse the rest of the arr to find the next greater elem
                while i < len(nums2):
                    if nums2[i] > n1: # if exists 
                        max_num = nums2[i]
                        break 
                    i += 1
                res.append(max_num)     
            return res
                
                
            

            