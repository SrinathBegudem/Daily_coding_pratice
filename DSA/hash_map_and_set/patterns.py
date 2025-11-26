"""
═══════════════════════════════════════════════════════════════════════════════
                    HASHMAP & HASHSET MASTERY GUIDE
            All Patterns, Templates & Recognition Keywords
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. HASHMAP vs HASHSET - WHEN TO USE WHICH?

   HASHMAP (Dictionary in Python):
   - Stores KEY → VALUE pairs
   - Use when you need to ASSOCIATE data
   - Examples: frequency counting, indexing, caching
   - Python: dict = {}
   - Time: O(1) average for get/put/delete
   
   HASHSET (Set in Python):
   - Stores only KEYS (unique values)
   - Use when you only need EXISTENCE check
   - Examples: deduplication, fast lookup, uniqueness
   - Python: set_var = set()
   - Time: O(1) average for add/remove/contains
   
   Rule of Thumb:
   - Need to count/track/map? → HashMap
   - Just need yes/no existence? → HashSet

2. TIME COMPLEXITY:
   - Average: O(1) for all operations
   - Worst case: O(n) with hash collisions (rare)
   - Space: O(n) where n = number of elements

3. 12 ESSENTIAL HASHMAP PATTERNS:
   ✅ Pattern 1: Complement Lookup (Two Sum)
   ✅ Pattern 2: Frequency Counter
   ✅ Pattern 3: HashMap + Index (value → index)
   ✅ Pattern 4: HashMap + Prefix Sum
   ✅ Pattern 5: HashMap + Sliding Window
   ✅ Pattern 6: Grouping/Bucketing (Anagrams)
   ✅ Pattern 7: HashMap for Caching/Memoization
   ✅ Pattern 8: HashMap + Two Pointers
   ✅ Pattern 9: Multiple HashMaps (Intersection)
   ✅ Pattern 10: HashMap + Graph (Adjacency)
   ✅ Pattern 11: HashMap + Custom Objects
   ✅ Pattern 12: LRU Cache (HashMap + LinkedList)

4. 6 ESSENTIAL HASHSET PATTERNS:
   ✅ Pattern 1: Deduplication/Uniqueness
   ✅ Pattern 2: Fast Lookup/Contains
   ✅ Pattern 3: Set Operations (Union/Intersection)
   ✅ Pattern 4: Cycle Detection
   ✅ Pattern 5: Sliding Window with Set
   ✅ Pattern 6: Two-Pointer with Set

5. RECOGNITION KEYWORDS:
   
   HashMap Keywords:
   - "count/frequency"
   - "first/last occurrence"
   - "map/associate"
   - "group by"
   - "complement/pair"
   - "index of"
   - "cache/memoize"
   
   HashSet Keywords:
   - "unique"
   - "duplicate"
   - "contains"
   - "exists"
   - "distinct"
   - "intersection/union"
   - "cycle/visited"

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Dict, Set, Optional
from collections import defaultdict, Counter
import heapq


class HashMapPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: COMPLEMENT LOOKUP (Two Sum Pattern)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find two numbers that sum to target
    2. Find pairs with specific difference
    3. Find pairs with specific product
    4. Max operations by pairing
    5. Count valid pairs
    
    🔑 KEY CONCEPT:
    Store what you've seen, check if complement exists
    
    If: a + b = target
    Then: b = target - a (complement)
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - TWO SUM:
    nums = [2, 7, 11, 15], target = 9
    
    HashMap: {} (stores value → index)
    
    i=0, num=2:
      complement = 9 - 2 = 7
      7 in map? No
      map[2] = 0
      map = {2: 0}
    
    i=1, num=7:
      complement = 9 - 7 = 2
      2 in map? Yes! map[2] = 0
      Found pair: indices [0, 1] ✓
      return [0, 1]
    
    📝 DRY RUN - MAX K-SUM PAIRS:
    nums = [1,2,3,4], k = 5
    
    Goal: Max pairs that sum to k
    
    freq = {} (stores value → count)
    pairs = 0
    
    num=1:
      complement = 5 - 1 = 4
      4 in freq? No
      freq[1] = 1
      freq = {1: 1}
    
    num=2:
      complement = 5 - 2 = 3
      3 in freq? No
      freq[2] = 1
      freq = {1: 1, 2: 1}
    
    num=3:
      complement = 5 - 3 = 2
      2 in freq? Yes! freq[2] = 1 > 0
      Form pair! pairs = 1
      freq[2] -= 1 (use up one 2)
      freq = {1: 1, 2: 0}
    
    num=4:
      complement = 5 - 4 = 1
      1 in freq? Yes! freq[1] = 1 > 0
      Form pair! pairs = 2
      freq[1] -= 1
      freq = {1: 0, 2: 0}
    
    Result: 2 pairs ✓
    Pairs: (2,3) and (1,4)
    
    🔑 WHY THIS WORKS:
    Instead of checking all pairs O(n²), we:
    1. Store complements as we go
    2. Check if current number's pair exists
    3. O(1) lookup → O(n) total
    
    🎯 TEMPLATE TO MEMORIZE:
    
    # For finding indices:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    # For counting/max pairs:
    freq = {}
    count = 0
    for num in nums:
        complement = target - num
        if complement in freq and freq[complement] > 0:
            count += 1
            freq[complement] -= 1
        else:
            freq[num] = freq.get(num, 0) + 1
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 1: Two Sum (easy) ⭐⭐⭐ MUST KNOW!
    - LeetCode 167: Two Sum II (easy) ⭐⭐
    - LeetCode 1679: Max Number of K-Sum Pairs (medium) ⭐⭐⭐
    - LeetCode 2006: Count Pairs With Absolute Difference K (easy) ⭐⭐
    - LeetCode 454: 4Sum II (medium) ⭐⭐
    - LeetCode 1512: Number of Good Pairs (easy) ⭐⭐
    - LeetCode 1711: Count Good Meals (medium) ⭐
    """
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        LeetCode 1: Two Sum
        
        THE most famous HashMap problem!
        Asked by: Google, Amazon, Apple, Facebook, Microsoft
        """
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []
    
    
    def max_operations(self, nums: List[int], k: int) -> int:
        """
        LeetCode 1679: Max Number of K-Sum Pairs
        
        🔑 KEY: Use frequency map, decrement when paired
        """
        freq = {}
        operations = 0
        
        for num in nums:
            complement = k - num
            
            # Check if complement exists and has count > 0
            if complement in freq and freq[complement] > 0:
                operations += 1
                freq[complement] -= 1
            else:
                # Store current number
                freq[num] = freq.get(num, 0) + 1
        
        return operations
    
    
    def count_k_difference(self, nums: List[int], k: int) -> int:
        """
        LeetCode 2006: Count Pairs With Absolute Difference K
        
        🔑 KEY: |a - b| = k means b = a + k OR b = a - k
        Check both complements!
        
        📝 EXAMPLE:
        nums = [1,2,2,1], k = 1
        
        For each num, check:
        - complement1 = num + k
        - complement2 = num - k
        
        num=1: check 2 and 0
          - 2 not seen yet, count = 0
        num=2: check 3 and 1
          - 1 seen 1 time, count = 1
        num=2: check 3 and 1
          - 1 seen 1 time, count = 2
        num=1: check 2 and 0
          - 2 seen 2 times, count = 4
        
        Total: 4 pairs ✓
        """
        freq = {}
        count = 0
        
        for num in nums:
            # Check both complements
            complement1 = num + k
            complement2 = num - k
            
            count += freq.get(complement1, 0)
            if k != 0:  # Avoid double counting when k=0
                count += freq.get(complement2, 0)
            
            freq[num] = freq.get(num, 0) + 1
        
        return count
    
    
    def four_sum_count(self, nums1: List[int], nums2: List[int], 
                       nums3: List[int], nums4: List[int]) -> int:
        """
        LeetCode 454: 4Sum II
        
        🔑 KEY: Split into two groups
        - Group 1: all sums from nums1 + nums2
        - Group 2: check if -(nums3 + nums4) exists
        
        📝 EXAMPLE:
        nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
        
        Group 1 sums (nums1 + nums2):
        1 + (-2) = -1
        1 + (-1) = 0
        2 + (-2) = 0
        2 + (-1) = 1
        sum_map = {-1: 1, 0: 2, 1: 1}
        
        Group 2 check (nums3 + nums4):
        For each sum, check if -sum exists in map
        -1 + 0 = -1, need -(-1) = 1, exists! count += 1
        -1 + 2 = 1, need -1 = -1, exists! count += 1
        2 + 0 = 2, need -2, doesn't exist
        2 + 2 = 4, need -4, doesn't exist
        
        Total: 2 tuples ✓
        """
        # Store all sums from nums1 + nums2
        sum_map = {}
        for a in nums1:
            for b in nums2:
                sum_ab = a + b
                sum_map[sum_ab] = sum_map.get(sum_ab, 0) + 1
        
        # Check complements from nums3 + nums4
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += sum_map.get(target, 0)
        
        return count
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: FREQUENCY COUNTER
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Count occurrences of elements
    2. Find most/least frequent element
    3. Check if frequencies match
    4. Sort by frequency
    5. Find elements with specific frequency
    
    🔑 KEY CONCEPT:
    Count how many times each element appears
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - MAJORITY ELEMENT:
    nums = [2,2,1,1,1,2,2]
    
    Goal: Find element appearing > n/2 times
    
    freq = {}
    
    num=2: freq = {2: 1}
    num=2: freq = {2: 2}
    num=1: freq = {2: 2, 1: 1}
    num=1: freq = {2: 2, 1: 2}
    num=1: freq = {2: 2, 1: 3}
    num=2: freq = {2: 3, 1: 3}
    num=2: freq = {2: 4, 1: 3}
    
    n/2 = 7/2 = 3.5
    Element 2 appears 4 times (> 3.5) ✓
    Return 2
    
    🎯 TEMPLATE TO MEMORIZE:
    
    # Basic frequency count:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Or use Counter (cleaner):
    from collections import Counter
    freq = Counter(nums)
    
    # Find max frequency:
    max_freq = max(freq.values())
    
    # Find element with max frequency:
    most_common = max(freq.keys(), key=freq.get)
    # Or: Counter(nums).most_common(1)[0][0]
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 169: Majority Element (easy) ⭐⭐⭐
    - LeetCode 347: Top K Frequent Elements (medium) ⭐⭐⭐
    - LeetCode 451: Sort Characters By Frequency (medium) ⭐⭐
    - LeetCode 387: First Unique Character (easy) ⭐⭐
    - LeetCode 383: Ransom Note (easy) ⭐⭐
    - LeetCode 1346: Check If N and Double Exist (easy) ⭐
    - LeetCode 1160: Find Words Formed by Characters (easy) ⭐
    """
    
    def majority_element(self, nums: List[int]) -> int:
        """
        LeetCode 169: Majority Element
        
        🔑 OPTIMIZATION: Boyer-Moore Voting Algorithm O(1) space
        But HashMap is simpler to understand!
        """
        freq = {}
        majority_count = len(nums) // 2
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
            # Early termination
            if freq[num] > majority_count:
                return num
        
        return -1
    
    
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        LeetCode 347: Top K Frequent Elements
        
        🔑 METHODS:
        1. Heap: O(n log k)
        2. Bucket sort: O(n)
        3. Counter.most_common(): O(n log n)
        
        📝 EXAMPLE:
        nums = [1,1,1,2,2,3], k = 2
        
        Frequency: {1: 3, 2: 2, 3: 1}
        Top 2: [1, 2] ✓
        """
        # Method 1: Using Counter (simplest)
        from collections import Counter
        freq = Counter(nums)
        return [num for num, _ in freq.most_common(k)]
        
        # Method 2: Using heap (better for large data)
        # freq = Counter(nums)
        # return heapq.nlargest(k, freq.keys(), key=freq.get)
    
    
    def first_uniq_char(self, s: str) -> int:
        """
        LeetCode 387: First Unique Character in a String
        
        🔑 TWO-PASS:
        1. Count frequencies
        2. Find first with frequency 1
        
        📝 EXAMPLE:
        s = "leetcode"
        
        freq = {l:1, e:3, t:1, c:1, o:1, d:1}
        First pass indices: l(0), e(1)
        First unique at index 0: 'l' ✓
        """
        from collections import Counter
        freq = Counter(s)
        
        # Find first unique
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1
    
    
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        """
        LeetCode 383: Ransom Note
        
        🔑 KEY: Check if magazine has enough of each character
        
        📝 EXAMPLE:
        ransomNote = "aa", magazine = "aab"
        
        Need: {a: 2}
        Have: {a: 2, b: 1}
        Can construct? Yes ✓
        """
        from collections import Counter
        need = Counter(ransomNote)
        have = Counter(magazine)
        
        # Check if we have enough of each character
        for char, count in need.items():
            if have[char] < count:
                return False
        
        return True
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: HASHMAP + INDEX (Value → Index/Position)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find first/last occurrence index
    2. Find duplicates within distance k
    3. Check if value exists at index
    4. Find nearest occurrence
    
    🔑 KEY CONCEPT:
    Map value to its index/indices for fast lookup
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - CONTAINS DUPLICATE II:
    nums = [1,2,3,1], k = 3
    
    Goal: Check if duplicate exists within distance k
    
    index_map = {} (value → most recent index)
    
    i=0, num=1:
      1 not in map
      map[1] = 0
      map = {1: 0}
    
    i=1, num=2:
      2 not in map
      map[2] = 1
      map = {1: 0, 2: 1}
    
    i=2, num=3:
      3 not in map
      map[3] = 2
      map = {1: 0, 2: 1, 3: 2}
    
    i=3, num=1:
      1 in map! index = 0
      distance = 3 - 0 = 3
      3 <= 3? Yes! ✓
      return True
    
    🎯 TEMPLATE TO MEMORIZE:
    
    # Find first occurrence:
    index_map = {}
    for i, num in enumerate(nums):
        if num not in index_map:
            index_map[num] = i
    
    # Find last occurrence:
    index_map = {}
    for i, num in enumerate(nums):
        index_map[num] = i  # Always update
    
    # Check duplicates within distance:
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 219: Contains Duplicate II (easy) ⭐⭐⭐
    - LeetCode 217: Contains Duplicate (easy) ⭐⭐
    - LeetCode 1: Two Sum (uses this!) ⭐⭐⭐
    - LeetCode 359: Logger Rate Limiter (easy) ⭐⭐
    """
    
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        """
        LeetCode 219: Contains Duplicate II
        
        🔑 KEY: Store most recent index, check distance
        """
        index_map = {}
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        
        return False
    
    
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        LeetCode 217: Contains Duplicate
        
        🔑 SIMPLE: Just check if seen before
        (Could also use set!)
        """
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
        
        # Or simply: return len(nums) != len(set(nums))
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: HASHMAP + PREFIX SUM
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Subarray sum equals K
    2. Continuous subarray sum
    3. Subarray sums divisible by K
    4. Path sum in tree
    
    🔑 KEY CONCEPT:
    Store prefix sums in HashMap to find subarrays
    
    If prefix[j] - prefix[i] = K
    Then prefix[i] = prefix[j] - K
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 NOTE: This was covered in detail in Prefix Sum guide!
    Refer to that for full explanation.
    
    🎯 TEMPLATE:
    
    count = 0
    curr_sum = 0
    prefix_map = {0: 1}
    
    for num in nums:
        curr_sum += num
        target = curr_sum - k
        count += prefix_map.get(target, 0)
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 560: Subarray Sum Equals K (medium) ⭐⭐⭐
    - LeetCode 974: Subarray Sums Divisible by K (medium) ⭐⭐⭐
    - LeetCode 523: Continuous Subarray Sum (medium) ⭐⭐⭐
    - LeetCode 525: Contiguous Array (medium) ⭐⭐⭐
    - LeetCode 437: Path Sum III (medium) ⭐⭐⭐
    """
    
    # Refer to Prefix Sum guide for implementations!
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: HASHMAP + SLIDING WINDOW
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Longest substring with K distinct characters
    2. Longest substring without repeating characters
    3. Minimum window substring
    4. Fruits into baskets
    
    🔑 KEY CONCEPT:
    Use HashMap to track window contents
    Expand window with right pointer
    Shrink window with left pointer when invalid
    
    ⏱️  Time: O(n) | Space: O(k) where k = window size
    
    📝 DRY RUN - LONGEST SUBSTRING WITHOUT REPEATING:
    s = "abcabcbb"
    
    Goal: Longest substring without repeating characters
    
    char_map = {} (char → count in window)
    left = 0, max_len = 0
    
    right=0, char='a':
      char_map = {a: 1}
      No duplicates, max_len = 1
    
    right=1, char='b':
      char_map = {a: 1, b: 1}
      No duplicates, max_len = 2
    
    right=2, char='c':
      char_map = {a: 1, b: 1, c: 1}
      No duplicates, max_len = 3
    
    right=3, char='a':
      char_map = {a: 2, b: 1, c: 1}
      Duplicate 'a'! Shrink window:
      Remove left=0 ('a'): char_map = {a: 1, b: 1, c: 1}
      left = 1
      max_len = 3
    
    right=4, char='b':
      char_map = {a: 1, b: 2, c: 1}
      Duplicate 'b'! Shrink window:
      Remove left=1 ('b'): char_map = {a: 1, b: 1, c: 1}
      left = 2
      max_len = 3
    
    Continue...
    Final max_len = 3 ✓
    Substring: "abc"
    
    🎯 TEMPLATE TO MEMORIZE:
    
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Expand window
        char_map[s[right]] = char_map.get(s[right], 0) + 1
        
        # Shrink window if invalid
        while condition_violated:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1
        
        # Update result
        max_len = max(max_len, right - left + 1)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 3: Longest Substring Without Repeating (medium) ⭐⭐⭐
    - LeetCode 340: Longest Substring K Distinct (medium) ⭐⭐⭐
    - LeetCode 76: Minimum Window Substring (hard) ⭐⭐⭐
    - LeetCode 904: Fruit Into Baskets (medium) ⭐⭐
    - LeetCode 424: Longest Repeating Character Replacement (medium) ⭐⭐
    - LeetCode 438: Find All Anagrams (medium) ⭐⭐⭐
    """
    
    def length_of_longest_substring(self, s: str) -> int:
        """
        LeetCode 3: Longest Substring Without Repeating Characters
        
        🔑 KEY: Sliding window with HashMap
        """
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Add character to window
            char = s[right]
            char_map[char] = char_map.get(char, 0) + 1
            
            # Shrink window if duplicate
            while char_map[char] > 1:
                char_map[s[left]] -= 1
                left += 1
            
            # Update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        """
        LeetCode 340: Longest Substring with At Most K Distinct Characters
        
        🔑 KEY: Shrink when distinct characters > k
        
        📝 EXAMPLE:
        s = "eceba", k = 2
        
        Window: e → ec → ece
        At 'b': eceb has 3 distinct (e,c,b) > 2
        Shrink: remove 'e' → ceb (3 distinct still)
        Shrink: remove 'c' → eb (2 distinct) ✓
        
        Max = 3 ("ece")
        """
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Expand window
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            
            # Shrink if too many distinct
            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
            
            # Update max
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    
    def min_window(self, s: str, t: str) -> str:
        """
        LeetCode 76: Minimum Window Substring
        
        🔑 HARD! But uses same sliding window + HashMap
        
        📝 ALGORITHM:
        1. Count characters needed from t
        2. Expand window until all characters found
        3. Shrink window while still valid
        4. Track minimum window
        """
        if not t or not s:
            return ""
        
        from collections import Counter
        need = Counter(t)
        have = {}
        
        # Track how many characters we've satisfied
        required = len(need)
        formed = 0
        
        left = 0
        min_len = float('inf')
        min_window = (0, 0)
        
        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1
            
            # Check if this character satisfies requirement
            if char in need and have[char] == need[char]:
                formed += 1
            
            # Try to shrink window
            while formed == required and left <= right:
                # Update result if smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)
                
                # Remove leftmost character
                char = s[left]
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    formed -= 1
                
                left += 1
        
        l, r = min_window
        return s[l:r+1] if min_len != float('inf') else ""
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: GROUPING/BUCKETING (Anagrams, Group By)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Group anagrams
    2. Group strings by pattern
    3. Group numbers by property
    4. Categorize elements
    
    🔑 KEY CONCEPT:
    Use a "key" to group related items
    HashMap: key → list of items
    
    ⏱️  Time: O(n) | Space: O(n)
    
    📝 DRY RUN - GROUP ANAGRAMS:
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    Goal: Group anagrams together
    
    Key idea: Anagrams have same sorted characters
    "eat" sorted → "aet"
    "tea" sorted → "aet"
    Same key! They're anagrams.
    
    groups = {} (sorted_str → list of original strings)
    
    "eat" → key "aet":
      groups = {"aet": ["eat"]}
    
    "tea" → key "aet":
      groups = {"aet": ["eat", "tea"]}
    
    "tan" → key "ant":
      groups = {"aet": ["eat", "tea"], "ant": ["tan"]}
    
    "ate" → key "aet":
      groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
    
    "nat" → key "ant":
      groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
    
    "bat" → key "abt":
      groups = {"aet": ["eat", "tea", "ate"], 
                "ant": ["tan", "nat"], 
                "abt": ["bat"]}
    
    Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]] ✓
    
    🎯 TEMPLATE TO MEMORIZE:
    
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for item in items:
        # Generate key (e.g., sorted string, pattern, etc.)
        key = generate_key(item)
        groups[key].append(item)
    
    return list(groups.values())
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 49: Group Anagrams (medium) ⭐⭐⭐
    - LeetCode 890: Find and Replace Pattern (medium) ⭐⭐
    - LeetCode 249: Group Shifted Strings (medium) ⭐⭐
    - LeetCode 599: Minimum Index Sum of Two Lists (easy) ⭐
    """
    
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        LeetCode 49: Group Anagrams
        
        🔑 KEY: Use sorted string as key
        
        Alternative: Use character count as key
        e.g., "aab" → (2,1,0,0,...) for a,b,c,...
        """
        from collections import defaultdict
        
        groups = defaultdict(list)
        
        for s in strs:
            # Use sorted string as key
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
    
    
    def find_and_replace_pattern(self, words: List[str], pattern: str) -> List[str]:
        """
        LeetCode 890: Find and Replace Pattern
        
        🔑 KEY: Generate pattern signature
        
        📝 EXAMPLE:
        word = "abb", pattern = "mee"
        
        Mapping: a→m, b→e, b→e
        Pattern matches! ✓
        
        Signature for pattern "mee": "0 1 1"
        Signature for word "abb": "0 1 1"
        Same! Match!
        """
        def get_pattern(word):
            # Map each char to its first occurrence index
            mapping = {}
            pattern = []
            for char in word:
                if char not in mapping:
                    mapping[char] = len(mapping)
                pattern.append(mapping[char])
            return tuple(pattern)
        
        target_pattern = get_pattern(pattern)
        result = []
        
        for word in words:
            if get_pattern(word) == target_pattern:
                result.append(word)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: HASHMAP FOR CACHING/MEMOIZATION
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Cache expensive computations
    2. Fibonacci with memoization
    3. DP problems
    4. Avoid recomputation
    
    🔑 KEY CONCEPT:
    Store results of expensive operations
    Check cache before recomputing
    
    ⏱️  Time: O(n) instead of O(2^n) | Space: O(n)
    
    📝 NOTE: This was covered in Recursion guide!
    
    🎯 TEMPLATE:
    
    memo = {}
    
    def helper(params):
        if params in memo:
            return memo[params]
        
        # Compute result
        result = expensive_computation(params)
        
        memo[params] = result
        return result
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 70: Climbing Stairs (easy) ⭐⭐⭐
    - LeetCode 509: Fibonacci (easy) ⭐⭐
    - LeetCode 198: House Robber (medium) ⭐⭐⭐
    - LeetCode 139: Word Break (medium) ⭐⭐⭐
    """
    
    # Refer to Recursion/DP guides for implementations!
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: HASHMAP + TWO POINTERS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. 3Sum, 4Sum problems
    2. Find triplets with sum
    3. Container problems
    
    🔑 KEY CONCEPT:
    Combine HashMap for fast lookup
    With two pointers for pair finding
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 15: 3Sum (medium) ⭐⭐⭐
    - LeetCode 18: 4Sum (medium) ⭐⭐
    - LeetCode 259: 3Sum Smaller (medium) ⭐⭐
    """
    
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode 15: 3Sum
        
        🔑 KEY: Fix one element, use two pointers for pair
        
        📝 ALGORITHM:
        1. Sort array
        2. For each num, find pair that sums to -num
        3. Use two pointers for the pair
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointers for remaining pair
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                curr_sum = nums[left] + nums[right]
                
                if curr_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result


# ═══════════════════════════════════════════════════════════════════════════
# HASHSET PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

class HashSetPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: DEDUPLICATION/UNIQUENESS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Remove duplicates
    2. Count unique elements
    3. Check for uniqueness
    4. Find unique elements
    
    🔑 KEY CONCEPT:
    Set automatically handles uniqueness
    
    ⏱️  Time: O(n) | Space: O(n)
    
    🎯 TEMPLATE:
    
    # Remove duplicates:
    unique = list(set(nums))
    
    # Count unique:
    unique_count = len(set(nums))
    
    # Check if all unique:
    is_unique = len(nums) == len(set(nums))
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 217: Contains Duplicate (easy) ⭐⭐
    - LeetCode 268: Missing Number (easy) ⭐⭐
    - LeetCode 287: Find Duplicate Number (medium) ⭐⭐
    - LeetCode 442: Find All Duplicates (medium) ⭐⭐
    """
    
    def contains_duplicate_set(self, nums: List[int]) -> bool:
        """
        LeetCode 217: Contains Duplicate (Set version)
        
        🔑 SIMPLE: Compare lengths
        """
        return len(nums) != len(set(nums))
    
    
    def missing_number(self, nums: List[int]) -> int:
        """
        LeetCode 268: Missing Number
        
        🔑 KEY: Use set for O(1) lookup
        Or: Use math (sum formula)
        """
        # Method 1: Set
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
        
        # Method 2: Math (better!)
        # return len(nums) * (len(nums) + 1) // 2 - sum(nums)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: FAST LOOKUP/CONTAINS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Check if element exists
    2. Validate against list
    3. Quick membership test
    
    🔑 KEY CONCEPT:
    O(1) contains check vs O(n) for list
    
    🎯 TEMPLATE:
    
    # Convert to set for fast lookup
    lookup_set = set(valid_items)
    
    for item in items:
        if item in lookup_set:  # O(1) instead of O(n)
            # process
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 202: Happy Number (easy) ⭐⭐
    - LeetCode 349: Intersection of Two Arrays (easy) ⭐⭐
    - LeetCode 350: Intersection of Two Arrays II (easy) ⭐⭐
    """
    
    def is_happy(self, n: int) -> bool:
        """
        LeetCode 202: Happy Number
        
        🔑 KEY: Use set to detect cycle
        
        📝 EXAMPLE:
        n = 19
        
        1² + 9² = 82
        8² + 2² = 68
        6² + 8² = 100
        1² + 0² + 0² = 1 ✓ Happy!
        
        n = 2
        2² = 4
        4² = 16
        1² + 6² = 37
        3² + 7² = 58
        5² + 8² = 89
        8² + 9² = 145
        1² + 4² + 5² = 42
        4² + 2² = 20
        2² + 0² = 4 ← Cycle! Not happy
        """
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return n == 1
    
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        LeetCode 349: Intersection of Two Arrays
        
        🔑 SIMPLE: Use set intersection
        """
        return list(set(nums1) & set(nums2))
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: SET OPERATIONS (Union/Intersection/Difference)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Find common elements
    2. Find unique to one set
    3. Combine sets
    4. Set arithmetic
    
    🔑 KEY OPERATIONS:
    - Union: set1 | set2 (all elements)
    - Intersection: set1 & set2 (common elements)
    - Difference: set1 - set2 (in set1 but not set2)
    - Symmetric Difference: set1 ^ set2 (in one but not both)
    
    🎯 TEMPLATE:
    
    set1 = set(nums1)
    set2 = set(nums2)
    
    union = set1 | set2
    intersection = set1 & set2
    diff = set1 - set2
    sym_diff = set1 ^ set2
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 349: Intersection (easy) ⭐⭐
    - LeetCode 350: Intersection II (easy) ⭐⭐
    """
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: CYCLE DETECTION
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Detect cycles in linked list
    2. Detect cycles in sequences
    3. Track visited states
    
    🔑 KEY CONCEPT:
    If we see the same value twice, there's a cycle
    
    🎯 TEMPLATE:
    
    visited = set()
    current = start
    
    while current not in visited:
        visited.add(current)
        current = next_state(current)
    
    # If loop exits, found cycle at 'current'
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 141: Linked List Cycle (easy) ⭐⭐⭐
    - LeetCode 142: Linked List Cycle II (medium) ⭐⭐
    - LeetCode 202: Happy Number (easy) ⭐⭐
    """
    
    def has_cycle_set(self, head) -> bool:
        """
        LeetCode 141: Linked List Cycle (Set version)
        
        🔑 NOTE: Two-pointer is better O(1) space
        But set version is simpler to understand
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        
        return False
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: SLIDING WINDOW WITH SET
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASES:
    1. Longest substring without repeating
    2. Longest consecutive sequence
    3. Window with unique elements
    
    🔑 KEY CONCEPT:
    Use set to track unique elements in window
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 3: Longest Substring (medium) ⭐⭐⭐
    - LeetCode 128: Longest Consecutive (medium) ⭐⭐⭐
    - LeetCode 395: Longest Substring K Repeating (medium) ⭐⭐
    """
    
    def length_of_longest_substring_set(self, s: str) -> int:
        """
        LeetCode 3: Longest Substring (Set version)
        
        🔑 KEY: Set for O(1) duplicate check
        """
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Shrink window if duplicate
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        LeetCode 128: Longest Consecutive Sequence
        
        🔑 KEY: Use set for O(1) lookup
        
        📝 EXAMPLE:
        nums = [100, 4, 200, 1, 3, 2]
        
        Set: {100, 4, 200, 1, 3, 2}
        
        For each num, check if it's start of sequence:
        - 100: no 99, start! Check 101, 102,... (length 1)
        - 4: has 3, not start
        - 200: no 199, start! (length 1)
        - 1: no 0, start! Check 2, 3, 4 (length 4) ✓
        - 3: has 2, not start
        - 2: has 1, not start
        
        Max = 4: [1,2,3,4]
        """
        if not nums:
            return 0
        
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            # Check if start of sequence
            if num - 1 not in num_set:
                current = num
                length = 1
                
                # Count sequence length
                while current + 1 in num_set:
                    current += 1
                    length += 1
                
                max_len = max(max_len, length)
        
        return max_len


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 50 HASHMAP/HASHSET PROBLEMS (Ranked by Importance)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 TIER 1: ABSOLUTE MUST-KNOW (Top 10)
═══════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LeetCode 1: Two Sum (easy)
   - Pattern: Complement Lookup
   - Why: #1 MOST ASKED INTERVIEW QUESTION!
   - Difficulty: 10/10 importance
   - Company: ALL (Google, Amazon, Facebook, Microsoft, Apple)

2. ⭐⭐⭐ LeetCode 49: Group Anagrams (medium)
   - Pattern: Grouping/Bucketing
   - Why: Very common, tests HashMap mastery
   - Difficulty: 9/10 importance
   - Company: Amazon, Google, Facebook

3. ⭐⭐⭐ LeetCode 3: Longest Substring Without Repeating (medium)
   - Pattern: Sliding Window + HashMap/Set
   - Why: Top sliding window problem
   - Difficulty: 9/10 importance
   - Company: Amazon, Microsoft, Facebook, Apple

4. ⭐⭐⭐ LeetCode 560: Subarray Sum Equals K (medium)
   - Pattern: Prefix Sum + HashMap
   - Why: Most important prefix sum problem
   - Difficulty: 10/10 importance
   - Company: Facebook, Google, Amazon

5. ⭐⭐⭐ LeetCode 146: LRU Cache (medium)
   - Pattern: HashMap + LinkedList
   - Why: Design problem, very common
   - Difficulty: 10/10 importance
   - Company: Google, Amazon, Facebook, Microsoft

6. ⭐⭐⭐ LeetCode 76: Minimum Window Substring (hard)
   - Pattern: Sliding Window + HashMap
   - Why: Hardest sliding window, very common
   - Difficulty: 9/10 importance
   - Company: Facebook, Amazon, Google

7. ⭐⭐⭐ LeetCode 347: Top K Frequent Elements (medium)
   - Pattern: Frequency Counter + Heap
   - Why: Frequency counting is super common
   - Difficulty: 8/10 importance
   - Company: Amazon, Yelp, Bloomberg

8. ⭐⭐⭐ LeetCode 128: Longest Consecutive Sequence (medium)
   - Pattern: HashSet Lookup
   - Why: Clever set usage
   - Difficulty: 8/10 importance
   - Company: Google, Facebook

9. ⭐⭐⭐ LeetCode 15: 3Sum (medium)
   - Pattern: HashMap + Two Pointers
   - Why: Extension of Two Sum
   - Difficulty: 8/10 importance
   - Company: Facebook, Amazon, Microsoft

10. ⭐⭐⭐ LeetCode 438: Find All Anagrams (medium)
    - Pattern: Sliding Window + HashMap
    - Why: Common string problem
    - Difficulty: 8/10 importance
    - Company: Amazon, Facebook


🔥🔥 TIER 2: VERY IMPORTANT (11-25)
═══════════════════════════════════════════════════════════════════════════

11. ⭐⭐ LeetCode 217: Contains Duplicate (easy)
    - Pattern: HashSet
    - Why: Simplest set problem
    - Difficulty: 6/10 importance

12. ⭐⭐ LeetCode 219: Contains Duplicate II (easy)
    - Pattern: HashMap + Index
    - Why: Extension with distance
    - Difficulty: 7/10 importance

13. ⭐⭐⭐ LeetCode 1679: Max K-Sum Pairs (medium)
    - Pattern: Complement Lookup
    - Why: Two Sum variant
    - Difficulty: 7/10 importance

14. ⭐⭐ LeetCode 454: 4Sum II (medium)
    - Pattern: HashMap Groups
    - Why: Multiple array combination
    - Difficulty: 7/10 importance

15. ⭐⭐⭐ LeetCode 974: Subarray Sums Divisible by K (medium)
    - Pattern: Prefix Sum + HashMap
    - Why: Modulo arithmetic
    - Difficulty: 8/10 importance

16. ⭐⭐⭐ LeetCode 523: Continuous Subarray Sum (medium)
    - Pattern: Prefix Sum + HashMap
    - Why: Similar to 974
    - Difficulty: 7/10 importance

17. ⭐⭐⭐ LeetCode 525: Contiguous Array (medium)
    - Pattern: Prefix Sum + HashMap
    - Why: Binary array trick
    - Difficulty: 7/10 importance

18. ⭐⭐ LeetCode 169: Majority Element (easy)
    - Pattern: Frequency Counter
    - Why: Can also use Boyer-Moore
    - Difficulty: 6/10 importance

19. ⭐⭐ LeetCode 387: First Unique Character (easy)
    - Pattern: Frequency Counter
    - Why: Common string problem
    - Difficulty: 6/10 importance

20. ⭐⭐ LeetCode 383: Ransom Note (easy)
    - Pattern: Frequency Counter
    - Why: Character matching
    - Difficulty: 5/10 importance

21. ⭐⭐ LeetCode 242: Valid Anagram (easy)
    - Pattern: Frequency Counter
    - Why: Foundation for anagrams
    - Difficulty: 6/10 importance

22. ⭐⭐ LeetCode 202: Happy Number (easy)
    - Pattern: Cycle Detection
    - Why: Clever set usage
    - Difficulty: 6/10 importance

23. ⭐⭐ LeetCode 349: Intersection of Arrays (easy)
    - Pattern: Set Operations
    - Why: Set intersection
    - Difficulty: 5/10 importance

24. ⭐⭐ LeetCode 141: Linked List Cycle (easy)
    - Pattern: Cycle Detection
    - Why: Can use set or two-pointer
    - Difficulty: 7/10 importance

25. ⭐⭐⭐ LeetCode 340: Longest Substring K Distinct (medium)
    - Pattern: Sliding Window + HashMap
    - Why: Extension of problem 3
    - Difficulty: 7/10 importance


🔥 TIER 3: IMPORTANT (26-40)
═══════════════════════════════════════════════════════════════════════════

26. ⭐⭐ LeetCode 451: Sort Characters By Frequency (medium)
    - Pattern: Frequency Counter
    - Difficulty: 6/10 importance

27. ⭐ LeetCode 1512: Number of Good Pairs (easy)
    - Pattern: Frequency Counter
    - Difficulty: 5/10 importance

28. ⭐⭐ LeetCode 2006: Count Pairs Difference K (easy)
    - Pattern: Complement Lookup
    - Difficulty: 6/10 importance

29. ⭐ LeetCode 1: Two Sum (easy) - already listed
30. ⭐⭐ LeetCode 904: Fruit Into Baskets (medium)
    - Pattern: Sliding Window
    - Difficulty: 6/10 importance

31. ⭐⭐ LeetCode 424: Longest Repeating Replacement (medium)
    - Pattern: Sliding Window
    - Difficulty: 6/10 importance

32. ⭐⭐ LeetCode 290: Word Pattern (easy)
    - Pattern: Bijection Mapping
    - Difficulty: 5/10 importance

33. ⭐⭐ LeetCode 205: Isomorphic Strings (easy)
    - Pattern: Bijection Mapping
    - Difficulty: 5/10 importance

34. ⭐ LeetCode 268: Missing Number (easy)
    - Pattern: Set/Math
    - Difficulty: 5/10 importance

35. ⭐⭐ LeetCode 41: First Missing Positive (hard)
    - Pattern: Set/Index Marking
    - Difficulty: 7/10 importance

36. ⭐⭐ LeetCode 18: 4Sum (medium)
    - Pattern: HashMap + Two Pointers
    - Difficulty: 6/10 importance

37. ⭐⭐ LeetCode 437: Path Sum III (medium)
    - Pattern: Prefix Sum + HashMap (Tree!)
    - Difficulty: 7/10 importance

38. ⭐ LeetCode 359: Logger Rate Limiter (easy)
    - Pattern: HashMap + Timestamp
    - Difficulty: 5/10 importance

39. ⭐ LeetCode 1160: Find Words Formed by Characters (easy)
    - Pattern: Frequency Counter
    - Difficulty: 4/10 importance

40. ⭐⭐ LeetCode 890: Find and Replace Pattern (medium)
    - Pattern: Pattern Matching
    - Difficulty: 5/10 importance


TIER 4: ADVANCED (41-50)
═══════════════════════════════════════════════════════════════════════════

41. ⭐ LeetCode 1711: Count Good Meals (medium)
42. ⭐ LeetCode 350: Intersection II (easy)
43. ⭐ LeetCode 442: Find All Duplicates (medium)
44. ⭐ LeetCode 287: Find Duplicate Number (medium)
45. ⭐ LeetCode 249: Group Shifted Strings (medium)
46. ⭐ LeetCode 599: Minimum Index Sum (easy)
47. ⭐ LeetCode 1346: Check N and Double (easy)
48. ⭐ LeetCode 1: Two Sum variations
49. ⭐ LeetCode 930: Binary Subarrays With Sum (medium)
50. ⭐ LeetCode 1248: Count Nice Subarrays (medium)


═══════════════════════════════════════════════════════════════════════════
📊 PROBLEM BREAKDOWN:
═══════════════════════════════════════════════════════════════════════════

By Difficulty:
- Easy: 20 problems
- Medium: 25 problems
- Hard: 5 problems

By Pattern:
- Complement Lookup: 8 problems ⭐ MOST IMPORTANT!
- Frequency Counter: 10 problems
- Sliding Window + HashMap: 8 problems
- Prefix Sum + HashMap: 6 problems
- HashSet Operations: 6 problems
- Grouping: 4 problems
- Others: 8 problems


═══════════════════════════════════════════════════════════════════════════
🎯 4-WEEK STUDY PLAN:
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - FOUNDATION:
────────────────────────────────────────────────────────────────────────
Day 1: Pattern 1 - Complement Lookup
       - 1 (Two Sum) ⚠️ CRITICAL!
       - 1679 (Max K-Sum Pairs)

Day 2: Pattern 2 - Frequency Counter
       - 169 (Majority Element)
       - 387 (First Unique Char)
       - 383 (Ransom Note)

Day 3: Pattern 3 - HashMap + Index
       - 217 (Contains Duplicate)
       - 219 (Contains Duplicate II)

Day 4: HashSet Basics
       - 202 (Happy Number)
       - 349 (Intersection)
       - 268 (Missing Number)

Day 5: Review + Practice
       - Redo 1 (Two Sum) until you can do it in 3 minutes
       - Template memorization

Day 6-7: Extra practice from Week 1


WEEK 2 - ADVANCED HASHMAP:
────────────────────────────────────────────────────────────────────────
Day 1: Grouping Pattern
       - 49 (Group Anagrams) ⚠️ IMPORTANT!
       - 242 (Valid Anagram)

Day 2: Complement Variations
       - 2006 (Count Pairs Difference K)
       - 454 (4Sum II)

Day 3: Frequency Advanced
       - 347 (Top K Frequent) ⚠️
       - 451 (Sort by Frequency)

Day 4: HashMap + Two Pointers
       - 15 (3Sum) ⚠️
       - 18 (4Sum)

Day 5-7: Review all patterns + Practice


WEEK 3 - SLIDING WINDOW:
────────────────────────────────────────────────────────────────────────
Day 1: Basic Sliding Window
       - 3 (Longest Substring) ⚠️⚠️ CRITICAL!

Day 2: Sliding Window + HashMap
       - 340 (K Distinct Characters)
       - 904 (Fruit Into Baskets)

Day 3: Advanced Sliding Window
       - 76 (Minimum Window) ⚠️⚠️ HARD!
       - 438 (Find Anagrams)

Day 4: Sliding Window Practice
       - 424 (Longest Repeating)

Day 5-7: Master all sliding window problems


WEEK 4 - PREFIX SUM & ADVANCED:
────────────────────────────────────────────────────────────────────────
Day 1: Prefix Sum + HashMap
       - 560 (Subarray Sum K) ⚠️⚠️ CRITICAL!
       - 974 (Divisible by K)

Day 2: Prefix Sum Advanced
       - 523 (Continuous Subarray)
       - 525 (Contiguous Array)

Day 3: HashSet Advanced
       - 128 (Longest Consecutive) ⚠️
       - 141 (Cycle Detection)

Day 4: Design Problems
       - 146 (LRU Cache) ⚠️⚠️ HARD!

Day 5-7: COMPREHENSIVE REVIEW
       - Redo all TIER 1 problems (1-10)
       - Practice recognition keywords
       - Template review


═══════════════════════════════════════════════════════════════════════════
💡 RECOGNITION GUIDE:
═══════════════════════════════════════════════════════════════════════════

KEYWORD → PATTERN → DATA STRUCTURE:
──────────────────────────────────────────────────────────────────────────

"find two/pair that sum to"
→ Complement Lookup
→ HashMap (value → index/count)

"count frequency" / "most/least frequent"
→ Frequency Counter
→ HashMap (element → count)

"group by" / "anagrams" / "categorize"
→ Grouping/Bucketing
→ HashMap (key → list)

"longest substring" / "window"
→ Sliding Window
→ HashMap or HashSet

"subarray sum" / "continuous"
→ Prefix Sum
→ HashMap (prefix_sum → count/index)

"unique" / "duplicate" / "distinct"
→ Uniqueness Check
→ HashSet

"contains" / "exists" / "membership"
→ Fast Lookup
→ HashSet

"intersection" / "union" / "common"
→ Set Operations
→ HashSet

"cycle" / "visited" / "seen"
→ Cycle Detection
→ HashSet

"first/last occurrence"
→ Index Tracking
→ HashMap (value → index)


═══════════════════════════════════════════════════════════════════════════
🎓 COMPANY-SPECIFIC FOCUS:
═══════════════════════════════════════════════════════════════════════════

Amazon: 1, 3, 49, 347, 1679, 438, 15
Google: 1, 76, 560, 49, 128, 3, 146
Facebook: 1, 560, 76, 3, 438, 15, 49
Microsoft: 1, 3, 15, 146, 347, 1679
Apple: 1, 3, 49, 347, 169


If targeting FAANG:
MUST master: 1, 3, 49, 560, 76, 146, 347, 128


═══════════════════════════════════════════════════════════════════════════
🔑 MASTER TEMPLATES (MEMORIZE THESE!):
═══════════════════════════════════════════════════════════════════════════

TEMPLATE 1: Complement Lookup
──────────────────────────────────────────────────────────────────────────
# Find indices:
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i

# Count/max pairs:
freq = {}
count = 0
for num in nums:
    complement = target - num
    if complement in freq and freq[complement] > 0:
        count += 1
        freq[complement] -= 1
    else:
        freq[num] = freq.get(num, 0) + 1


TEMPLATE 2: Frequency Counter
──────────────────────────────────────────────────────────────────────────
# Basic count:
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Or use Counter:
from collections import Counter
freq = Counter(items)

# Find max frequency:
max_freq_item = max(freq.keys(), key=freq.get)


TEMPLATE 3: Sliding Window + HashMap
──────────────────────────────────────────────────────────────────────────
char_map = {}
left = 0
result = 0

for right in range(len(s)):
    # Expand window
    char_map[s[right]] = char_map.get(s[right], 0) + 1
    
    # Shrink window if invalid
    while condition_violated:
        char_map[s[left]] -= 1
        if char_map[s[left]] == 0:
            del char_map[s[left]]
        left += 1
    
    # Update result
    result = max(result, right - left + 1)


TEMPLATE 4: Prefix Sum + HashMap
──────────────────────────────────────────────────────────────────────────
count = 0
curr_sum = 0
prefix_map = {0: 1}

for num in nums:
    curr_sum += num
    target = curr_sum - k
    count += prefix_map.get(target, 0)
    prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1


TEMPLATE 5: Grouping/Bucketing
──────────────────────────────────────────────────────────────────────────
from collections import defaultdict

groups = defaultdict(list)

for item in items:
    key = generate_key(item)  # e.g., sorted string
    groups[key].append(item)

return list(groups.values())


TEMPLATE 6: HashSet Uniqueness
──────────────────────────────────────────────────────────────────────────
# Check duplicates:
return len(nums) != len(set(nums))

# Fast lookup:
lookup_set = set(valid_items)
for item in items:
    if item in lookup_set:  # O(1)
        process(item)

# Cycle detection:
visited = set()
while current not in visited:
    visited.add(current)
    current = next(current)


═══════════════════════════════════════════════════════════════════════════
🚀 PRO TIPS:
═══════════════════════════════════════════════════════════════════════════

1. HASHMAP vs HASHSET Decision:
   - Need to STORE/MAP something? → HashMap
   - Just need YES/NO existence? → HashSet
   - Need to COUNT? → HashMap
   - Need to DEDUPLICATE? → HashSet

2. Common mistakes:
   ❌ Using list when set is better (O(n) vs O(1) lookup)
   ❌ Forgetting to check if key exists before accessing
   ❌ Not handling default values (use .get(key, default))
   ❌ Modifying dict while iterating
   ❌ Not using Counter when counting frequencies

3. Python-specific tips:
   ✅ Use Counter for frequency counting
   ✅ Use defaultdict to avoid KeyError
   ✅ Use .get(key, default) for safe access
   ✅ Set operations: & (intersection), | (union), - (difference)

4. Template selection:
   - Two numbers that sum to K? → Complement Lookup
   - Count occurrences? → Frequency Counter
   - Variable window? → Sliding Window + HashMap
   - Subarray sum? → Prefix Sum + HashMap
   - Group items? → Grouping with HashMap
   - Just check existence? → HashSet

5. Interview strategy:
   1. Identify the pattern from keywords
   2. Choose HashMap vs HashSet
   3. Select appropriate template
   4. Walk through example
   5. Code using template
   6. Test edge cases

6. Edge cases to test:
   - Empty input
   - Single element
   - All same elements
   - No solution exists
   - Multiple solutions


═══════════════════════════════════════════════════════════════════════════
✅ PROGRESS CHECKLIST:
═══════════════════════════════════════════════════════════════════════════

Week 1 - Foundation:
□ 1: Two Sum ⚠️⚠️⚠️ MUST MASTER!
□ 1679: Max K-Sum Pairs ⚠️
□ 169: Majority Element
□ 387: First Unique Char
□ 217: Contains Duplicate
□ 219: Contains Duplicate II
□ 202: Happy Number
□ 349: Intersection

Week 2 - Advanced:
□ 49: Group Anagrams ⚠️⚠️
□ 242: Valid Anagram
□ 2006: Count Pairs Difference
□ 454: 4Sum II
□ 347: Top K Frequent ⚠️⚠️
□ 15: 3Sum ⚠️⚠️

Week 3 - Sliding Window:
□ 3: Longest Substring ⚠️⚠️⚠️ CRITICAL!
□ 340: K Distinct Characters ⚠️
□ 76: Minimum Window ⚠️⚠️⚠️ HARD!
□ 438: Find Anagrams ⚠️⚠️
□ 904: Fruit Into Baskets

Week 4 - Advanced:
□ 560: Subarray Sum K ⚠️⚠️⚠️ CRITICAL!
□ 974: Divisible by K ⚠️⚠️
□ 523: Continuous Subarray ⚠️
□ 525: Contiguous Array ⚠️
□ 128: Longest Consecutive ⚠️⚠️
□ 146: LRU Cache ⚠️⚠️⚠️ HARD!

🎉 Completed all? You're a HashMap/HashSet Master!


═══════════════════════════════════════════════════════════════════════════
🎯 YOU'RE READY FOR INTERVIEWS WHEN:
═══════════════════════════════════════════════════════════════════════════

✅ Can solve LeetCode 1 in under 3 minutes
✅ Can solve LeetCode 3 in under 15 minutes
✅ Can solve LeetCode 49 in under 10 minutes
✅ Can solve LeetCode 560 in under 10 minutes
✅ Recognize pattern from problem description instantly
✅ Know when to use HashMap vs HashSet
✅ Can recite complement lookup template from memory
✅ Can recite sliding window template from memory
✅ Understand all 6 master templates
✅ Can explain why each pattern works


═══════════════════════════════════════════════════════════════════════════
🔑 FINAL REMINDERS:
═══════════════════════════════════════════════════════════════════════════

1. THE MOST IMPORTANT PATTERNS:
   - Complement Lookup (Two Sum)
   - Sliding Window + HashMap
   - Prefix Sum + HashMap
   - Frequency Counter

2. Master these 5 problems first:
   - LeetCode 1 (Two Sum)
   - LeetCode 3 (Longest Substring)
   - LeetCode 49 (Group Anagrams)
   - LeetCode 560 (Subarray Sum K)
   - LeetCode 146 (LRU Cache)

3. Recognition is key:
   - Keywords → Pattern → Template
   - Practice until automatic
   - Templates save time in interviews

4. HashMap vs HashSet:
   - Need values/counts? → HashMap
   - Just existence? → HashSet
   - When in doubt, HashMap is more flexible

5. Common combinations:
   - HashMap + Sliding Window (VERY COMMON!)
   - HashMap + Prefix Sum (VERY COMMON!)
   - HashMap + Two Pointers
   - HashSet + Cycle Detection

6. Interview success formula:
   1. Recognize pattern (keywords!)
   2. Choose right data structure
   3. Apply template
   4. Test thoroughly

Remember: HashMap/HashSet problems are the MOST common in interviews!
Master these patterns → You'll ace 40% of interview questions! 🚀

Good luck! You've got this! 💪
"""


if __name__ == "__main__":
    print("🧪 Testing HashMap & HashSet Patterns...\n")
    
    hm = HashMapPatterns()
    hs = HashSetPatterns()
    
    # Test Two Sum
    assert hm.two_sum([2, 7, 11, 15], 9) == [0, 1]
    print("✅ Two Sum: Passed")
    
    # Test Max K-Sum Pairs
    assert hm.max_operations([1, 2, 3, 4], 5) == 2
    print("✅ Max K-Sum Pairs: Passed")
    
    # Test Group Anagrams
    result = hm.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(result) == 3
    print("✅ Group Anagrams: Passed")
    
    # Test Longest Substring
    assert hm.length_of_longest_substring("abcabcbb") == 3
    print("✅ Longest Substring: Passed")
    
    # Test Contains Duplicate
    assert hs.contains_duplicate_set([1, 2, 3, 1]) == True
    print("✅ Contains Duplicate: Passed")
    
    # Test Happy Number
    assert hs.is_happy(19) == True
    print("✅ Happy Number: Passed")
    
    # Test Longest Consecutive
    assert hs.longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    print("✅ Longest Consecutive: Passed")
    
    print("\n🎉 All HashMap & HashSet patterns tested!")
    print("\n📚 MASTER THESE PATTERNS - They're in 40% of interviews!")
    print("⏰ Recommended: 4 weeks, 1 hour daily")
    print("🎯 Focus: Two Sum, Longest Substring, Subarray Sum K")