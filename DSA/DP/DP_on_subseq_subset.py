from typing import List

"""
═══════════════════════════════════════════════════════════════════════════════
          DP ON SUBSEQUENCES / SUBSETS — THE 3 CORE PATTERNS
              *** UNIVERSAL VERSION (handles zeros in array) ***
═══════════════════════════════════════════════════════════════════════════════

🎯 THE BIG PICTURE:

   For each element: TAKE it or SKIP it

   skip = dp(i-1, s)               ← don't include nums[i-1]
   take = dp(i-1, s - nums[i-1])   ← include nums[i-1]

   HOW we combine skip and take defines the PATTERN:

   ┌──────────────┬───────────┬──────────┬────────────────────┐
   │   Pattern    │ Combine   │ Base     │ Question           │
   ├──────────────┼───────────┼──────────┼────────────────────┤
   │ 1. Counting  │ skip+take │ 1 or 0   │ HOW MANY ways?     │
   │ 2. Boolean   │ skip|take │ T or F   │ IS IT possible?    │
   │ 3. Optimize  │ min/max   │ 0 or INF │ WHAT'S the best?   │
   └──────────────┴───────────┴──────────┴────────────────────┘

═══════════════════════════════════════════════════════════════════════════════

🔥 WHY UNIVERSAL? — THE ZERO BUG IN OLD TEMPLATES:

   OLD (BROKEN with zeros):
     Pre-fill ENTIRE column 0: dp[i][0] = 1 for all i
     Inner loop: for s in range(1, target+1)    ← skips s=0

     Bug: nums = [0, 1, 2], counting subsets summing to 0
       Pre-fill hardcodes dp[1][0] = 1
       But REAL answer is 2 → {} and {0} both sum to 0!

   NEW (UNIVERSAL):
     Set ONLY dp[0][0] = base_value
     Inner loop: for s in range(target + 1)     ← includes s=0

     Now: dp[1][0] = skip + take = dp[0][0] + dp[0][0] = 1 + 1 = 2 ✓

   RULE: Set ONLY dp[0][0]. Let the loop handle EVERYTHING else.

═══════════════════════════════════════════════════════════════════════════════
"""


# ═══════════════════════════════════════════════════════════════════════════
# ███████████████████████████████████████████████████████████████████████████
#
#   PATTERN 1: COUNTING DP — "How many subsets sum to target?"
#
#   Combine: dp[i][s] = skip + take
#   Base:    dp[0][0] = 1  (one way: empty subset)
#            dp[0][s>0] = 0 (zero init handles this)
#
# ███████████████████████████████████████████████████████████████████████████
# ═══════════════════════════════════════════════════════════════════════════
"""
📝 DRY RUN WITH ZEROS: nums = [0, 1, 2, 3], target = 3

   Subsets summing to 3:
   {3}, {1,2}, {0,3}, {0,1,2} → Answer: 4

        s:  0  1  2  3
   i=0:     1  0  0  0    ← ONLY dp[0][0]=1
   i=1:     2  0  0  0    ← element=0: s=0: skip=1, take=dp[0][0-0]=1 → 2
   i=2:     2  2  0  0    ← element=1: s=0: skip=2, s<1 no take → 2
                                        s=1: skip=0, take=dp[1][0]=2 → 2
   i=3:     2  2  2  2    ← element=2
   i=4:     2  2  2  4    ← element=3: s=3: skip=2, take=dp[3][0]=2 → 4 ✓

   OLD pre-fill would give dp[1][0]=1 → final answer=2 ❌

📝 DRY RUN NO ZEROS: nums = [1, 2, 3], target = 3

        s:  0  1  2  3
   i=0:     1  0  0  0
   i=1:     1  1  0  0    ← s=0: skip=1, 0<1 can't take → 1 (propagates!)
   i=2:     1  1  1  1
   i=3:     1  1  1  2    ← s=3: skip=1, take=dp[2][0]=1 → 2 ✓

   Column 0 naturally stays 1 via skip path. No pre-fill needed!

💡 LEETCODE PROBLEMS:
   ⭐⭐⭐ 494. Target Sum (medium) — reduces to counting subsets
   ⭐⭐⭐ 518. Coin Change II (medium) — unbounded variant
   ⭐⭐  377. Combination Sum IV (medium)
   ⭐   1155. Number of Dice Rolls With Target Sum (medium)
"""


def count_subsets_memo(nums: List[int], target: int) -> int:
    """FUNCTION 1/9: Counting — Memoization"""
    n = len(nums)
    cache = {}

    def solve(i, s):
        if i == 0:
            return 1 if s == 0 else 0

        if (i, s) in cache:
            return cache[(i, s)]

        skip = solve(i - 1, s)

        take = 0
        if s >= nums[i - 1]:       # works when nums[i-1]=0: 0>=0 is True
            take = solve(i - 1, s - nums[i - 1])

        cache[(i, s)] = skip + take
        return cache[(i, s)]

    return solve(n, target)


def count_subsets_2d_dp(nums: List[int], target: int) -> int:
    """
    FUNCTION 2/9: Counting — 2D Table (UNIVERSAL)

    🔥 ONLY dp[0][0] = 1.  Inner loop from s = 0.
    """
    n = len(nums)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    dp[0][0] = 1                             # ✅ ONLY base

    for i in range(1, n + 1):
        for s in range(target + 1):          # 🔥 FROM 0, not 1
            skip = dp[i - 1][s]

            take = 0
            if s >= nums[i - 1]:
                take = dp[i - 1][s - nums[i - 1]]

            dp[i][s] = skip + take

    return dp[n][target]


def count_subsets_1d_dp(nums: List[int], target: int) -> int:
    """
    FUNCTION 3/9: Counting — 1D Backward (UNIVERSAL)

    If nums[i-1]=0: dp[s] += dp[s-0] = dp[s] → doubles.
    Correct! {} and {0} both make same sum → 2× ways.

    📝 TRACE: nums = [0, 1, 2, 3], target = 3

    dp = [1, 0, 0, 0]

    i=1 (el=0), backward s=3 to s=0:
      s=0: dp[0] += dp[0] → 1+1=2
      dp = [2, 0, 0, 0]

    i=2 (el=1), backward s=3 to s=1:
      s=1: dp[1] += dp[0] = 0+2=2
      dp = [2, 2, 0, 0]

    i=3 (el=2), backward s=3 to s=2:
      s=3: dp[3] += dp[1] = 0+2=2
      s=2: dp[2] += dp[0] = 0+2=2
      dp = [2, 2, 2, 2]

    i=4 (el=3), backward s=3 to s=3:
      s=3: dp[3] += dp[0] = 2+2=4 ✓
      dp = [2, 2, 2, 4]
    """
    n = len(nums)
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for s in range(target, nums[i - 1] - 1, -1):   # down to element value
            dp[s] += dp[s - nums[i - 1]]

    return dp[target]


# ═══════════════════════════════════════════════════════════════════════════
# ███████████████████████████████████████████████████████████████████████████
#
#   PATTERN 2: BOOLEAN DP — "Can any subset sum to target?"
#
#   Combine: dp[i][s] = skip OR take
#   Base:    dp[0][0] = True
#            dp[0][s>0] = False (False init handles this)
#
# ███████████████████████████████████████████████████████████████████████████
# ═══════════════════════════════════════════════════════════════════════════
"""
📝 DRY RUN: nums = [1, 5, 11, 5], target = 11

        s:  0   1   2   3   4   5   6  ...  11
   i=0:     T   F   F   F   F   F   F  ...   F
   i=1:     T   T   F   F   F   F   F        F
       s=0: skip=T, 0<1 can't take → T  (propagates naturally!)
       s=1: skip=F, take=dp[0][0]=T → T
   i=2:     T   T   F   F   F   T   T        F
   i=3:     T   T   F   F   F   T   T        T ✓
       s=11: skip=F, take=dp[2][0]=T → T
   i=4:     T   T   F   F   F   T   T        T

🔥 Column 0 propagation without pre-fill:
   When element > 0: skip carries T down, can't take → T ✓
   When element = 0: skip=T, take=T, T or T = T ✓

💡 LEETCODE PROBLEMS:
   ⭐⭐⭐ 416. Partition Equal Subset Sum (medium) — THE classic
   ⭐⭐⭐ 698. Partition to K Equal Sum Subsets (medium)
   ⭐⭐  473. Matchsticks to Square (medium)
"""


def subset_sum_memo(nums: List[int], target: int) -> bool:
    """FUNCTION 4/9: Boolean — Memoization"""
    n = len(nums)
    cache = {}

    def solve(i, s):
        if i == 0:
            return s == 0

        if (i, s) in cache:
            return cache[(i, s)]

        skip = solve(i - 1, s)

        take = False
        if s >= nums[i - 1]:
            take = solve(i - 1, s - nums[i - 1])

        cache[(i, s)] = skip or take
        return cache[(i, s)]

    return solve(n, target)


def subset_sum_2d_dp(nums: List[int], target: int) -> bool:
    """
    FUNCTION 5/9: Boolean — 2D Table (UNIVERSAL)

    🔥 ONLY dp[0][0] = True. Inner loop from s = 0.
    """
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    dp[0][0] = True                          # ✅ ONLY base

    for i in range(1, n + 1):
        for s in range(target + 1):          # 🔥 FROM 0, not 1
            skip = dp[i - 1][s]

            take = False
            if s >= nums[i - 1]:
                take = dp[i - 1][s - nums[i - 1]]

            dp[i][s] = skip or take

    return dp[n][target]


def subset_sum_1d_dp(nums: List[int], target: int) -> bool:
    """
    FUNCTION 6/9: Boolean — 1D Backward (UNIVERSAL)

    If nums[i-1]=0: dp[s] = dp[s] or dp[s] → no change.
    Correct! Adding 0 doesn't unlock new sums.

    📝 TRACE: nums = [1, 5, 11, 5], target = 11

    dp = [T, F, F, F, F, F, F, F, F, F, F, F]

    i=1 (el=1): s=1: dp[1] |= dp[0]=T → T
      dp = [T, T, F, F, F, F, F, F, F, F, F, F]

    i=2 (el=5): s=6: |=dp[1]=T, s=5: |=dp[0]=T
      dp = [T, T, F, F, F, T, T, F, F, F, F, F]

    i=3 (el=11): s=11: |=dp[0]=T ✓
      dp = [T, T, F, F, F, T, T, F, F, F, F, T]

    i=4 (el=5): s=10: |=dp[5]=T
      dp = [T, T, F, F, F, T, T, F, F, F, T, T]
    """
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for s in range(target, nums[i - 1] - 1, -1):
            dp[s] = dp[s] or dp[s - nums[i - 1]]

    return dp[target]


# ═══════════════════════════════════════════════════════════════════════════
# ███████████████████████████████████████████████████████████████████████████
#
#   PATTERN 3: OPTIMIZATION DP — "Min partition difference?"
#
#   Partition nums into S1, S2. Minimize |sum(S1) - sum(S2)|.
#   → Find max subset sum ≤ total/2.
#
#   dp[i][s] = max achievable sum using first i elements with budget s
#   Combine: max(skip, take)
#   Base:    dp[0][s] = 0 for all s (all-zeros init handles this)
#
# ███████████████████████████████████████████████████████████████████████████
# ═══════════════════════════════════════════════════════════════════════════
"""
📝 DRY RUN: nums = [1, 6, 11, 5], total = 23, half = 11

   Best: S1={6,5}=11, S2={1,11}=12 → diff=1

        s:  0  1  2  3  4  5  6  7  8  9 10 11
   i=0:     0  0  0  0  0  0  0  0  0  0  0  0
   i=1:     0  1  1  1  1  1  1  1  1  1  1  1
       s=0: skip=0, 0<1 can't take → 0
       s=1: skip=0, take=1+dp[0][0]=1 → 1
   i=2:     0  1  1  1  1  1  6  7  7  7  7  7
       s=6: skip=1, take=6+dp[1][0]=6 → 6
   i=3:     0  1  1  1  1  1  6  7  7  7  7 11
       s=11: skip=7, take=11+dp[2][0]=11 → 11
   i=4:     0  1  1  1  1  5  6  7  7  7  7 11

   best_s1 = 11 → diff = 23 - 22 = 1 ✓

💡 LEETCODE PROBLEMS:
   ⭐⭐⭐ 1049. Last Stone Weight II (medium) — exactly this!
   ⭐⭐  2035. Partition Array Min Sum Diff (hard)
   ⭐   1755. Closest Subsequence Sum (hard)
"""


def min_subset_diff_memo(nums: List[int]) -> int:
    """FUNCTION 7/9: Optimization — Memoization"""
    total = sum(nums)
    half = total // 2
    n = len(nums)
    cache = {}

    def solve(i, s):
        if i == 0:
            return 0

        if (i, s) in cache:
            return cache[(i, s)]

        skip = solve(i - 1, s)

        take = -1
        if s >= nums[i - 1]:
            take = nums[i - 1] + solve(i - 1, s - nums[i - 1])

        cache[(i, s)] = max(skip, take)
        return cache[(i, s)]

    best_s1 = solve(n, half)
    return abs(total - 2 * best_s1)


def min_subset_diff_2d_dp(nums: List[int]) -> int:
    """
    FUNCTION 8/9: Optimization — 2D Table (UNIVERSAL)

    Base row all zeros. Inner loop from s = 0.
    """
    total = sum(nums)
    half = total // 2
    n = len(nums)
    dp = [[0] * (half + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for s in range(half + 1):            # 🔥 FROM 0
            skip = dp[i - 1][s]

            take = -1
            if s >= nums[i - 1]:
                take = nums[i - 1] + dp[i - 1][s - nums[i - 1]]

            dp[i][s] = max(skip, take)

    best_s1 = dp[n][half]
    return abs(total - 2 * best_s1)


def min_subset_diff_1d_dp(nums: List[int]) -> int:
    """
    FUNCTION 9/9: Optimization — 1D Backward (UNIVERSAL)

    If nums[i-1]=0: dp[s] = max(dp[s], 0+dp[s]) = dp[s] → no change.
    Correct! Adding 0 doesn't change subset sum.

    📝 TRACE: nums = [1, 6, 11, 5], half = 11

    dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i=1 (el=1): s=1: max(0, 1+0)=1  ...same for s=2..11
      dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    i=2 (el=6): s=11: max(1,6+dp[5])=7, s=7: 7, s=6: 6
      dp = [0, 1, 1, 1, 1, 1, 6, 7, 7, 7, 7, 7]

    i=3 (el=11): s=11: max(7,11+dp[0])=11 ✓
      dp = [0, 1, 1, 1, 1, 1, 6, 7, 7, 7, 7, 11]

    i=4 (el=5): s=5: max(1,5+0)=5
      dp = [0, 1, 1, 1, 1, 5, 6, 7, 7, 7, 7, 11]

    best_s1=11 → diff = 23-22 = 1 ✓
    """
    total = sum(nums)
    half = total // 2
    n = len(nums)
    dp = [0] * (half + 1)

    for i in range(1, n + 1):
        for s in range(half, nums[i - 1] - 1, -1):
            dp[s] = max(dp[s], nums[i - 1] + dp[s - nums[i - 1]])

    best_s1 = dp[half]
    return abs(total - 2 * best_s1)


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 COMPREHENSIVE TESTS — including ZERO edge cases
# ═══════════════════════════════════════════════════════════════════════════

def test_all():
    print("=" * 70)
    print("  DP ON SUBSEQUENCES — UNIVERSAL VERSION (handles zeros)")
    print("=" * 70)

    # ─── PATTERN 1: COUNTING ─────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  PATTERN 1: COUNTING (skip + take)")
    print(f"{'─'*60}")

    tests_count = [
        ([1, 2, 3], 3, 2, "basic: {3},{1,2}"),
        ([0, 1, 2, 3], 3, 4, "🔥 ZEROS: {3},{1,2},{0,3},{0,1,2}"),
        ([0, 0, 1], 1, 4, "🔥 TWO ZEROS: 4 ways"),
        ([1, 1, 1, 1, 1], 3, 10, "C(5,3)=10"),
        ([5], 5, 1, "single match"),
        ([5], 3, 0, "single no match"),
        ([], 0, 1, "empty target=0"),
    ]

    for nums, target, expected, desc in tests_count:
        r1 = count_subsets_memo(nums, target)
        r2 = count_subsets_2d_dp(nums, target)
        r3 = count_subsets_1d_dp(nums, target)
        ok = (r1 == r2 == r3 == expected)
        print(f"  {'✅' if ok else '❌'} {desc}")
        print(f"     nums={nums}, target={target} → memo={r1}, 2d={r2}, 1d={r3} (exp={expected})")

    # ─── PATTERN 2: BOOLEAN ──────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  PATTERN 2: BOOLEAN (skip or take)")
    print(f"{'─'*60}")

    tests_bool = [
        ([1, 5, 11, 5], 11, True, "LC 416: {11} or {1,5,5}"),
        ([1, 2, 3, 5], 15, False, "impossible: total=11<15"),
        ([0, 1, 5], 0, True, "🔥 ZERO: target=0"),
        ([0, 0, 0], 0, True, "🔥 ALL ZEROS"),
        ([3, 3, 3], 6, True, "{3,3}"),
        ([2, 4], 3, False, "no subset sums to 3"),
        ([], 0, True, "empty target=0"),
    ]

    for nums, target, expected, desc in tests_bool:
        r1 = subset_sum_memo(nums, target)
        r2 = subset_sum_2d_dp(nums, target)
        r3 = subset_sum_1d_dp(nums, target)
        ok = (r1 == r2 == r3 == expected)
        print(f"  {'✅' if ok else '❌'} {desc}")
        print(f"     nums={nums}, target={target} → memo={r1}, 2d={r2}, 1d={r3} (exp={expected})")

    # LC 416 demo
    nums_416 = [1, 5, 11, 5]
    t = sum(nums_416)
    can = (t % 2 == 0) and subset_sum_1d_dp(nums_416, t // 2)
    print(f"\n  {'✅' if can else '❌'} LC 416: {nums_416} → canPartition={can}")

    # ─── PATTERN 3: OPTIMIZATION ─────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  PATTERN 3: OPTIMIZATION (max of skip, take)")
    print(f"{'─'*60}")

    tests_opt = [
        ([1, 6, 11, 5], 1, "{6,5}=11 vs {1,11}=12"),
        ([2, 7, 4, 1, 8, 1], 1, "LC 1049: stones"),
        ([3, 3], 0, "equal split"),
        ([1], 1, "single element"),
        ([0, 1, 6, 11, 5], 1, "🔥 ZERO in array"),
        ([0, 0, 5, 5], 0, "🔥 ZEROS: {0,5} vs {0,5}"),
    ]

    for nums, expected, desc in tests_opt:
        r1 = min_subset_diff_memo(nums)
        r2 = min_subset_diff_2d_dp(nums)
        r3 = min_subset_diff_1d_dp(nums)
        ok = (r1 == r2 == r3 == expected)
        print(f"  {'✅' if ok else '❌'} {desc}")
        print(f"     nums={nums} → memo={r1}, 2d={r2}, 1d={r3} (exp={expected})")

    # ─── BONUS: LC 494 Target Sum ────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  BONUS: LC 494 Target Sum (reduces to Counting)")
    print(f"{'─'*60}")

    def target_sum(nums, target):
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        p = (total + target) // 2
        return count_subsets_1d_dp(nums, p)

    tests_494 = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([1], 1, 1),
        ([0, 0, 1], 1, 4, ),
    ]

    for nums, target, expected in tests_494:
        result = target_sum(nums, target)
        print(f"  {'✅' if result == expected else '❌'} nums={nums}, target={target} → {result} (exp={expected})")

    print(f"\n{'=' * 70}")
    print(f"  ALL TESTS COMPLETE!")
    print(f"{'=' * 70}")


# ═══════════════════════════════════════════════════════════════════════════
# 📊 MASTER CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════
"""
┌───────────────┬─────────────┬────────────────┬───────────────┬──────────────┐
│  Pattern      │ Question    │ Combine        │ Base dp[0][0] │ Base dp[0][s]│
├───────────────┼─────────────┼────────────────┼───────────────┼──────────────┤
│ 1. Counting   │ How many?   │ skip + take    │ 1             │ 0            │
│ 2. Boolean    │ Possible?   │ skip or take   │ True          │ False        │
│ 3. Optimize   │ Best value? │ max(skip,take) │ 0             │ 0            │
└───────────────┴─────────────┴────────────────┴───────────────┴──────────────┘

🔥 UNIVERSAL RULES:
  1. Set ONLY dp[0][0]. Do NOT pre-fill entire column 0.
  2. Inner loop: for s in range(target + 1) — ALWAYS from 0.
  3. Column 0 propagates naturally via the skip path.
  4. 1D: BACKWARD loop (0/1 knapsack, each element once).

WHY THIS WORKS FOR COLUMN 0:

  s=0, element > 0:
    skip = dp[i-1][0]  → carries base forward
    take: 0 < element  → can't take
    dp[i][0] = skip    → same as row above ✓

  s=0, element = 0:
    skip = dp[i-1][0]
    take = dp[i-1][0]  (s - 0 = 0)

    Counting: skip+take = 2 × dp[i-1][0]   → DOUBLES ✓ ({} and {0})
    Boolean:  skip or take = same           → no change ✓
    Optimize: max(skip,take) = same         → no change ✓

  Pre-filling MISSES the doubling for counting → WRONG!

═══════════════════════════════════════════════════════════════════════════════

🎯 MUST-DO LEETCODE (Ranked)

TIER 1:
  416  Partition Equal Subset Sum    Boolean     Amazon/Google/Meta
  494  Target Sum                    Counting    Amazon/Google/Meta
  322  Coin Change                   Optimize    (unbounded, in knapsack file)
  518  Coin Change II                Counting    (unbounded, in knapsack file)
  1049 Last Stone Weight II          Optimize    Google/Amazon

TIER 2:
  474  Ones and Zeroes               Optimize    Google
  377  Combination Sum IV            Counting    Google/Amazon
  279  Perfect Squares               Optimize    Amazon/Google
  698  Partition to K Equal Sum      Boolean     Amazon/Google

═══════════════════════════════════════════════════════════════════════════════

🔄 PROBLEM → PATTERN MAP

LC 416: total/2 → BOOLEAN subset_sum
LC 494: P=(total+target)/2 → COUNTING count_subsets
LC 1049: partition → OPTIMIZE min_subset_diff
LC 518: unlimited coins → COUNTING + FORWARD loop (unbounded)
LC 322: unlimited coins → OPTIMIZE + FORWARD loop (unbounded)

🧠 INSTANT RECOGNITION:
  "how many ways"    → COUNTING (skip + take)
  "is it possible"   → BOOLEAN  (skip or take)
  "minimum/maximum"  → OPTIMIZE (min/max)
  "each element once" → 0/1 → BACKWARD
  "unlimited use"    → UNBOUNDED → FORWARD
"""


if __name__ == "__main__":
    test_all()