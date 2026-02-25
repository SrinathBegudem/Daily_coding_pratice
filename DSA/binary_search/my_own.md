# Binary Search Patterns — Amazon Interview Cheat Sheet

> **Core Insight:** Every binary search is the SAME skeleton. Only 3 things change:
> 1. **Range** → `[0, n]` vs `[0, n-1]`
> 2. **Condition** → what decides `l = mid+1` vs `r = mid`
> 3. **Loop style** → `l < r` (converge to answer) vs `l <= r` (find exact match)

---

## PATTERN 0: Classic Binary Search (Find Exact Match)

```python
def classic_binary_search(arr, target):
    """Find exact element. Returns index or -1."""
    l, r = 0, len(arr) - 1          # ← r = n-1 (valid index range)

    while l <= r:                    # ← KEY: <= (shrinks to nothing)
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid               # ← Found it! Return immediately
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1             # ← KEY: mid-1 (not mid)

    return -1                        # Not found
```

**Why different:** Only pattern that returns mid INSIDE the loop. All others converge l == r.

```
LEETCODE:
- LC 704: Binary Search
- LC 374: Guess Number Higher or Lower
- LC 33:  Search in Rotated Sorted Array ⭐⭐⭐
- LC 81:  Search in Rotated Sorted Array II
- LC 74:  Search a 2D Matrix
```

---

## PATTERN 1: Lower Bound (First ≥ target) — THE MASTER TEMPLATE

```python
def lower_bound(arr, target):
    """First position where arr[mid] >= target. Returns 0 to n."""
    l, r = 0, len(arr)              # ← r = n (can return past-end)

    while l < r:                    # ← KEY: < (converges l == r)
        mid = (l + r) // 2

        if arr[mid] < target:       # ← too small → go right
            l = mid + 1
        else:                       # ← arr[mid] >= target → possible answer
            r = mid

    return l                         # l == r == answer
```

**This is the base. Every pattern below is a TWEAK of this.**

```
LEETCODE:
- LC 35:  Search Insert Position (exact same problem!)
- LC 34:  Find First and Last Position (first part)
- LC 278: First Bad Version
- LC 2300: Successful Pairs of Spells and Potions
```

---

## PATTERN 2: Upper Bound (First > target)

```python
def upper_bound(arr, target):
    """First position where arr[mid] > target. Returns 0 to n."""
    l, r = 0, len(arr)              # ← same range as lower bound

    while l < r:
        mid = (l + r) // 2

        if arr[mid] <= target:      # ← KEY CHANGE: <= (not <)
            l = mid + 1
        else:
            r = mid

    return l
```

**Only difference from lower bound:** `<` becomes `<=` in the condition.

> **Tip:** `upper_bound - 1` = last occurrence of target.

```
LEETCODE:
- LC 34:  Find First and Last Position (second part: upper_bound - 1)
- LC 981: Time Based Key-Value Store ⭐⭐⭐
- LC 2389: Longest Subsequence With Limited Sum
```

---

## PATTERN 3: First True / Last False

```python
def first_true(n, condition):
    """First index where condition(mid) is True. Array: [F,F,F,T,T,T]"""
    l, r = 0, n                     # ← same range

    while l < r:
        mid = (l + r) // 2

        if not condition(mid):      # ← condition is False → go right
            l = mid + 1
        else:                       # ← condition is True → possible answer
            r = mid

    return l                         # first True position

def last_false(n, condition):
    """Last index where condition(mid) is False. = first_true - 1"""
    return first_true(n, condition) - 1
```

**Same as lower bound** but condition replaces `arr[mid] < target`.

> Lower bound IS first_true where condition = `arr[mid] >= target`.

```
LEETCODE:
- LC 278: First Bad Version (first True)
- LC 1539: Kth Missing Positive Number
- LC 162: Find Peak Element (variant)
```

---

## PATTERN 4: Peak / Mountain Array

```python
def peak_index(arr):
    """Find peak in mountain array (bitonic array)."""
    l, r = 0, len(arr) - 1          # ← r = n-1 (need mid+1 valid)

    while l < r:
        mid = (l + r) // 2

        if arr[mid] < arr[mid + 1]: # ← increasing → peak is right
            l = mid + 1
        else:                       # ← decreasing → peak is here or left
            r = mid

    return l                         # l == r == peak index
```

**Differences from lower bound:**
- `r = n-1` (because we access `mid+1`)
- Condition compares neighbors, not target

```
LEETCODE:
- LC 852: Peak Index in a Mountain Array
- LC 162: Find Peak Element ⭐⭐⭐
- LC 1095: Find in Mountain Array
```

---

## PATTERN 5: Search on Answer — Find MINIMUM ⭐⭐⭐

```python
def binary_search_min(lo, hi, is_feasible):
    """Find MINIMUM value where is_feasible(mid) == True.
    Search space: [F,F,F,T,T,T] → find first T
    """
    l, r = lo, hi                    # ← search space bounds

    while l < r:
        mid = (l + r) // 2

        if is_feasible(mid):         # ← feasible → try smaller
            r = mid
        else:                        # ← not feasible → need larger
            l = mid + 1

    return l
```

**Exactly first_true** but on an answer range instead of array indices!

```
LEETCODE:
- LC 875:  Koko Eating Bananas ⭐⭐⭐ (min speed)
- LC 1011: Capacity To Ship Packages ⭐⭐⭐ (min capacity)
- LC 410:  Split Array Largest Sum (min largest sum)
- LC 1283: Smallest Divisor Given Threshold
- LC 1482: Min Days to Make m Bouquets
- LC 2187: Min Time to Complete Trips
- LC 774:  Minimize Max Distance to Gas Station
```

---

## PATTERN 6: Search on Answer — Find MAXIMUM ⭐⭐⭐

### Option A: Flipped ceiling division (tricky but elegant)

```python
def binary_search_max_a(lo, hi, is_feasible):
    """Find MAXIMUM value where is_feasible(mid) == True.
    Search space: [T,T,T,F,F,F] → find last T
    """
    l, r = lo, hi

    while l < r:
        mid = (l + r + 1) // 2      # ← KEY: +1 (ceiling div avoids infinite loop!)

        if is_feasible(mid):         # ← feasible → try larger
            l = mid                  # ← KEY: l = mid (not mid+1)
        else:
            r = mid - 1             # ← KEY: r = mid-1

    return l
```

### Option B: Save-result style (easier to remember)

```python
def binary_search_max_b(lo, hi, is_feasible):
    """Same logic, different bookkeeping."""
    l, r = lo, hi
    result = lo                      # ← save best answer

    while l <= r:                   # ← KEY: <= (like classic)
        mid = (l + r) // 2

        if is_feasible(mid):
            result = mid             # ← save this answer
            l = mid + 1             # ← try larger
        else:
            r = mid - 1

    return result
```

**Why +1 in Option A:** When `l = mid`, if `mid = (l+r)//2` rounds down to `l`, you get infinite loop. Ceiling division fixes it.

```
LEETCODE:
- LC 1552: Magnetic Force Between Balls ⭐⭐⭐ (max min distance)
- LC 2226: Max Candies Allocated to K Children
- LC 1231: Divide Chocolate (max min sweetness)
- LC 1870: Min Speed to Arrive on Time (inverse → max)
- LC 2517: Max Tastiness of Candy Basket
```

---

## PATTERN 7: Rotated Sorted Array

```python
def search_rotated(arr, target):
    """Search in rotated sorted array (no duplicates)."""
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid

        if arr[l] <= arr[mid]:       # ← left half is sorted
            if arr[l] <= target < arr[mid]:
                r = mid - 1          # target in sorted left half
            else:
                l = mid + 1
        else:                        # ← right half is sorted
            if arr[mid] < target <= arr[r]:
                l = mid + 1          # target in sorted right half
            else:
                r = mid - 1

    return -1
```

**Key insight:** One half is ALWAYS sorted. Check if target is in sorted half.

```python
def find_min_rotated(arr):
    """Find minimum in rotated sorted array (LC 153)."""
    l, r = 0, len(arr) - 1

    while l < r:
        mid = (l + r) // 2

        if arr[mid] > arr[r]:        # ← min is in right half
            l = mid + 1
        else:                        # ← min is in left half (including mid)
            r = mid

    return arr[l]
```

```
LEETCODE:
- LC 33:  Search in Rotated Sorted Array ⭐⭐⭐
- LC 81:  Search in Rotated Sorted Array II (duplicates)
- LC 153: Find Minimum in Rotated Sorted Array ⭐⭐⭐
- LC 154: Find Minimum in Rotated Sorted Array II
```

---

## PATTERN 8: 2D Matrix Search

```python
def search_matrix(matrix, target):
    """Treat m×n matrix as sorted 1D array."""
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1             # ← flatten to 1D indices

    while l <= r:
        mid = (l + r) // 2
        val = matrix[mid // n][mid % n]  # ← KEY: convert 1D → 2D

        if val == target:
            return True
        elif val < target:
            l = mid + 1
        else:
            r = mid - 1

    return False
```

**Only trick:** `row = mid // cols`, `col = mid % cols`

```python
def search_matrix_ii(matrix, target):
    """240: Each row & col sorted (staircase search, NOT binary search)."""
    r, c = 0, len(matrix[0]) - 1    # start top-right corner

    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            r += 1                   # too small → go down
        else:
            c -= 1                   # too big → go left

    return False                     # O(m + n) time
```

```
LEETCODE:
- LC 74:  Search a 2D Matrix (sorted flatten → classic BS)
- LC 240: Search a 2D Matrix II (staircase, O(m+n))
```

---

## PATTERN 9: Binary Search on Floating Point

```python
def sqrt_float(x, eps=1e-6):
    """Find square root to precision eps."""
    l, r = 0, max(1, x)

    while r - l > eps:               # ← KEY: no integer convergence, use epsilon
        mid = (l + r) / 2           # ← real division (not //)

        if mid * mid < x:
            l = mid                  # ← no +1 (continuous space)
        else:
            r = mid                  # ← no -1

    return l

# Alternative: fixed iterations (simpler, always works)
def sqrt_float_v2(x):
    l, r = 0, max(1, x)
    for _ in range(100):             # 100 iterations ≈ 10^-30 precision
        mid = (l + r) / 2
        if mid * mid < x:
            l = mid
        else:
            r = mid
    return l
```

**Difference:** No `+1/-1`, use epsilon or fixed iterations.

```
LEETCODE:
- LC 69:   Sqrt(x) (integer version)
- LC 367:  Valid Perfect Square
```

---

## QUICK REFERENCE TABLE

| Pattern | Range | Loop | Condition | Move |
|---------|-------|------|-----------|------|
| **Classic** | `[0, n-1]` | `l <= r` | `== target` | return mid |
| **Lower Bound** | `[0, n]` | `l < r` | `arr[mid] < target` | `l=mid+1` else `r=mid` |
| **Upper Bound** | `[0, n]` | `l < r` | `arr[mid] <= target` | `l=mid+1` else `r=mid` |
| **First True** | `[0, n]` | `l < r` | `!condition(mid)` | `l=mid+1` else `r=mid` |
| **Peak** | `[0, n-1]` | `l < r` | `arr[mid] < arr[mid+1]` | `l=mid+1` else `r=mid` |
| **Min Answer** | `[lo, hi]` | `l < r` | `!feasible(mid)` | `l=mid+1` else `r=mid` |
| **Max Answer** | `[lo, hi]` | `l < r` | `feasible(mid)` | `l=mid` else `r=mid-1` ⚠️ use `(l+r+1)//2` |
| **Rotated** | `[0, n-1]` | `l <= r` | sorted half logic | `mid±1` |
| **2D Matrix** | `[0, m*n-1]` | `l <= r` | `matrix[mid//n][mid%n]` | classic style |
| **Float** | `[lo, hi]` | `r-l > eps` | continuous condition | `l=mid` or `r=mid` |

---

## DECISION FLOWCHART

```
Q: Do I need an EXACT match?
├── YES → Pattern 0 (Classic): l <= r, return mid inside loop
└── NO → "Find a boundary"
    │
    Q: Am I searching an ARRAY or an ANSWER SPACE?
    ├── ARRAY
    │   Q: What boundary?
    │   ├── First >= target → Pattern 1 (Lower Bound)
    │   ├── First >  target → Pattern 2 (Upper Bound: change < to <=)
    │   ├── First True condition → Pattern 3 (First True)
    │   ├── Peak element → Pattern 4 (compare neighbors)
    │   └── Rotated → Pattern 7 (check which half is sorted)
    │
    └── ANSWER SPACE (min/max optimization)
        Q: Minimize or Maximize?
        ├── MINIMIZE → Pattern 5 (= First True on answer space)
        └── MAXIMIZE → Pattern 6 (use ceiling div OR save result)
```

---

## AMAZON FAVORITES (High Frequency)

```
TIER 1 (Very Likely):
- LC 33:   Search in Rotated Sorted Array
- LC 34:   Find First and Last Position
- LC 153:  Find Min in Rotated Array
- LC 875:  Koko Eating Bananas
- LC 1011: Capacity to Ship Packages
- LC 162:  Find Peak Element

TIER 2 (Likely):
- LC 74:   Search a 2D Matrix
- LC 240:  Search a 2D Matrix II
- LC 410:  Split Array Largest Sum
- LC 1552: Magnetic Force Between Balls
- LC 981:  Time Based Key-Value Store
- LC 278:  First Bad Version

TIER 3 (Possible):
- LC 4:    Median of Two Sorted Arrays (hard, unique pattern)
- LC 1283: Smallest Divisor Given Threshold
- LC 852:  Peak Index in Mountain Array
- LC 2187: Min Time to Complete Trips
```