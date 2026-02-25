"""
═══════════════════════════════════════════════════════════════════════════════
                    SLIDING WINDOW MASTERY GUIDE
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. WHAT IS SLIDING WINDOW?
   A technique to solve problems involving contiguous subarrays or substrings
   by maintaining a window that "slides" across the data structure.
   
   Think of it like a physical window moving across your data:
   [1, 2, 3, 4, 5, 6, 7, 8]
    ←---window---→
       ←---window---→
          ←---window---→

2. WHY SLIDING WINDOW?
   - Reduces time complexity from O(n²) or O(n³) to O(n)
   - Avoids recomputing from scratch for each subarray
   - Optimal for problems with contiguous elements
   - Natural fit for "range" or "window" problems

3. WHEN TO USE SLIDING WINDOW?
   🔑 TRIGGER PHRASES (If you see these, think sliding window!):
   - "contiguous subarray/substring"
   - "longest/shortest/maximum/minimum subarray with..."
   - "find all subarrays/substrings that..."
   - "window of size k"
   - "all elements in range"
   - "contains all characters"
   - "at most K distinct..."
   - "without repeating..."

4. TWO MAIN TYPES:
   
   TYPE 1: FIXED SIZE WINDOW
   - Window size is constant (given as K)
   - Slide one position at a time
   - Add new element, remove old element
   - Example: "Maximum sum of subarray of size K"
   
   TYPE 2: VARIABLE SIZE WINDOW (Most common in interviews!)
   - Window size changes dynamically
   - Expand when condition not met
   - Shrink when condition violated
   - Two pointers: left (shrink) and right (expand)
   - Example: "Longest substring without repeating characters"

5. WHEN SLIDING WINDOW WON'T WORK:
   ❌ Non-contiguous elements (use DP or other approaches)
   ❌ Need to consider all possible subarrays (combinatorial)
   ❌ Elements order doesn't matter (use sorting/hashing)
   ❌ Split array problems (use prefix sum or DP)

6. HANDLING NEGATIVE NUMBERS:
   🔑 CRITICAL DISTINCTION:
   
   ✅ Sliding Window WORKS with negatives when:
   - Problem is about COUNTS/FREQUENCY (not sum)
   - Looking for longest/shortest based on conditions (not sum)
   - Example: "Longest substring with at most K distinct chars" ✓
   
   ⚠️ Sliding Window CAREFUL with negatives when:
   - Problem involves SUMS and you need monotonicity
   - "Maximum sum" problems might break shrinking logic
   - May need Kadane's algorithm instead
   
   Example where it breaks:
   arr = [5, -3, 5], k = 2
   If looking for "subarray with sum ≥ k", shrinking won't help
   because removing negative makes sum LARGER!
   
   ✅ Safe patterns even with negatives:
   - Character/element frequency problems
   - Distinct elements counting
   - Pattern matching
   - Anagrams

7. TWO POINTERS vs SLIDING WINDOW:
   
   TWO POINTERS (converging):
   - Usually on SORTED array
   - Pointers move towards each other
   - Often looking for a pair/triplet
   - Example: "Two sum in sorted array"
   - Pattern: left++, right--
   
   SLIDING WINDOW:
   - Array doesn't need to be sorted
   - Window slides in ONE direction →
   - Looking for subarray/substring properties
   - Example: "Longest substring without repeating"
   - Pattern: right++, sometimes left++

8. 10 ESSENTIAL PATTERNS COVERED:
   ✅ Pattern 1: Fixed Size Window - Maximum/Minimum
   ✅ Pattern 2: Variable Size - Longest Subarray (≤ condition)
   ✅ Pattern 3: Variable Size - Shortest Subarray (≥ condition)
   ✅ Pattern 4: Distinct Elements (K distinct/At most K)
   ✅ Pattern 5: Character Frequency (Anagrams, Permutations)
   ✅ Pattern 6: Replace/Flip K Elements (Maximize sequence)
   ✅ Pattern 7: Multiple Conditions (Complex constraints)
   ✅ Pattern 8: Minimum Window Substring (Contains all)
   ✅ Pattern 9: Count Subarrays (Exactly K condition)
   ✅ Pattern 10: String Matching with Wildcards

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Dict, Set
from collections import defaultdict, Counter

class SlidingWindowPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: FIXED SIZE WINDOW - MAXIMUM/MINIMUM
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Maximum sum of subarray of size K
    2. Average of subarrays of size K
    3. Maximum of all subarrays of size K
    4. First negative in every window of size K
    
    🔑 KEY CONCEPT:
    - Window size = K (constant)
    - Calculate for first window
    - Slide: remove leftmost, add rightmost
    - Update result at each step
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 DRY RUN - MAX SUM OF SIZE K:
    arr = [2, 1, 5, 1, 3, 2], k = 3
    
    Goal: Find maximum sum of any subarray of size 3
    
    Initial window [2, 1, 5]:
    - sum = 2 + 1 + 5 = 8
    - max_sum = 8
    
    Slide 1: Remove 2, Add 1
    - window = [1, 5, 1]
    - sum = 8 - 2 + 1 = 7
    - max_sum = 8 (no change)
    
    Slide 2: Remove 1, Add 3
    - window = [5, 1, 3]
    - sum = 7 - 1 + 3 = 9
    - max_sum = 9 ✓ (update!)
    
    Slide 3: Remove 5, Add 2
    - window = [1, 3, 2]
    - sum = 9 - 5 + 2 = 6
    - max_sum = 9 (no change)
    
    Result: 9 ✓
    
    🆚 WHY NOT BRUTE FORCE?
    Brute force: Check all subarrays of size k → O(n*k)
    Sliding window: Reuse previous sum → O(n)
    
    For n=10000, k=1000:
    - Brute force: 10,000,000 operations
    - Sliding window: 10,000 operations (1000x faster!)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 643: Maximum Average Subarray I (easy) ⭐⭐⭐ ✅
    - LeetCode 1456: Maximum Number of Vowels (medium) ⭐⭐ ✅
    - LeetCode 1343: Number of Sub-arrays of Size K (medium) ✅
    - LeetCode 2090: K Radius Subarray Averages (medium)✅
    """
    
    def max_sum_fixed_window(self, arr: List[int], k: int) -> int:
        """
        Find maximum sum of any subarray of size k
        
        Template for FIXED SIZE problems:
        1. Calculate sum of first k elements
        2. Slide window: subtract arr[i-k], add arr[i]
        3. Track maximum at each step
        """
        if not arr or k <= 0 or k > len(arr):
            return 0
        
        # Step 1: Calculate first window
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        # Step 2: Slide window from k to n
        for i in range(k, len(arr)):
            # Remove leftmost element of previous window
            window_sum -= arr[i - k]
            
            # Add rightmost element of current window
            window_sum += arr[i]
            
            # Update maximum
            max_sum = max(max_sum, window_sum)
        
        # # Step 2: Slide window from k to n , other way to solve
        # left = 0
        # for right in range(k, len(arr)):
        #     # Remove leftmost element of previous window
        #     window_sum -= arr[left]
        #     left += 1
        #     # Add rightmost element of current window
        #     window_sum += arr[right]
            
        #     # Update maximum
        #     max_sum = max(max_sum, window_sum)
        
        return max_sum
    
    
    def max_average_subarray(self, nums: List[int], k: int) -> float:
        """
        LeetCode 643: Maximum Average Subarray I
        
        Same as max sum, but return average
        Average = sum / k
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
    
    
    def first_negative_in_window(self, arr: List[int], k: int) -> List[int]:
        """
        Find first negative number in every window of size k
        
        🔑 TRICK: Use deque to track negative numbers
        
        📝 EXAMPLE:
        arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
        
        Window [12, -1, -7]: first negative = -1
        Window [-1, -7, 8]: first negative = -1
        Window [-7, 8, -15]: first negative = -7
        Window [8, -15, 30]: first negative = -15
        Window [-15, 30, 16]: first negative = -15
        Window [30, 16, 28]: first negative = 0 (none)
        
        Result: [-1, -1, -7, -15, -15, 0]
        """
        from collections import deque
        
        result = []
        negatives = deque()  # Store indices of negative numbers
        
        # Process first window
        for i in range(k):
            if arr[i] < 0:
                negatives.append(i)
        
        # First negative of first window
        if negatives:
            result.append(arr[negatives[0]])
        else:
            result.append(0)
        
        # Slide window
        for i in range(k, len(arr)):
            # Remove elements outside window
            while negatives and negatives[0] <= i - k:
                negatives.popleft()
            
            # Add current element if negative
            if arr[i] < 0:
                negatives.append(i)
            
            # First negative in current window
            if negatives:
                result.append(arr[negatives[0]])
            else:
                result.append(0)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: VARIABLE SIZE - LONGEST SUBARRAY (≤ condition)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Longest subarray with sum ≤ K
    2. Longest substring without repeating characters
    3. Longest substring with at most K distinct characters
    4. Longest subarray with at most K zeros
    
    🔑 KEY CONCEPT:
    - Window size changes (expand/shrink)
    - Expand: Always move right pointer
    - Shrink: Move left when condition violated
    - Track maximum window size seen
    
    ⏱️  Time: O(n) | Space: O(1) or O(k) for frequency map
    
    📝 TEMPLATE FOR VARIABLE SIZE (≤ condition):
    
    left = 0
    max_length = 0
    
    for right in range(n):
        # Add arr[right] to window
        window.add(arr[right])
        
        # Shrink while condition is VIOLATED
        while condition_violated:
            # Remove arr[left] from window
            window.remove(arr[left])
            left += 1
        
        # Update maximum (condition is satisfied here)
        max_length = max(max_length, right - left + 1)
    
    return max_length
    
    📝 DRY RUN - LONGEST SUBSTRING WITHOUT REPEATING:
    s = "abcabcbb"
    
    Goal: Find longest substring without repeating characters
    
    left = 0, right = 0, seen = {}
    
    Step 1: right=0, s[0]='a'
    - seen = {'a': 0}
    - length = 0 - 0 + 1 = 1
    - max_length = 1
    
    Step 2: right=1, s[1]='b'
    - seen = {'a': 0, 'b': 1}
    - length = 1 - 0 + 1 = 2
    - max_length = 2
    
    Step 3: right=2, s[2]='c'
    - seen = {'a': 0, 'b': 1, 'c': 2}
    - length = 2 - 0 + 1 = 3
    - max_length = 3
    
    Step 4: right=3, s[3]='a' (DUPLICATE!)
    - 'a' already in seen at index 0
    - Shrink: left = max(0, 0 + 1) = 1
    - seen = {'a': 3, 'b': 1, 'c': 2}
    - length = 3 - 1 + 1 = 3
    - max_length = 3
    
    Step 5: right=4, s[4]='b' (DUPLICATE!)
    - 'b' at index 1 (in window)
    - Shrink: left = max(1, 1 + 1) = 2
    - seen = {'a': 3, 'b': 4, 'c': 2}
    - length = 4 - 2 + 1 = 3
    - max_length = 3
    
    Continue...
    Result: 3 (substring "abc") ✓
    
    🆚 WHY THIS WORKS:
    - Right pointer explores all possibilities
    - Left pointer maintains valid window
    - Each element added/removed at most once → O(n)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 3: Longest Substring Without Repeating Characters (medium) ⭐⭐⭐
    - LeetCode 340: Longest Substring with At Most K Distinct (medium) ⭐⭐⭐
    - LeetCode 1004: Max Consecutive Ones III (medium) ⭐⭐⭐
    - LeetCode 424: Longest Repeating Character Replacement (medium) ⭐⭐
    - LeetCode 1493: Longest Subarray After Deleting One Element (medium)
    """
    
    def length_of_longest_substring(self, s: str) -> int:
        """
        LeetCode 3: Longest Substring Without Repeating Characters
        
        🔑 KEY: Use hashmap to track last seen position
        When duplicate found, jump left pointer
        """
        # the chapgpt and claude gave hashmap version but i did with hashset way better sol
        # char_index = {}  # char -> last seen index
        # left = 0
        # max_length = 0
        
        # for right in range(len(s)):
        #     char = s[right]
            
        #     # If char seen and in current window
        #     if char in char_index and char_index[char] >= left:
        #         # Move left past the previous occurrence
        #         left = char_index[char] + 1
            
        #     # Update last seen position
        #     char_index[char] = right
            
        #     # Update maximum length
        #     max_length = max(max_length, right - left + 1)
        
        # return max_length
        # my own solution with hashset(), similar to 219. Contains Duplicate II this pattern
        window = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] in window:
                while left < right and s[right] in window:
                    window.remove(s[left])
                    left += 1
            
            window.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
    
    
    
    def longest_substring_k_distinct(self, s: str, k: int) -> int:
        """
        LeetCode 340: Longest Substring with At Most K Distinct
        
        🔑 KEY: Track character frequency
        Shrink when distinct count > k
        
        📝 EXAMPLE:
        s = "eceba", k = 2
        
        Window "ece": 2 distinct (e, c) ✓
        Window "eceb": 3 distinct (e, c, b) ✗ → shrink
        After shrink "ceb": 3 distinct ✗ → shrink
        After shrink "eb": 2 distinct ✓
        
        Result: 3 (substring "ece")
        """
        if k == 0:
            return 0
        
        char_count = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Add right char to window
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            
            # Shrink while more than k distinct
            while len(char_count) > k:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
            
            # Update maximum
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    
    def max_consecutive_ones_iii(self, nums: List[int], k: int) -> int:
        """
        LeetCode 1004: Max Consecutive Ones III
        
        Find longest subarray of 1's after flipping at most k 0's
        
        🔑 KEY: Count zeros in window
        When zeros > k, shrink from left
        
        📝 EXAMPLE:
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        
        Expand until 2 zeros: [1,1,1,0,0] ✓
        Add another 0: [1,1,1,0,0,0] ✗ (3 zeros > k)
        Shrink: Remove 1's until one 0 removed
        Result: 6 (flip two 0's in middle)
        """
        left = 0
        zeros_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Add right element
            if nums[right] == 0:
                zeros_count += 1
            
            # Shrink while too many zeros
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            # Update maximum
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: VARIABLE SIZE - SHORTEST SUBARRAY (≥ condition)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Minimum size subarray with sum ≥ target
    2. Shortest subarray with sum at least K
    3. Minimum window containing pattern
    
    🔑 KEY CONCEPT:
    - Looking for MINIMUM/SHORTEST
    - Expand until condition MET
    - Shrink while condition STILL MET (greedy)
    - Track minimum window size
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 TEMPLATE FOR VARIABLE SIZE (≥ condition):
    
    left = 0
    min_length = float('inf')
    
    for right in range(n):
        # Add arr[right] to window
        window.add(arr[right])
        
        # Shrink while condition is SATISFIED (greedy!)
        while condition_satisfied:
            # Update minimum
            min_length = min(min_length, right - left + 1)
            
            # Try to shrink more
            window.remove(arr[left])
            left += 1
    
    return min_length if min_length != inf else 0
    
    📝 DRY RUN - MINIMUM SIZE SUBARRAY SUM:
    target = 7, nums = [2, 3, 1, 2, 4, 3]
    
    Goal: Find minimum length subarray with sum ≥ 7
    
    left = 0, right = 0, current_sum = 0, min_length = ∞
    
    Step 1: right=0, nums[0]=2
    - current_sum = 2
    - 2 < 7 (not satisfied) → expand
    
    Step 2: right=1, nums[1]=3
    - current_sum = 5
    - 5 < 7 → expand
    
    Step 3: right=2, nums[2]=1
    - current_sum = 6
    - 6 < 7 → expand
    
    Step 4: right=3, nums[3]=2
    - current_sum = 8
    - 8 ≥ 7 ✓ (satisfied!)
    - length = 3 - 0 + 1 = 4
    - min_length = 4
    - Try shrink: remove nums[0]=2
    - current_sum = 6 (< 7, can't shrink more)
    
    Step 5: right=4, nums[4]=4
    - current_sum = 10
    - 10 ≥ 7 ✓
    - length = 4 - 0 + 1 = 5 (not better)
    - Try shrink: remove nums[0]=2
    - current_sum = 8 (still ≥ 7)
    - length = 4 - 1 + 1 = 4 (not better)
    - Try shrink: remove nums[1]=3
    - current_sum = 5 (< 7, stop)
    
    Continue...
    Result: 2 (subarray [4, 3]) ✓
    
    🆚 KEY DIFFERENCE FROM PATTERN 2:
    - Pattern 2 (≤): Shrink when VIOLATED
    - Pattern 3 (≥): Shrink while SATISFIED (greedy)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 209: Minimum Size Subarray Sum (medium) ⭐⭐⭐
    - LeetCode 862: Shortest Subarray with Sum at Least K (hard) ⭐⭐
    - LeetCode 76: Minimum Window Substring (hard) ⭐⭐⭐
    """
    
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        """
        LeetCode 209: Minimum Size Subarray Sum
        
        Find minimum length subarray with sum ≥ target
        
        🔑 KEY: Shrink while sum still ≥ target (greedy)
        """
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            # Expand: add right element
            current_sum += nums[right]
            
            # Shrink: while condition satisfied, try to minimize
            while current_sum >= target:
                # Update minimum
                min_length = min(min_length, right - left + 1)
                
                # Remove left element and shrink
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: DISTINCT ELEMENTS (K distinct / At most K)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Subarrays with exactly K distinct elements
    2. Longest substring with at most K distinct
    3. Count subarrays with K different integers
    4. Fruits into baskets (at most 2 types)
    
    🔑 KEY CONCEPT:
    - Use hashmap/set to track distinct count
    - "Exactly K" = "At most K" - "At most K-1"
    - Maintain frequency for proper counting
    
    ⏱️  Time: O(n) | Space: O(k)
    
    📝 TRICK FOR "EXACTLY K":
    
    exactly_k_distinct(arr, k) = 
        at_most_k_distinct(arr, k) - at_most_k_distinct(arr, k-1)
    
    Why? 
    "Exactly 3" = "At most 3" minus "At most 2"
    = (subarrays with ≤3 distinct) - (subarrays with ≤2 distinct)
    = subarrays with exactly 3 distinct
    
    📝 DRY RUN - FRUITS INTO BASKETS:
    fruits = [1, 2, 1, 2, 3, 1, 1]
    
    Goal: Longest subarray with at most 2 distinct types
    
    left = 0, basket = {}
    
    Step 1-4: [1, 2, 1, 2]
    - basket = {1: 2, 2: 2}
    - 2 distinct ✓
    - length = 4
    
    Step 5: Add 3
    - basket = {1: 2, 2: 2, 3: 1}
    - 3 distinct ✗
    - Shrink: remove 1 → {1: 1, 2: 2, 3: 1}
    - Still 3 distinct ✗
    - Shrink: remove 2 → {1: 1, 2: 1, 3: 1}
    - Still 3 distinct ✗
    - Shrink: remove 1 → {2: 1, 3: 1}
    - Now 2 distinct ✓
    
    Continue...
    Result: 4 ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 904: Fruit Into Baskets (medium) ⭐⭐⭐
    - LeetCode 992: Subarrays with K Different Integers (hard) ⭐⭐⭐
    - LeetCode 340: Longest Substring with At Most K Distinct (medium) ⭐⭐⭐
    - LeetCode 159: Longest Substring with At Most Two Distinct (medium)
    """
    
    def total_fruit(self, fruits: List[int]) -> int:
        """
        LeetCode 904: Fruit Into Baskets
        
        Longest subarray with at most 2 distinct elements
        (Can pick from at most 2 types of trees continuously)
        """
        basket = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            # Add fruit to basket
            fruit_type = fruits[right]
            basket[fruit_type] = basket.get(fruit_type, 0) + 1
            
            # Shrink while more than 2 types
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            
            # Update maximum
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
    
    
    def subarrays_with_k_distinct(self, nums: List[int], k: int) -> int:
        """
        LeetCode 992: Subarrays with K Different Integers
        
        Count subarrays with exactly k distinct integers
        
        🔑 TRICK: exactly_k = at_most_k - at_most_(k-1)
        """
        def at_most_k(k):
            count_map = {}
            left = 0
            result = 0
            
            for right in range(len(nums)):
                # Add right element
                count_map[nums[right]] = count_map.get(nums[right], 0) + 1
                
                # Shrink while more than k distinct
                while len(count_map) > k:
                    count_map[nums[left]] -= 1
                    if count_map[nums[left]] == 0:
                        del count_map[nums[left]]
                    left += 1
                
                # All subarrays ending at right with ≤ k distinct
                result += right - left + 1
            
            return result
        
        return at_most_k(k) - at_most_k(k - 1)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: CHARACTER FREQUENCY (Anagrams, Permutations)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find all anagrams of pattern in string
    2. Check if string contains permutation of another
    3. Substring with concatenation of all words
    4. Pattern matching problems
    
    🔑 KEY CONCEPT:
    - Fixed size window (pattern length)
    - Compare frequency maps
    - Slide and update frequencies efficiently
    
    ⏱️  Time: O(n) | Space: O(k) where k = charset size
    
    📝 DRY RUN - FIND ANAGRAMS:
    s = "cbaebabacd", p = "abc"
    
    Goal: Find all start indices where s contains anagram of p
    
    p_count = {'a': 1, 'b': 1, 'c': 1}
    window_count = {}
    k = 3
    
    Window [c, b, a]: {'c': 1, 'b': 1, 'a': 1}
    - Matches p_count ✓
    - Add index 0 to result
    
    Slide to [b, a, e]:
    - Remove 'c': {'b': 1, 'a': 1}
    - Add 'e': {'b': 1, 'a': 1, 'e': 1}
    - Doesn't match ✗
    
    Slide to [a, e, b]:
    - Remove 'b', add 'b'
    - {'a': 1, 'e': 1, 'b': 1}
    - Doesn't match ✗
    
    Continue...
    Result: [0, 6] (indices where anagrams start) ✓
    
    🔑 OPTIMIZATION:
    Instead of comparing entire maps, maintain a "matches" counter:
    - matches = number of characters with correct frequency
    - When matches == len(p_count), we have anagram
    - O(1) comparison instead of O(k)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 438: Find All Anagrams in a String (medium) ⭐⭐⭐
    - LeetCode 567: Permutation in String (medium) ⭐⭐⭐
    - LeetCode 30: Substring with Concatenation of All Words (hard) ⭐⭐
    - LeetCode 76: Minimum Window Substring (hard) ⭐⭐⭐
    """
    
    def find_anagrams(self, s: str, p: str) -> List[int]:
        """
        LeetCode 438: Find All Anagrams in a String
        
        Find all start indices of p's anagrams in s
        
        🔑 KEY: Use frequency map comparison
        Window size = len(p)
        """
        if len(p) > len(s):
            return []
        
        result = []
        p_count = Counter(p)
        window_count = Counter()
        k = len(p)
        
        # Build first window
        for i in range(k):
            window_count[s[i]] += 1
        
        # Check first window
        if window_count == p_count:
            result.append(0)
        
        # Slide window
        for i in range(k, len(s)):
            # Add new char
            window_count[s[i]] += 1
            
            # Remove old char
            left_char = s[i - k]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Check if anagram
            if window_count == p_count:
                result.append(i - k + 1)
        
        return result
    
    
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """
        LeetCode 567: Permutation in String
        
        Check if s2 contains permutation of s1
        (Same as find_anagrams but return boolean)
        
        🔑 OPTIMIZED: Use matches counter
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()
        matches = 0
        k = len(s1)
        
        # Count matches in first window
        for i in range(k):
            char = s2[i]
            window_count[char] += 1
            if window_count[char] == s1_count[char]:
                matches += 1
        
        # Check if first window is permutation
        if matches == len(s1_count):
            return True
        
        # Slide window
        for i in range(k, len(s2)):
            # Add right char
            right_char = s2[i]
            if right_char in s1_count:
                if window_count[right_char] == s1_count[right_char]:
                    matches -= 1
                window_count[right_char] += 1
                if window_count[right_char] == s1_count[right_char]:
                    matches += 1
            else:
                window_count[right_char] += 1
            
            # Remove left char
            left_char = s2[i - k]
            if left_char in s1_count:
                if window_count[left_char] == s1_count[left_char]:
                    matches -= 1
                window_count[left_char] -= 1
                if window_count[left_char] == s1_count[left_char]:
                    matches += 1
            else:
                window_count[left_char] -= 1
            
            # Check if permutation found
            if matches == len(s1_count):
                return True
        
        return False
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: REPLACE/FLIP K ELEMENTS (Maximize sequence)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Longest subarray of 1's after flipping K 0's
    2. Longest repeating character after K replacements
    3. Max consecutive ones after deleting one element
    4. Maximize consecutive characters with K changes
    
    🔑 KEY CONCEPT:
    - Track "bad" elements (need replacement)
    - Allow up to K bad elements in window
    - Shrink when bad count > K
    
    ⏱️  Time: O(n) | Space: O(1) or O(26) for chars
    
    📝 DRY RUN - LONGEST REPEATING CHARACTER REPLACEMENT:
    s = "AABABBA", k = 1
    
    Goal: Longest substring with same char after ≤ k replacements
    
    Concept: 
    - In a window of size w with most frequent char count = max_freq
    - Replacements needed = w - max_freq
    - Valid window: w - max_freq ≤ k
    
    Window "AAB": size=3, max_freq('A')=2
    - Replacements = 3 - 2 = 1 ≤ k ✓
    
    Window "AABA": size=4, max_freq('A')=3
    - Replacements = 4 - 3 = 1 ≤ k ✓
    
    Window "AABAB": size=5, max_freq('A')=3
    - Replacements = 5 - 3 = 2 > k ✗
    - Shrink!
    
    Result: 4 (substring "AABA" → all A's with 1 replacement) ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 424: Longest Repeating Character Replacement (medium) ⭐⭐⭐
    - LeetCode 1004: Max Consecutive Ones III (medium) ⭐⭐⭐
    - LeetCode 1493: Longest Subarray of 1's After Deleting One (medium) ⭐⭐
    - LeetCode 1343: Maximum Erasure Value (medium)
    """
    
    def character_replacement(self, s: str, k: int) -> int:
        """
        LeetCode 424: Longest Repeating Character Replacement
        
        After replacing at most k characters,
        find longest substring with all same characters
        
        🔑 KEY: window_size - max_frequency ≤ k
        """
        char_count = {}
        left = 0
        max_length = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Add right char
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            
            # Update max frequency in current window
            max_freq = max(max_freq, char_count[char])
            
            # Window size
            window_size = right - left + 1
            
            # Shrink if replacements needed > k
            while window_size - max_freq > k:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
                window_size = right - left + 1
                # Note: We don't update max_freq on shrink
                # It's okay to keep it as upper bound
            
            # Update maximum
            max_length = max(max_length, window_size)
        
        return max_length
    
    
    def longest_subarray_delete_one(self, nums: List[int]) -> int:
        """
        LeetCode 1493: Longest Subarray of 1's After Deleting One
        
        Same as max consecutive ones, but MUST delete exactly one
        
        🔑 KEY: Allow at most 1 zero, then subtract 1 at end
        """
        left = 0
        zeros_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            
            # Shrink if more than 1 zero
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            # Update maximum (subtract 1 for mandatory deletion)
            max_length = max(max_length, right - left)
        
        return max_length
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: MULTIPLE CONDITIONS (Complex constraints)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Subarray with multiple constraints
    2. Nice subarrays (odd numbers exactly k)
    3. Binary subarrays with sum (multiple conditions)
    4. Complex validity checks
    
    🔑 KEY CONCEPT:
    - Multiple conditions to track
    - Carefully combine condition checks
    - Often need helper functions
    
    ⏱️  Time: O(n) | Space: O(1)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 1248: Count Nice Subarrays (medium) ⭐⭐
    - LeetCode 930: Binary Subarrays With Sum (medium) ⭐⭐
    - LeetCode 795: Number of Subarrays with Bounded Max (medium)
    """
    
    def number_of_subarrays(self, nums: List[int], k: int) -> int:
        """
        LeetCode 1248: Count Number of Nice Subarrays
        
        Count subarrays with exactly k odd numbers
        
        🔑 TRICK: Transform to "subarrays with sum = k"
        Replace odd with 1, even with 0
        Then use prefix sum approach or sliding window
        """
        def at_most_k(k):
            count = 0
            left = 0
            odds = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odds += 1
                
                while odds > k:
                    if nums[left] % 2 == 1:
                        odds -= 1
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return at_most_k(k) - at_most_k(k - 1)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: MINIMUM WINDOW SUBSTRING (Contains all)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Minimum window containing all characters of pattern
    2. Smallest window with all elements from array
    3. Substring covering all target characters
    
    🔑 KEY CONCEPT:
    - Expand until all required elements found
    - Shrink while still valid (greedy minimize)
    - Track "formed" count (how many requirements met)
    
    ⏱️  Time: O(n + m) | Space: O(k)
    
    📝 DRY RUN - MINIMUM WINDOW SUBSTRING:
    s = "ADOBECODEBANC", t = "ABC"
    
    Goal: Find minimum window in s containing all chars of t
    
    t_count = {'A': 1, 'B': 1, 'C': 1}
    required = 3 (need 3 distinct chars)
    formed = 0
    
    Expand:
    "ADOBEC": formed = 3 (has A, B, C) ✓
    - min_window = "ADOBEC" (length 6)
    
    Shrink (try to minimize):
    Remove 'A': "DOBEC" (no A, invalid)
    Can't shrink more
    
    Continue expanding:
    "ODEBANC": formed = 3 ✓
    - min_window = "BANC" (length 4) ✓
    
    Result: "BANC" ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 76: Minimum Window Substring (hard) ⭐⭐⭐
    - LeetCode 727: Minimum Window Subsequence (hard)
    """
    
    def min_window(self, s: str, t: str) -> str:
        """
        LeetCode 76: Minimum Window Substring
        
        Find minimum window in s containing all characters of t
        
        🔑 KEY: Track "formed" count for efficiency
        """
        if not s or not t:
            return ""
        
        # Frequency of characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Window frequency
        window_count = {}
        
        # formed: how many unique chars in window have desired frequency
        formed = 0
        
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right in range(len(s)):
            # Add char from right
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if frequency matches
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to shrink while valid
            while formed == required and left <= right:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remove from left
                left_char = s[left]
                window_count[left_char] -= 1
                
                # Check if we broke a requirement
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1
        
        return s[min_left:min_left + min_len] if min_len != float('inf') else ""
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: COUNT SUBARRAYS (Exactly K condition)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Count subarrays with exactly K distinct
    2. Count subarrays with exactly K odd numbers
    3. Subarray product less than K
    
    🔑 KEY CONCEPT:
    - exactly_k = at_most_k - at_most_(k-1)
    - Count subarrays ending at each position
    - For valid window [left, right], count = right - left + 1
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 WHY COUNT = right - left + 1?
    
    Window [a, b, c, d] at indices [0, 1, 2, 3]
    
    Subarrays ending at index 3 (element 'd'):
    - [d] (starts at 3)
    - [c, d] (starts at 2)
    - [b, c, d] (starts at 1)
    - [a, b, c, d] (starts at 0)
    
    Total = 4 = right - left + 1 = 3 - 0 + 1 ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 992: Subarrays with K Different Integers (hard) ⭐⭐⭐
    - LeetCode 930: Binary Subarrays With Sum (medium) ⭐⭐
    - LeetCode 1248: Count Nice Subarrays (medium) ⭐⭐
    - LeetCode 713: Subarray Product Less Than K (medium) ⭐⭐
    """
    
    def num_subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        """
        LeetCode 713: Subarray Product Less Than K
        
        Count subarrays where product < k
        
        🔑 KEY: For each right, count all valid subarrays ending at right
        """
        if k <= 1:
            return 0
        
        product = 1
        left = 0
        count = 0
        
        for right in range(len(nums)):
            # Add right element
            product *= nums[right]
            
            # Shrink while product >= k
            while product >= k:
                product //= nums[left]
                left += 1
            
            # Count subarrays ending at right
            # All subarrays from left to right
            count += right - left + 1
        
        return count
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 10: STRING MATCHING WITH WILDCARDS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find substring with wildcard characters
    2. Pattern matching with '?'
    3. Regex-like matching in strings
    
    🔑 KEY CONCEPT:
    - Similar to anagram finding
    - Handle wildcard as "matches any"
    - Adjust frequency counting accordingly
    
    💡 LEETCODE PROBLEMS:
    - Similar to Pattern 5 but with wildcards
    """


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 30 MUST-KNOW SLIDING WINDOW PROBLEMS (RANKED BY IMPORTANCE)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 ABSOLUTE MUST-KNOW (Master These First!):
═══════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LeetCode 3: Longest Substring Without Repeating Characters (medium)
   - Pattern: Variable Size - Longest (no repeats)
   - Why: THE classic sliding window, asked everywhere
   - Difficulty: 10/10 importance
   - Company: Amazon, Google, Facebook, Microsoft, Apple, Bloomberg
   - Master this first! Foundation for all variable window problems

2. ⭐⭐⭐ LeetCode 76: Minimum Window Substring (hard)
   - Pattern: Minimum Window (Contains all)
   - Why: Top 5 most asked, tests complete understanding
   - Difficulty: 10/10 importance
   - Company: Facebook, Amazon, Google, LinkedIn, Uber
   - The most complex sliding window problem

3. ⭐⭐⭐ LeetCode 209: Minimum Size Subarray Sum (medium)
   - Pattern: Shortest Subarray (≥ condition)
   - Why: Essential shrinking while satisfied pattern
   - Difficulty: 9/10 importance
   - Company: Facebook, Amazon, Microsoft

4. ⭐⭐⭐ LeetCode 438: Find All Anagrams in a String (medium)
   - Pattern: Character Frequency (Fixed size)
   - Why: Extremely common, tests frequency matching
   - Difficulty: 9/10 importance
   - Company: Amazon, Facebook, Microsoft, Google

5. ⭐⭐⭐ LeetCode 567: Permutation in String (medium)
   - Pattern: Character Frequency
   - Why: Variant of #4, must know both
   - Difficulty: 9/10 importance
   - Company: Microsoft, Amazon, Facebook

6. ⭐⭐⭐ LeetCode 424: Longest Repeating Character Replacement (medium)
   - Pattern: Replace K Elements
   - Why: Tests understanding of "replacements needed"
   - Difficulty: 9/10 importance
   - Company: Amazon, Google, Facebook

7. ⭐⭐⭐ LeetCode 1004: Max Consecutive Ones III (medium)
   - Pattern: Replace K Elements (flip zeros)
   - Why: Very common variant, Amazon favorite
   - Difficulty: 9/10 importance
   - Company: Amazon, Facebook, Google

8. ⭐⭐⭐ LeetCode 992: Subarrays with K Different Integers (hard)
   - Pattern: Exactly K Distinct (at_most trick)
   - Why: Tests the "exactly K = at_most_K - at_most_(K-1)" technique
   - Difficulty: 8/10 importance
   - Company: Google, Amazon, Facebook


🔥🔥 VERY IMPORTANT (Must Practice):
═══════════════════════════════════════════════════════════════════════════

9. ⭐⭐ LeetCode 643: Maximum Average Subarray I (easy)
   - Pattern: Fixed Size Window
   - Why: Easiest sliding window, learn fundamentals
   - Difficulty: 7/10 importance
   - Company: Amazon, Google

10. ⭐⭐ LeetCode 340: Longest Substring with At Most K Distinct (medium)
    - Pattern: K Distinct Elements
    - Why: Core pattern for distinct counting
    - Difficulty: 8/10 importance
    - Company: Amazon, Google, Facebook

11. ⭐⭐ LeetCode 904: Fruit Into Baskets (medium)
    - Pattern: At Most K Distinct (K=2)
    - Why: Real-world problem framing, Amazon loves it
    - Difficulty: 7/10 importance
    - Company: Amazon, DoorDash

12. ⭐⭐ LeetCode 713: Subarray Product Less Than K (medium)
    - Pattern: Count Subarrays
    - Why: Tests counting technique (right - left + 1)
    - Difficulty: 7/10 importance
    - Company: Amazon, Facebook, Google

13. ⭐⭐ LeetCode 1493: Longest Subarray After Deleting One Element (medium)
    - Pattern: Replace/Flip (must delete exactly 1)
    - Why: Common variant of consecutive ones
    - Difficulty: 7/10 importance
    - Company: Amazon, Facebook

14. ⭐⭐ LeetCode 1248: Count Nice Subarrays (medium)
    - Pattern: Exactly K condition
    - Why: Tests transformation (odd→1, even→0)
    - Difficulty: 7/10 importance
    - Company: Amazon, Microsoft

15. ⭐⭐ LeetCode 159: Longest Substring with At Most Two Distinct (medium)
    - Pattern: K Distinct (K=2)
    - Why: Simpler version of #10, good practice
    - Difficulty: 7/10 importance
    - Company: Google, Facebook


🔥 IMPORTANT (Complete the Foundation):
═══════════════════════════════════════════════════════════════════════════

16. ⭐ LeetCode 1456: Maximum Number of Vowels in Substring (medium)
    - Pattern: Fixed Size Window
    - Why: Count specific elements in window
    - Difficulty: 6/10 importance

17. ⭐⭐ LeetCode 30: Substring with Concatenation of All Words (hard)
    - Pattern: Character Frequency (complex)
    - Why: Advanced frequency matching
    - Difficulty: 7/10 importance
    - Company: Amazon, Microsoft

18. ⭐⭐ LeetCode 930: Binary Subarrays With Sum (medium)
    - Pattern: Exactly K (prefix sum or at_most)
    - Why: Multiple solution approaches
    - Difficulty: 6/10 importance

19. ⭐ LeetCode 1343: Number of Sub-arrays of Size K (medium)
    - Pattern: Fixed Size + Threshold
    - Why: Fixed window with condition
    - Difficulty: 6/10 importance

20. ⭐⭐ LeetCode 1151: Minimum Swaps to Group All 1's Together (medium)
    - Pattern: Fixed Size (count zeros)
    - Why: Creative fixed window application
    - Difficulty: 6/10 importance

21. ⭐ LeetCode 2090: K Radius Subarray Averages (medium)
    - Pattern: Fixed Size Window
    - Why: Window with radius (size = 2k+1)
    - Difficulty: 5/10 importance

22. ⭐⭐ LeetCode 1438: Longest Subarray with Absolute Diff ≤ Limit (medium)
    - Pattern: Variable Size + Monotonic deque
    - Why: Combines sliding window with data structure
    - Difficulty: 7/10 importance
    - Company: Google, Amazon

23. ⭐⭐ LeetCode 1208: Get Equal Substrings Within Budget (medium)
    - Pattern: Variable Size (≤ condition)
    - Why: Cost-based window expansion
    - Difficulty: 6/10 importance

24. ⭐ LeetCode 1052: Grumpy Bookstore Owner (medium)
    - Pattern: Fixed Size (maximize sum)
    - Why: Real-world scenario, fixed window optimization
    - Difficulty: 6/10 importance

25. ⭐⭐ LeetCode 2024: Maximize Confusion of Exam (medium)
    - Pattern: Replace K Elements (like #6)
    - Why: Same pattern as character replacement
    - Difficulty: 6/10 importance

26. ⭐ LeetCode 1100: Find K-Length Substrings With No Repeated Chars (medium)
    - Pattern: Fixed Size + Distinct check
    - Why: Combines fixed size with uniqueness
    - Difficulty: 6/10 importance

27. ⭐⭐ LeetCode 2516: Take K of Each Character From Left and Right (medium)
    - Pattern: Variable Size (complement thinking)
    - Why: Creative approach, minimum removal
    - Difficulty: 6/10 importance

28. ⭐ LeetCode 2134: Minimum Swaps to Group All 1's Together II (medium)
    - Pattern: Fixed Size (circular array)
    - Why: Extends #20 to circular
    - Difficulty: 6/10 importance

29. ⭐⭐ LeetCode 395: Longest Substring with At Least K Repeating (medium)
    - Pattern: Variable Size (complex validation)
    - Why: Every char must appear ≥ k times
    - Difficulty: 7/10 importance
    - Company: Facebook, Google

30. ⭐ LeetCode 1358: Number of Substrings Containing All Three (medium)
    - Pattern: Variable Size (count subarrays)
    - Why: Tests counting with multiple conditions
    - Difficulty: 6/10 importance


═══════════════════════════════════════════════════════════════════════════
📊 PROBLEM DIFFICULTY DISTRIBUTION:
═══════════════════════════════════════════════════════════════════════════

Easy: 1 problem (#9)
Medium: 26 problems
Hard: 3 problems (#2, #8, #17)

By Pattern:
- Fixed Size Window: 7 problems
- Variable Size (Longest): 10 problems
- Variable Size (Shortest): 2 problems
- Distinct Elements: 5 problems
- Character Frequency: 5 problems
- Replace/Flip K: 4 problems
- Count Subarrays: 3 problems
- Complex Conditions: 4 problems


═══════════════════════════════════════════════════════════════════════════
🎯 STUDY PLAN (4 WEEKS):
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - Foundation (Fixed + Basic Variable):
Day 1-2: 643 (Fixed Size - easy), 1456 (Fixed - vowels)
Day 3-4: 3 (Longest No Repeat) ⚠️ CRITICAL! Spend time here
Day 5-6: 209 (Minimum Size), 340 (K Distinct)
Day 7: Review + understand the difference between fixed and variable

WEEK 2 - Character Frequency & Distinct:
Day 1-2: 438 (Find Anagrams), 567 (Permutation) ⚠️ Very similar
Day 3-4: 904 (Fruit Baskets), 159 (Two Distinct)
Day 5-6: 713 (Product Less Than K), 992 (K Different)
Day 7: Review counting technique (right - left + 1)

WEEK 3 - Replace/Flip & Complex:
Day 1-2: 424 (Character Replacement) ⚠️ Tricky!
Day 3-4: 1004 (Max Ones III), 1493 (Delete One)
Day 5-6: 1248 (Nice Subarrays), 930 (Binary Sum)
Day 7: Review the "exactly K = at_most_K - at_most_(K-1)" trick

WEEK 4 - Hard Problems + Mastery:
Day 1-3: 76 (Minimum Window) ⚠️⚠️ Hardest problem, needs time
Day 4-5: 30 (Concatenation), 1438 (Absolute Diff)
Day 6: Review all patterns, identify which to use
Day 7: Redo your weakest 5 problems


═══════════════════════════════════════════════════════════════════════════
💡 PATTERN RECOGNITION CHEATSHEET:
═══════════════════════════════════════════════════════════════════════════

🔍 HOW TO IDENTIFY WHICH PATTERN:

KEYWORDS → PATTERN:

"subarray/substring of size K" / "exactly K elements"
→ FIXED SIZE WINDOW (Pattern 1)
→ Build first window, then slide

"longest/maximum subarray with..." / "without repeating"
→ VARIABLE SIZE - LONGEST (Pattern 2)
→ Expand right, shrink when violated

"shortest/minimum subarray with sum ≥" / "at least K"
→ VARIABLE SIZE - SHORTEST (Pattern 3)
→ Expand right, shrink while satisfied

"at most K distinct" / "K different" / "K types"
→ DISTINCT ELEMENTS (Pattern 4)
→ Track distinct count, shrink when > K

"anagram" / "permutation" / "substring contains"
→ CHARACTER FREQUENCY (Pattern 5)
→ Compare frequency maps, fixed size = pattern length

"after flipping K" / "replace K characters" / "delete one"
→ REPLACE/FLIP K (Pattern 6)
→ Track "bad" elements, allow up to K

"exactly K" / "with K odd numbers" / "count subarrays"
→ COUNT SUBARRAYS (Pattern 9)
→ Use at_most_K - at_most_(K-1)

"contains all characters" / "covering substring"
→ MINIMUM WINDOW (Pattern 8)
→ Expand until all found, shrink while valid


═══════════════════════════════════════════════════════════════════════════
🎓 COMPANY-SPECIFIC FOCUS:
═══════════════════════════════════════════════════════════════════════════

Amazon: 3, 438, 904, 1004, 424, 713, 209
Microsoft: 567, 438, 424, 30, 209, 1248
Facebook: 76, 3, 438, 424, 340, 992, 713
Google: 3, 76, 992, 340, 438, 1438, 395
Apple: 3, 209, 643, 438

If targeting FAANG: 
- MUST master: #1-8 (the ⭐⭐⭐ problems)
- These cover 90% of sliding window interviews


═══════════════════════════════════════════════════════════════════════════
🚀 PRO TIPS FOR SLIDING WINDOW INTERVIEWS:
═══════════════════════════════════════════════════════════════════════════

1. IDENTIFY THE PATTERN FIRST:
   ✅ Fixed size? → Window size given
   ✅ Longest? → Expand right, shrink when invalid
   ✅ Shortest? → Expand right, shrink while valid
   ✅ Count? → Use at_most trick for "exactly K"

2. CLARIFY IMMEDIATELY:
   - Is the array/string always non-empty?
   - Can there be negative numbers? (affects sum problems!)
   - Fixed or variable size window?
   - What should I return if no valid window exists?

3. DRAW IT OUT:
   - Visualize with 5-6 elements
   - Show window boundaries with brackets
   - Trace left and right pointers step by step

4. CODE STRUCTURE:
   ```python
   # Initialize
   left = 0
   result = 0  # or float('inf') for minimum
   window_state = {}  # frequency, sum, count, etc.
   
   for right in range(len(arr)):
       # 1. Add arr[right] to window
       window_state.add(arr[right])
       
       # 2. Shrink if needed (while loop!)
       while condition:
           window_state.remove(arr[left])
           left += 1
       
       # 3. Update result
       result = max/min/count(result, window_size)
   ```

5. COMMON MISTAKES TO AVOID:
   ❌ Forgetting to update window state when shrinking
   ❌ Using if instead of while for shrinking
   ❌ Not handling empty array edge case
   ❌ Off-by-one errors in window size (right - left + 1)
   ❌ Comparing frequency maps without optimizing

6. OPTIMIZATION TRICKS:
   ✅ Use "matches" counter instead of comparing entire maps
   ✅ Keep max_freq as upper bound (don't recalculate)
   ✅ Use Counter from collections for frequency
   ✅ For "exactly K", use at_most_K - at_most_(K-1)

7. TEMPLATE SELECTION:
   Fixed Size:
   ```python
   window = sum(arr[:k])
   result = window
   for i in range(k, n):
       window = window - arr[i-k] + arr[i]
       result = update(result, window)
   ```
   
   Variable Size (Longest):
   ```python
   left = 0
   for right in range(n):
       add(arr[right])
       while invalid:
           remove(arr[left])
           left += 1
       result = max(result, right - left + 1)
   ```
   
   Variable Size (Shortest):
   ```python
   left = 0
   result = inf
   for right in range(n):
       add(arr[right])
       while valid:
           result = min(result, right - left + 1)
           remove(arr[left])
           left += 1
   ```

8. NEGATIVE NUMBERS:
   ✅ Safe: Character counts, distinct elements, frequency
   ⚠️  Careful: Sum-based problems (might need Kadane's)
   ✅ Rule: If problem is about COUNTS, negatives are fine
   ⚠️  Rule: If problem is about SUMS with monotonicity, beware

9. TESTING STRATEGY:
   Test with:
   - Empty array: []
   - Single element: [1]
   - All same: [5,5,5,5]
   - K > array length
   - K = 0 or K = 1
   - K = array length

10. TIME COMPLEXITY ANALYSIS:
    - Each element added once (right pointer)
    - Each element removed once (left pointer)
    - Total operations: O(2n) = O(n)
    - Space: O(k) for frequency map or O(1)


═══════════════════════════════════════════════════════════════════════════
✅ COMPLETION CHECKLIST:
═══════════════════════════════════════════════════════════════════════════

Foundation (Week 1):
□ 643: Maximum Average Subarray I
□ 1456: Maximum Vowels
□ 3: Longest Substring Without Repeating ⚠️⚠️
□ 209: Minimum Size Subarray Sum ⚠️
□ 340: Longest with K Distinct ⚠️

Character & Distinct (Week 2):
□ 438: Find All Anagrams ⚠️⚠️
□ 567: Permutation in String ⚠️⚠️
□ 904: Fruit Into Baskets
□ 159: Two Distinct Characters
□ 713: Subarray Product Less Than K
□ 992: K Different Integers ⚠️

Replace/Flip (Week 3):
□ 424: Character Replacement ⚠️⚠️
□ 1004: Max Consecutive Ones III ⚠️⚠️
□ 1493: Longest After Deleting One
□ 1248: Count Nice Subarrays
□ 930: Binary Subarrays With Sum

Hard & Complex (Week 4):
□ 76: Minimum Window Substring ⚠️⚠️⚠️
□ 30: Substring with Concatenation
□ 1438: Absolute Diff Limit

Bonus (If time):
□ 1208: Equal Substrings
□ 2024: Maximize Confusion
□ 395: At Least K Repeating

🎉 Completed all? You're a Sliding Window Master! 
   Ready for any interview!


═══════════════════════════════════════════════════════════════════════════
🔑 FINAL WISDOM:
═══════════════════════════════════════════════════════════════════════════

1. Sliding window is ALWAYS O(n) - each element touched at most twice
2. When you see "contiguous", think sliding window first
3. Master problems #1-8 and you're 90% ready for any interview
4. The hardest part is recognizing WHICH pattern to use
5. Practice until you can identify pattern in 30 seconds
6. Draw window boundaries before coding
7. Test with edge cases: empty, single, all same
8. Most bugs are in: shrinking condition, updating state, window size calc
9. Fixed size = easy | Variable size = most common | Minimum window = hardest
10. Negative numbers? Check if problem is about COUNTS (safe) or SUMS (careful)

Remember: Sliding window is one of the most beautiful algorithmic techniques.
Once mastered, it becomes second nature. Practice these 30 problems and
you'll never fear a sliding window question again! 🚀
"""


def test_sliding_window_patterns():
    """Test key sliding window patterns"""
    sw = SlidingWindowPatterns()
    
    print("🧪 Testing Sliding Window Patterns...\n")
    
    # Test 1: Fixed Size Max Sum
    assert sw.max_sum_fixed_window([2, 1, 5, 1, 3, 2], 3) == 9
    print("✅ Pattern 1 (Fixed Size): Passed")
    
    # Test 2: Longest Without Repeating
    assert sw.length_of_longest_substring("abcabcbb") == 3
    assert sw.length_of_longest_substring("pwwkew") == 3
    print("✅ Pattern 2 (Longest No Repeat): Passed")
    
    # Test 3: Minimum Size Subarray Sum
    assert sw.min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    print("✅ Pattern 3 (Minimum Size): Passed")
    
    # Test 4: Longest K Distinct
    assert sw.longest_substring_k_distinct("eceba", 2) == 3
    print("✅ Pattern 4 (K Distinct): Passed")
    
    # Test 5: Find Anagrams
    assert sw.find_anagrams("cbaebabacd", "abc") == [0, 6]
    print("✅ Pattern 5 (Anagrams): Passed")
    
    # Test 6: Max Consecutive Ones
    assert sw.max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    print("✅ Pattern 6 (Max Ones III): Passed")
    
    # Test 7: Character Replacement
    assert sw.character_replacement("AABABBA", 1) == 4
    print("✅ Pattern 7 (Character Replacement): Passed")
    
    # Test 8: Minimum Window
    assert sw.min_window("ADOBECODEBANC", "ABC") == "BANC"
    print("✅ Pattern 8 (Minimum Window): Passed")
    
    # Test 9: Subarray Product
    assert sw.num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
    print("✅ Pattern 9 (Subarray Product): Passed")
    
    print("\n🎉 All tests passed! Sliding window patterns mastered!")


if __name__ == "__main__":
    test_sliding_window_patterns()