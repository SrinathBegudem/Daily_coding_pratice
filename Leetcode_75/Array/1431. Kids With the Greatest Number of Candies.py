class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # time = o(n), space = o(n)


        res = [] # o(n)
        #traverse once to find out the greatest no candies a person have in given arr
        max_candies = max(candies) #o(n) 
        # for candie in candies:
        #     if candie > max_candies:
        #         max_candies = candie

        # loop through the arr to form the boolean res arr 
        for candie in candies: # o(n)
            cur_max = candie + extraCandies
            # if cur_max >= max_candies:
            #     res.append(True)
            # else:
            #     res.append(False)
            res.append(cur_max >= max_candies)
        return res

        # pythonic way 
        # max_candies = max(candies)
        # return [c+extraCandies >= max_candies for c in candies]
