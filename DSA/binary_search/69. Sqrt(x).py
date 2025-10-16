class Solution:
    def mySqrt(self, x: int) -> int:
        """
        s(1) = 1     
        s(2) = 1.414
        s(3) = 1.73.     3//2 + 1 = 2
        s(4) = 2
        s(5) = 2.
        s(6) = 2.
        s(7) = 2.
        s(8) = 2. 
        s(9) = 3 
        s(10) = 3.      10//2 + 6 = 6 
        the above is to show that sqrt of a num will be always less than or eq to  num//2 + 1, this helps us in micro optimisation instead of going all the way to n we can only do till n//2 + 1 to cut half of the time complexity 
        """
        def brute_force():
            #time = sqrt(n) ????? because at max we do sqrt(n) iterations 
            num = 1
            res = 1
            while res < x:
                num += 1
                res = num * num 
            return num if res == x else num - 1
        

        def optimal_sol():
            """
            classic Binary search take log n time 
            """
            lo = 0
            hi = x//2 + 1
            res = 0 
            while lo <= hi:
                mid = (lo+hi)//2
                sq = mid * mid
                if sq < x:
                    lo = mid + 1
                    res = mid # there might be a chance that this could be res if we break the loop ex 2 for sqrt(8)
                    # we store this val becase this is the floor of the val that is just less than x, i mean if there is no perfect sqaure the result gonna store just the floor that means the val which is less than the acutal true sq
                # for instance sq of 8 is 2.82 so result stores 2 whose true sq root is 4 thats exactly what they want us to return
                elif sq > x:
                    hi = mid - 1
                else:
                    return mid # directly found the sqrt 
            return res # if there is no sq root exisists 
        # return optimal_sol()


        def optimal_sol2():
            """
            Solving using upper boundary binary seaach pattern / right most occurence 
            things to rememeber
            lo = 0, hi = (x//2+1) + 1 # exclusve: one past the end 
            while left < right 
            use lo <= hi so we always go to the target next element
            return lo - 1 which is our ans
            """
            lo = 0 
            hi = (x//2+1) + 1
            while lo < hi:
                mid = (lo+hi)//2
                sq = mid**2
                if sq <= x: # ← KEY: use <= (include equals!)
                    lo = mid + 1
                else:
                    hi = mid
            # lo now points to FIRST integer where sq > x
            # So the answer is lo - 1
            return lo -1 
        return optimal_sol2()




        