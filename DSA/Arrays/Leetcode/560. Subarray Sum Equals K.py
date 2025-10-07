class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        return self.optimal_sol_2(nums,k)

    def my_first_code(self,nums,k): #brute force, time = o(n**2) and space o(1)
        '''
        i tried to use nested loops and slide for each subarray and find the sum this logics seems okay and works as brute force sol and starting point passed 82/90 test cases and encountered time limit exceed error" 
        '''
        n = len(nums)
        count = 0
        for i in range(n):
            sum_num = 0
            for j in range(i,n):
                sum_num += nums[j]
                if sum_num == k:
                    count +=1
        return count 
    def optimal_sol_1(self,nums,k):
        '''
    this sol is said by strivers and neetcode where tehy cover the base case of cur sum == k by just adding count of 0 = 1 in the hashmap 

    let me explain a little bit about this case if we have lets say prefix_arr = [1,2,3,4] and the pointer is in indx 3 and k = 4 
    so we need to add the count += 1 but our forulae is 4-4 = 0 and if we dont add prefix_map[0] = 1 we will skip this count and this will fail our test cases so just to make sure if the cur prefix_sum directly equal to k we use that condition
        '''
        #create a var to store count, prefix_sum and hashmap 
        count = 0 
        prefix_sum = 0 
        prefix_map = {}
        prefix_map[0] = 1 # this is the edge case we are talking about this can be aviod in shradha didi code 
        for num in nums:
            prefix_sum += num
            val = prefix_sum - k # we are checking possible sub array starting points that is prefix[i-1]
            if val in prefix_map: # lets check if the target val is in prefix map if yes we directly add its count to our count
                count += prefix_map[val]
            if prefix_sum in prefix_map: # here we are checking the prefix sum exsists in our map or not lets say for case 
            # [1,2,0,0] ----> prefix = [1,2,2,2] so we can increase the count of 2 by 3 as there are 3 sub arrays with sum = 3 
                prefix_map[prefix_sum] += 1
            else: # if the prefix_sum is not there we just put it in our hash map so we can perform future lookup for our subarrays
                prefix_map[prefix_sum] = 1 
        return count
    def optimal_sol_2(self,nums,k):
        '''
        here we are going to use shradah didi approch little bit stragith forward and doesnt require of checking the edge case 
        prefix[0] = 1 as we directly check this in if condition so its safe compared to the case 1 optimal sol
        '''
        count = 0 
        prefix_sum = 0
        prefix_map = {}
        for num in nums:
            prefix_sum += num
            if prefix_sum == k: # this is the conditions i am talking about this will remove us adding prefix_map[0] = 1 
                count += 1
            # REST OF THE CODE IS SAME 
            val = prefix_sum - k 
            if val in prefix_map:
                count += prefix_map[val]
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1 
        return count


             



        
        