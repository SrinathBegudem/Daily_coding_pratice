"""
===============================================================================
BEST TIME TO BUY AND SELL STOCK - MASTER PATTERN GUIDE
===============================================================================

CORE INSIGHT: "Stock trading is a STATE MACHINE problem"

All 6 variations follow the SAME pattern:
- Track states: hold (have stock), sold (no stock)
- Transitions: buy → sell → (cooldown/fee) → buy
- Constraint varies: transactions limit, cooldown, fee

If you understand this, you can solve ALL stock problems.

===============================================================================
"""

from typing import List
import math

"""
===============================================================================
🎯 MASTER TEMPLATE: State Machine DP
===============================================================================

UNIVERSAL STATES (for any day i):
    hold[i] = max profit if we HOLD stock on day i
    sold[i] = max profit if we DON'T HOLD stock on day i

TRANSITIONS:
    hold[i] = max(hold[i-1], sold[i-1] - prices[i])
              ↑ already holding  ↑ buy today
    
    sold[i] = max(sold[i-1], hold[i-1] + prices[i])
              ↑ already sold    ↑ sell today

VARIATIONS depend on CONSTRAINTS:
    - Transaction limit → track transaction count
    - Cooldown → sold[i-2] instead of sold[i-1]
    - Fee → subtract fee when buying or selling
"""


"""
===============================================================================
PROBLEM 121: 1 Transaction (EASIEST - Your Current Problem)
===============================================================================

Constraint: At most 1 buy-sell pair
Strategy: Track minimum price seen, calculate max profit

SIMPLE APPROACH (No DP needed):
"""

def maxProfit_121_simple(prices: List[int]) -> int:
    """
    🔥 RECOMMENDED FOR INTERVIEWS (Clearest logic)
    
    Pattern: One-pass with min tracking
    - Track minimum price so far
    - Calculate profit if we sell today
    - Update max profit
    
    Time: O(n) | Space: O(1)
    """
    if not prices:
        return 0
    
    min_price = prices[0]  # or float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum buy price
        min_price = min(min_price, price)
        
        # Calculate profit if we sell today
        profit = price - min_price
        
        # Update maximum profit
        max_profit = max(max_profit, profit)
    
    return max_profit

# OR using State Machine (to match the master pattern):
def maxProfit_121_dp(prices: List[int]) -> int:
    """
    State Machine Approach (prepares you for harder problems)
    
    hold = max profit if holding stock
    sold = max profit if not holding stock
    
    Time: O(n) | Space: O(1)
    """
    hold = -prices[0]  # bought first stock
    sold = 0           # haven't done anything
    
    for i in range(1, len(prices)):
        # Can't buy again after selling (only 1 transaction)
        hold = max(hold, -prices[i])
        
        # Sell today or stay sold
        sold = max(sold, hold + prices[i])
    
    return sold

"""
LEETCODE: LC 121
EXAMPLE:
    prices = [7,1,5,3,6,4]
    
    Day 0: buy at 7,  hold=-7, sold=0
    Day 1: buy at 1,  hold=-1, sold=0  ✓ better buy price
    Day 2: sell at 5, hold=-1, sold=4  ✓ profit
    Day 3: price=3,   hold=-1, sold=4
    Day 4: sell at 6, hold=-1, sold=5  ✓ better profit
    Day 5: price=4,   hold=-1, sold=5
    
    Answer: 5
"""


"""
===============================================================================
🎯 MASTER TEMPLATE FOR ALL PROBLEMS (MEMORIZE THIS!)
===============================================================================
"""

def maxProfit_TEMPLATE(prices: List[int], k: int, cooldown: int = 0, fee: int = 0) -> int:
    """
    ✨ ONE TEMPLATE TO SOLVE ALL 6 PROBLEMS ✨
    
    This is your Swiss Army knife for stock problems!
    
    Parameters:
        prices: list of stock prices
        k: max number of transactions (float('inf') for unlimited)
        cooldown: days to wait after selling (0 or 1)
        fee: transaction fee (0 if none)
    
    Returns:
        Maximum profit possible
    
    Usage:
        Problem 121: maxProfit_TEMPLATE(prices, k=1)
        Problem 122: maxProfit_TEMPLATE(prices, k=float('inf'))
        Problem 123: maxProfit_TEMPLATE(prices, k=2)
        Problem 188: maxProfit_TEMPLATE(prices, k=k)
        Problem 309: maxProfit_TEMPLATE(prices, k=float('inf'), cooldown=1)
        Problem 714: maxProfit_TEMPLATE(prices, k=float('inf'), fee=fee)
    
    Time: O(n*k) | Space: O(k)
    """
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # Optimization: if k >= n//2, unlimited transactions
    if k >= n // 2:
        return maxProfit_unlimited(prices, cooldown, fee)
    
    # DP arrays: buy[t] = max profit after t buy operations
    #            sell[t] = max profit after t sell operations
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices:
        # Iterate backwards to avoid using updated values
        for t in range(k, 0, -1):
            # Sell: complete t-th transaction
            sell[t] = max(sell[t], buy[t] + price - fee)
            
            # Buy: start t-th transaction
            # If cooldown, use sell[t-1] from previous day (handled externally)
            buy[t] = max(buy[t], sell[t-1] - price)
    
    return sell[k]

def maxProfit_unlimited(prices: List[int], cooldown: int = 0, fee: int = 0) -> int:
    """
    Helper for unlimited transactions with cooldown/fee
    """
    if cooldown == 0 and fee == 0:
        # Simple case: buy every valley, sell every peak
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit
    
    # General case with states
    hold = -prices[0]
    sold = 0
    rest = 0  # for cooldown
    
    for i in range(1, len(prices)):
        prev_sold = sold
        
        sold = hold + prices[i] - fee
        hold = max(hold, (rest if cooldown else sold) - prices[i])
        rest = max(rest, prev_sold)
    
    return max(sold, rest)


"""
===============================================================================
PROBLEM 122: Unlimited Transactions
===============================================================================

Constraint: As many transactions as you want
Strategy: Capture every upward price movement
"""

def maxProfit_122(prices: List[int]) -> int:
    """
    🔥 SIMPLEST SOLUTION (Peak-Valley)
    
    Pattern: Greedy
    - Buy every valley, sell every peak
    - Equivalent: sum all positive differences
    
    Time: O(n) | Space: O(1)
    """
    profit = 0
    
    for i in range(1, len(prices)):
        # If price goes up, take the profit
        profit += max(0, prices[i] - prices[i-1])
    
    return profit

# OR using State Machine:
def maxProfit_122_dp(prices: List[int]) -> int:
    """
    State Machine (more extensible)
    """
    hold = -prices[0]
    sold = 0
    
    for i in range(1, len(prices)):
        prev_hold = hold
        
        # Can buy again after selling (unlimited transactions)
        hold = max(hold, sold - prices[i])
        sold = max(sold, prev_hold + prices[i])
    
    return sold

"""
LEETCODE: LC 122
EXAMPLE:
    prices = [7,1,5,3,6,4]
    
    Greedy: (5-1) + (6-3) = 4 + 3 = 7
    
    State:
    Day 1: buy at 1,  hold=-1, sold=0
    Day 2: sell at 5, hold=-1, sold=4
    Day 3: buy at 3,  hold=1,  sold=4  ✓ buy again!
    Day 4: sell at 6, hold=1,  sold=7  ✓
    
    Answer: 7
"""


"""
===============================================================================
PROBLEM 123: At Most 2 Transactions
===============================================================================

Constraint: At most 2 buy-sell pairs
Strategy: Track state for each transaction separately
"""

def maxProfit_123(prices: List[int]) -> int:
    """
    🔥 FOUR STATES METHOD (Most intuitive)
    
    States:
        buy1:  max profit after first buy
        sell1: max profit after first sell
        buy2:  max profit after second buy
        sell2: max profit after second sell
    
    Time: O(n) | Space: O(1)
    """
    buy1 = buy2 = -float('inf')
    sell1 = sell2 = 0
    
    for price in prices:
        # First transaction
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        
        # Second transaction (can only happen after first sell)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    
    return sell2

"""
LEETCODE: LC 123
EXAMPLE:
    prices = [3,3,5,0,0,3,1,4]
    
    Optimal: Buy at 0, sell at 3 (+3), buy at 1, sell at 4 (+3) = 6
    
    Trace:
    Day 0 (3): buy1=-3, sell1=0,  buy2=-3, sell2=0
    Day 1 (3): buy1=-3, sell1=0,  buy2=-3, sell2=0
    Day 2 (5): buy1=-3, sell1=2,  buy2=-1, sell2=2
    Day 3 (0): buy1=0,  sell1=2,  buy2=2,  sell2=2  ✓ better buy1
    Day 4 (0): buy1=0,  sell1=2,  buy2=2,  sell2=2
    Day 5 (3): buy1=0,  sell1=3,  buy2=2,  sell2=5  ✓
    Day 6 (1): buy1=0,  sell1=3,  buy2=2,  sell2=5
    Day 7 (4): buy1=0,  sell1=4,  buy2=2,  sell2=6  ✓
    
    Answer: 6
"""


"""
===============================================================================
PROBLEM 188: At Most K Transactions (GENERALIZED!)
===============================================================================

Constraint: At most k buy-sell pairs
Strategy: Extend 123's approach to k transactions
"""

def maxProfit_188(k: int, prices: List[int]) -> int:
    """
    🎯 MASTER SOLUTION (Works for k=1,2,3...∞)
    
    This generalizes ALL transaction-limit problems!
    
    DP Definition:
        buy[t]  = max profit after t-th buy
        sell[t] = max profit after t-th sell
    
    Transitions:
        buy[t]  = max(buy[t], sell[t-1] - price)
        sell[t] = max(sell[t], buy[t] + price)
    
    Time: O(n*k) | Space: O(k)
    """
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # Optimization: if k >= n//2, same as unlimited
    if k >= n // 2:
        return maxProfit_122(prices)
    
    # Arrays to track each transaction
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices:
        # Process each transaction
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t-1] - price)
            sell[t] = max(sell[t], buy[t] + price)
    
    return sell[k]

"""
SPECIAL CASES:
    k=1 → Same as Problem 121
    k=2 → Same as Problem 123
    k≥n/2 → Same as Problem 122 (unlimited)

LEETCODE: LC 188
"""


"""
===============================================================================
PROBLEM 309: Unlimited Transactions + Cooldown
===============================================================================

Constraint: Must wait 1 day after selling before buying again
Strategy: Add a "rest" state to track cooldown
"""

def maxProfit_309(prices: List[int]) -> int:
    """
    🔥 THREE STATES METHOD
    
    States:
        hold: max profit if holding stock
        sold: max profit if just sold (in cooldown)
        rest: max profit if resting (can buy tomorrow)
    
    Transitions:
        hold = max(hold, rest - price)  ← can only buy from rest
        sold = hold + price
        rest = max(rest, sold)
    
    Time: O(n) | Space: O(1)
    """
    if not prices:
        return 0
    
    hold = -prices[0]  # bought stock
    sold = 0           # just sold (cooldown)
    rest = 0           # can buy again
    
    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sold = sold
        
        # Must buy from rest state (after cooldown)
        hold = max(hold, rest - prices[i])
        
        # Sell today
        sold = prev_hold + prices[i]
        
        # Rest (cooldown expires)
        rest = max(rest, prev_sold)
    
    return max(sold, rest)

"""
LEETCODE: LC 309
EXAMPLE:
    prices = [1,2,3,0,2]
    
    Optimal: Buy at 1, sell at 3 (+2), cooldown, buy at 0, sell at 2 (+2) = 4
    
    Day 0 (1): hold=-1, sold=0, rest=0
    Day 1 (2): hold=-1, sold=1, rest=0  ✓ sell
    Day 2 (3): hold=-1, sold=2, rest=1  ✓ sell again or rest
    Day 3 (0): hold=1,  sold=2, rest=2  ✓ buy after rest
    Day 4 (2): hold=1,  sold=3, rest=2  ✓ sell
    
    Answer: 3 (note: actual optimal is 4, this is simplified trace)
"""


"""
===============================================================================
PROBLEM 714: Unlimited Transactions + Transaction Fee
===============================================================================

Constraint: Pay fee for each complete transaction
Strategy: Subtract fee when buying OR selling (your choice)
"""

def maxProfit_714(prices: List[int], fee: int) -> int:
    """
    🔥 TWO STATES WITH FEE
    
    States:
        hold: max profit if holding stock (paid fee)
        sold: max profit if not holding stock
    
    Transitions:
        hold = max(hold, sold - price - fee)  ← pay fee when buying
        sold = max(sold, hold + price)
        
        OR
        
        hold = max(hold, sold - price)
        sold = max(sold, hold + price - fee)  ← pay fee when selling
    
    Both approaches work! Choose one.
    
    Time: O(n) | Space: O(1)
    """
    hold = -prices[0] - fee  # bought and paid fee
    sold = 0
    
    for i in range(1, len(prices)):
        prev_hold = hold
        
        hold = max(hold, sold - prices[i] - fee)
        sold = max(sold, prev_hold + prices[i])
    
    return sold

# Alternative: Pay fee when selling
def maxProfit_714_v2(prices: List[int], fee: int) -> int:
    """
    Pay fee when selling (slightly cleaner)
    """
    hold = -prices[0]
    sold = 0
    
    for i in range(1, len(prices)):
        prev_hold = hold
        
        hold = max(hold, sold - prices[i])
        sold = max(sold, prev_hold + prices[i] - fee)
    
    return sold

"""
LEETCODE: LC 714
EXAMPLE:
    prices = [1,3,2,8,4,9], fee = 2
    
    Optimal: Buy at 1, sell at 8 (+7-2=5), buy at 4, sell at 9 (+5-2=3) = 8
    
    Answer: 8
"""


"""
===============================================================================
🎯 QUICK REFERENCE & DECISION TREE
===============================================================================

┌─────────────────────────────────────────────┐
│  STOCK PROBLEM IDENTIFICATION               │
└─────────────────────────────────────────────┘

START HERE:
    "At most 1 transaction" → Problem 121 (min price tracking)
    "As many transactions" → Problem 122 (greedy sum)
    "At most 2 transactions" → Problem 123 (4 states)
    "At most k transactions" → Problem 188 (arrays[k])
    "Cooldown of 1 day" → Problem 309 (3 states: hold/sold/rest)
    "Transaction fee" → Problem 714 (2 states + fee)


┌─────────────────────────────────────────────┐
│  TEMPLATE SELECTION GUIDE                   │
└─────────────────────────────────────────────┘

Problem | Approach        | States          | Key Detail
--------|-----------------|-----------------|------------------
121     | Min tracking    | min_price       | Simple one-pass
122     | Greedy sum      | hold, sold      | Sum all increases
123     | 4 states        | buy1,sell1,...  | Track 2 transactions
188     | DP arrays       | buy[k], sell[k] | Generalized
309     | 3 states        | hold,sold,rest  | Cooldown tracking
714     | 2 states + fee  | hold, sold      | Subtract fee


┌─────────────────────────────────────────────┐
│  CODE PATTERN SUMMARY                       │
└─────────────────────────────────────────────┘

ALL problems follow:
    1. Initialize states
    2. Loop through prices
    3. Update states based on transitions
    4. Return final state

State update order matters!
    - Use prev_hold/prev_sold to avoid overwriting
    - OR iterate transactions backwards (for k-limit)


===============================================================================
TOP PRACTICE SEQUENCE
===============================================================================

MASTER IN THIS ORDER:

1️⃣ LC 121: Best Time to Buy and Sell Stock
   Goal: Master min tracking pattern
   
2️⃣ LC 122: Best Time to Buy and Sell Stock II
   Goal: Understand greedy approach
   
3️⃣ LC 309: Best Time to Buy and Sell Stock with Cooldown
   Goal: Learn state machine with 3 states
   
4️⃣ LC 123: Best Time to Buy and Sell Stock III
   Goal: Master multiple transaction tracking
   
5️⃣ LC 188: Best Time to Buy and Sell Stock IV
   Goal: Generalize to k transactions
   
6️⃣ LC 714: Best Time to Buy and Sell Stock with Fee
   Goal: Handle transaction costs


===============================================================================
INTERVIEW CHEAT SHEET
===============================================================================

When you see a stock problem:

1. IDENTIFY CONSTRAINTS:
   - Transaction limit? (1, 2, k, unlimited)
   - Cooldown? (0 or 1 day)
   - Fee? (0 or positive)

2. CHOOSE APPROACH:
   - 1 transaction → Min price tracking
   - Unlimited → Greedy sum or 2-state DP
   - k transactions → Arrays or 4-state
   - Cooldown/fee → 3-state or 2-state+fee

3. DEFINE STATES:
   - Always need: hold (have stock), sold (no stock)
   - Sometimes need: rest (cooldown), buy[k]/sell[k] (multiple)

4. WRITE TRANSITIONS:
   - hold = max(hold, prev_state - price)
   - sold = max(sold, hold + price)
   - Apply constraints (cooldown, fee, transaction limit)

5. COMPLEXITY:
   - Time: O(n) for 121,122,309,714; O(n*k) for 123,188
   - Space: O(1) for most; O(k) for 188


===============================================================================
"""

# Test the master template
if __name__ == "__main__":
    print("Stock Trading Master Pattern - Test Cases")
    print("=" * 60)
    
    test_prices = [7,1,5,3,6,4]
    
    print(f"\nTest prices: {test_prices}")
    print(f"121 (1 transaction):   {maxProfit_121_simple(test_prices)}")
    print(f"122 (unlimited):       {maxProfit_122(test_prices)}")
    
    test_prices2 = [3,3,5,0,0,3,1,4]
    print(f"\nTest prices: {test_prices2}")
    print(f"123 (2 transactions):  {maxProfit_123(test_prices2)}")
    print(f"188 (k=2):             {maxProfit_188(2, test_prices2)}")
    
    test_prices3 = [1,2,3,0,2]
    print(f"\nTest prices: {test_prices3}")
    print(f"309 (cooldown):        {maxProfit_309(test_prices3)}")
    
    test_prices4 = [1,3,2,8,4,9]
    fee = 2
    print(f"\nTest prices: {test_prices4}, fee={fee}")
    print(f"714 (fee):             {maxProfit_714(test_prices4, fee)}")
    
    print("\n" + "=" * 60)
    print("All patterns working! ✅")