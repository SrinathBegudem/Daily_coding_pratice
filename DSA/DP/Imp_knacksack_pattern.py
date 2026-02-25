from typing import List

"""
═══════════════════════════════════════════════════════════════════════════════
              KNAPSACK DP MASTERY GUIDE (0/1 + UNBOUNDED)
═══════════════════════════════════════════════════════════════════════════════

🎯 TWO PROBLEM TYPES:

   0/1 KNAPSACK: Each item can be used AT MOST ONCE
   - "Pick or skip this item, move on either way"
   - take = val[i] + dp(i-1, rem - wt[i])   ← move to i-1 after taking
   
   UNBOUNDED KNAPSACK: Each item can be used UNLIMITED times
   - "Pick this item and STAY, or skip and move on"
   - take = val[i] + dp(i, rem - wt[i])     ← STAY at i after taking

═══════════════════════════════════════════════════════════════════════════════

🎯 TWO CODING STYLES:

   STYLE A — "MY VERSION" (index-based base case):
   - i goes from 0 to n-1
   - Base case: i == 0 means "we are AT index 0" (still have 1 item to consider)
   - At i == 0, we handle the first item explicitly
   - Top-level call: solve(n-1, capacity)
   
   STYLE B — "STANDARD VERSION" (size-based base case):
   - i goes from 0 to n (where i represents "first i items available")
   - Base case: i == 0 means "NO items left to consider" → return 0
   - Items accessed as items[i-1] (1-indexed logic)
   - Top-level call: solve(n, capacity)

═══════════════════════════════════════════════════════════════════════════════

🔥 THE CRITICAL SPACE OPTIMIZATION DIFFERENCE:

   0/1 KNAPSACK → 1D array, inner loop goes BACKWARDS (right to left)
   ─────────────────────────────────────────────────────────────────
   WHY? Because dp[i][w] depends on dp[i-1][w - wt[i]]
        When we flatten to 1D, dp[w] = old dp[i-1][w]
        If we go LEFT to RIGHT, we'd overwrite dp[w - wt[i]] BEFORE
        we need its OLD value → we'd accidentally use the SAME row
        (i.e., use the item twice!)
        Going RIGHT to LEFT ensures we read old values before overwriting.

   UNBOUNDED KNAPSACK → 1D array, inner loop goes FORWARDS (left to right)
   ─────────────────────────────────────────────────────────────────
   WHY? Because dp[i][w] depends on dp[i][w - coins[i]] (SAME row!)
        We WANT the updated value from the current row.
        Going LEFT to RIGHT means dp[w - coins[i]] is already updated
        for this row, which is exactly what we need (reuse same item).

   VISUAL:
   
   0/1 Knapsack (backward):
   dp = [0, 0, 0, 0, 5, 5, 5]
                  ←←←←←←←←←←  (read old values on the left)
   
   Unbounded (forward):
   dp = [0, 3, 6, 9, ?, ?, ?]
         →→→→→→→→→→→→→→→→→  (read UPDATED values on the left = reuse)

═══════════════════════════════════════════════════════════════════════════════

📝 RUNNING EXAMPLE FOR ALL 16 FUNCTIONS:

   0/1 KNAPSACK EXAMPLE:
   weights = [1, 3, 4, 5]
   values  = [1, 4, 5, 7]
   capacity = 7
   
   Answer: 9 (take items with wt=3,val=4 and wt=4,val=5)
   
   UNBOUNDED KNAPSACK EXAMPLE (Coin Change - minimum coins):
   coins  = [1, 3, 4]
   amount = 6
   
   Answer: 2 (use coin 3 twice: 3+3=6)

═══════════════════════════════════════════════════════════════════════════════
"""


# ═══════════════════════════════════════════════════════════════════════════
# ███████████████████████████████████████████████████████████████████████████
#
#                    PART 1: 0/1 KNAPSACK
#
#   Each item used AT MOST ONCE.
#   When we TAKE item i, we move to i-1 (can't reuse i).
#
#   Recurrence:
#     skip = dp(i-1, w)
#     take = val[i] + dp(i-1, w - wt[i])   if w >= wt[i]
#     dp(i, w) = max(skip, take)
#
# ███████████████████████████████████████████████████████████████████████████
# ═══════════════════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────────────────
# SECTION A: 0/1 KNAPSACK — MY VERSION (i==0 means "at index 0")
# ───────────────────────────────────────────────────────────────────────────
"""
📝 DRY RUN — MY VERSION BASE CASE:

   weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7

   When i == 0, we are looking at the FIRST item (wt=1, val=1).
   We can either take it (if capacity allows) or skip it.
   
   Base case i == 0:
     if w >= weights[0]: return values[0]   (take the single item)
     else:               return 0           (can't fit it)
   
   This is slightly more work at the base but means our indices
   directly map to the array: coins[i], weights[i], values[i].
"""


def knapsack_01_myversion_memo(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 1/16: 0/1 Knapsack — My Version — Memoization
    
    📝 DRY RUN:
    weights = [1, 3, 4, 5], values = [1, 4, 5, 7], W = 7
    
    solve(3, 7):                              # considering item 3 (wt=5, val=7)
      skip = solve(2, 7)                      # skip item 3
        solve(2, 7):                          # considering item 2 (wt=4, val=5)
          skip = solve(1, 7)                  # skip item 2
            solve(1, 7):                      # considering item 1 (wt=3, val=4)
              skip = solve(0, 7) = 1          # base: wt[0]=1 <= 7, return val[0]=1
              take = 4 + solve(0, 4) = 4+1=5  # take item 1, then base: wt[0]=1<=4
              return max(1, 5) = 5
          take = 5 + solve(1, 3)              # take item 2
            solve(1, 3):
              skip = solve(0, 3) = 1
              take = 4 + solve(0, 0) = 4+0=4  # wt[0]=1<=0? NO → but rem=0, base=0
              return max(1, 4) = 4
          return max(5, 5+4) = max(5, 9) = 9
      take = 7 + solve(2, 2)                  # take item 3 (7 - 5 = 2 remaining)
        solve(2, 2):                          # wt[2]=4 > 2, can't take
          skip = solve(1, 2)
            solve(1, 2): wt[1]=3 > 2, can't take
              skip = solve(0, 2) = 1          # wt[0]=1 <= 2
              return 1
          return 1
        return 7 + 1 = 8
      return max(9, 8) = 9 ✓
    """
    n = len(weights)
    cache = {}

    def solve(i, w):
        # Base case: at index 0, decide for the first item only
        if i == 0:
            return values[0] if w >= weights[0] else 0

        if (i, w) in cache:
            return cache[(i, w)]

        # Option 1: Skip item i
        skip = solve(i - 1, w)

        # Option 2: Take item i (if it fits)
        take = -1
        if w >= weights[i]:
            # 0/1: move to i-1 after taking (can't reuse)
            take = values[i] + solve(i - 1, w - weights[i])

        cache[(i, w)] = max(skip, take)
        return cache[(i, w)]

    return solve(n - 1, capacity)


def knapsack_01_myversion_2d_dp(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 2/16: 0/1 Knapsack — My Version — 2D DP Table
    
    dp[i][w] = max value using items 0..i with capacity w
    
    📝 TABLE CONSTRUCTION (weights=[1,3,4,5], values=[1,4,5,7], W=7):
    
    Row i=0 (only item 0, wt=1, val=1):
      w:  0  1  2  3  4  5  6  7
          0  1  1  1  1  1  1  1    ← can take item 0 if w >= 1
    
    Row i=1 (items 0-1, adding wt=3, val=4):
      w:  0  1  2  3  4  5  6  7
          0  1  1  4  5  5  5  5
          w=3: max(skip=1, take=4+dp[0][0]=4) = 4
          w=4: max(skip=1, take=4+dp[0][1]=5) = 5
    
    Row i=2 (items 0-2, adding wt=4, val=5):
      w:  0  1  2  3  4  5  6  7
          0  1  1  4  5  6  6  9
          w=4: max(skip=1, take=5+dp[1][0]=5) = 5  → actually max(5,5)=5... 
          w=7: max(skip=5, take=5+dp[1][3]=5+4=9) = 9 ✓
    
    Row i=3 (items 0-3, adding wt=5, val=7):
      w:  0  1  2  3  4  5  6  7
          0  1  1  4  5  7  8  9
          w=7: max(skip=9, take=7+dp[2][2]=7+1=8) = 9
    
    Answer: dp[3][7] = 9 ✓
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # Base case: row i=0 (only the first item available)
    for w in range(capacity + 1):
        if w >= weights[0]:
            dp[0][w] = values[0]
        # else dp[0][w] remains 0

    # Fill remaining rows
    for i in range(1, n):
        for w in range(capacity + 1):
            skip = dp[i - 1][w]

            take = -1
            if w >= weights[i]:
                # 0/1: look at previous row (i-1) after taking
                take = values[i] + dp[i - 1][w - weights[i]]

            dp[i][w] = max(skip, take)

    return dp[n - 1][capacity]


def knapsack_01_myversion_prev_cur(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 3/16: 0/1 Knapsack — My Version — Two 1D Arrays (prev + cur)
    
    Key observation: dp[i][w] only depends on dp[i-1][...] (previous row).
    So we only need TWO rows at any time: prev (row i-1) and cur (row i).
    
    This is a direct translation of the 2D solution:
      dp[i-1][w]           → prev[w]
      dp[i][w]             → cur[w]
      After each row: prev = cur
    
    Space: O(W) instead of O(n * W)
    """
    n = len(weights)
    prev = [0] * (capacity + 1)

    # Base case: row i=0
    for w in range(capacity + 1):
        if w >= weights[0]:
            prev[w] = values[0]

    for i in range(1, n):
        cur = [0] * (capacity + 1)
        for w in range(capacity + 1):
            skip = prev[w]

            take = -1
            if w >= weights[i]:
                take = values[i] + prev[w - weights[i]]

            cur[w] = max(skip, take)
        prev = cur

    return prev[capacity]


def knapsack_01_myversion_1d_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 4/16: 0/1 Knapsack — My Version — Single 1D Array (BACKWARD loop)
    
    🔥 THE KEY INSIGHT — WHY BACKWARD?
    
    In 0/1 knapsack: take = values[i] + dp[i-1][w - weights[i]]
    We need the PREVIOUS row's value at position (w - weights[i]).
    
    If we loop LEFT to RIGHT:
      When computing dp[w], dp[w - weights[i]] has ALREADY been updated
      to the CURRENT row's value → we'd be reusing the item! (wrong for 0/1)
    
    If we loop RIGHT to LEFT:
      When computing dp[w], dp[w - weights[i]] is still the OLD value
      from the previous row → correct! Item used at most once.
    
    📝 VISUAL EXAMPLE (weights=[1,3,4,5], values=[1,4,5,7]):
    
    After i=0: dp = [0, 1, 1, 1, 1, 1, 1, 1]
    
    Processing i=1 (wt=3, val=4), BACKWARD from w=7 to w=3:
      w=7: dp[7] = max(dp[7]=1, 4 + dp[7-3]=dp[4]=1) = max(1, 5) = 5
      w=6: dp[6] = max(1, 4 + dp[3]=1) = 5
      w=5: dp[5] = max(1, 4 + dp[2]=1) = 5
      w=4: dp[4] = max(1, 4 + dp[1]=1) = 5
      w=3: dp[3] = max(1, 4 + dp[0]=0) = 4
      dp = [0, 1, 1, 4, 5, 5, 5, 5]
      
      ✅ Notice: when computing dp[4], dp[1] still has the OLD value (1),
         which is correct. If we went forward, dp[3] would already be 4,
         and dp[6] = max(1, 4+4) = 8 → WRONG (used item 1 twice)!
    
    Processing i=2 (wt=4, val=5), BACKWARD:
      w=7: dp[7] = max(5, 5 + dp[3]=4) = 9 ✓
      ...
    """
    n = len(weights)
    dp = [0] * (capacity + 1)

    # Base case: row i=0
    for w in range(capacity + 1):
        if w >= weights[0]:
            dp[w] = values[0]

    for i in range(1, n):
        # 🔥 BACKWARD: right to left so we don't reuse items
        for w in range(capacity, weights[i] - 1, -1):
            # dp[w] currently holds dp[i-1][w] (skip value)
            # dp[w - weights[i]] still holds dp[i-1][w-weights[i]] (not yet overwritten)
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
        # For w < weights[i], dp[w] stays as dp[i-1][w] (skip only), no change needed

    return dp[capacity]


# ───────────────────────────────────────────────────────────────────────────
# SECTION B: 0/1 KNAPSACK — STANDARD VERSION (i==0 means "no items left")
# ───────────────────────────────────────────────────────────────────────────
"""
📝 STANDARD VERSION BASE CASE:

   i represents "number of items we can choose from" (1-indexed logic).
   i == 0 means NO items available → return 0 (can't pick anything).
   
   Items are accessed as weights[i-1], values[i-1].
   
   This makes the base case trivial but shifts all item accesses by 1.
   
   dp dimensions: (n+1) x (capacity+1)
   Row 0: all zeros (no items = no value)
   Col 0: all zeros (no capacity = no value)
"""


def knapsack_01_standard_memo(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 5/16: 0/1 Knapsack — Standard Version — Memoization
    
    Here i means "we have items 1..i available" (1-indexed).
    i == 0 → no items left → return 0.
    Access actual item as weights[i-1], values[i-1].
    
    📝 DRY RUN:
    weights = [1, 3, 4, 5], values = [1, 4, 5, 7], W = 7
    
    solve(4, 7):                               # items 1..4 available
      skip = solve(3, 7)                       # don't use item 4
      take = 7 + solve(3, 2)                   # use item 4 (wt=5), capacity left=2
      
    solve(3, 7):                               # items 1..3 available
      skip = solve(2, 7)
      take = 5 + solve(2, 3)                   # use item 3 (wt=4)
      
    ... eventually ...
    solve(0, anything) = 0                     # no items left!
    
    Final answer: 9 ✓
    """
    n = len(weights)
    cache = {}

    def solve(i, w):
        # Base case: no items left
        if i == 0:
            return 0

        if (i, w) in cache:
            return cache[(i, w)]

        # Items are 1-indexed in logic, so actual item is at i-1
        skip = solve(i - 1, w)

        take = -1
        if w >= weights[i - 1]:
            take = values[i - 1] + solve(i - 1, w - weights[i - 1])

        cache[(i, w)] = max(skip, take)
        return cache[(i, w)]

    return solve(n, capacity)


def knapsack_01_standard_2d_dp(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 6/16: 0/1 Knapsack — Standard Version — 2D DP Table
    
    dp[i][w] = max value using first i items with capacity w
    dp[0][w] = 0 for all w (no items)
    dp[i][0] = 0 for all i (no capacity)
    
    📝 TABLE (weights=[1,3,4,5], values=[1,4,5,7], W=7):
    
         w:  0  1  2  3  4  5  6  7
    i=0:     0  0  0  0  0  0  0  0    ← no items
    i=1:     0  1  1  1  1  1  1  1    ← item 0 (wt=1,val=1)
    i=2:     0  1  1  4  5  5  5  5    ← + item 1 (wt=3,val=4)
    i=3:     0  1  1  4  5  6  6  9    ← + item 2 (wt=4,val=5)
    i=4:     0  1  1  4  5  7  8  9    ← + item 3 (wt=5,val=7)
    
    Answer: dp[4][7] = 9 ✓
    """
    n = len(weights)
    # (n+1) rows, (capacity+1) cols — row 0 = no items (all zeros)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Skip item i (use value from i-1 items)
            skip = dp[i - 1][w]

            take = -1
            if w >= weights[i - 1]:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            dp[i][w] = max(skip, take)

    return dp[n][capacity]


def knapsack_01_standard_prev_cur(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 7/16: 0/1 Knapsack — Standard Version — Two 1D Arrays (prev + cur)
    
    Same as 2D but only keep two rows.
    prev starts as all zeros (representing dp[0] = no items).
    """
    n = len(weights)
    prev = [0] * (capacity + 1)  # dp[0][...] = 0 (no items)

    for i in range(1, n + 1):
        cur = [0] * (capacity + 1)
        for w in range(capacity + 1):
            skip = prev[w]

            take = -1
            if w >= weights[i - 1]:
                take = values[i - 1] + prev[w - weights[i - 1]]

            cur[w] = max(skip, take)
        prev = cur

    return prev[capacity]


def knapsack_01_standard_1d_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    FUNCTION 8/16: 0/1 Knapsack — Standard Version — Single 1D Array (BACKWARD)
    
    🔥 BACKWARD LOOP — same reasoning as My Version:
    We need dp[i-1][w - wt] which is the OLD value.
    Looping backward preserves old values on the left side.
    
    This is the cleanest version for 0/1 knapsack.
    dp starts as all zeros (no items selected).
    """
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(1, n + 1):
        # 🔥 BACKWARD loop: ensures each item used at most once
        for w in range(capacity, weights[i - 1] - 1, -1):
            dp[w] = max(dp[w], values[i - 1] + dp[w - weights[i - 1]])

    return dp[capacity]


# ═══════════════════════════════════════════════════════════════════════════
# ███████████████████████████████████████████████████████████████████████████
#
#                    PART 2: UNBOUNDED KNAPSACK
#                    (Coin Change — Minimum Coins)
#
#   Each item (coin) can be used UNLIMITED times.
#   When we TAKE coin i, we STAY at i (can reuse it).
#
#   Recurrence:
#     skip = dp(i-1, rem)
#     take = 1 + dp(i, rem - coins[i])    ← STAY at i!
#     dp(i, rem) = min(skip, take)
#
#   Note: We use min() and INF because we want MINIMUM coins.
#   For a max-value unbounded knapsack, use max() instead.
#
# ███████████████████████████████████████████████████████████████████████████
# ═══════════════════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────────────────
# SECTION C: UNBOUNDED KNAPSACK — MY VERSION (i==0 means "at index 0")
# ───────────────────────────────────────────────────────────────────────────
"""
📝 MY VERSION BASE CASE FOR UNBOUNDED:

   When i == 0, we are at the FIRST coin (coins[0]).
   This is the ONLY coin we can use (no more indices to try).
   Since it's unbounded, we can use coins[0] as many times as needed.
   
   Base case i == 0:
     if rem % coins[0] == 0: return rem // coins[0]  (use coins[0] repeatedly)
     else:                   return INF               (impossible with just this coin)
   
   Example: coins = [1, 3, 4], amount = 6
     i==0, rem=6: 6 % 1 == 0 → return 6 (six 1-coins)
     i==0, rem=5: 5 % 1 == 0 → return 5 (five 1-coins)
     
   Example: coins = [3, 4], amount = 5
     i==0, rem=5: 5 % 3 != 0 → return INF (can't make 5 with only 3s)
"""


def coinchange_myversion_memo(coins: List[int], amount: int) -> int:
    """
    FUNCTION 9/16: Unbounded Knapsack (Coin Change) — My Version — Memoization
    
    📝 DRY RUN: coins = [1, 3, 4], amount = 6
    
    solve(2, 6):                                # considering coin 4
      skip = solve(1, 6)                        # skip coin 4
        solve(1, 6):                            # considering coin 3
          skip = solve(0, 6) = 6                # base: 6/1 = 6 ones
          take = 1 + solve(1, 3)                # use coin 3, rem=3
            solve(1, 3):
              skip = solve(0, 3) = 3            # base: 3/1 = 3 ones
              take = 1 + solve(1, 0)            # use coin 3, rem=0
                solve(1, 0): rem==0 → return 0
              take = 1 + 0 = 1
              return min(3, 1) = 1              # one coin-3
          take = 1 + 1 = 2                      # two coin-3s!
          return min(6, 2) = 2
      take = 1 + solve(2, 2)                    # use coin 4? 4 > 2, can't take
      return min(2, INF) = 2 ✓
      
    Answer: 2 (coins [3, 3]) ✓
    """
    INF = float('inf')
    n = len(coins)
    cache = {}

    def solve(i, rem):
        # Base: no remaining amount needed
        if rem == 0:
            return 0

        # Base: at index 0, only coins[0] available (can reuse it)
        if i == 0:
            if rem % coins[0] == 0:
                return rem // coins[0]
            return INF

        if (i, rem) in cache:
            return cache[(i, rem)]

        # Option 1: Skip this coin denomination entirely
        skip = solve(i - 1, rem)

        # Option 2: Use this coin (STAY at i — unbounded, can reuse)
        take = INF
        if rem >= coins[i]:
            take = 1 + solve(i, rem - coins[i])  # ← STAY at i!

        cache[(i, rem)] = min(skip, take)
        return cache[(i, rem)]

    ans = solve(n - 1, amount)
    return -1 if ans >= INF else ans


def coinchange_myversion_2d_dp(coins: List[int], amount: int) -> int:
    """
    FUNCTION 10/16: Unbounded Knapsack (Coin Change) — My Version — 2D DP
    
    dp[i][s] = min coins using denominations 0..i to make amount s
    
    📝 TABLE (coins=[1, 3, 4], amount=6):
    
    Row i=0 (only coin 1):
      s:  0  1  2  3  4  5  6
          0  1  2  3  4  5  6    ← rem/1 for each amount
    
    Row i=1 (coins 1 and 3):
      s:  0  1  2  3  4  5  6
          0  1  2  1  2  3  2
      s=3: min(skip=dp[0][3]=3, take=1+dp[1][0]=1) = 1
      s=4: min(skip=dp[0][4]=4, take=1+dp[1][1]=2) = 2
      s=6: min(skip=dp[0][6]=6, take=1+dp[1][3]=2) = 2 ✓
    
    Row i=2 (coins 1, 3, and 4):
      s:  0  1  2  3  4  5  6
          0  1  2  1  1  2  2
      s=4: min(skip=dp[1][4]=2, take=1+dp[2][0]=1) = 1
      s=6: min(skip=dp[1][6]=2, take=1+dp[2][2]=3) = 2
    
    Answer: dp[2][6] = 2 ✓
    
    🔑 KEY DIFFERENCE FROM 0/1:
    take = 1 + dp[i][s - coins[i]]    ← SAME row i (not i-1!)
    This means we can reuse the same coin.
    """
    INF = float('inf')
    n = len(coins)
    dp = [[INF] * (amount + 1) for _ in range(n)]

    # Base case: row i=0 (only coins[0] available, can reuse) 
    for s in range(amount + 1): # here we modify first row and standard dp sol we modify first col
        if s % coins[0] == 0:
            dp[0][s] = s // coins[0]
        # else stays INF

    # Fill remaining rows
    for i in range(1, n):
        for s in range(amount + 1):
            skip = dp[i - 1][s]

            take = INF
            if s >= coins[i]:
                # 🔥 UNBOUNDED: dp[i][s - coins[i]] — SAME row!
                take = 1 + dp[i][s - coins[i]]

            dp[i][s] = min(skip, take)

    ans = dp[n - 1][amount]
    return -1 if ans >= INF else ans


def coinchange_myversion_prev_cur(coins: List[int], amount: int) -> int:
    """
    FUNCTION 11/16: Unbounded Knapsack (Coin Change) — My Version — prev + cur
    
    🔑 CRITICAL OBSERVATION:
    skip = dp[i-1][s]       → prev[s]          (previous row)
    take = dp[i][s-coins[i]] → cur[s-coins[i]]  (CURRENT row, already computed!)
    
    So we DO need two arrays, but 'take' reads from 'cur' not 'prev'.
    This works because we fill cur left-to-right, so cur[s-coins[i]]
    is already computed when we reach s (since s-coins[i] < s).
    """
    INF = float('inf')
    n = len(coins)
    prev = [INF] * (amount + 1)

    # Base case: row i=0
    for s in range(amount + 1):
        if s % coins[0] == 0:
            prev[s] = s // coins[0]

    for i in range(1, n):
        cur = [INF] * (amount + 1)
        for s in range(amount + 1):
            skip = prev[s]

            take = INF
            if s >= coins[i]:
                # Read from cur (current row) — already computed for s-coins[i]
                take = 1 + cur[s - coins[i]]

            cur[s] = min(skip, take)
        prev = cur

    ans = prev[amount]
    return -1 if ans >= INF else ans


def coinchange_myversion_1d_optimized(coins: List[int], amount: int) -> int:
    """
    FUNCTION 12/16: Unbounded Knapsack (Coin Change) — My Version — 1D (FORWARD)
    
    🔥 THE KEY INSIGHT — WHY FORWARD?
    
    In unbounded: take = 1 + dp[i][s - coins[i]]  (SAME row!)
    We WANT the updated (current row) value at s - coins[i].
    
    If we loop LEFT to RIGHT (forward):
      dp[s - coins[i]] has already been updated to the current row.
      This is EXACTLY what we want — it means the coin can be reused!
    
    📝 VISUAL: coins = [1, 3, 4], amount = 6
    
    After i=0: dp = [0, 1, 2, 3, 4, 5, 6]  (all amounts using coin-1)
    
    Processing i=1 (coin=3), FORWARD from s=0 to s=6:
      s=0: dp[0] = min(dp[0]=0) = 0                      (skip only, coin too big)
      s=1: dp[1] = min(dp[1]=1) = 1                      (skip only, coin too big)
      s=2: dp[2] = min(dp[2]=2) = 2                      (skip only, coin too big)
      s=3: dp[3] = min(dp[3]=3, 1+dp[0]=1) = 1           ← one coin-3
      s=4: dp[4] = min(dp[4]=4, 1+dp[1]=2) = 2           ← coin-3 + coin-1
      s=5: dp[5] = min(dp[5]=5, 1+dp[2]=3) = 3           ← coin-3 + 2×coin-1
      s=6: dp[6] = min(dp[6]=6, 1+dp[3]=1+1=2) = 2       ← two coin-3s! ✓
                                        ↑
                         dp[3] was ALREADY updated to 1 (current row)
                         So 1 + 1 = 2 means reusing coin-3. Correct!
    
    Compare with 0/1 (backward): if we went backward here, dp[3] would
    still be 3 (old value), giving dp[6] = 1+3 = 4 → WRONG for unbounded.
    
    After i=1: dp = [0, 1, 2, 1, 2, 3, 2]
    
    Processing i=2 (coin=4), FORWARD:
      s=4: dp[4] = min(dp[4]=2, 1+dp[0]=1) = 1           ← one coin-4
      s=5: dp[5] = min(dp[5]=3, 1+dp[1]=2) = 2           ← coin-4 + coin-1
      s=6: dp[6] = min(dp[6]=2, 1+dp[2]=3) = 2           ← stays 2
    
    Final: dp = [0, 1, 2, 1, 1, 2, 2]
    Answer: dp[6] = 2 ✓
    """
    INF = float('inf')
    n = len(coins)
    dp = [INF] * (amount + 1)

    # Base case: row i=0
    for s in range(amount + 1):
        if s % coins[0] == 0:
            dp[s] = s // coins[0]

    for i in range(1, n):
        # 🔥 FORWARD loop: allows reusing the same coin
        for s in range(amount + 1):
            # dp[s] already holds prev[s] (skip value from previous row)
            if s >= coins[i]:
                # dp[s - coins[i]] is ALREADY updated for current row i
                dp[s] = min(dp[s], 1 + dp[s - coins[i]])

    ans = dp[amount]
    return -1 if ans >= INF else ans


# ───────────────────────────────────────────────────────────────────────────
# SECTION D: UNBOUNDED KNAPSACK — STANDARD VERSION (i==0 means "no coins")
# ───────────────────────────────────────────────────────────────────────────
"""
📝 STANDARD VERSION BASE CASE FOR UNBOUNDED:

   i represents "number of coin denominations available" (1-indexed logic).
   i == 0 means NO coins available.
   
   Base cases:
     dp[0][0] = 0           (0 amount with 0 coins = 0 coins needed)
     dp[0][s>0] = INF       (positive amount with no coins = impossible)
     dp[i][0] = 0           (0 amount always needs 0 coins)
   
   This is simpler — no modulo logic needed at the base.
   Items accessed as coins[i-1].
   
   dp dimensions: (n+1) x (amount+1)
"""


def coinchange_standard_memo(coins: List[int], amount: int) -> int:
    """
    FUNCTION 13/16: Unbounded Knapsack (Coin Change) — Standard Version — Memo
    
    i = number of coin types available (1..i)
    i == 0 → no coins → return 0 if rem==0, else INF
    
    📝 DRY RUN: coins = [1, 3, 4], amount = 6
    
    solve(3, 6):                              # 3 coin types available
      skip = solve(2, 6)                      # don't use coin-4 at all
        solve(2, 6):                          # 2 types: coin-1, coin-3
          skip = solve(1, 6)                  # don't use coin-3
            solve(1, 6):                      # only coin-1
              skip = solve(0, 6) = INF        # no coins, can't make 6
              take = 1 + solve(1, 5)          # use coin-1
                ... eventually = 6            # six coin-1s
              return 6
          take = 1 + solve(2, 3)              # use coin-3, rem=3
            solve(2, 3):
              skip = solve(1, 3) = 3          # three coin-1s
              take = 1 + solve(2, 0) = 1      # one coin-3, done!
              return min(3, 1) = 1
          return min(6, 1+1) = 2              # two coin-3s ✓
      take = 1 + solve(3, 2) = ...            # use coin-4? 4>2, can't
      return 2 ✓
    """
    INF = float('inf')
    n = len(coins)
    cache = {}

    def solve(i, rem):
        # Base: amount is 0, no coins needed
        if rem == 0:
            return 0

        # Base: no coin types left but still have remaining amount
        if i == 0:
            return INF

        if (i, rem) in cache:
            return cache[(i, rem)]

        # Skip this coin denomination
        skip = solve(i - 1, rem)

        # Take this coin (stay at i — unbounded)
        take = INF
        if rem >= coins[i - 1]:
            take = 1 + solve(i, rem - coins[i - 1])

        cache[(i, rem)] = min(skip, take)
        return cache[(i, rem)]

    ans = solve(n, amount)
    return -1 if ans >= INF else ans


def coinchange_standard_2d_dp(coins: List[int], amount: int) -> int:
    """
    FUNCTION 14/16: Unbounded Knapsack (Coin Change) — Standard Version — 2D DP
    
    dp[i][s] = min coins to make amount s using first i coin types
    
    📝 TABLE (coins=[1, 3, 4], amount=6):
    
         s:  0    1    2    3    4    5    6
    i=0:     0   INF  INF  INF  INF  INF  INF   ← no coins available
    i=1:     0    1    2    3    4    5    6      ← only coin-1
    i=2:     0    1    2    1    2    3    2      ← coins 1,3
    i=3:     0    1    2    1    1    2    2      ← coins 1,3,4
    
    Answer: dp[3][6] = 2 ✓
    
    Row i=0 is the clean base: all INF except dp[0][0]=0.
    No modulo logic needed!
    """
    INF = float('inf')
    n = len(coins)
    dp = [[INF] * (amount + 1) for _ in range(n + 1)]

    # Base case: dp[i][0] = 0 for all i (0 amount needs 0 coins)
    for i in range(n + 1): # in my own striver sol we modify first row and there we modify col
        dp[i][0] = 0
    # or we can do 
    # dp[0][0] = 0 
    # and start the 2 loop from for s in range(amount+1)

    # dp[0][s>0] = INF already set (no coins, can't make positive amount)

    for i in range(1, n + 1):
        for s in range(1, amount + 1):
            skip = dp[i - 1][s]

            take = INF
            if s >= coins[i - 1]:
                # UNBOUNDED: same row i
                take = 1 + dp[i][s - coins[i - 1]]

            dp[i][s] = min(skip, take)

    ans = dp[n][amount]
    return -1 if ans >= INF else ans


def coinchange_standard_prev_cur(coins: List[int], amount: int) -> int:
    """
    FUNCTION 15/16: Unbounded Knapsack (Coin Change) — Standard Version — prev + cur
    
    prev starts as dp[0]: [0, INF, INF, ..., INF]
    """
    INF = float('inf')
    n = len(coins)
    prev = [INF] * (amount + 1)
    prev[0] = 0  # Base: 0 amount = 0 coins

    for i in range(1, n + 1):
        cur = [INF] * (amount + 1)
        cur[0] = 0  # 0 amount always needs 0 coins
        for s in range(1, amount + 1):
            skip = prev[s]

            take = INF
            if s >= coins[i - 1]:
                take = 1 + cur[s - coins[i - 1]]  # Read from cur (same row)

            cur[s] = min(skip, take)
        prev = cur

    ans = prev[amount]
    return -1 if ans >= INF else ans


def coinchange_standard_1d_optimized(coins: List[int], amount: int) -> int:
    """
    FUNCTION 16/16: Unbounded Knapsack (Coin Change) — Standard Version — 1D (FORWARD)
    
    🔥 FORWARD LOOP — same reasoning as My Version:
    We want dp[s - coins[i-1]] from the CURRENT row (reuse coin).
    Forward ensures it's already updated.
    
    dp starts as [0, INF, INF, ..., INF].
    
    📝 TRACE: coins = [1, 3, 4], amount = 6
    
    Initial: dp = [0, INF, INF, INF, INF, INF, INF]
    
    i=1 (coin=1), FORWARD:
      s=1: dp[1] = min(INF, 1+dp[0]=1) = 1
      s=2: dp[2] = min(INF, 1+dp[1]=2) = 2       ← dp[1] already updated!
      s=3: dp[3] = min(INF, 1+dp[2]=3) = 3
      ...
      dp = [0, 1, 2, 3, 4, 5, 6]
    
    i=2 (coin=3), FORWARD:
      s=1: no change (3 > 1)
      s=2: no change (3 > 2)
      s=3: dp[3] = min(3, 1+dp[0]=1) = 1
      s=4: dp[4] = min(4, 1+dp[1]=2) = 2
      s=5: dp[5] = min(5, 1+dp[2]=3) = 3
      s=6: dp[6] = min(6, 1+dp[3]=1+1=2) = 2     ← reuses coin-3 ✓
      dp = [0, 1, 2, 1, 2, 3, 2]
    
    i=3 (coin=4), FORWARD:
      s=4: dp[4] = min(2, 1+dp[0]=1) = 1
      s=5: dp[5] = min(3, 1+dp[1]=2) = 2
      s=6: dp[6] = min(2, 1+dp[2]=3) = 2
      dp = [0, 1, 2, 1, 1, 2, 2]
    
    Answer: dp[6] = 2 ✓
    """
    INF = float('inf')
    n = len(coins)
    dp = [INF] * (amount + 1)
    dp[0] = 0  # Base: 0 amount = 0 coins

    for i in range(1, n + 1):
        # 🔥 FORWARD loop: allows reusing the same coin
        for s in range(coins[i - 1], amount + 1):
            dp[s] = min(dp[s], 1 + dp[s - coins[i - 1]])

    ans = dp[amount]
    return -1 if ans >= INF else ans


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 COMPREHENSIVE TESTS
# ═══════════════════════════════════════════════════════════════════════════

def test_all():
    print("=" * 70)
    print("  TESTING ALL 16 FUNCTIONS")
    print("=" * 70)

    # ─── 0/1 Knapsack Tests ──────────────────────────────────────────────
    weights = [1, 3, 4, 5]
    values  = [1, 4, 5, 7]
    capacity = 7
    expected_01 = 9  # items (wt=3,val=4) + (wt=4,val=5)

    print("\n─── 0/1 KNAPSACK ───")
    print(f"  weights={weights}, values={values}, capacity={capacity}")
    print(f"  Expected: {expected_01}\n")

    r1 = knapsack_01_myversion_memo(weights, values, capacity)
    print(f"  [ 1/16] My Version — Memo:       {r1}  {'✅' if r1 == expected_01 else '❌'}")

    r2 = knapsack_01_myversion_2d_dp(weights, values, capacity)
    print(f"  [ 2/16] My Version — 2D DP:      {r2}  {'✅' if r2 == expected_01 else '❌'}")

    r3 = knapsack_01_myversion_prev_cur(weights, values, capacity)
    print(f"  [ 3/16] My Version — Prev/Cur:   {r3}  {'✅' if r3 == expected_01 else '❌'}")

    r4 = knapsack_01_myversion_1d_optimized(weights, values, capacity)
    print(f"  [ 4/16] My Version — 1D Backward:{r4}  {'✅' if r4 == expected_01 else '❌'}")

    r5 = knapsack_01_standard_memo(weights, values, capacity)
    print(f"  [ 5/16] Standard  — Memo:        {r5}  {'✅' if r5 == expected_01 else '❌'}")

    r6 = knapsack_01_standard_2d_dp(weights, values, capacity)
    print(f"  [ 6/16] Standard  — 2D DP:       {r6}  {'✅' if r6 == expected_01 else '❌'}")

    r7 = knapsack_01_standard_prev_cur(weights, values, capacity)
    print(f"  [ 7/16] Standard  — Prev/Cur:    {r7}  {'✅' if r7 == expected_01 else '❌'}")

    r8 = knapsack_01_standard_1d_optimized(weights, values, capacity)
    print(f"  [ 8/16] Standard  — 1D Backward: {r8}  {'✅' if r8 == expected_01 else '❌'}")

    # ─── Unbounded Knapsack (Coin Change) Tests ──────────────────────────
    coins = [1, 3, 4]
    amount = 6
    expected_ub = 2  # coins [3, 3]

    print("\n─── UNBOUNDED KNAPSACK (Coin Change) ───")
    print(f"  coins={coins}, amount={amount}")
    print(f"  Expected: {expected_ub}\n")

    r9  = coinchange_myversion_memo(coins, amount)
    print(f"  [ 9/16] My Version — Memo:       {r9}  {'✅' if r9 == expected_ub else '❌'}")

    r10 = coinchange_myversion_2d_dp(coins, amount)
    print(f"  [10/16] My Version — 2D DP:      {r10}  {'✅' if r10 == expected_ub else '❌'}")

    r11 = coinchange_myversion_prev_cur(coins, amount)
    print(f"  [11/16] My Version — Prev/Cur:   {r11}  {'✅' if r11 == expected_ub else '❌'}")

    r12 = coinchange_myversion_1d_optimized(coins, amount)
    print(f"  [12/16] My Version — 1D Forward: {r12}  {'✅' if r12 == expected_ub else '❌'}")

    r13 = coinchange_standard_memo(coins, amount)
    print(f"  [13/16] Standard  — Memo:        {r13}  {'✅' if r13 == expected_ub else '❌'}")

    r14 = coinchange_standard_2d_dp(coins, amount)
    print(f"  [14/16] Standard  — 2D DP:       {r14}  {'✅' if r14 == expected_ub else '❌'}")

    r15 = coinchange_standard_prev_cur(coins, amount)
    print(f"  [15/16] Standard  — Prev/Cur:    {r15}  {'✅' if r15 == expected_ub else '❌'}")

    r16 = coinchange_standard_1d_optimized(coins, amount)
    print(f"  [16/16] Standard  — 1D Forward:  {r16}  {'✅' if r16 == expected_ub else '❌'}")

    # ─── Additional Edge Case Tests ──────────────────────────────────────
    print("\n─── EDGE CASES ───\n")

    # Coin change impossible
    coins2 = [2]
    amount2 = 3
    for name, fn in [("MyMemo", coinchange_myversion_memo),
                     ("Std1D",  coinchange_standard_1d_optimized)]:
        r = fn(coins2, amount2)
        print(f"  coins={coins2}, amount={amount2} → {name}: {r}  {'✅' if r == -1 else '❌'}")

    # 0/1 knapsack: all items fit
    w2 = [1, 2, 3]
    v2 = [6, 10, 12]
    c2 = 6
    exp2 = 28  # take all
    for name, fn in [("MyMemo", knapsack_01_myversion_memo),
                     ("Std1D",  knapsack_01_standard_1d_optimized)]:
        r = fn(w2, v2, c2)
        print(f"  wt={w2}, val={v2}, cap={c2} → {name}: {r}  {'✅' if r == exp2 else '❌'}")

    # Single item tests
    w3 = [5]
    v3 = [10]
    r_fit = knapsack_01_myversion_1d_optimized(w3, v3, 5)
    r_no  = knapsack_01_myversion_1d_optimized(w3, v3, 4)
    print(f"  Single item fits: {r_fit}  {'✅' if r_fit == 10 else '❌'}")
    print(f"  Single item no fit: {r_no}  {'✅' if r_no == 0 else '❌'}")

    print("\n" + "=" * 70)
    print("  ALL TESTS COMPLETE!")
    print("=" * 70)


# ═══════════════════════════════════════════════════════════════════════════
# 📊 SUMMARY CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════
"""
┌──────────────────┬────────────────────────┬────────────────────────────┐
│                  │    0/1 KNAPSACK        │    UNBOUNDED KNAPSACK      │
├──────────────────┼────────────────────────┼────────────────────────────┤
│ Item reuse       │ AT MOST ONCE           │ UNLIMITED times            │
│ take transition  │ dp(i-1, w-wt[i])       │ dp(i, w-wt[i])            │
│                  │ (move to prev item)    │ (stay at same item)        │
│ 2D dependency    │ dp[i-1][w-wt]          │ dp[i][w-wt] (same row!)   │
│ 1D inner loop    │ BACKWARD (right→left)  │ FORWARD (left→right)      │
│ Why?             │ Need OLD row values    │ Need UPDATED row values    │
├──────────────────┼────────────────────────┼────────────────────────────┤
│ My version base  │ i==0: can take item 0  │ i==0: use coins[0]        │
│ (i==0 = index 0) │ if w >= wt[0]          │ repeatedly if divisible   │
│ Standard base    │ i==0: no items → 0     │ i==0: no coins → INF      │
│ (i==0 = empty)   │ (trivially simple)     │ except dp[0][0] = 0       │
├──────────────────┼────────────────────────┼────────────────────────────┤
│ Time             │ O(n × W)               │ O(n × W)                  │
│ Space (2D)       │ O(n × W)               │ O(n × W)                  │
│ Space (1D)       │ O(W)                   │ O(W)                      │
└──────────────────┴────────────────────────┴────────────────────────────┘

MEMORY TRICK:
  0/1 = "Once" = "Old values" = "← Backward"
  Unbounded = "Unlimited" = "Updated values" = "→ Forward"

COMMON PROBLEMS:
  0/1 Knapsack: Subset Sum, Partition Equal Subset, Target Sum
  Unbounded: Coin Change, Rod Cutting, Unbounded Knapsack (max value)
  
LEETCODE:
  0/1:
    ⭐ 416. Partition Equal Subset Sum (medium)
    ⭐ 494. Target Sum (medium)
    ⭐ 474. Ones and Zeroes (medium)
    ⭐ 1049. Last Stone Weight II (medium)
    
  Unbounded:
    ⭐ 322. Coin Change (medium)
    ⭐ 518. Coin Change II (medium)
    ⭐ 279. Perfect Squares (medium)
    ⭐ 983. Minimum Cost For Tickets (medium)
"""


if __name__ == "__main__":
    test_all()