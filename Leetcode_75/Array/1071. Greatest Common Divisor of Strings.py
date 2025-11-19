class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        The core concept is : (check depthi tulsera video)
        - They gave us str s is divisible if it composes of concat of t i.e s = t+t+t
        - so the condition here we have to check is 
        - lets assums for example2  s1 is made of 4 x concat and s2 is 2 cocat x where x = AB
        s1 = x + x + x + x and s2 = x + x 
        so to have check the str compatability 
        s1 + s2 = s2 + s1 which is (x + x + x + x) + (x + x) = (x + x) + (x + x + x + x)
        lets say if they have something like s1 = ABABABAC and s2 = ABAB
        then s1 = x + x + x + y and s2 = x + x 
        so to have check the str compatability (failed)
        s1 + s2 = s2 + s1 which is (x + x + x + y) + (x + x) = (x + x) + (y + x + x + x)
        so if this happens we return empty because there is no way we form the bot hstr using single div str
        After that
        - once we are done checking str compatabilty now we know there exists a certain len of str that div both 
        - we use gcd/hcf concept to get it out 
        - because we need largest str that div both, so indirectly they are asking us to get the hcf/gcf of 2 str
        The gcf can be found (brute force)
        traverse the len of min(s1,s2):
        then or each num see if the num divides both the s1 and s2 len but to find max we need to traverse till the end and have max var and update it as the bigger num satisfy the cond 
        - the better way would be start from end and try and see if we can find any largest num that divided both if yes return that
        The optimal way would be eculidiean gcd 
        - while b != 0: gcd(a,b) = gcd(b,a%b) # you can prove this by induction
        """
        #check the str compatability 
        if str1 +str2 != str2 + str1: 
            return ""
        
        def gcd(l1,l2):
            """
            Brute force code time = o(min(l1,l2))
            l1,l2 are len of str1 and str 2 
            """
            n = min(l1,l2)
            for i in range(n,0,-1): # we dont go till 0 because the smallest hcf can be 1 
                if l1%i ==0 and l2%i == 0:
                    return i
        def gcd_optimal(a,b):
            #eculidean formula
            while b != 0:
                a,b = b,a%b
            return a
        gcd = gcd(len(str1),len(str2))
        gcd_optimal = gcd_optimal(len(str1),len(str2))
        return str1[:gcd_optimal]


 




        