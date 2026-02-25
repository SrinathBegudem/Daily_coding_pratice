"""
═══════════════════════════════════════════════════════════════════════════════
        COMPLETE SUBARRAY/SUBSTRING PATTERN RECOGNITION GUIDE
     WITH GREEDY VS DP DECISION FRAMEWORK - NEVER GET CONFUSED AGAIN!
═══════════════════════════════════════════════════════════════════════════════

🎯 THE ULTIMATE DECISION TREE - MEMORIZE THIS!

                    Subarray/Substring Problem?
                                │
                ┌───────────────┴───────────────┐
                │                               │
          All Positive?                  Has Negatives?
                │                               │
        SLIDING WINDOW!                   ┌─────┴─────┐
          O(n)                            │           │
                                    Exact Sum?    Max Sum?
                                          │           │
                                   PREFIX+HASH   KADANE!
                                      O(n)        O(n)
                                      
                                          
        Special Case: Reachability/Greedy?
                    │
            ┌───────┴───────┐
            │               │
      Can prove?    Try counter?
            │               │
        GREEDY!            DP!
          O(n)            O(n²)


═══════════════════════════════════════════════════════════════════════════════
THE 6 PATTERNS YOU NEED TO MASTER
═══════════════════════════════════════════════════════════════════════════════

1. SLIDING WINDOW → All positive, need length
2. PREFIX SUM + HASHMAP → Has negatives, need EXACT sum
3. KADANE'S ALGORITHM → Has negatives, need MAXIMUM sum
4. TWO POINTERS → Sorted array, opposite ends
5. GREEDY → Reachability, unlimited actions (PROVE IT WORKS!)
6. DYNAMIC PROGRAMMING → Count ways, greedy fails


═══════════════════════════════════════════════════════════════════════════════
PATTERN 1: SLIDING WINDOW
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ All elements POSITIVE (or countable equally)
✅ "longest substring/subarray"
✅ "minimum length"
✅ Window can shrink/expand

❌ FAILS IF:
- Array has NEGATIVES (breaks monotonicity!)
- Need EXACT sum

TEMPLATE:
────────────────────────────────────────────────────────────────────────────
def sliding_window(arr, target):
    left = 0
    window_sum = 0
    result = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum > target:  # Shrink if invalid
            window_sum -= arr[left]
            left += 1
        
        result = max(result, right - left + 1)
    
    return result

TOP PROBLEMS:
⭐⭐⭐ LC 209: Minimum Size Subarray Sum
⭐⭐⭐ LC 3: Longest Substring Without Repeating
⭐⭐⭐ LC 76: Minimum Window Substring
⭐⭐ LC 424: Longest Repeating Character Replacement
⭐⭐ LC 1004: Max Consecutive Ones III


═══════════════════════════════════════════════════════════════════════════════
PATTERN 2: PREFIX SUM + HASHMAP
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ Array HAS NEGATIVES
✅ Need EXACT sum (= k)
✅ "subarray sum equals k"
✅ "count subarrays"

KEY INSIGHT: prefix[j] - prefix[i] = subarray[i+1...j]
If subarray sum = k → prefix[j] - prefix[i] = k
→ prefix[i] = prefix[j] - k

TEMPLATE (Count):
────────────────────────────────────────────────────────────────────────────
def subarray_sum_count(nums, k):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]
        
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    
    return count

TEMPLATE (Max Length):
────────────────────────────────────────────────────────────────────────────
def max_subarray_len(nums, k):
    prefix_sum = 0
    max_len = 0
    hashmap = {0: -1}  # prefix_sum: earliest_index
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if prefix_sum - k in hashmap:
            max_len = max(max_len, i - hashmap[prefix_sum - k])
        
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i
    
    return max_len

TOP PROBLEMS:
⭐⭐⭐ LC 560: Subarray Sum Equals K (MOST IMPORTANT!)
⭐⭐⭐ LC 325: Maximum Size Subarray Sum Equals k
⭐⭐⭐ LC 974: Subarray Sums Divisible by K
⭐⭐⭐ LC 523: Continuous Subarray Sum
⭐⭐⭐ LC 525: Contiguous Array


═══════════════════════════════════════════════════════════════════════════════
PATTERN 3: KADANE'S ALGORITHM
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ Array HAS NEGATIVES
✅ Need MAXIMUM sum (not exact!)
✅ "maximum subarray sum"

KEY INSIGHT: At each position, decide:
- Continue current subarray? (curr_sum + num)
- Start fresh? (num)

TEMPLATE:
────────────────────────────────────────────────────────────────────────────
def kadane(nums):
    max_sum = curr_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

TOP PROBLEMS:
⭐⭐⭐ LC 53: Maximum Subarray (THE ORIGINAL!)
⭐⭐⭐ LC 152: Maximum Product Subarray
⭐⭐ LC 918: Maximum Sum Circular Subarray
⭐⭐ LC 1191: K-Concatenation Maximum Sum


═══════════════════════════════════════════════════════════════════════════════
PATTERN 4: TWO POINTERS
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ Array is SORTED
✅ "two sum", "three sum"
✅ Opposite ends comparison

TEMPLATE:
────────────────────────────────────────────────────────────────────────────
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

TOP PROBLEMS:
⭐⭐⭐ LC 167: Two Sum II
⭐⭐⭐ LC 15: 3Sum
⭐⭐⭐ LC 11: Container With Most Water


═══════════════════════════════════════════════════════════════════════════════
PATTERN 5: GREEDY (THE CONFUSING ONE!)
═══════════════════════════════════════════════════════════════════════════════

🎯 THE BIG QUESTION: "WHEN GREEDY VS DP?"

This confuses EVERYONE! Here's the decision framework:

GREEDY WORKS IF:
✅ Local optimal → Global optimal (can PROVE it!)
✅ No need to reconsider decisions
✅ One pass solves it
✅ Can explain WHY clearly

DP NEEDED IF:
❌ Greedy counterexample exists!
❌ Must explore ALL possibilities
❌ "Count number of ways"
❌ Overlapping subproblems


THE 3-QUESTION TEST (Before using Greedy):
────────────────────────────────────────────────────────────────────────────

Q1: "Can I find COUNTEREXAMPLE where greedy fails?"
    YES → Use DP!
    NO → Continue to Q2

Q2: "Does local optimal guarantee global optimal?"
    YES → Greedy works!
    NO → Use DP!

Q3: "Do I need to reconsider past decisions?"
    YES → Use DP!
    NO → Greedy works!


TEMPLATE 1: MAXIMUM REACHABILITY (Jump Game)
────────────────────────────────────────────────────────────────────────────
def can_jump(nums):
    \"""
    LC 55: Jump Game ⭐⭐⭐ #1 GREEDY PROBLEM!
    
    Input: [2,3,1,1,4]
    Output: True
    
    WHY GREEDY WORKS:
    If we can reach i, we've checked ALL j < i.
    So max_reach gives global optimality!
    \"""
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return True


def min_jumps(nums):
    \"""
    LC 45: Jump Game II ⭐⭐⭐
    
    Input: [2,3,1,1,4]
    Output: 2 (0→1→4)
    
    WHY GREEDY WORKS:
    BFS-like. Each level = one jump.
    Going furthest at each level is optimal!
    \"""
    jumps = 0
    current_end = 0
    furthest = 0
    
    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = furthest
    
    return jumps


TEMPLATE 2: FAILURE PROPAGATION (Gas Station)
────────────────────────────────────────────────────────────────────────────
def can_complete_circuit(gas, cost):
    \"""
    LC 134: Gas Station ⭐⭐⭐ TRICKIEST GREEDY!
    
    Input: gas=[1,2,3,4,5], cost=[3,4,5,1,2]
    Output: 3
    
    🔑 GENIUS INSIGHT:
    If we start at i and FAIL to reach j,
    then starting at ANY k (i < k < j) will ALSO FAIL!
    
    WHY? Starting at k has LESS gas than starting at i
    (we used gas to reach k from i).
    
    This "failure propagation" makes greedy optimal!
    \"""
    total = 0
    current = 0
    start = 0
    
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        current += gas[i] - cost[i]
        
        if current < 0:
            start = i + 1  # Skip entire [start, i]!
            current = 0
    
    return start if total >= 0 else -1


TEMPLATE 3: CAPTURE ALL INCREASES (Stock Trading)
────────────────────────────────────────────────────────────────────────────
def max_profit(prices):
    \"""
    LC 122: Stock II ⭐⭐⭐
    
    Input: [7,1,5,3,6,4]
    Output: 7 (buy 1 sell 5: +4, buy 3 sell 6: +3)
    
    WHY GREEDY WORKS:
    Every upward price = profit opportunity!
    Capture ALL increases!
    \"""
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit


TEMPLATE 4: SORT + ASSIGN (Matching)
────────────────────────────────────────────────────────────────────────────
def assign_cookies(children, cookies):
    \"""
    LC 455: Assign Cookies ⭐⭐
    
    Input: children=[1,2,3], cookies=[1,1]
    Output: 1
    
    WHY GREEDY WORKS:
    Sort both!
    Give smallest cookie to least greedy child.
    \"""
    children.sort()
    cookies.sort()
    
    child = cookie = 0
    
    while child < len(children) and cookie < len(cookies):
        if cookies[cookie] >= children[child]:
            child += 1
        cookie += 1
    
    return child


TEMPLATE 5: TWO-PASS GREEDY (Candy)
────────────────────────────────────────────────────────────────────────────
def candy(ratings):
    \"""
    LC 135: Candy ⭐⭐⭐ HARDEST GREEDY!
    
    Input: [1,0,2]
    Output: 5 ([2,1,2])
    
    WHY TWO-PASS?
    Can't satisfy BOTH neighbors in one pass!
    
    Pass 1: Satisfy left neighbor
    Pass 2: Satisfy right neighbor
    Take MAX!
    \"""
    n = len(ratings)
    candies = [1] * n
    
    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    # Right to left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    return sum(candies)


TOP GREEDY PROBLEMS:
────────────────────────────────────────────────────────────────────────────
EASY:
✅ LC 455: Assign Cookies ⭐⭐
✅ LC 860: Lemonade Change ⭐⭐
✅ LC 1710: Maximum Units on Truck ⭐⭐

MEDIUM:
✅ LC 55: Jump Game ⭐⭐⭐ #1 MOST IMPORTANT!
✅ LC 45: Jump Game II ⭐⭐⭐
✅ LC 134: Gas Station ⭐⭐⭐ (Understand this deeply!)
✅ LC 122: Stock II ⭐⭐⭐
✅ LC 406: Queue Reconstruction ⭐⭐
✅ LC 881: Boats to Save People ⭐⭐

HARD:
✅ LC 135: Candy ⭐⭐⭐


GREEDY EXAMPLES SHOWING WHY IT WORKS:
────────────────────────────────────────────────────────────────────────────

EXAMPLE: Jump Game (LC 55)
nums = [2,3,1,1,4]

GREEDY O(n):
i=0: max_reach = max(0, 0+2) = 2
i=1: max_reach = max(2, 1+3) = 4 ≥ 4 ✓
Return True

WHY NOT DP?
- DP would be O(n²)
- Greedy proves local max_reach = global reachability!


EXAMPLE: Gas Station (LC 134)
gas=[1,2,3,4,5], cost=[3,4,5,1,2]

Start at 0: current = -2 (fail!) → skip to 1
Start at 1: current = -2 (fail!) → skip to 2
Start at 2: current = -2 (fail!) → skip to 3
Start at 3: current = 3 ✓
Continue... total ≥ 0 ✓
Return 3


WHEN GREEDY FAILS - USE DP!
────────────────────────────────────────────────────────────────────────────

EXAMPLE: Coin Change
coins = [1,3,4], amount = 6

GREEDY: Take largest first
- Take 4 (remaining: 2)
- Take 1, 1 (remaining: 0)
- Total: 3 coins ✗

OPTIMAL (DP):
- Take 3, 3
- Total: 2 coins ✓

Greedy FAILS! Must use DP!


EXAMPLE: Partition Equal Subset Sum
nums = [1,5,11,5], target = 11

GREEDY: Take 11? But then [1,5,5] = 11 too!
What if we needed 11 in other partition?
Need to TRY BOTH! → DP!


═══════════════════════════════════════════════════════════════════════════════
PATTERN 6: DYNAMIC PROGRAMMING
═══════════════════════════════════════════════════════════════════════════════

🔑 WHEN TO USE:
✅ "Count number of ways" (ALWAYS DP!)
✅ "Can partition into K parts"
✅ Greedy counterexample exists
✅ Must track multiple states
✅ Overlapping subproblems

TOP PROBLEMS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 416: Partition Equal Subset Sum (greedy fails!)
⭐⭐⭐ LC 494: Target Sum (count ways → DP!)
⭐⭐⭐ LC 322: Coin Change (greedy fails!)
⭐⭐⭐ LC 198: House Robber
⭐⭐ LC 1043: Partition Array Maximum Sum
⭐⭐ LC 188: Stock IV (K transactions limit)


═══════════════════════════════════════════════════════════════════════════════
GREEDY VS DP DECISION TABLE
═══════════════════════════════════════════════════════════════════════════════

| Problem Type | Greedy? | DP? | Why? |
|-------------|---------|-----|------|
| Can reach end? | ✅ | ❌ | Track max reach works |
| Min jumps? | ✅ | ❌ | BFS-like greedy optimal |
| Max profit unlimited? | ✅ | ❌ | Sum all increases |
| Max profit K times? | ❌ | ✅ | Need state tracking |
| Can partition equal? | ❌ | ✅ | Greedy fails! |
| Count ways? | ❌ | ✅ | Must explore all |
| Coin change? | ❌ | ✅ | Classic greedy failure |
| Gas station? | ✅ | ❌ | Failure propagation |
| Assign cookies? | ✅ | ❌ | Sort + match works |


═══════════════════════════════════════════════════════════════════════════════
THE ULTIMATE DECISION FLOWCHART
═══════════════════════════════════════════════════════════════════════════════

Step 1: CHECK FOR NEGATIVES
────────────────────────────────────────────────────────────────────────────
Has negatives?
├─ NO → SLIDING WINDOW (if need length)
└─ YES → Go to Step 2


Step 2: EXACT SUM OR MAX SUM?
────────────────────────────────────────────────────────────────────────────
What do we need?
├─ EXACT sum (= k) → PREFIX SUM + HASHMAP
├─ MAX sum → KADANE
└─ Neither → Go to Step 3


Step 3: IS IT REACHABILITY?
────────────────────────────────────────────────────────────────────────────
"Can reach/complete?"
├─ YES → Try GREEDY (but prove it!)
└─ NO → Go to Step 4


Step 4: CAN YOU PROVE GREEDY?
────────────────────────────────────────────────────────────────────────────
Find counterexample?
├─ NO counterexample → GREEDY works!
└─ Found counterexample → DP!


Step 5: COUNT WAYS?
────────────────────────────────────────────────────────────────────────────
"Count number of ways"?
├─ YES → DP (always!)
└─ NO → Review Steps 1-4


═══════════════════════════════════════════════════════════════════════════════
COMPLETE PROBLEM LIST
═══════════════════════════════════════════════════════════════════════════════

🔵 SLIDING WINDOW:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 209: Minimum Size Subarray Sum
⭐⭐⭐ LC 3: Longest Substring Without Repeating
⭐⭐⭐ LC 76: Minimum Window Substring
⭐⭐ LC 424: Longest Repeating Character Replacement
⭐⭐ LC 1004: Max Consecutive Ones III
⭐⭐ LC 1493: Longest Subarray of 1's
⭐⭐ LC 2024: Maximize Confusion of Exam

🟢 PREFIX SUM + HASHMAP:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 560: Subarray Sum Equals K (MOST IMPORTANT!)
⭐⭐⭐ LC 325: Maximum Size Subarray Sum Equals k
⭐⭐⭐ LC 974: Subarray Sums Divisible by K
⭐⭐⭐ LC 523: Continuous Subarray Sum
⭐⭐⭐ LC 525: Contiguous Array
⭐⭐ LC 1248: Count Nice Subarrays
⭐⭐ LC 930: Binary Subarrays With Sum
⭐⭐ LC 1074: Number of Submatrices Sum to Target

🟡 KADANE'S:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 53: Maximum Subarray
⭐⭐⭐ LC 152: Maximum Product Subarray
⭐⭐ LC 918: Maximum Sum Circular Subarray
⭐⭐ LC 1191: K-Concatenation Maximum Sum

🟣 TWO POINTERS:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 167: Two Sum II
⭐⭐⭐ LC 15: 3Sum
⭐⭐ LC 16: 3Sum Closest
⭐⭐⭐ LC 11: Container With Most Water

🟠 GREEDY:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 55: Jump Game (#1 GREEDY!)
⭐⭐⭐ LC 45: Jump Game II
⭐⭐⭐ LC 134: Gas Station (Trickiest!)
⭐⭐⭐ LC 122: Stock II
⭐⭐⭐ LC 135: Candy (Hardest!)
⭐⭐ LC 455: Assign Cookies
⭐⭐ LC 860: Lemonade Change

🔴 DYNAMIC PROGRAMMING:
────────────────────────────────────────────────────────────────────────────
⭐⭐⭐ LC 416: Partition Equal Subset Sum
⭐⭐⭐ LC 494: Target Sum
⭐⭐⭐ LC 322: Coin Change
⭐⭐⭐ LC 198: House Robber
⭐⭐ LC 1043: Partition Array Maximum Sum


═══════════════════════════════════════════════════════════════════════════════
PRACTICE PLAN - 4 WEEKS
═══════════════════════════════════════════════════════════════════════════════

WEEK 1: SLIDING WINDOW + PREFIX SUM
Day 1-2: LC 209, LC 3
Day 3-4: LC 560 (CRITICAL!) ⚠️⚠️⚠️
Day 5: LC 325 (your question!)
Day 6-7: LC 974, LC 523, review

WEEK 2: KADANE + GREEDY
Day 1-2: LC 53 (Kadane)
Day 3-4: LC 55, LC 45 (Greedy foundations)
Day 5: LC 134 (Gas Station - SPEND TIME!)
Day 6-7: LC 122, LC 135, review

WEEK 3: GREEDY VS DP
Day 1-2: LC 416 (try greedy, watch fail, then DP)
Day 3: LC 322 (greedy fails!)
Day 4-5: LC 494 (count ways → DP)
Day 6-7: Compare all greedy vs DP problems

WEEK 4: MIXED + REVIEW
Day 1-3: Mixed pattern problems
Day 4-5: Speed practice
Day 6-7: Mock interviews


═══════════════════════════════════════════════════════════════════════════════
THE BIG 10 TO MASTER (90% Coverage!)
═══════════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LC 560 (Prefix Sum + HashMap - count)
2. ⭐⭐⭐ LC 325 (Prefix Sum + HashMap - length)
3. ⭐⭐⭐ LC 209 (Sliding Window)
4. ⭐⭐⭐ LC 53 (Kadane)
5. ⭐⭐⭐ LC 3 (Sliding Window - substring)
6. ⭐⭐⭐ LC 55 (Greedy - Jump Game)
7. ⭐⭐⭐ LC 134 (Greedy - Gas Station)
8. ⭐⭐⭐ LC 122 (Greedy - Stock II)
9. ⭐⭐⭐ LC 416 (DP - Partition)
10. ⭐⭐⭐ LC 322 (DP - Coin Change)


═══════════════════════════════════════════════════════════════════════════════
MEMORY TRICKS
═══════════════════════════════════════════════════════════════════════════════

🎯 "SPANK-G" Method:

S - SLIDING: All positive? Slide it!
P - PREFIX: Need exact? Prefix + Hash it!
A - ALGORITHM (Kadane): Max sum? Kadane it!
N - NO pattern? Check Two Pointers!
K - KEEP (reachability)? Try Greedy! (but prove it!)
G - GIVE UP (greedy fails)? DP!


🎯 The "Negative Check":
Has negatives?
├─ Exact sum? → PREFIX + HASH
├─ Max sum? → KADANE
└─ Reachability? → Try GREEDY (prove it!)

No negatives?
└─ SLIDING WINDOW!


🎯 The "Count Ways Check":
"Count ways" or "count number"?
└─ DP (always!)


═══════════════════════════════════════════════════════════════════════════════
YOU'RE READY WHEN:
═══════════════════════════════════════════════════════════════════════════════

□ Decide pattern in <30 seconds
□ Solve all BIG 10 without hints
□ Explain WHY greedy works for LC 55, 134, 122
□ Find counterexample for LC 416, 322
□ Know when sliding window FAILS (negatives!)
□ Understand prefix sum formula by heart
□ Implement Kadane from memory
□ Never confuse "exact sum" with "max sum"
□ Can prove when greedy works vs fails
□ Recognize "count ways" → always DP


GOOD LUCK! You now have the COMPLETE framework! 🚀
\"""


if __name__ == "__main__":
    print("=" * 80)
    print("QUICK REFERENCE:")
    print("=" * 80)
    print()
    print("❓ All positive + need length?")
    print("   → SLIDING WINDOW")
    print()
    print("❓ Has negatives + exact sum?")
    print("   → PREFIX SUM + HASHMAP")
    print()
    print("❓ Has negatives + max sum?")
    print("   → KADANE")
    print()
    print("❓ Can reach/complete?")
    print("   → Try GREEDY (but PROVE it!)")
    print()
    print("❓ Count ways?")
    print("   → DP (always!)")
    print()
    print("=" * 80)
"""