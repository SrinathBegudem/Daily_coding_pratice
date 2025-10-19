class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Similar to lc 392 do that before this 
        We are asked to make t sub seq of s 
        - same take one pointer for s and one pointer for t 
        - traverse both till one of the str is exhausted 
        -simly return the diff of len of t and its the now of index its pointer adavcanced
        - time = o(len(s)) You advance s1 every iteration and the loop runs at most len(s) times. (t1 only moves when there’s a match; it doesn’t add extra iterations.)
        - space = o(1)
        """
        t1 =0
        s1 = 0 
        #edge case : empty t str is always subeq of s 
        # if not t: # not needed
        #     return 0
        while t1 < len(t) and s1 < len(s):
            # increase the t pointer only if therr is a match in s
            if t[t1] == s[s1]:
                t1 += 1
            #move the s pointer until the match is found 
            s1 += 1
        # after the while loop is broken we take the char left out in t, if its a sub seq we return len(t) - t1 which is zero, else we return the num char that need to be appended to s str which the diff 
        return len(t) - t1 

        