class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        This can be optimally solved with kmp and rabin karp algo (which are very hard so skip)
        - if we sovle using in operator the time compelxity would be o(n^2 * l) because it internally used kmp or rabin karp algo and highly optimised.
        - if create a manually is_subrstring fucntion it would be  o(n^2 * l^2)
        """
        def optimal_sol():
            res = []
            for i in range(len(words)):
                for j in range(len(words)):
                    if i != j and words[i] in words[j]:
                        res.append(words[i])
                        break
            return res
        return optimal_sol()

        def brute_force():
            res = []
            def is_substring(small, big):
                for i in range(len(big) - len(small) + 1): # o(L)
                    if big[i:i + len(small)] == small: # o(L^2)
                        return True
                return False
            
            for i in range(len(words)): # o(n)
                for j in range(len(words)): #o(n^2)
                    if i != j and len(words[i]) <= len(words[j]):
                        # check if substr
                        if is_substring(words[i],words[j]):
                            res.append(words[i])
                            break
            return res


