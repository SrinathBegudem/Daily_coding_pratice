class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def brute_force():
            """
            time = o(n) and space = o(1)
            the intuition i will start from 1 and go to all the way till the num to find the perfect sqaure its linear sol
            """
            start = 1 
            res = start*start 
            while res <= num:
                res = start*start 
                if res == num:
                    return True
                start += 1
            return False
        # return brute_force()

        def optimal_sol():
            """
            time = o(logn),space = o(1)
            instead of linear search we can do bianry search and rapidly reduce the search space 
            """
            lo = 1
            # hi = num this wokrs but the below is micro optimzation that optimise the code more 
            hi = num//2 + 1  # No need to check beyond num/2 for large nums (always true )
            while lo <= hi:
                mid = (lo+hi)//2
                res = mid * mid
                if res == num:
                    return True
                elif res < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False 
        return optimal_sol()




        