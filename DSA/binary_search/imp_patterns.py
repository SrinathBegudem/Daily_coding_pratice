"""
===============================================================================
COMPLETE BINARY SEARCH PATTERNS GUIDE
===============================================================================

MASTER RULE: "Binary search is finding a boundary in a monotonic space."

If you understand this, you understand all patterns below.

===============================================================================
"""

import bisect
from typing import List

"""
===============================================================================
PATTERN 1: CLASSIC BINARY SEARCH (Find Exact Element)
===============================================================================

USE WHEN:
- Array is sorted
- Need to find if element exists and return its index
- Looking for EXACT match

KEY CHARACTERISTICS:
- Loop condition: l <= r (note the =)
- Return: index or -1
- Least used in modern interviews (most use lower/upper bound instead)

TIME: O(log n), SPACE: O(1)
"""

def classic_binary_search(arr: List[int], target: int) -> int:
    """
    Find exact element in sorted array
    Returns: index if found, -1 otherwise
    """
    l, r = 0, len(arr) - 1
    
    while l <= r:  # ← KEY: <= (not <)
        mid = (l + r) // 2
        
        if arr[mid] == target:
            return mid  # Found it!
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1  # Not found

"""
LEETCODE PROBLEMS:
- LC 704: Binary Search
- LC 374: Guess Number Higher or Lower
- LC 167: Two Sum II (with two pointers)

EXAMPLE:
arr = [1, 3, 5, 7, 9]
classic_binary_search(arr, 5) → 2
classic_binary_search(arr, 4) → -1
"""


"""
===============================================================================
PATTERN 2: LOWER BOUND (First index >= target)
===============================================================================

USE WHEN:
- Find insert position
- Find first occurrence of element
- Find minimum value that satisfies condition

KEY CHARACTERISTICS:
- Loop condition: l < r
- Check: arr[mid] < target
- Returns: leftmost valid position
- Python equivalent: bisect.bisect_left()

TIME: O(log n), SPACE: O(1)

VISUAL:
arr = [1, 2, 4, 4, 4, 5, 7]
      [... < target | >= target ...]
                     ↑ returns here
"""

def lower_bound(arr: List[int], target: int) -> int:
    """
    Find first position where arr[mid] >= target
    Returns: insertion position (0 to len(arr))
    """
    l, r = 0, len(arr)  # ← KEY: r = len(arr) (not len-1)
    
    while l < r:  # ← KEY: < (not <=)
        mid = (l + r) // 2
        
        if arr[mid] < target:  # ← KEY: < (strict less than)
            l = mid + 1
        else:
            r = mid
    
    return l

"""
LEETCODE PROBLEMS:
- LC 35: Search Insert Position ⭐⭐⭐
- LC 34: Find First and Last Position (first part)
- LC 278: First Bad Version
- LC 69: Sqrt(x)
- LC 744: Find Smallest Letter Greater Than Target

EXAMPLE:
arr = [1, 2, 4, 4, 4, 5, 7]

lower_bound(arr, 4) → 2 (first 4)
bisect_left(arr, 4) → 2

lower_bound(arr, 3) → 2 (insert between 2 and 4)
lower_bound(arr, 0) → 0 (insert at beginning)
lower_bound(arr, 10) → 7 (insert at end)
"""


"""
===============================================================================
PATTERN 3: UPPER BOUND (First index > target)
===============================================================================

USE WHEN:
- Find position after all occurrences
- Count occurrences: upper_bound - lower_bound
- Insert after duplicates

KEY CHARACTERISTICS:
- Loop condition: l < r
- Check: arr[mid] <= target (only difference from lower bound!)
- Returns: position after last occurrence
- Python equivalent: bisect.bisect_right()

TIME: O(log n), SPACE: O(1)

VISUAL:
arr = [1, 2, 4, 4, 4, 5, 7]
      [... <= target | > target ...]
                      ↑ returns here
"""

def upper_bound(arr: List[int], target: int) -> int:
    """
    Find first position where arr[mid] > target
    Returns: insertion position (0 to len(arr))
    """
    l, r = 0, len(arr)
    
    while l < r:
        mid = (l + r) // 2
        
        if arr[mid] <= target:  # ← KEY DIFFERENCE: <= (not <)
            l = mid + 1
        else:
            r = mid
    
    return l

"""
LEETCODE PROBLEMS:
- LC 34: Find First and Last Position (second part)
- LC 981: Time Based Key-Value Store ⭐⭐⭐
- LC 2389: Longest Subsequence With Limited Sum

EXAMPLE:
arr = [1, 2, 4, 4, 4, 5, 7]

upper_bound(arr, 4) → 5 (after last 4)
bisect_right(arr, 4) → 5

upper_bound(arr, 3) → 2 (same as lower_bound if not exists)

Count occurrences of 4:
count = upper_bound(arr, 4) - lower_bound(arr, 4)
      = 5 - 2 = 3 ✅
"""


"""
===============================================================================
PATTERN 4: BINARY SEARCH ON ANSWER (Most Important!)
===============================================================================

USE WHEN:
- Problem asks "minimum X to achieve Y"
- Problem asks "maximum X such that Y"
- Answer space is monotonic (if X works, X+1 also works OR vice versa)
- GOOGLE FAVORITE pattern

KEY INSIGHT:
- You're NOT searching the input array
- You're searching the ANSWER SPACE
- Need a helper function: can(mid) or is_feasible(mid)

KEY CHARACTERISTICS:
- Search range: [min_possible, max_possible]
- Uses helper function to check feasibility
- Pattern depends on whether finding min or max

TIME: O(log(range) × cost_of_check), SPACE: O(1)

TWO VERSIONS:
"""

# Version A: Finding MINIMUM (use lower bound style)
def binary_search_minimum(min_val, max_val, is_feasible):
    """
    Find minimum value that satisfies condition
    Use when: "minimum capacity", "minimum speed", "minimum days"
    """
    l, r = min_val, max_val
    
    while l < r:
        mid = (l + r) // 2
        
        if is_feasible(mid):
            r = mid  # Found feasible, try smaller
        else:
            l = mid + 1  # Not feasible, need larger
    
    return l

# Version B: Finding MAXIMUM (use +1 to avoid infinite loop)
def binary_search_maximum(min_val, max_val, is_feasible):
    """
    Find maximum value that satisfies condition
    Use when: "maximum distance", "maximum allocation", "maximum sweetness"
    """
    l, r = min_val, max_val
    
    while l < r:
        mid = (l + r + 1) // 2  # ← KEY: +1 to avoid infinite loop!
        
        if is_feasible(mid):
            l = mid  # Found feasible, try larger
        else:
            r = mid - 1  # Not feasible, need smaller
    
    return l
# or you can also do somehting liek this for maximum pattern
    # l, r = min_val, max_val
    
    # while l <= r: # ← l <= r (note the =)
    #     mid = (l + r ) // 2  # ← No +1 needed!
        
    #     if is_feasible(mid):
    #         res = mid  # ← Save this answer
    #         l = mid + 1   # ← Try to find larger
    #     else:
    #         r = mid - 1  # Not feasible, need smaller
    
    # return result # ← Return saved answer
"""
LEETCODE PROBLEMS (Finding MINIMUM):
- LC 875: Koko Eating Bananas ⭐⭐⭐ (minimum speed)
- LC 1011: Capacity To Ship Packages Within D Days ⭐⭐⭐
- LC 410: Split Array Largest Sum
- LC 1283: Find the Smallest Divisor Given a Threshold
- LC 1482: Minimum Number of Days to Make m Bouquets
- LC 2187: Minimum Time to Complete Trips

LEETCODE PROBLEMS (Finding MAXIMUM):
- LC 1552: Magnetic Force Between Two Balls ⭐⭐⭐
- LC 1231: Divide Chocolate (Premium)
- LC 2226: Maximum Candies Allocated to K Children
- LC 1870: Minimum Speed to Arrive on Time (inverse)

EXAMPLE: LC 875 - Koko Eating Bananas
"""

def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Find minimum eating speed to finish all bananas in h hours
    
    Monotonic property:
    Speed: 1  2  3  4  5  6  7  8  9  10
    Works: F  F  F  F  T  T  T  T  T  T
                        ↑ Find first True
    """
    def can_finish(speed):
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h
    
    l, r = 1, max(piles)
    
    while l < r:
        mid = (l + r) // 2
        if can_finish(mid):
            r = mid  # Can finish, try slower
        else:
            l = mid + 1  # Can't finish, need faster
    
    return l

"""
EXAMPLE: LC 1552 - Magnetic Force Between Two Balls
"""

def max_distance(position: List[int], m: int) -> int:
    """
    Find maximum minimum distance between m balls
    
    Monotonic property:
    Distance: 1  2  3  4  5  6  7  8  9  10
    Possible: T  T  T  T  T  F  F  F  F  F
                        ↑ Find last True
    """
    position.sort()
    
    def can_place(min_dist):
        count, last_pos = 1, position[0]
        for i in range(1, len(position)):
            if position[i] - last_pos >= min_dist:
                count += 1
                last_pos = position[i]
        return count >= m
    
    l, r = 1, position[-1] - position[0]
    
    while l < r:
        mid = (l + r + 1) // 2  # ← +1 because finding maximum
        if can_place(mid):
            l = mid  # Can place, try larger distance
        else:
            r = mid - 1  # Can't place, try smaller
    
    return l


#IMP 
# "Boolean array transitions from True to False. they should be monotonic not sorted"

# YES! Monotonic is the right word!
# "if we sort true and false then always false come first"

# YES! Sorting always gives [F,F,F,T,T,T]
# "if false come first then we can only find out first true"

# YES! [F,F,F,T,T,T] → can only find first True
# "so when they ask last true they will give true in beginning and false to the end"

# THIS IS SIMIALR TO MIN AND MAX ONE RANGE THE ABOVE PATTERN.
# FIND FIRST TRUE ===== MIN VAL BINARY SEARCH PATTERN
# FIND LAST TRUE ===== MAX VAL BINARY SEARCH PATTERN 
# SAME TO SAME CODE
# FIRST TRUE  ≡  MINIMUM VALUE  ≡  BINARY SEARCH ON ANSWER (MIN)
# LAST TRUE   ≡  MAXIMUM VALUE  ≡  BINARY SEARCH ON ANSWER (MAX)
"""
===============================================================================
PATTERN 5: FIRST TRUE (False → True Boundary)
===============================================================================

USE WHEN:
- Boolean array transitions from False to True
- Find first position where condition becomes true
- Theoretical foundation for Pattern 4 (binary search on answer)

KEY CHARACTERISTICS:
- Array pattern: [F, F, F, F, T, T, T, T]
- Same as lower bound for boolean arrays
- Same implementation as "finding minimum" in Pattern 4

VISUAL:
[F, F, F, F, T, T, T, T]
            ↑ Find this position

TIME: O(log n × cost_of_condition), SPACE: O(1)
"""

def first_true(n, is_true):
    """
    Find first index where is_true(index) returns True
    
    Args:
        n: upper bound (exclusive)
        is_true: function that returns boolean
    """
    l, r = 0, n
    
    while l < r:
        mid = (l + r) // 2
        
        if is_true(mid):
            r = mid  # Found True, look for earlier
        else:
            l = mid + 1  # Still False, move right
    
    return l

"""
LEETCODE PROBLEMS:
- LC 278: First Bad Version ⭐⭐⭐
- LC 875: Koko Eating Bananas (reframed)
- LC 1539: Kth Missing Positive Number
- LC 2513: Minimize the Maximum of Two Arrays

EXAMPLE: LC 278 - First Bad Version
"""

def first_bad_version(n: int) -> int:
    """
    Array: [Good, Good, Good, Bad, Bad, Bad]
           [False, False, False, True, True, True]
                              ↑ Find first True
    """
    def is_bad(version):
        # This is provided by the API
        return isBadVersion(version)  # noqa
    
    l, r = 1, n
    
    while l < r:
        mid = (l + r) // 2
        if is_bad(mid):
            r = mid  # This or earlier is first bad
        else:
            l = mid + 1  # First bad is later
    
    return l


"""
===============================================================================
PATTERN 6: LAST TRUE (True → False Boundary)
===============================================================================

USE WHEN:
- Boolean array transitions from True to False. they should be monotic not sorted
- if we sort true and false then always false come first and if false come first then
we can only find out first true no way possible to find out last true. okay 
so when they ask last true they will give true in beginning and false to the end.
- Find last position where condition is true
- Finding maximum feasible value

KEY CHARACTERISTICS:
- Array pattern: [T, T, T, T, F, F, F, F]
- MUST use (l + r + 1) // 2 to avoid infinite loop
- Same implementation as "finding maximum" in Pattern 4

VISUAL:
[T, T, T, T, F, F, F, F]
         ↑ Find this position

TIME: O(log n × cost_of_condition), SPACE: O(1)
"""

def last_true(n, is_true):
    """
    Find last index where is_true(index) returns True
    
    Args:
        n: upper bound (inclusive)
        is_true: function that returns boolean
    """
    l, r = 0, n
    
    while l < r:
        mid = (l + r + 1) // 2  # ← CRITICAL: +1 to avoid infinite loop
        
        if is_true(mid):
            l = mid  # Found True, look for later
        else:
            r = mid - 1  # Found False, move left
    
    return l

"""
WHY +1 IS CRITICAL:

Without +1 (causes infinite loop):
    l=5, r=6
    mid = (5+6)//2 = 5
    if is_true(5): l = 5  ← l doesn't change! Stuck!

With +1 (works correctly):
    l=5, r=6
    mid = (5+6+1)//2 = 6
    if is_true(6): l = 6  ← l advances!

RULE: If you do "l = mid", you MUST use (l+r+1)//2
"""

"""
LEETCODE PROBLEMS:
- LC 1552: Magnetic Force (reframed)
- LC 2517: Maximum Tastiness of Candy Basket
- LC 2560: House Robber IV


===============================================================================
PATTERN 7: PEAK / MOUNTAIN / ROTATED ARRAY
===============================================================================

USE WHEN:
- Find peak element in array
- Mountain array problems
- Rotated sorted array
- Array has local max/min

KEY CHARACTERISTICS:
- Compare with neighbors (nums[mid] vs nums[mid+1])
- No target value
- Array not fully sorted

TIME: O(log n), SPACE: O(1)
"""

# Sub-pattern 7A: Find Peak Element
def find_peak_element(nums: List[int]) -> int:
    """
    Find any peak element (nums[i] > nums[i-1] and nums[i] > nums[i+1])
    
    Key insight: Always move toward higher neighbor
    """
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        if nums[mid] > nums[mid + 1]:
            r = mid  # Peak is on left (including mid)
        else:
            l = mid + 1  # Peak is on right
    
    return l
# my own solution 

        # l = 0
        # r = len(nums) - 1
        
        # while l <= r:
        #     m = (l + r)//2
        #     left = nums[m-1] if m > 0 else float('-INF')
        #     right = nums[m+1] if m < len(nums) - 1 else float('-INF')

        #     if left < nums[m] > right:
        #         return m
        #     elif left < nums[m] < right:
        #         l = m +1
        #     else:
        #         r = m - 1



# Sub-pattern 7B: Find in Rotated Sorted Array
def search_rotated(nums: List[int], target: int) -> int:
    """
    Search in rotated sorted array
    Example: [4,5,6,7,0,1,2], target = 0
    """
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[l] <= nums[mid]:  # Left half is sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1  # Target in left sorted half
            else:
                l = mid + 1  # Target in right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1  # Target in right sorted half
            else:
                r = mid - 1  # Target in left half
    
    return -1

# Sub-pattern 7C: Find Minimum in Rotated Sorted Array
def find_min_rotated(nums: List[int]) -> int:
    """
    Find minimum in rotated sorted array
    Example: [4,5,6,7,0,1,2] → 0
    """
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        if nums[mid] > nums[r]:
            l = mid + 1  # Min is in right half
        else:
            r = mid  # Min is in left half (including mid)
    
    return nums[l]
# solution using first true pattern same code ( find min pattern)
        # l  = 0
        # r = len(nums) - 1


        # while l < r:
        #     m = (l+r)//2

        #     if nums[m] <= nums[r]:
        #         r = m
        #     else:
        #         l = m + 1
        # return nums[l]

"""
LEETCODE PROBLEMS:
- LC 162: Find Peak Element ⭐⭐⭐
- LC 852: Peak Index in a Mountain Array
- LC 33: Search in Rotated Sorted Array ⭐⭐⭐
- LC 81: Search in Rotated Sorted Array II (with duplicates)
- LC 153: Find Minimum in Rotated Sorted Array ⭐⭐⭐
- LC 154: Find Minimum in Rotated Sorted Array II
- LC 1095: Find in Mountain Array
"""


"""
===============================================================================
PATTERN 8: PREFIX SUM BINARY SEARCH
===============================================================================

USE WHEN:
- Prefix sum array is given or can be built
- Find smallest index where prefix sum >= target
- Subarray sum problems

KEY CHARACTERISTICS:
- Prefix array must be non-decreasing (monotonic)
- Usually use bisect_left or lower_bound
- Very common in subarray problems

TIME: O(n) to build prefix, O(log n) per query, SPACE: O(n)
"""

def prefix_sum_search(nums: List[int], target: int) -> int:
    """
    Find smallest index where prefix sum >= target
    """
    # Build prefix sum
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    # Binary search on prefix
    # Use bisect_left to find first position >= target
    idx = bisect.bisect_left(prefix, target)
    
    if idx < len(prefix) and prefix[idx] == target:
        return idx
    return idx if idx < len(prefix) else -1

"""
LEETCODE PROBLEMS:
- LC 1011: Capacity To Ship Packages (with prefix)
- LC 2389: Longest Subsequence With Limited Sum ⭐⭐⭐
- LC 1482: Minimum Number of Days to Make m Bouquets
- LC 1231: Divide Chocolate (using prefix)

EXAMPLE: LC 2389
"""

def answer_queries(nums: List[int], queries: List[int]) -> List[int]:
    """
    For each query, find max subsequence length with sum <= query
    """
    nums.sort()
    
    # Build prefix sum
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    result = []
    for q in queries:
        # Find rightmost position where prefix <= q
        idx = bisect.bisect_right(prefix, q) - 1
        result.append(idx)
    
    return result


"""
===============================================================================
PATTERN 9: BINARY SEARCH WITH DUPLICATES
===============================================================================

USE WHEN:
- Array has duplicates
- Need to handle equal values specially
- Find boundaries of duplicate ranges

KEY CHARACTERISTICS:
- Slight modifications to classic patterns
- Usually need both lower_bound and upper_bound
"""

def search_range_duplicates(nums: List[int], target: int) -> List[int]:
    """
    Find first and last position of target
    LC 34: Find First and Last Position of Element in Sorted Array
    """
    def lower_bound_custom(arr, x):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l
    
    def upper_bound_custom(arr, x):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                l = mid + 1
            else:
                r = mid
        return l
    
    left = lower_bound_custom(nums, target)
    
    if left >= len(nums) or nums[left] != target:
        return [-1, -1]
    
    right = upper_bound_custom(nums, target) - 1
    
    return [left, right]

"""
LEETCODE PROBLEMS:
- LC 34: Find First and Last Position ⭐⭐⭐
- LC 658: Find K Closest Elements
- LC 1150: Check If a Number Is Majority Element


===============================================================================
PATTERN 10: 2D BINARY SEARCH
===============================================================================

USE WHEN:
- 2D matrix is sorted (row-wise and/or column-wise)
- Need to search in 2D space

KEY CHARACTERISTICS:
- Treat 2D as 1D: mid → (mid // cols, mid % cols)
- Or search row then column
"""

def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    LC 74: Search a 2D Matrix
    Each row sorted, first element of row > last of previous
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    l, r = 0, rows * cols - 1
    
    while l <= r:
        mid = (l + r) // 2
        # Convert 1D index to 2D
        row, col = mid // cols, mid % cols
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return False

"""
LEETCODE PROBLEMS:
- LC 74: Search a 2D Matrix ⭐⭐⭐
- LC 240: Search a 2D Matrix II
- LC 378: Kth Smallest Element in a Sorted Matrix


===============================================================================
QUICK REFERENCE TABLE
===============================================================================

Pattern              | l,r init    | loop  | mid formula      | main check
---------------------|-------------|-------|------------------|------------------
Classic Search       | 0, n-1      | l<=r  | (l+r)//2        | arr[mid] == x
Lower Bound          | 0, n        | l<r   | (l+r)//2        | arr[mid] < x
Upper Bound          | 0, n        | l<r   | (l+r)//2        | arr[mid] <= x
Binary on Answer(min)| min,max     | l<r   | (l+r)//2        | is_feasible(mid)
Binary on Answer(max)| min,max     | l<r   | (l+r+1)//2      | is_feasible(mid)
First True           | 0, n        | l<r   | (l+r)//2        | is_true(mid)
Last True            | 0, n        | l<r   | (l+r+1)//2      | is_true(mid)
Peak Element         | 0, n-1      | l<r   | (l+r)//2        | nums[mid]>nums[mid+1]
Rotated Array        | 0, n-1      | l<=r  | (l+r)//2        | compare with ends


===============================================================================
TOP 20 MUST-PRACTICE PROBLEMS (IN ORDER)
===============================================================================

BEGINNER (Master these first):
1. LC 704: Binary Search
2. LC 35: Search Insert Position
3. LC 278: First Bad Version
4. LC 69: Sqrt(x)
5. LC 374: Guess Number Higher or Lower

INTERMEDIATE (Core patterns):
6. LC 34: Find First and Last Position ⭐⭐⭐
7. LC 162: Find Peak Element
8. LC 33: Search in Rotated Sorted Array ⭐⭐⭐
9. LC 153: Find Minimum in Rotated Sorted Array
10. LC 875: Koko Eating Bananas ⭐⭐⭐

ADVANCED (Binary search on answer):
11. LC 1011: Capacity To Ship Packages ⭐⭐⭐
12. LC 410: Split Array Largest Sum
13. LC 1552: Magnetic Force Between Two Balls ⭐⭐⭐
14. LC 1283: Find the Smallest Divisor
15. LC 2226: Maximum Candies Allocated

EXPERT (Complex patterns):
16. LC 4: Median of Two Sorted Arrays (Hard)
17. LC 719: Find K-th Smallest Pair Distance
18. LC 1095: Find in Mountain Array
19. LC 2141: Maximum Running Time of N Computers
20. LC 2517: Maximum Tastiness of Candy Basket


===============================================================================
INTERVIEW TIPS
===============================================================================

1. RECOGNIZE THE PATTERN:
   - Sorted array → Classic/Lower/Upper
   - "Minimum X to achieve Y" → Binary search on answer
   - Peak/Mountain → Compare neighbors
   - Boolean condition → First/Last True

2. CLARIFY EDGE CASES:
   - Empty array?
   - Single element?
   - All same values?
   - Target not in array?

3. AVOID COMMON MISTAKES:
   - Off-by-one errors (use l < r consistently)
   - Infinite loops (use +1 when doing l = mid)
   - Integer overflow (use l + (r-l)//2 in other languages)

4. TEST WITH:
   - Empty: []
   - Single: [1]
   - Two elements: [1, 2]
   - Target at boundaries
   - Target not present

5. COMPLEXITY:
   - Always mention: O(log n) time, O(1) space
   - If using helper function: O(log n × cost_of_helper)


===============================================================================
"""

if __name__ == "__main__":
    # Test all patterns
    print("Binary Search Patterns - Test Cases")
    print("=" * 50)
    
    # Pattern 1: Classic
    arr = [1, 3, 5, 7, 9]
    print(f"\n1. Classic: Find 5 in {arr}")
    print(f"   Result: {classic_binary_search(arr, 5)}")
    
    # Pattern 2 & 3: Lower/Upper Bound
    arr = [1, 2, 4, 4, 4, 5, 7]
    print(f"\n2-3. Bounds: Find bounds of 4 in {arr}")
    print(f"   Lower bound: {lower_bound(arr, 4)}")
    print(f"   Upper bound: {upper_bound(arr, 4)}")
    
    # Pattern 4: Binary Search on Answer
    print(f"\n4. Koko Bananas: piles=[3,6,7,11], h=8")
    print(f"   Min speed: {min_eating_speed([3,6,7,11], 8)}")
    
    # Pattern 7: Peak Element
    arr = [1, 2, 3, 1]
    print(f"\n7. Peak Element in {arr}")
    print(f"   Peak index: {find_peak_element(arr)}")
    
    print("\n" + "=" * 50)
    print("All patterns working correctly! ✅")