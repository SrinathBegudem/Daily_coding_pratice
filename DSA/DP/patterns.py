"""
═══════════════════════════════════════════════════════════════════════════════
                    DYNAMIC PROGRAMMING PATTERNS MASTERY
        Reverse Recursion → Memoization → Tabulation (Direct Mapping!)
                    For Google, Amazon, Meta, Microsoft
═══════════════════════════════════════════════════════════════════════════════

🎯 THE DP PHILOSOPHY (MEMORIZE THIS!):

1. ALWAYS start with REVERSE RECURSION (NOT forward!)
   Why? Direct mapping to DP table!

2. State = minimum variables needed to identify a subproblem
   Same state → same future → same answer

3. Progression (3 steps):
   Step 1: Reverse Recursion (get the logic right)
   Step 2: Add Memoization (add 2 lines: check cache, store result)
   Step 3: Convert to Tabulation (loops replace recursion)

4. The mapping is DIRECT:
   solve(i, j) → dp[i][j]
   return value → dp[i][j] = value
   solve(i-1) → dp[i-1]


═══════════════════════════════════════════════════════════════════════════════
PATTERN 1: 0/1 KNAPSACK (Foundation Pattern!)
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Can partition into equal sum?"
✅ "Target sum with +/- operations"
✅ "Subset sum equals k"
✅ Each item can be used AT MOST ONCE
✅ Binary choice: take or skip

🔑 STATE:
- i = number of items available
- cap = remaining capacity
- dp[i][cap] = best value using first i items with capacity cap


TEMPLATE - REVERSE RECURSION:
────────────────────────────────────────────────────────────────────────────
def knapsack_recursion(weights, values, capacity):
    n = len(weights)
    
    def solve(i, cap):
        # Base case: no items or no capacity
        if i == 0 or cap == 0:
            return 0
        
        # Choice 1: Skip the i-th item
        skip = solve(i-1, cap)
        
        # Choice 2: Take the i-th item (if it fits)
        take = 0
        if weights[i-1] <= cap:
            take = values[i-1] + solve(i-1, cap - weights[i-1])
        
        return max(skip, take)
    
    return solve(n, capacity)


TEMPLATE - MEMOIZATION (Add 2 lines!):
────────────────────────────────────────────────────────────────────────────
def knapsack_memo(weights, values, capacity):
    n = len(weights)
    memo = {}  # LINE 1: Create cache
    
    def solve(i, cap):
        if i == 0 or cap == 0:
            return 0
        
        # LINE 2: Check cache
        if (i, cap) in memo:
            return memo[(i, cap)]
        
        skip = solve(i-1, cap)
        
        take = 0
        if weights[i-1] <= cap:
            take = values[i-1] + solve(i-1, cap - weights[i-1])
        
        # LINE 3: Store before return
        memo[(i, cap)] = max(skip, take)
        return memo[(i, cap)]
    
    return solve(n, capacity)


TEMPLATE - TABULATION (Direct mapping!):
────────────────────────────────────────────────────────────────────────────
def knapsack_dp(weights, values, capacity):
    n = len(weights)
    # Create DP table (base case built-in!)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill table (force recursion order with loops)
    for i in range(1, n + 1):
        for cap in range(1, capacity + 1):
            # solve(i-1, cap) → dp[i-1][cap]
            skip = dp[i-1][cap]
            
            # solve(i-1, cap-weight) → dp[i-1][cap-weights[i-1]]
            take = 0
            if weights[i-1] <= cap:
                take = values[i-1] + dp[i-1][cap - weights[i-1]]
            
            # return max(skip, take) → dp[i][cap] = max(skip, take)
            dp[i][cap] = max(skip, take)
    
    # solve(n, capacity) → dp[n][capacity]
    return dp[n][capacity]


🎯 COMPLETE SOLUTION - LC 416: Partition Equal Subset Sum
────────────────────────────────────────────────────────────────────────────
\"""
LC 416: Partition Equal Subset Sum ⭐⭐⭐ MOST IMPORTANT!

Given array, can partition into two subsets with equal sum?

Input: nums = [1,5,11,5]
Output: True
Explanation: [1,5,5] and [11]

🔑 KEY INSIGHT:
If total sum is odd → impossible!
If even → check if subset sum = total/2 exists!
This becomes 0/1 Knapsack!
\"""

def canPartition(nums):
    total = sum(nums)
    
    # If odd, can't partition equally
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    
    # Reverse Recursion
    def solve(i, remaining):
        # Found exact target
        if remaining == 0:
            return True
        
        # No items left or negative remaining
        if i == 0 or remaining < 0:
            return False
        
        # Skip or take
        skip = solve(i-1, remaining)
        take = solve(i-1, remaining - nums[i-1])
        
        return skip or take
    
    return solve(n, target)


def canPartition_memo(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    memo = {}
    
    def solve(i, remaining):
        if remaining == 0:
            return True
        if i == 0 or remaining < 0:
            return False
        
        # Check cache
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        skip = solve(i-1, remaining)
        take = solve(i-1, remaining - nums[i-1])
        
        # Store result
        memo[(i, remaining)] = skip or take
        return memo[(i, remaining)]
    
    return solve(n, target)


def canPartition_dp(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    
    # dp[i][j] = can make sum j using first i items
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Skip current item
            skip = dp[i-1][j]
            
            # Take current item (if it fits)
            take = False
            if nums[i-1] <= j:
                take = dp[i-1][j - nums[i-1]]
            
            dp[i][j] = skip or take
    
    return dp[n][target]


🎯 COMPLETE SOLUTION - LC 494: Target Sum
────────────────────────────────────────────────────────────────────────────
\"""
LC 494: Target Sum ⭐⭐⭐

Assign +/- to each number to reach target. Count ways.

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, etc.

🔑 KEY INSIGHT:
Let P = sum of positive numbers, N = sum of negative numbers
P - N = target
P + N = sum(nums)
→ 2P = target + sum(nums)
→ P = (target + sum(nums)) / 2

This becomes: Count subsets with sum = P (0/1 Knapsack variant!)
\"""

def findTargetSumWays(nums, target):
    total = sum(nums)
    
    # Check if possible
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    
    subset_sum = (target + total) // 2
    n = len(nums)
    
    # Reverse Recursion: Count ways to make subset_sum
    def solve(i, remaining):
        # Found exact sum
        if remaining == 0:
            return 1
        
        # No items left or negative
        if i == 0:
            return 0
        
        # Skip current item
        skip = solve(i-1, remaining)
        
        # Take current item (if it fits)
        take = 0
        if nums[i-1] <= remaining:
            take = solve(i-1, remaining - nums[i-1])
        
        return skip + take
    
    return solve(n, subset_sum)


def findTargetSumWays_memo(nums, target):
    total = sum(nums)
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    
    subset_sum = (target + total) // 2
    n = len(nums)
    memo = {}
    
    def solve(i, remaining):
        if remaining == 0:
            return 1
        if i == 0:
            return 0
        
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        skip = solve(i-1, remaining)
        
        take = 0
        if nums[i-1] <= remaining:
            take = solve(i-1, remaining - nums[i-1])
        
        memo[(i, remaining)] = skip + take
        return memo[(i, remaining)]
    
    return solve(n, subset_sum)


def findTargetSumWays_dp(nums, target):
    total = sum(nums)
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    
    subset_sum = (target + total) // 2
    n = len(nums)
    
    # dp[i][j] = number of ways to make sum j using first i items
    dp = [[0] * (subset_sum + 1) for _ in range(n + 1)]
    
    # Base case: one way to make sum 0 (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(subset_sum + 1):
            # Skip
            skip = dp[i-1][j]
            
            # Take (if fits)
            take = 0
            if nums[i-1] <= j:
                take = dp[i-1][j - nums[i-1]]
            
            dp[i][j] = skip + take
    
    return dp[n][subset_sum]


0/1 KNAPSACK PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 416: Partition Equal Subset Sum
⭐⭐⭐ LC 494: Target Sum
⭐⭐ LC 1049: Last Stone Weight II
⭐⭐ LC 474: Ones and Zeroes (2D knapsack!)


═══════════════════════════════════════════════════════════════════════════════
PATTERN 2: UNBOUNDED KNAPSACK (Unlimited Supply!)
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Coin change" (minimum coins)
✅ "Coin change 2" (count ways)
✅ Each item can be used UNLIMITED times
✅ "Minimum/maximum using unlimited items"

🔑 KEY DIFFERENCE FROM 0/1:
- 0/1: After taking item i, move to i-1 (can't reuse)
- Unbounded: After taking item i, STAY at i (can reuse!)


TEMPLATE - REVERSE RECURSION:
────────────────────────────────────────────────────────────────────────────
def unbounded_knapsack(weights, values, capacity):
    n = len(weights)
    
    def solve(i, cap):
        # Base case
        if i == 0 or cap == 0:
            return 0
        
        # Skip item i
        skip = solve(i-1, cap)
        
        # Take item i (STAY at i, can reuse!)
        take = 0
        if weights[i-1] <= cap:
            take = values[i-1] + solve(i, cap - weights[i-1])  # STAY at i!
        
        return max(skip, take)
    
    return solve(n, capacity)


🎯 COMPLETE SOLUTION - LC 322: Coin Change
────────────────────────────────────────────────────────────────────────────
\"""
LC 322: Coin Change ⭐⭐⭐ MOST ASKED UNBOUNDED!

Minimum coins to make amount. Coins can be reused unlimited times.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

🔑 WHY GREEDY FAILS:
coins = [1,3,4], amount = 6
Greedy: 4 + 1 + 1 = 3 coins ✗
Optimal: 3 + 3 = 2 coins ✓
\"""

def coinChange(coins, amount):
    n = len(coins)
    
    # Reverse Recursion
    def solve(i, remaining):
        # Found exact amount
        if remaining == 0:
            return 0
        
        # No coins left or negative amount
        if i == 0 or remaining < 0:
            return float('inf')
        
        # Skip this coin
        skip = solve(i-1, remaining)
        
        # Take this coin (STAY at i, can reuse!)
        take = float('inf')
        if coins[i-1] <= remaining:
            take = 1 + solve(i, remaining - coins[i-1])  # STAY at i!
        
        return min(skip, take)
    
    result = solve(n, amount)
    return result if result != float('inf') else -1


def coinChange_memo(coins, amount):
    n = len(coins)
    memo = {}
    
    def solve(i, remaining):
        if remaining == 0:
            return 0
        if i == 0 or remaining < 0:
            return float('inf')
        
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        skip = solve(i-1, remaining)
        
        take = float('inf')
        if coins[i-1] <= remaining:
            take = 1 + solve(i, remaining - coins[i-1])
        
        memo[(i, remaining)] = min(skip, take)
        return memo[(i, remaining)]
    
    result = solve(n, amount)
    return result if result != float('inf') else -1


def coinChange_dp(coins, amount):
    n = len(coins)
    
    # dp[i][j] = min coins to make amount j using first i coins
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    
    # Base case: 0 coins needed for amount 0
    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            # Skip this coin
            skip = dp[i-1][j]
            
            # Take this coin (can reuse!)
            take = float('inf')
            if coins[i-1] <= j:
                take = 1 + dp[i][j - coins[i-1]]  # STAY at i!
            
            dp[i][j] = min(skip, take)
    
    return dp[n][amount] if dp[n][amount] != float('inf') else -1


🎯 COMPLETE SOLUTION - LC 518: Coin Change II
────────────────────────────────────────────────────────────────────────────
\"""
LC 518: Coin Change II ⭐⭐⭐

Count WAYS to make amount using coins (unlimited).

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: [5], [2,2,1], [2,1,1,1], [1,1,1,1,1]
\"""

def change(amount, coins):
    n = len(coins)
    
    def solve(i, remaining):
        # Found exact amount
        if remaining == 0:
            return 1
        
        # No coins left or negative
        if i == 0 or remaining < 0:
            return 0
        
        # Skip this coin
        skip = solve(i-1, remaining)
        
        # Take this coin (unlimited!)
        take = 0
        if coins[i-1] <= remaining:
            take = solve(i, remaining - coins[i-1])  # STAY at i!
        
        return skip + take
    
    return solve(n, amount)


def change_dp(amount, coins):
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    
    # Base case: 1 way to make 0 (use no coins)
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            skip = dp[i-1][j]
            
            take = 0
            if coins[i-1] <= j:
                take = dp[i][j - coins[i-1]]  # Unbounded!
            
            dp[i][j] = skip + take
    
    return dp[n][amount]


UNBOUNDED KNAPSACK PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 322: Coin Change (minimum coins)
⭐⭐⭐ LC 518: Coin Change II (count ways)
⭐⭐ LC 377: Combination Sum IV
⭐⭐ LC 983: Minimum Cost For Tickets


═══════════════════════════════════════════════════════════════════════════════
PATTERN 3: LONGEST COMMON SUBSEQUENCE (LCS)
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Longest common subsequence"
✅ "Edit distance"
✅ "Minimum deletions to make palindrome"
✅ Two sequences comparison

🔑 STATE:
- i = position in string1
- j = position in string2
- dp[i][j] = LCS length using first i chars of s1 and first j chars of s2


TEMPLATE - REVERSE RECURSION:
────────────────────────────────────────────────────────────────────────────
def lcs_recursion(text1, text2):
    n, m = len(text1), len(text2)
    
    def solve(i, j):
        # Base case: reached end of either string
        if i == 0 or j == 0:
            return 0
        
        # If characters match, both contribute to LCS
        if text1[i-1] == text2[j-1]:
            return 1 + solve(i-1, j-1)
        
        # If don't match, try skipping from either side
        skip_s1 = solve(i-1, j)
        skip_s2 = solve(i, j-1)
        
        return max(skip_s1, skip_s2)
    
    return solve(n, m)


🎯 COMPLETE SOLUTION - LC 1143: Longest Common Subsequence
────────────────────────────────────────────────────────────────────────────
\"""
LC 1143: Longest Common Subsequence ⭐⭐⭐

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: "ace" is LCS
\"""

def longestCommonSubsequence(text1, text2):
    n, m = len(text1), len(text2)
    memo = {}
    
    def solve(i, j):
        if i == 0 or j == 0:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if text1[i-1] == text2[j-1]:
            result = 1 + solve(i-1, j-1)
        else:
            result = max(solve(i-1, j), solve(i, j-1))
        
        memo[(i, j)] = result
        return result
    
    return solve(n, m)


def longestCommonSubsequence_dp(text1, text2):
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]


🎯 COMPLETE SOLUTION - LC 72: Edit Distance
────────────────────────────────────────────────────────────────────────────
\"""
LC 72: Edit Distance ⭐⭐⭐ GOOGLE FAVORITE!

Minimum operations (insert, delete, replace) to convert word1 to word2.

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse -> rose -> ros
\"""

def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    memo = {}
    
    def solve(i, j):
        # Base cases
        if i == 0:
            return j  # Need to insert j characters
        if j == 0:
            return i  # Need to delete i characters
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If characters match, no operation needed
        if word1[i-1] == word2[j-1]:
            result = solve(i-1, j-1)
        else:
            # Try all three operations
            insert = 1 + solve(i, j-1)      # Insert word2[j-1]
            delete = 1 + solve(i-1, j)      # Delete word1[i-1]
            replace = 1 + solve(i-1, j-1)   # Replace word1[i-1]
            
            result = min(insert, delete, replace)
        
        memo[(i, j)] = result
        return result
    
    return solve(n, m)


def minDistance_dp(word1, word2):
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                insert = dp[i][j-1]
                delete = dp[i-1][j]
                replace = dp[i-1][j-1]
                dp[i][j] = 1 + min(insert, delete, replace)
    
    return dp[n][m]


LCS PATTERN PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 1143: Longest Common Subsequence
⭐⭐⭐ LC 72: Edit Distance (Google favorite!)
⭐⭐ LC 583: Delete Operation for Two Strings
⭐⭐ LC 712: Minimum ASCII Delete Sum
⭐⭐ LC 1092: Shortest Common Supersequence


═══════════════════════════════════════════════════════════════════════════════
PATTERN 4: LONGEST INCREASING SUBSEQUENCE (LIS) - 1D DP!
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Longest increasing subsequence"
✅ "Number of LIS"
✅ "Russian doll envelopes"
✅ Single sequence optimization

🔑 STATE (DIFFERENT!):
- This is 1D DP!
- dp[i] = length of LIS ending at index i


TEMPLATE - DP SOLUTION (Most efficient: O(n²) or O(n log n)):
────────────────────────────────────────────────────────────────────────────
def lengthOfLIS(nums):
    n = len(nums)
    # dp[i] = length of LIS ending at index i
    dp = [1] * n  # Each element is LIS of length 1
    
    for i in range(1, n):
        for j in range(i):
            # If nums[j] < nums[i], we can extend LIS ending at j
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


🎯 COMPLETE SOLUTION - LC 300: Longest Increasing Subsequence
────────────────────────────────────────────────────────────────────────────
\"""
LC 300: Longest Increasing Subsequence ⭐⭐⭐

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: [2,3,7,101]
\"""

def lengthOfLIS_memo(nums):
    n = len(nums)
    memo = {}
    
    def solve(i, prev):
        # Base case: processed all elements
        if i == n:
            return 0
        
        if (i, prev) in memo:
            return memo[(i, prev)]
        
        # Option 1: Skip current element
        skip = solve(i + 1, prev)
        
        # Option 2: Take current element (if valid)
        take = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + solve(i + 1, i)
        
        memo[(i, prev)] = max(skip, take)
        return memo[(i, prev)]
    
    return solve(0, -1)


def lengthOfLIS_dp(nums):
    \"""O(n²) solution\"""
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def lengthOfLIS_optimal(nums):
    \"""
    O(n log n) solution using Binary Search
    
    Maintain array 'tails' where tails[i] = smallest tail element
    for all increasing subsequences of length i+1
    \"""
    tails = []
    
    for num in nums:
        # Binary search for position to insert/replace
        left, right = 0, len(tails)
        
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If left == len, append (extending LIS)
        if left == len(tails):
            tails.append(num)
        else:
            # Replace with smaller value
            tails[left] = num
    
    return len(tails)


LIS PATTERN PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 300: Longest Increasing Subsequence
⭐⭐ LC 673: Number of Longest Increasing Subsequence
⭐⭐ LC 354: Russian Doll Envelopes (2D LIS!)
⭐⭐ LC 1048: Longest String Chain


═══════════════════════════════════════════════════════════════════════════════
PATTERN 5: PALINDROME DP
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Longest palindromic substring"
✅ "Minimum insertions to make palindrome"
✅ "Palindrome partitioning"

🔑 STATE:
- i = start index
- j = end index
- dp[i][j] = answer for substring s[i...j]


🎯 COMPLETE SOLUTION - LC 5: Longest Palindromic Substring
────────────────────────────────────────────────────────────────────────────
\"""
LC 5: Longest Palindromic Substring ⭐⭐⭐

Input: s = "babad"
Output: "bab" (or "aba")
\"""

def longestPalindrome(s):
    n = len(s)
    # dp[i][j] = is s[i...j] a palindrome?
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_len = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for lengths >= 3
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # s[i...j] is palindrome if:
            # 1. s[i] == s[j] AND
            # 2. s[i+1...j-1] is palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]


🎯 COMPLETE SOLUTION - LC 516: Longest Palindromic Subsequence
────────────────────────────────────────────────────────────────────────────
\"""
LC 516: Longest Palindromic Subsequence ⭐⭐⭐

Input: s = "bbbab"
Output: 4 ("bbbb")
\"""

def longestPalindromeSubseq(s):
    n = len(s)
    # dp[i][j] = length of LPS in s[i...j]
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]


PALINDROME DP PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 5: Longest Palindromic Substring
⭐⭐⭐ LC 516: Longest Palindromic Subsequence
⭐⭐ LC 647: Palindromic Substrings (count)
⭐⭐ LC 131: Palindrome Partitioning


═══════════════════════════════════════════════════════════════════════════════
PATTERN 6: BUY/SELL STOCK DP (State Machine!)
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Best time to buy and sell stock"
✅ With transaction limits or cooldown
✅ State machine pattern

🔑 STATE:
- i = day index
- holding = 0 (not holding) or 1 (holding stock)
- k = transactions remaining (if limited)


🎯 COMPLETE SOLUTION - LC 121: Best Time to Buy and Sell Stock
────────────────────────────────────────────────────────────────────────────
\"""
LC 121: Best Time to Buy and Sell Stock ⭐⭐⭐

One transaction only.

Input: prices = [7,1,5,3,6,4]
Output: 5 (buy at 1, sell at 6)
\"""

def maxProfit_one_transaction(prices):
    \"""Simple O(n) solution\"""
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit


🎯 COMPLETE SOLUTION - LC 122: Best Time to Buy and Sell Stock II
────────────────────────────────────────────────────────────────────────────
\"""
LC 122: Unlimited transactions (no overlapping)

Input: prices = [7,1,5,3,6,4]
Output: 7 (buy 1 sell 5: +4, buy 3 sell 6: +3)
\"""

def maxProfit_unlimited(prices):
    \"""Greedy: Capture every increase!\"""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


🎯 COMPLETE SOLUTION - LC 123: Best Time to Buy and Sell Stock III
────────────────────────────────────────────────────────────────────────────
\"""
LC 123: At most 2 transactions

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6 (buy 0 sell 3: +3, buy 1 sell 4: +3)
\"""

def maxProfit_two_transactions(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # dp[i][k][holding]
    # i = day, k = transactions left, holding = 0 or 1
    
    # State machine approach
    buy1 = -prices[0]  # Bought first stock
    sell1 = 0          # Sold first stock
    buy2 = -prices[0]  # Bought second stock
    sell2 = 0          # Sold second stock
    
    for i in range(1, n):
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])
        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])
    
    return sell2


🎯 COMPLETE SOLUTION - LC 309: Best Time to Buy and Sell Stock with Cooldown
────────────────────────────────────────────────────────────────────────────
\"""
LC 309: With cooldown (can't buy immediately after sell)

Input: prices = [1,2,3,0,2]
Output: 3 (buy 1, sell 3, cooldown, buy 0, sell 2)
\"""

def maxProfit_cooldown(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # Three states:
    # hold = holding stock
    # sold = just sold (cooldown)
    # rest = can buy (cooled down)
    
    hold = -prices[0]
    sold = 0
    rest = 0
    
    for i in range(1, n):
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest
        
        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)
    
    return max(sold, rest)


STOCK DP PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 121: Best Time to Buy and Sell Stock (1 transaction)
⭐⭐⭐ LC 122: Best Time to Buy and Sell Stock II (unlimited)
⭐⭐⭐ LC 123: Best Time to Buy and Sell Stock III (2 transactions)
⭐⭐ LC 188: Best Time to Buy and Sell Stock IV (k transactions)
⭐⭐ LC 309: With Cooldown
⭐⭐ LC 714: With Transaction Fee


═══════════════════════════════════════════════════════════════════════════════
THE BIG 15 DP PROBLEMS TO MASTER (95% Coverage!)
═══════════════════════════════════════════════════════════════════════════════

0/1 KNAPSACK:
1. ⭐⭐⭐ LC 416: Partition Equal Subset Sum
2. ⭐⭐⭐ LC 494: Target Sum

UNBOUNDED KNAPSACK:
3. ⭐⭐⭐ LC 322: Coin Change
4. ⭐⭐⭐ LC 518: Coin Change II

LCS:
5. ⭐⭐⭐ LC 1143: Longest Common Subsequence
6. ⭐⭐⭐ LC 72: Edit Distance

LIS:
7. ⭐⭐⭐ LC 300: Longest Increasing Subsequence

PALINDROME:
8. ⭐⭐⭐ LC 5: Longest Palindromic Substring
9. ⭐⭐⭐ LC 516: Longest Palindromic Subsequence

STOCK:
10. ⭐⭐⭐ LC 121: Stock (1 transaction)
11. ⭐⭐⭐ LC 122: Stock (unlimited)
12. ⭐⭐⭐ LC 123: Stock (2 transactions)

BONUS (Game Theory):
13. ⭐⭐ LC 198: House Robber
14. ⭐⭐ LC 213: House Robber II (circular)
15. ⭐⭐ LC 377: Combination Sum IV


═══════════════════════════════════════════════════════════════════════════════
PRACTICE PLAN - 4 WEEKS
═══════════════════════════════════════════════════════════════════════════════

WEEK 1: KNAPSACK PATTERNS
Day 1-2: LC 416 (try all 3 approaches!)
Day 3-4: LC 494 (understand the transformation!)
Day 5: LC 322 (unbounded vs 0/1)
Day 6-7: LC 518, Review

WEEK 2: LCS & LIS
Day 1-2: LC 1143 (LCS foundation)
Day 3-4: LC 72 (Edit Distance - HARD but important!)
Day 5-6: LC 300 (LIS - both O(n²) and O(n log n))
Day 7: Review all

WEEK 3: PALINDROME & STOCK
Day 1-2: LC 5, LC 516 (Palindrome patterns)
Day 3-4: LC 121, 122, 123 (Stock series)
Day 5-7: Mixed problems, review

WEEK 4: ADVANCED + MOCK
Day 1-3: Harder variants
Day 4-7: Mock interviews, speed practice


═══════════════════════════════════════════════════════════════════════════════
KEY INSIGHTS TO REMEMBER
═══════════════════════════════════════════════════════════════════════════════

1. ALWAYS use REVERSE RECURSION for direct DP mapping
   solve(n, capacity) → start with all items
   
2. Memoization = Recursion + 2 lines:
   - Check cache before computing
   - Store result before returning
   
3. Tabulation = Convert recursion order to loops:
   - solve(i, j) → dp[i][j]
   - return value → dp[i][j] = value
   - solve(i-1) → dp[i-1]
   
4. State = position + remaining resources
   - 0/1 Knapsack: (i, capacity)
   - LCS: (i, j)
   - LIS: (i, prev)
   
5. 0/1 vs Unbounded:
   - 0/1: solve(i-1, ...) after taking
   - Unbounded: solve(i, ...) after taking (can reuse!)
   
6. Greedy fails → DP needed:
   - Coin Change: coins=[1,3,4], amount=6
   - Greedy: 4+1+1=3 ✗, Optimal: 3+3=2 ✓


YOU'RE READY WHEN YOU CAN:
───────────────────────────────────────────────────────────────────────────
□ Write reverse recursion for any DP problem
□ Convert recursion to memo (add 2 lines!)
□ Convert memo to tabulation (change loops!)
□ Explain state clearly for each problem
□ Solve all BIG 15 without hints
□ Distinguish 0/1 from Unbounded
□ Know when greedy fails


GOOD LUCK! Master these patterns and DP becomes your superpower! 🚀
"""