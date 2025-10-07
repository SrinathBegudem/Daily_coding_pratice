class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        the inuition here is to use sort + queue 
        sorting gives you [2,3,5,7,11,13,17] now this is not we want in the output but this is the order expected when we follow the rules that is draw one and reveal it and then put the next at the botton so the order we draw should be incresing so we have to arrange this in an order so that when we follow the rules we get increasing order.
        for that we are goung to use queue, we popleft the first index and then reavel it and push the next index to the end of the queue 
        we repaet this until nothing is left in queue. this works we are pushing indexs not the num in that indexs
        """
        from collections import deque
        # lets sort the input deck 
        deck.sort()
        n = len(deck)
        # created a res list of len n
        res = [0]*n
        # create a deque of indexs from 0 to range(n)
        idx = deque(range(n)) # or simply deque(range(n))
        for i in deck:
            # pop and reaveal the num
            q = idx.popleft()
            res[q] = i
            # push the next num back to end of the deck 
            if idx:
                i.append(idx.popleft())
        return res

            




        