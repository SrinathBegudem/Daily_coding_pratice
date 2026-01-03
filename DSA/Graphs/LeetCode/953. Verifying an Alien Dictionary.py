class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
# got code
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            decided = False

            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if rank[c1] > rank[c2]:
                    return False
                if rank[c1] < rank[c2]:
                    decided = True
                    break

            # if all compared chars equal, shorter word must come first
            if not decided and len(w1) > len(w2):
                return False

        return True






        # #my code
        # order = {v:indx for indx,v in enumerate(order)}

        # for i in range(1,len(words)):
        #     word1 = words[i-1]
        #     word2 = words[i]
        #     j,k = 0,0
        #     same = True
        #     while j < len(word1) and k < len(word2):
        #         char1 = word1[j]
        #         char2 = word2[k] 
        #         if order[char1] > order[char2]: return False
        #         elif order[char1] < order[char2]: 
        #             same = False
        #             break
        #         else:
        #             j += 1
        #             k += 1
        #     if same:
        #         if len(word1) > len(word2): return False

        # return True

