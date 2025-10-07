class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.sliding_window_sol(prices)

    def n_sqaure_sol(self,prices): # time = o(n**2)
        """
    This function simply checks the combination of each prices on each day and return the diff the profit, this is a brute force and easiest solution to come up with.
        """
        profit = 0
        n = len(prices)
        for i in range(n):
            cur_profit = 0
            for j in range(i,n):
                cur_profit = prices[j] - prices[i]
                if cur_profit > profit:
                    profit = cur_profit
                else:
                    continue
        return profit

    def optimal_sol(self,prices): # this is also and the below is also kadanes algo 
        """
        so here the logic is as you travser the prices you need to find the min price in that process and update it to a min_price variable then you traervse till you find the most profitable selling point the min price only updates if it finds min price than the exisiting one because in this sum we are going in one direction, i mean time travel only in one direction.
        time = o(n)
        space = o(1)
        i think this sum cannot be optimsed more.
        """
        min_price = float('inf')
        profit = 0 
        for price in prices:
            if price < min_price:
                min_price = price
            cur_profit  = price - min_price
            profit = max(profit,cur_profit)
        return profit 
    
    def sliding_window_sol(self,prices):
        """
        This sum can also be optimally solved using sliding window and this problem comes under sliding window conept though it can also directly solved without silding window, but learning sliding window helps.
        you will have two pointer left and right you but at the left and increae the right pointer until you find another indx where the prices are less than the cur left indx and update the left pointer to that postion and extend the window to find the max profit and parellely update the max profit 
        """
        left =0 
        right =1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit,max_profit)
            else:
                left = right # udpate to the new lowest point and try finding the max_profit if any 
            right += 1 # no matter what we increse our right pointer
        return max_profit

#-----------can also be solved like this---------------- kadane algo 
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit = prices[0]
        profit = 0 # because if no profit we return zero
        low = prices[0]
        for price in prices[1:]:
            cur_profit = price - low
            profit = max(cur_profit,profit)
            if price < low:
                low = price
            
            
        return profit 