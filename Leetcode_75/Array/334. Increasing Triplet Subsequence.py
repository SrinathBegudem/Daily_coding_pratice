class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
            """
            This problem can only be solved by greedy method 
            - we will traverse along the nums 
            - use the benefits of if elif else statement ( only one excutes in a loop and excutes in order)
            - we will have first num which is the smallest
            - we will have second num which is second smallest 
            - and comapre all nums once we find that there is a number bigger than first and second we return instantly


            The key idea is:
            - we update i and j when we see the smaller num so we have that range for k
            - Anything bigger than  j will be returned immediatly 
            - in process we update of i sometimes after j and this is fine , dont worry of breaking i < J < k because in the arr there is a pair that is less than j and before j ( the old pair )
            - so we only care about j and the nums after j for k to return true 
            - even if i becomes smaller and smaller we can about j in elif statemtn check it and if and only if the num greater than j then we return true
            - so intailly we will have i and j pair following i < j and nums[i] < nums[j], and after we dont care about i any more even if i udpates to smaller number and the i index is after j, we still have this intailly condition where i < j, so as we find the num greater than j we return true thats our k 
            Most optimal and greedy solution
            time,space = o(n),o(1)
            """
            # intialize the num at index i and j, as big as possible 
            num_i = float("inf") 
            num_j = float("inf")

            # traverse through the arr 
            for num in nums:
                #case1: if we encounter a num which is smaller than num_i, we update the num_i, and if statement excutes until i is set to smalles intially, after that once we encounter a num more than j than and only then num_j is updated so we have the intial condition i < j and nums[i] < nums[j]
                if num <= num_i:
                    num_i = num
                # once we encounter a num greater than num_i we update num_j and from then we never care about num of i being updated to smaller num than num_j and surpasses index nums of j because the intail condition (i<j and nums[i]<nums[j]) always exsits in arr, so now only care about num of j and above that num range for k 
                elif num <= num_j:
                    num_j = num
                # now once we found out the num which is greater than j (abv i too but we dont care), then we return because we encountered a pair which accepts the condition
                else:
                    return True
            return False
        



            
            
            
        