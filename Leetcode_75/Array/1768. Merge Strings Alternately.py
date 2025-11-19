class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointer approch , use list for efficency
        # time = space = o(word1 + word2) 
        i = 0 
        j = 0 
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        

            #not recommendated 
            # if i <= j:
            #     res.append(word1[i])
            #     i += 1
            # else:
            #     res.append(word2[j])
            #     j += 1
        while i < len(word1): 
            res.append(word1[i])
            i += 1
        while j < len(word2):
            res.append(word2[j])
            j += 1
        return "".join(res)



        