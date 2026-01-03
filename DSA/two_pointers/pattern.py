"""
═══════════════════════════════════════════════════════════════════════════════
                TWO POINTERS MASTERY GUIDE - COMPLETE (FAANG FOCUS)
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. TWO POINTERS PATTERN TYPES:
   ✅ Opposite Direction (left ← → right)
   ✅ Same Direction (slow → fast →)
   ✅ Multiple Pointers (3Sum, 4Sum)
   ✅ Partition/Sorting (Quick Select, Dutch Flag)
   ✅ Merge Operations (Sorted arrays)
   ✅ Palindrome Checking
   ✅ Sliding Window (separate but related)

2. WHEN TO USE TWO POINTERS:
   - Array is SORTED (or can be sorted)
   - Need to find pairs/triplets with certain sum
   - Need to partition or rearrange
   - Need to merge sorted arrays
   - Need to check palindrome properties
   - Need to remove duplicates in-place

3. KEY INSIGHT:
   Two pointers reduces O(n²) brute force to O(n) by:
   - Moving pointers based on conditions
   - Avoiding redundant comparisons
   - Processing elements exactly once

4. 9 ESSENTIAL PATTERNS COVERED:
   ✅ Pattern 1: Opposite Direction (Container, Trapping Water, Two Sum)
   ✅ Pattern 2: Same Direction Fast/Slow (Partition, Remove Element)
   ✅ Pattern 3: Palindrome Checking (Valid Palindrome variants)
   ✅ Pattern 4: Three Pointers (3Sum, 4Sum)
   ✅ Pattern 5: Merge Sorted Arrays (Intersection, Union)
   ✅ Pattern 6: Partition Problems (Dutch Flag, Sort Colors)
   ✅ Pattern 7: Subsequence Problems (Is Subsequence)
   ✅ Pattern 8: Reverse Operations (Reverse String, Words)
   ✅ Pattern 9: Linked List Two Pointers (Cycle, Middle - see LinkedList guide)

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Optional

class TwoPointersPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: OPPOSITE DIRECTION (Left ← → Right)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Two pointers start at opposite ends, move toward each other.
    Make decisions based on comparison of elements at both pointers.
    
    🔑 KEY INSIGHT:
    When to move which pointer?
    - If sum/area too large → move right pointer left (decrease)
    - If sum/area too small → move left pointer right (increase)
    - This greedy approach eliminates suboptimal choices
    
    💡 WHEN TO USE:
    - Array is sorted
    - Finding pairs with target sum
    - Maximizing/minimizing based on two elements
    - Container/area problems
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def opposite_pointers(arr, target):
        left, right = 0, len(arr) - 1
        
        while left < right:
            current = calculate(arr[left], arr[right])
            
            if current == target:
                return [left, right]
            elif current < target:
                left += 1   # Need larger value
            else:
                right -= 1  # Need smaller value
        
        return [-1, -1]  # Not found
    
    📊 VARIATIONS:
    - Two Sum (sorted array)
    - Container With Most Water
    - Trapping Rain Water
    - 3Sum Closest
    - Remove Duplicates from Sorted Array
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 167. Two Sum II - Input Array Is Sorted ⭐⭐⭐
    ✅ 344. Reverse String ⭐⭐
    ✅ 345. Reverse Vowels of a String ⭐
    
    Medium:
    ✅ 11. Container With Most Water ⭐⭐⭐ (TOP 10 MOST ASKED!)
    ✅ 15. 3Sum ⭐⭐⭐ (FAANG FAVORITE!)
    ✅ 16. 3Sum Closest ⭐⭐
    ✅ 75. Sort Colors ⭐⭐⭐
    
    Hard:
    ✅ 42. Trapping Rain Water ⭐⭐⭐ (GOOGLE/META FAVORITE!)
    """
    
    def twoSum_sorted_template(self, numbers: List[int], target: int) -> List[int]:
        """
        🎯 MASTER TEMPLATE: Two Sum in sorted array
        
        Find two numbers that add up to target.
        
        Algorithm:
        1. Start: left at beginning, right at end
        2. Calculate sum = numbers[left] + numbers[right]
        3. If sum == target: found!
        4. If sum < target: need larger, move left right
        5. If sum > target: need smaller, move right left
        
        Args:
            numbers: Sorted array (ascending)
            target: Target sum
        
        Returns:
            Indices [left+1, right+1] (1-indexed)
        
        Example:
            numbers = [2,7,11,15], target = 9
            output = [1,2] (2 + 7 = 9)
        
        Time: O(n) | Space: O(1)
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum < target:
                left += 1   # Need larger sum
            else:
                right -= 1  # Need smaller sum
        
        return [-1, -1]  # Not found
    
    
    def maxArea_template(self, height: List[int]) -> int:
        """
        🎯 MASTER TEMPLATE: Container With Most Water
        
        Find two lines that form container with maximum water.
        
        🔑 KEY INSIGHT:
        Area = min(height[left], height[right]) * (right - left)
        
        Greedy strategy:
        - Always move the pointer with SMALLER height
        - Why? Larger height can't increase area (limited by smaller)
        - Moving smaller height gives chance of finding taller line
        
        Args:
            height: Array of heights
        
        Returns:
            Maximum area
        
        Example:
            height = [1,8,6,2,5,4,8,3,7]
            output = 49 (between index 1 and 8)
        
        Time: O(n) | Space: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)
            
            # Move pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    
    def trap_template(self, height: List[int]) -> int:
        """
        🎯 MASTER TEMPLATE: Trapping Rain Water
        
        Calculate water trapped between bars after raining.
        
        🔑 KEY INSIGHT:
        Water at position i = min(max_left, max_right) - height[i]
        
        Two pointers approach:
        - Track left_max and right_max
        - Move pointer with smaller max (bottleneck)
        - Add trapped water as we go
        
        Args:
            height: Array of bar heights
        
        Returns:
            Total trapped water
        
        Example:
            height = [0,1,0,2,1,0,1,3,2,1,2,1]
            output = 6
        
        Time: O(n) | Space: O(1)
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                # Process left side (left is bottleneck)
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                # Process right side (right is bottleneck)
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        
        return water
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 1
    # ═══════════════════════════════════════════════════════════════════════
    
    def twoSum_LC167(self, numbers: List[int], target: int) -> List[int]:
        """
        LeetCode 167: Two Sum II - Input Array Is Sorted
        
        Find two numbers that add up to target (1-indexed).
        
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        
        DRY RUN:
        numbers = [2, 7, 11, 15], target = 9
        
        Step 1: left=0, right=3
                sum = 2 + 15 = 17 > 9
                Move right left
        
        Step 2: left=0, right=2
                sum = 2 + 11 = 13 > 9
                Move right left
        
        Step 3: left=0, right=1
                sum = 2 + 7 = 9 ✓
                return [1, 2]
        """
        return self.twoSum_sorted_template(numbers, target)
    
    
    def maxArea_LC11(self, height: List[int]) -> int:
        """
        LeetCode 11: Container With Most Water
        
        Find two lines that contain most water.
        
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        
        DRY RUN:
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        
        Step 1: left=0(1), right=8(7)
                area = min(1,7) * 8 = 8
                max_area = 8
                1 < 7, move left
        
        Step 2: left=1(8), right=8(7)
                area = min(8,7) * 7 = 49
                max_area = 49
                7 < 8, move right
        
        Continue...
        
        Result: 49 ✓
        """
        return self.maxArea_template(height)
    
    
    def trap_LC42(self, height: List[int]) -> int:
        """
        LeetCode 42: Trapping Rain Water
        
        Calculate how much water can be trapped.
        
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        
        DRY RUN:
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        
        left=0, right=11, left_max=0, right_max=0, water=0
        
        Step 1: h[0]=0 < h[11]=1
                left_max = 0, water += 0
                left = 1
        
        Step 2: h[1]=1 < h[11]=1
                left_max = 1, water += 0
                left = 2
        
        Step 3: h[2]=0 < h[11]=1
                water += 1 - 0 = 1
                left = 3
        
        Continue...
        
        Result: 6 ✓
        """
        return self.trap_template(height)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: SAME DIRECTION (Fast/Slow Pointers)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Two pointers move in same direction, typically at different speeds.
    Slow pointer marks "write position", fast pointer scans.
    
    🔑 KEY INSIGHT:
    Use slow pointer to build result in-place.
    Fast pointer explores and finds valid elements.
    
    💡 WHEN TO USE:
    - Remove elements in-place
    - Partition array
    - In-place modification without extra space
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def same_direction(arr, condition):
        slow = 0
        
        for fast in range(len(arr)):
            if condition(arr[fast]):
                arr[slow] = arr[fast]
                slow += 1
        
        return slow  # New length
    
    📊 VARIATIONS:
    - Remove Element
    - Move Zeroes
    - Remove Duplicates
    - Partition Array
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 27. Remove Element ⭐⭐⭐
    ✅ 283. Move Zeroes ⭐⭐⭐
    ✅ 26. Remove Duplicates from Sorted Array ⭐⭐⭐
    ✅ 977. Squares of a Sorted Array ⭐⭐
    
    Medium:
    ✅ 80. Remove Duplicates from Sorted Array II ⭐⭐
    ✅ 457. Circular Array Loop
    """
    
    def removeElement_template(self, nums: List[int], val: int) -> int:
        """
        🎯 MASTER TEMPLATE: Remove element in-place
        
        Remove all occurrences of val, return new length.
        
        Algorithm:
        1. Slow pointer = write position
        2. Fast pointer = read position
        3. If nums[fast] != val: write and advance slow
        4. Always advance fast
        
        Args:
            nums: Array (modified in-place)
            val: Value to remove
        
        Returns:
            New length
        
        Time: O(n) | Space: O(1)
        """
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
    
    
    def moveZeroes_template(self, nums: List[int]) -> None:
        """
        🎯 MASTER TEMPLATE: Move zeroes to end
        
        Move all 0s to end, maintain relative order of non-zeros.
        
        Algorithm:
        1. Use slow pointer for next non-zero position
        2. When fast finds non-zero, swap with slow position
        3. This naturally pushes zeros to end
        
        Args:
            nums: Array (modified in-place)
        
        Time: O(n) | Space: O(1)
        """
        slow = 0  # Position for next non-zero
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # Swap non-zero to front
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 2
    # ═══════════════════════════════════════════════════════════════════════
    
    def removeElement_LC27(self, nums: List[int], val: int) -> int:
        """
        LeetCode 27: Remove Element
        
        Remove all instances of val in-place.
        
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        
        DRY RUN:
        nums = [3, 2, 2, 3], val = 3
        
        slow = 0
        
        fast=0: nums[0]=3 == val, skip
        fast=1: nums[1]=2 != val
                nums[0] = 2, slow = 1
        fast=2: nums[2]=2 != val
                nums[1] = 2, slow = 2
        fast=3: nums[3]=3 == val, skip
        
        Result: nums = [2,2,2,3], return 2
        """
        return self.removeElement_template(nums, val)
    
    
    def moveZeroes_LC283(self, nums: List[int]) -> None:
        """
        LeetCode 283: Move Zeroes
        
        Move all 0's to end, maintain relative order.
        
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        
        DRY RUN:
        nums = [0, 1, 0, 3, 12]
        
        slow = 0
        
        fast=0: nums[0]=0, skip
        fast=1: nums[1]=1 != 0
                swap(nums[0], nums[1])
                nums = [1,0,0,3,12], slow=1
        fast=2: nums[2]=0, skip
        fast=3: nums[3]=3 != 0
                swap(nums[1], nums[3])
                nums = [1,3,0,0,12], slow=2
        fast=4: nums[4]=12 != 0
                swap(nums[2], nums[4])
                nums = [1,3,12,0,0], slow=3
        
        Result: [1,3,12,0,0] ✓
        """
        self.moveZeroes_template(nums)
    
    
    def sortedSquares_LC977(self, nums: List[int]) -> List[int]:
        """
        LeetCode 977: Squares of a Sorted Array
        
        Return sorted array of squares (nums is sorted).
        
        Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        
        🔑 APPROACH: Two pointers from both ends
        Negative numbers squared become positive and large.
        Compare absolute values from both ends, place larger square.
        
        Time: O(n) | Space: O(n) for result
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # Fill from end
        
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: PALINDROME CHECKING
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Use two pointers from both ends, move toward center.
    Check if characters match at each step.
    
    🔑 KEY INSIGHT:
    Palindrome: same forwards and backwards.
    Compare s[left] with s[right], move both inward.
    Skip non-alphanumeric if needed.
    
    💡 WHEN TO USE:
    - Check if string/array is palindrome
    - Palindrome with one deletion allowed
    - Longest palindromic substring (expand around center)
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def isPalindrome(s):
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 125. Valid Palindrome ⭐⭐⭐
    ✅ 680. Valid Palindrome II ⭐⭐⭐
    ✅ 234. Palindrome Linked List ⭐⭐
    
    Medium:
    ✅ 5. Longest Palindromic Substring ⭐⭐⭐
    ✅ 647. Palindromic Substrings ⭐⭐
    """
    
    def isPalindrome_template(self, s: str) -> bool:
        """
        🎯 MASTER TEMPLATE: Valid Palindrome
        
        Check if string is palindrome (ignore non-alphanumeric, case-insensitive).
        
        Algorithm:
        1. Two pointers from both ends
        2. Skip non-alphanumeric characters
        3. Compare characters (case-insensitive)
        4. Move both pointers inward
        
        Args:
            s: Input string
        
        Returns:
            True if palindrome
        
        Time: O(n) | Space: O(1)
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    
    def validPalindrome_template(self, s: str) -> bool:
        """
        🎯 TEMPLATE: Valid Palindrome II (one deletion allowed)
        
        Check if can be palindrome by deleting at most one character.
        
        🔑 APPROACH:
        When mismatch found, try skipping either left or right character.
        Check if remaining substring is palindrome.
        
        Args:
            s: Input string
        
        Returns:
            True if can form palindrome with <= 1 deletion
        
        Time: O(n) | Space: O(1)
        """
        def is_palindrome_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping left OR skipping right
                return (is_palindrome_range(left + 1, right) or
                        is_palindrome_range(left, right - 1))
            left += 1
            right -= 1
        
        return True
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 3
    # ═══════════════════════════════════════════════════════════════════════
    
    def isPalindrome_LC125(self, s: str) -> bool:
        """
        LeetCode 125: Valid Palindrome
        
        Check if palindrome (alphanumeric only, case-insensitive).
        
        Input: s = "A man, a plan, a canal: Panama"
        Output: True
        
        DRY RUN:
        s = "A man, a plan, a canal: Panama"
        
        Clean: "amanaplanacanalpanama"
        
        left=0(a), right=20(a): match, move both
        left=1(m), right=19(m): match, move both
        ...
        All match!
        
        Result: True ✓
        """
        return self.isPalindrome_template(s)
    
    
    def validPalindrome_LC680(self, s: str) -> bool:
        """
        LeetCode 680: Valid Palindrome II
        
        Valid palindrome by deleting at most one character.
        
        Input: s = "aba"
        Output: True
        
        Input: s = "abca"
        Output: True (delete 'c' or 'b')
        
        DRY RUN:
        s = "abca"
        
        left=0(a), right=3(a): match
        left=1(b), right=2(c): MISMATCH!
        
        Try skip left (check "ca"): not palindrome
        Try skip right (check "ab"): not palindrome
        
        Wait, let me recalculate...
        Actually "abca": delete c → "aba" ✓
        
        left=0, right=3: a==a
        left=1, right=2: b!=c
        Skip right: check s[1:3] = "bc" → not palindrome
        Skip left: check s[2:3] = "c" → palindrome ✓
        """
        return self.validPalindrome_template(s)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: THREE POINTERS (3Sum, 4Sum)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Fix one element, use two pointers for remaining elements.
    Combination of iteration + two pointers.
    
    🔑 KEY INSIGHT:
    For 3Sum:
    1. Sort array
    2. Fix first element (iterate)
    3. Use two pointers for remaining two elements
    4. Skip duplicates to avoid duplicate triplets
    
    💡 WHEN TO USE:
    - Find triplets/quadruplets with target sum
    - Avoiding duplicate combinations
    - K-sum problems (generalized)
    
    ⏱️  Time: O(n²) for 3Sum, O(n³) for 4Sum | Space: O(1) excluding output
    
    📝 GENERALIZED TEMPLATE:
    def threeSum(nums, target):
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointers for remaining
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 15. 3Sum ⭐⭐⭐ (TOP 5 MOST ASKED!)
    ✅ 16. 3Sum Closest ⭐⭐⭐
    ✅ 259. 3Sum Smaller ⭐⭐
    ✅ 18. 4Sum ⭐⭐
    
    Hard:
    ✅ 454. 4Sum II (HashMap variant)
    """
    
    def threeSum_template(self, nums: List[int]) -> List[List[int]]:
        """
        🎯 MASTER TEMPLATE: 3Sum
        
        Find all unique triplets that sum to zero.
        
        Algorithm:
        1. Sort array
        2. For each element (first in triplet):
           a. Skip duplicates
           b. Use two pointers for remaining two
           c. Find pairs that sum to -nums[i]
        3. Avoid duplicate triplets by skipping same values
        
        Args:
            nums: Array of integers
        
        Returns:
            List of unique triplets summing to 0
        
        Example:
            nums = [-1,0,1,2,-1,-4]
            output = [[-1,-1,2],[-1,0,1]]
        
        Time: O(n²) | Space: O(1) excluding output
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining two elements
            left, right = i + 1, n - 1
            target = -nums[i]  # We want nums[left] + nums[right] = target
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    
    def threeSumClosest_template(self, nums: List[int], target: int) -> int:
        """
        🎯 TEMPLATE: 3Sum Closest
        
        Find three integers whose sum is closest to target.
        
        Algorithm:
        Same as 3Sum, but track closest sum instead of exact match.
        
        Args:
            nums: Array of integers
            target: Target sum
        
        Returns:
            Sum of three integers closest to target
        
        Time: O(n²) | Space: O(1)
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if current is closer
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # Exact match
        
        return closest_sum
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 4
    # ═══════════════════════════════════════════════════════════════════════
    
    def threeSum_LC15(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode 15: 3Sum
        
        Find all unique triplets that sum to 0.
        
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        
        DRY RUN:
        nums = [-1, 0, 1, 2, -1, -4]
        After sort: [-4, -1, -1, 0, 1, 2]
        
        i=0, nums[0]=-4, target=4
        left=1, right=5: -1+2=1 < 4, left++
        left=2, right=5: -1+2=1 < 4, left++
        left=3, right=5: 0+2=2 < 4, left++
        left=4, right=5: 1+2=3 < 4, left++
        No triplet
        
        i=1, nums[1]=-1, target=1
        left=2, right=5: -1+2=1 ✓
        Add [-1,-1,2]
        Skip duplicates, left=3, right=4
        left=3, right=4: 0+1=1 ✓
        Add [-1,0,1]
        
        Result: [[-1,-1,2],[-1,0,1]] ✓
        """
        return self.threeSum_template(nums)
    
    
    def threeSumClosest_LC16(self, nums: List[int], target: int) -> int:
        """
        LeetCode 16: 3Sum Closest
        
        Find sum of three integers closest to target.
        
        Input: nums = [-1,2,1,-4], target = 1
        Output: 2 (sum of -1 + 2 + 1 = 2)
        
        DRY RUN:
        nums = [-1, 2, 1, -4]
        After sort: [-4, -1, 1, 2]
        target = 1
        
        i=0, nums[0]=-4
        left=1, right=3: -4+-1+2=-3, diff=4, closest=-3
        left=2, right=3: -4+1+2=-1, diff=2, closest=-1
        
        i=1, nums[1]=-1
        left=2, right=3: -1+1+2=2, diff=1, closest=2 ✓
        
        Result: 2 ✓
        """
        return self.threeSumClosest_template(nums, target)
    
    
    def fourSum_LC18(self, nums: List[int], target: int) -> List[List[int]]:
        """
        LeetCode 18: 4Sum
        
        Find all unique quadruplets that sum to target.
        
        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        
        🔑 APPROACH: Extension of 3Sum
        Fix two elements (two loops), use two pointers for remaining.
        
        Time: O(n³) | Space: O(1)
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers for remaining two elements
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4B: ALL SUM VARIANTS (COMPREHENSIVE FAANG COLLECTION)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Complete collection of all important Sum problems asked in FAANG.
    These are the most frequently asked two pointer problems!
    
    🔑 ALL SUM PROBLEM TYPES:
    
    1. TWO SUM FAMILY:
       ✅ Two Sum (unsorted) - HashMap O(n)
       ✅ Two Sum II (sorted) - Two Pointers O(n) ⭐⭐⭐
       ✅ Two Sum Less Than K - Two Pointers
       ✅ Two Sum BSTs - Two Pointers on BST
       ✅ Two Sum Closest - Track minimum difference
    
    2. THREE SUM FAMILY:
       ✅ 3Sum (target = 0) - Most asked! ⭐⭐⭐
       ✅ 3Sum Closest - Find closest to target ⭐⭐⭐
       ✅ 3Sum Smaller - Count triplets < target ⭐⭐
       ✅ 3Sum With Multiplicity - Handle duplicates
    
    3. FOUR SUM FAMILY:
       ✅ 4Sum - Find all quadruplets = target ⭐⭐
       ✅ 4Sum II - HashMap optimization ⭐⭐
    
    4. K-SUM GENERALIZATION:
       ✅ K-Sum problem (generalized solution)
    
    5. SUBARRAY SUM (Two Pointers):
       ✅ Subarray Sum Equals K (HashMap)
       ✅ Maximum Size Subarray Sum Equals k
       ✅ Minimum Size Subarray Sum ≥ target (Sliding Window)
    
    📊 DIFFICULTY RANKING:
    Easy: Two Sum II, Two Sum Less Than K
    Medium: 3Sum, 3Sum Closest, 3Sum Smaller, 4Sum, 4Sum II
    Hard: K-Sum (generalized)
    
    💡 LEETCODE PROBLEMS - SUM VARIANTS:
    Easy:
    ✅ 1. Two Sum ⭐⭐⭐
    ✅ 167. Two Sum II ⭐⭐⭐
    ✅ 653. Two Sum IV - BST ⭐⭐
    
    Medium:
    ✅ 15. 3Sum ⭐⭐⭐ (TOP 5 ASKED!)
    ✅ 16. 3Sum Closest ⭐⭐⭐
    ✅ 259. 3Sum Smaller ⭐⭐
    ✅ 18. 4Sum ⭐⭐
    ✅ 923. 3Sum With Multiplicity ⭐
    
    Hard:
    ✅ 454. 4Sum II ⭐⭐
    """
    
    def twoSum_unsorted_LC1(self, nums: List[int], target: int) -> List[int]:
        """
        LeetCode 1: Two Sum (MOST FAMOUS PROBLEM!)
        
        Find two numbers that add up to target (UNSORTED array).
        
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1] (indices of 2 and 7)
        
        🔑 APPROACH: HashMap (NOT two pointers since unsorted!)
        
        Algorithm:
        1. Store complement needed in HashMap
        2. For each num, check if it's in HashMap
        3. If yes, found pair!
        
        Time: O(n) | Space: O(n)
        
        ⚠️ NOTE: Two pointers only works on SORTED arrays!
        For unsorted, use HashMap approach.
        """
        seen = {}  # {value: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return [-1, -1]
    
    
    def twoSumLessThanK_LC1099(self, nums: List[int], k: int) -> int:
        """
        LeetCode 1099: Two Sum Less Than K
        
        Find maximum sum of two numbers < k.
        
        Input: nums = [34,23,1,24,75,33,54,8], k = 60
        Output: 58 (23 + 33)
        
        🔑 APPROACH: Sort + Two Pointers
        
        Algorithm:
        1. Sort array
        2. Two pointers: left=0, right=n-1
        3. If sum < k: update max, move left
        4. If sum >= k: move right (decrease sum)
        
        Time: O(n log n) | Space: O(1)
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = -1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum < k:
                max_sum = max(max_sum, current_sum)
                left += 1
            else:
                right -= 1
        
        return max_sum
    
    
    def threeSumSmaller_LC259(self, nums: List[int], target: int) -> int:
        """
        LeetCode 259: 3Sum Smaller
        
        Count triplets with sum < target.
        
        Input: nums = [-2,0,1,3], target = 2
        Output: 2 ([-2,0,1] and [-2,0,3])
        
        🔑 KEY INSIGHT:
        When nums[i] + nums[left] + nums[right] < target:
        - ALL elements between left and right work with current left!
        - Count = (right - left) triplets
        - Move left to explore more
        
        DRY RUN:
        nums = [-2, 0, 1, 3], target = 2
        After sort: [-2, 0, 1, 3]
        
        i=0, nums[0]=-2
        left=1, right=3: -2+0+3=1 < 2
            count += (3-1) = 2 triplets: (-2,0,1), (-2,0,3)
            left = 2
        left=2, right=3: -2+1+3=2 >= 2, right--
        
        i=1, nums[1]=0
        left=2, right=3: 0+1+3=4 >= 2, right--
        
        Total count = 2 ✓
        
        Time: O(n²) | Space: O(1)
        """
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < target:
                    # All elements between left and right work!
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return count
    
    
    def threeSumMultiplicity_LC923(self, arr: List[int], target: int) -> int:
        """
        LeetCode 923: 3Sum With Multiplicity
        
        Count triplets (i,j,k) where arr[i]+arr[j]+arr[k] = target.
        Count duplicates separately!
        
        Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
        Output: 20
        
        🔑 APPROACH: Two pointers with counting
        
        Key difference from regular 3Sum:
        - We COUNT occurrences, not find unique triplets
        - Use combinatorics for duplicates
        
        Time: O(n²) | Space: O(1)
        """
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        count = 0
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # Found valid triplet
                    if arr[left] == arr[right]:
                        # All elements between left and right are same
                        # Choose any 2: C(n,2) = n*(n-1)/2
                        k = right - left + 1
                        count += k * (k - 1) // 2
                        break
                    else:
                        # Count duplicates on left and right
                        left_count = right_count = 1
                        
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            left_count += 1
                            left += 1
                        
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            right_count += 1
                            right -= 1
                        
                        count += left_count * right_count
                        left += 1
                        right -= 1
        
        return count % MOD
    
    
    def fourSum_LC18_detailed(self, nums: List[int], target: int) -> List[List[int]]:
        """
        LeetCode 18: 4Sum (DETAILED WITH ALL OPTIMIZATIONS)
        
        Find all unique quadruplets that sum to target.
        
        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        
        🔑 OPTIMIZATIONS:
        1. Early termination if min sum > target
        2. Early termination if max sum < target
        3. Skip duplicates at ALL levels
        
        DRY RUN:
        nums = [1, 0, -1, 0, -2, 2], target = 0
        After sort: [-2, -1, 0, 0, 1, 2]
        
        i=0, nums[0]=-2
          j=1, nums[1]=-1, target for 2sum = 0-(-2)-(-1) = 3
            left=2, right=5: 0+2=2 < 3, left++
            left=3, right=5: 0+2=2 < 3, left++
            left=4, right=5: 1+2=3 ✓ → [-2,-1,1,2]
          
          j=2, nums[2]=0, target for 2sum = 3
            left=3, right=5: 0+2=2 < 3, left++
            left=4, right=5: 1+2=3 ✓ → [-2,0,1,2] (duplicate with i, skip)
        
        Continue...
        
        Time: O(n³) | Space: O(1)
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: smallest possible sum too large
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # Early termination: largest possible sum too small
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Early termination for inner loop
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # Two pointers for remaining two elements
                left, right = j + 1, n - 1
                two_sum_target = target - nums[i] - nums[j]
                
                while left < right:
                    current_sum = nums[left] + nums[right]
                    
                    if current_sum == two_sum_target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif current_sum < two_sum_target:
                        left += 1
                    else:
                        right -= 1
        
        return result
    
    
    def fourSumII_LC454(self, nums1: List[int], nums2: List[int], 
                         nums3: List[int], nums4: List[int]) -> int:
        """
        LeetCode 454: 4Sum II
        
        Count tuples (i,j,k,l) where:
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
        
        Input: nums1 = [1,2], nums2 = [-2,-1], 
               nums3 = [-1,2], nums4 = [0,2]
        Output: 2
        
        🔑 APPROACH: HashMap optimization (NOT two pointers!)
        
        Split into two parts:
        1. Store all sums from nums1+nums2 in HashMap
        2. For each sum from nums3+nums4, check if -(sum) exists
        
        This reduces O(n⁴) to O(n²)!
        
        Time: O(n²) | Space: O(n²)
        """
        count_map = {}
        
        # Store all sums from nums1 + nums2
        for a in nums1:
            for b in nums2:
                sum_ab = a + b
                count_map[sum_ab] = count_map.get(sum_ab, 0) + 1
        
        count = 0
        
        # Check if -(nums3[k] + nums4[l]) exists
        for c in nums3:
            for d in nums4:
                sum_cd = c + d
                target = -sum_cd
                
                if target in count_map:
                    count += count_map[target]
        
        return count
    
    
    def kSum_generalized(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        """
        🎯 GENERALIZED K-SUM SOLUTION
        
        Find all unique k-tuples that sum to target.
        
        This is the MASTER template that solves:
        - 2Sum (k=2)
        - 3Sum (k=3)
        - 4Sum (k=4)
        - Any K-Sum!
        
        Algorithm:
        1. Sort array
        2. Recursively reduce k:
           - Base case: k=2 → use two pointers
           - Recursive: fix one element, solve (k-1)-sum
        
        Time: O(n^(k-1)) | Space: O(k) for recursion
        """
        def kSumHelper(start: int, k: int, target: int, path: List[int]):
            # Base case: 2Sum with two pointers
            if k == 2:
                left, right = start, len(nums) - 1
                
                while left < right:
                    current_sum = nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append(path + [nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                return
            
            # Recursive case: reduce to (k-1)-sum
            for i in range(start, len(nums) - k + 1):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Fix nums[i], solve (k-1)-sum for remaining
                kSumHelper(i + 1, k - 1, target - nums[i], path + [nums[i]])
        
        nums.sort()
        result = []
        kSumHelper(0, k, target, [])
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: MERGE SORTED ARRAYS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Merge or find common elements in sorted arrays using two pointers.
    
    🔑 KEY INSIGHT:
    Both arrays sorted → compare current elements:
    - If arr1[i] < arr2[j]: advance i
    - If arr1[i] > arr2[j]: advance j
    - If arr1[i] == arr2[j]: found common, advance both
    
    💡 WHEN TO USE:
    - Intersection of sorted arrays
    - Union of sorted arrays
    - Merge sorted arrays
    
    ⏱️  Time: O(m+n) | Space: O(1) excluding output
    
    📝 GENERALIZED TEMPLATE:
    def intersection(arr1, arr2):
        i, j = 0, 0
        result = []
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
        
        return result
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 88. Merge Sorted Array ⭐⭐⭐
    ✅ 349. Intersection of Two Arrays ⭐⭐
    ✅ 350. Intersection of Two Arrays II ⭐⭐⭐
    
    Medium:
    ✅ 986. Interval List Intersections ⭐⭐
    """
    
    def intersect_template(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        🎯 MASTER TEMPLATE: Intersection of sorted arrays
        
        Find intersection (common elements with duplicates).
        
        Algorithm:
        1. Two pointers, one for each array
        2. If nums1[i] < nums2[j]: advance i
        3. If nums1[i] > nums2[j]: advance j
        4. If equal: add to result, advance both
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
        
        Returns:
            Intersection array
        
        Time: O(m+n) | Space: O(1) excluding output
        """
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 5
    # ═══════════════════════════════════════════════════════════════════════
    
    def merge_LC88(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        LeetCode 88: Merge Sorted Array
        
        Merge nums2 into nums1 (nums1 has size m+n).
        
        Input: nums1 = [1,2,3,0,0,0], m = 3
               nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        
        🔑 APPROACH: Merge from END to avoid overwriting
        
        Time: O(m+n) | Space: O(1)
        """
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining from nums2 (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    
    
    def intersect_LC350(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        LeetCode 350: Intersection of Two Arrays II
        
        Find intersection (include duplicates).
        
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        
        DRY RUN:
        nums1 = [1, 1, 2, 2] (sorted)
        nums2 = [2, 2] (sorted)
        
        i=0, j=0: 1 < 2, i++
        i=1, j=0: 1 < 2, i++
        i=2, j=0: 2 == 2, add 2, i++, j++
        i=3, j=1: 2 == 2, add 2, i++, j++
        
        Result: [2, 2] ✓
        """
        nums1.sort()
        nums2.sort()
        return self.intersect_template(nums1, nums2)
    
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5B: SUBARRAY SUM PROBLEMS (Sliding Window + Two Pointers)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Find subarrays with specific sum properties using sliding window.
    
    🔑 KEY INSIGHT:
    For POSITIVE numbers, sliding window works:
    - Expand right: sum too small
    - Shrink left: sum too large
    
    For arrays with NEGATIVES, use HashMap (not two pointers).
    
    💡 WHEN TO USE:
    - Minimum/maximum subarray with sum ≥ k
    - Count subarrays with sum = k (HashMap)
    - Longest subarray with sum ≤ k
    
    ⏱️  Time: O(n) for positive nums | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def minSubArrayLen(target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 643. Maximum Average Subarray I ⭐⭐
    
    Medium:
    ✅ 209. Minimum Size Subarray Sum ⭐⭐⭐
    ✅ 560. Subarray Sum Equals K (HashMap) ⭐⭐⭐
    ✅ 325. Maximum Size Subarray Sum Equals k ⭐⭐
    ✅ 862. Shortest Subarray with Sum at Least K (Deque) ⭐⭐
    ✅ 713. Subarray Product Less Than K ⭐⭐⭐
    """
    
    def minSubArrayLen_LC209(self, target: int, nums: List[int]) -> int:
        """
        LeetCode 209: Minimum Size Subarray Sum
        
        Find minimum length subarray with sum ≥ target.
        
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2 (subarray [4,3])
        
        🔑 APPROACH: Sliding Window (positive numbers)
        
        Algorithm:
        1. Expand right: add to sum
        2. While sum ≥ target:
           - Update min length
           - Shrink from left
        
        DRY RUN:
        target = 7, nums = [2, 3, 1, 2, 4, 3]
        
        right=0: sum=2 < 7
        right=1: sum=5 < 7
        right=2: sum=6 < 7
        right=3: sum=8 ≥ 7
            min_len=4, remove nums[0], sum=6, left=1
        right=4: sum=10 ≥ 7
            min_len=4, remove nums[1], sum=7, left=2
            Still ≥7! min_len=3, remove nums[2], sum=6, left=3
        right=5: sum=9 ≥ 7
            min_len=3, remove nums[3], sum=7, left=4
            Still ≥7! min_len=2, remove nums[4], sum=3, left=5 ✓
        
        Result: 2 ✓
        
        Time: O(n) | Space: O(1)
        """
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
    
    
    def subarraySum_LC560(self, nums: List[int], k: int) -> int:
        """
        LeetCode 560: Subarray Sum Equals K
        
        Count subarrays with sum = k.
        
        Input: nums = [1,1,1], k = 2
        Output: 2 (subarrays [1,1] at index 0-1 and 1-2)
        
        🔑 APPROACH: Prefix Sum + HashMap (NOT two pointers!)
        
        Why not two pointers? Array has negatives/zeros!
        Two pointers only work for POSITIVE numbers.
        
        Algorithm:
        1. Track prefix sum
        2. If (prefix_sum - k) exists in map → found subarray
        3. Store prefix sum counts in HashMap
        
        DRY RUN:
        nums = [1, 1, 1], k = 2
        
        prefix_sum_map = {0: 1}  # Base case
        
        i=0: sum=1
             sum-k = 1-2 = -1 (not in map)
             map = {0:1, 1:1}
        
        i=1: sum=2
             sum-k = 2-2 = 0 (in map! count++)
             count = 1
             map = {0:1, 1:1, 2:1}
        
        i=2: sum=3
             sum-k = 3-2 = 1 (in map! count++)
             count = 2
        
        Result: 2 ✓
        
        Time: O(n) | Space: O(n)
        """
        prefix_sum = 0
        count = 0
        sum_count = {0: 1}  # Base case: empty subarray
        
        for num in nums:
            prefix_sum += num
            
            # Check if (prefix_sum - k) exists
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            
            # Update prefix sum count
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count
    
    
    def numSubarrayProductLessThanK_LC713(self, nums: List[int], k: int) -> int:
        """
        LeetCode 713: Subarray Product Less Than K
        
        Count subarrays with product < k.
        
        Input: nums = [10,5,2,6], k = 100
        Output: 8
        
        🔑 KEY INSIGHT:
        When we expand right and product < k:
        - ALL subarrays ending at right are valid!
        - Count = (right - left + 1)
        
        Why? [10,5,2]:
        - [2] ✓
        - [5,2] ✓  
        - [10,5,2] ✓
        All 3 subarrays ending at index 2 are valid!
        
        DRY RUN:
        nums = [10, 5, 2, 6], k = 100
        
        left=0, right=0: prod=10 < 100
            count += 1 (subarray [10])
        
        left=0, right=1: prod=50 < 100
            count += 2 (subarrays [5], [10,5])
        
        left=0, right=2: prod=100 >= 100
            Remove left: prod=10, left=1
            prod=10 < 100
            count += 2 (subarrays [2], [5,2])
        
        left=1, right=3: prod=60 < 100
            count += 3 (subarrays [6], [2,6], [5,2,6])
        
        Total: 1+2+2+3 = 8 ✓
        
        Time: O(n) | Space: O(1)
        """
        if k <= 1:
            return 0
        
        left = 0
        product = 1
        count = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k:
                product //= nums[left]
                left += 1
            
            # All subarrays ending at right
            count += (right - left + 1)
        
        return count
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5C: CONTAINER/WATER VARIANTS (MORE PROBLEMS!)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 ADDITIONAL WATER/CONTAINER PROBLEMS:
    
    These all use the greedy two-pointer approach!
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 1779. Find Nearest Point That Has the Same X or Y Coordinate
    
    Medium:
    ✅ 11. Container With Most Water ⭐⭐⭐ (already covered)
    ✅ 42. Trapping Rain Water ⭐⭐⭐ (already covered)
    ✅ 407. Trapping Rain Water II (BFS + Heap) ⭐⭐
    
    Hard:
    ✅ 42. Trapping Rain Water ⭐⭐⭐
    """
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5D: PARTITION & REARRANGEMENT VARIANTS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 MORE PARTITION PROBLEMS:
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 905. Sort Array By Parity ⭐⭐
    ✅ 922. Sort Array By Parity II ⭐
    
    Medium:
    ✅ 75. Sort Colors ⭐⭐⭐ (already covered)
    ✅ 2149. Rearrange Array Elements by Sign ⭐⭐
    ✅ 86. Partition List (LinkedList) ⭐⭐
    ✅ 328. Odd Even Linked List ⭐⭐
    """
    
    def sortArrayByParity_LC905(self, nums: List[int]) -> List[int]:
        """
        LeetCode 905: Sort Array By Parity
        
        Move even numbers to front, odd to back.
        
        Input: nums = [3,1,2,4]
        Output: [2,4,3,1] (or any [even,even,odd,odd])
        
        🔑 APPROACH: Two pointers (same direction)
        
        Time: O(n) | Space: O(1)
        """
        left = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 0:  # Even number
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
    
    
    def rearrangeArray_LC2149(self, nums: List[int]) -> List[int]:
        """
        LeetCode 2149: Rearrange Array Elements by Sign
        
        Rearrange so every consecutive pair has opposite signs.
        
        Input: nums = [3,1,-2,-5,2,-4]
        Output: [3,-2,1,-5,2,-4]
        
        🔑 APPROACH: Two pointers for pos/neg positions
        
        Time: O(n) | Space: O(n)
        """
        n = len(nums)
        result = [0] * n
        pos_idx = 0  # Even indices
        neg_idx = 1  # Odd indices
        
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: PARTITION PROBLEMS (Dutch National Flag)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Partition array into regions using multiple pointers.
    
    🔑 KEY INSIGHT (Dutch National Flag):
    For 3 partitions (0s, 1s, 2s):
    - low: boundary of 0s
    - mid: current element
    - high: boundary of 2s
    
    💡 WHEN TO USE:
    - Sort array with limited values (0,1,2)
    - Partition array by condition
    - Quick Select / Quick Sort
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def sortColors(nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 75. Sort Colors ⭐⭐⭐ (Dutch National Flag)
    ✅ 148. Sort List (Merge Sort LinkedList)
    ✅ 324. Wiggle Sort II ⭐⭐
    """
    
    def sortColors_template(self, nums: List[int]) -> None:
        """
        🎯 MASTER TEMPLATE: Dutch National Flag
        
        Sort array of 0s, 1s, 2s in one pass.
        
        Algorithm:
        - low: next position for 0
        - mid: current element
        - high: next position for 2 (from end)
        
        Args:
            nums: Array with 0s, 1s, 2s
        
        Time: O(n) | Space: O(1)
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 6
    # ═══════════════════════════════════════════════════════════════════════
    
    def sortColors_LC75(self, nums: List[int]) -> None:
        """
        LeetCode 75: Sort Colors
        
        Sort array of 0s, 1s, 2s (Dutch National Flag).
        
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        
        DRY RUN:
        nums = [2, 0, 2, 1, 1, 0]
        
        low=0, mid=0, high=5
        
        Step 1: nums[0]=2, swap with high
                [0,0,2,1,1,2], high=4
        
        Step 2: nums[0]=0, swap with low
                [0,0,2,1,1,2], low=1, mid=1
        
        Step 3: nums[1]=0, swap with low
                [0,0,2,1,1,2], low=2, mid=2
        
        Step 4: nums[2]=2, swap with high
                [0,0,1,1,2,2], high=3
        
        Step 5: nums[2]=1, mid++
        Step 6: nums[3]=1, mid++
        
        Result: [0,0,1,1,2,2] ✓
        """
        self.sortColors_template(nums)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: SUBSEQUENCE PROBLEMS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Check if one string is subsequence of another using two pointers.
    
    🔑 KEY INSIGHT:
    Advance pointer in main string always.
    Advance pointer in subsequence only when characters match.
    If subsequence pointer reaches end → it's a subsequence!
    
    💡 WHEN TO USE:
    - Check if s is subsequence of t
    - Count matching subsequences
    - Longest common subsequence variants
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def isSubsequence(s, t):
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 392. Is Subsequence ⭐⭐⭐
    ✅ 524. Longest Word in Dictionary through Deleting ⭐⭐
    
    Medium:
    ✅ 792. Number of Matching Subsequences ⭐⭐
    """
    
    def isSubsequence_template(self, s: str, t: str) -> bool:
        """
        🎯 MASTER TEMPLATE: Is Subsequence
        
        Check if s is subsequence of t.
        
        Algorithm:
        1. Two pointers: i for s, j for t
        2. Always advance j
        3. Advance i only when s[i] == t[j]
        4. If i reaches end of s → subsequence!
        
        Args:
            s: Potential subsequence
            t: Main string
        
        Returns:
            True if s is subsequence of t
        
        Time: O(n) | Space: O(1)
        """
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 7
    # ═══════════════════════════════════════════════════════════════════════
    
    def isSubsequence_LC392(self, s: str, t: str) -> bool:
        """
        LeetCode 392: Is Subsequence
        
        Check if s is subsequence of t.
        
        Input: s = "abc", t = "ahbgdc"
        Output: True
        
        DRY RUN:
        s = "abc", t = "ahbgdc"
        
        i=0, j=0: s[0]='a' == t[0]='a', i++, j++
        i=1, j=1: s[1]='b' != t[1]='h', j++
        i=1, j=2: s[1]='b' == t[2]='b', i++, j++
        i=2, j=3: s[2]='c' != t[3]='g', j++
        i=2, j=4: s[2]='c' != t[4]='d', j++
        i=2, j=5: s[2]='c' == t[5]='c', i++, j++
        
        i=3 == len(s) → True ✓
        """
        return self.isSubsequence_template(s, t)
    
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7B: ADVANCED PALINDROME PROBLEMS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 MORE PALINDROME VARIATIONS:
    
    These are ALL important for FAANG interviews!
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 125. Valid Palindrome ⭐⭐⭐ (already covered)
    ✅ 680. Valid Palindrome II ⭐⭐⭐ (already covered)
    ✅ 234. Palindrome Linked List ⭐⭐
    ✅ 9. Palindrome Number ⭐
    
    Medium:
    ✅ 5. Longest Palindromic Substring ⭐⭐⭐ (EXPAND AROUND CENTER!)
    ✅ 647. Palindromic Substrings ⭐⭐
    ✅ 131. Palindrome Partitioning ⭐⭐
    ✅ 1332. Remove Palindromic Subsequences ⭐
    
    Hard:
    ✅ 214. Shortest Palindrome (KMP) ⭐⭐
    """
    
    def longestPalindrome_LC5(self, s: str) -> str:
        """
        LeetCode 5: Longest Palindromic Substring
        
        Find longest palindromic substring.
        
        Input: s = "babad"
        Output: "bab" (or "aba")
        
        🔑 APPROACH: Expand Around Center
        
        Key insight:
        - Palindrome mirrors around center
        - Try each position as center
        - Expand while characters match
        - Handle both odd and even length palindromes
        
        DRY RUN:
        s = "babad"
        
        Center at index 0 ('b'):
        - Odd: "b" (length 1)
        - Even: "" (no match)
        
        Center at index 1 ('a'):
        - Odd: expand to "bab" (length 3) ✓
        - Even: "" (b != b... wait 'b' == 'b')
        
        Center at index 2 ('b'):
        - Odd: expand to "aba" (length 3)
        - Even: ""
        
        Result: "bab" or "aba" ✓
        
        Time: O(n²) | Space: O(1)
        """
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if not s:
            return ""
        
        longest = ""
        
        for i in range(len(s)):
            # Odd length palindrome (center is single char)
            odd_pal = expand_around_center(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal
            
            # Even length palindrome (center is between two chars)
            even_pal = expand_around_center(i, i + 1)
            if len(even_pal) > len(longest):
                longest = even_pal
        
        return longest
    
    
    def countSubstrings_LC647(self, s: str) -> int:
        """
        LeetCode 647: Palindromic Substrings
        
        Count all palindromic substrings.
        
        Input: s = "abc"
        Output: 3 ("a", "b", "c")
        
        Input: s = "aaa"
        Output: 6 ("a", "a", "a", "aa", "aa", "aaa")
        
        🔑 APPROACH: Expand around each center
        
        Time: O(n²) | Space: O(1)
        """
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total = 0
        
        for i in range(len(s)):
            # Odd length
            total += expand_around_center(i, i)
            # Even length
            total += expand_around_center(i, i + 1)
        
        return total
    
    
    def isPalindrome_LC234_linkedlist(self, head: Optional['ListNode']) -> bool:
        """
        LeetCode 234: Palindrome Linked List
        
        Check if linked list is palindrome.
        
        Input: head = [1,2,2,1]
        Output: True
        
        🔑 APPROACH: Fast/Slow + Reverse second half
        
        Algorithm:
        1. Find middle using fast/slow pointers
        2. Reverse second half
        3. Compare first half with reversed second half
        
        Time: O(n) | Space: O(1)
        """
        if not head or not head.next:
            return True
        
        # Find middle using fast/slow
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second = self.reverse_linkedlist(slow.next)
        
        # Compare
        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    
    def reverse_linkedlist(self, head):
        """Helper: reverse linked list"""
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7C: STRING MANIPULATION WITH TWO POINTERS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 STRING PROBLEMS USING TWO POINTERS:
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 344. Reverse String ⭐⭐⭐
    ✅ 345. Reverse Vowels of a String ⭐⭐
    ✅ 557. Reverse Words in a String III ⭐
    ✅ 541. Reverse String II ⭐
    
    Medium:
    ✅ 151. Reverse Words in a String ⭐⭐⭐
    ✅ 186. Reverse Words in a String II ⭐⭐
    ✅ 443. String Compression ⭐⭐
    ✅ 2000. Reverse Prefix of Word ⭐
    """
    
    def reverseWords_LC151(self, s: str) -> str:
        """
        LeetCode 151: Reverse Words in a String
        
        Reverse word order, remove extra spaces.
        
        Input: s = "  hello world  "
        Output: "world hello"
        
        🔑 APPROACH: 
        1. Split by spaces
        2. Reverse word array
        3. Join
        
        Or more complex: in-place with multiple passes
        
        Time: O(n) | Space: O(n)
        """
        # Simple approach
        words = s.split()
        return ' '.join(reversed(words))
        
        # In-place approach (if allowed):
        # 1. Reverse entire string
        # 2. Reverse each word
        # 3. Remove extra spaces
    
    
    def compress_LC443(self, chars: List[str]) -> int:
        """
        LeetCode 443: String Compression
        
        Compress array of characters in-place.
        
        Input: chars = ["a","a","b","b","c","c","c"]
        Output: 6, chars = ["a","2","b","2","c","3"]
        
        🔑 APPROACH: Two pointers (read, write)
        
        Algorithm:
        1. Read pointer: scan through chars
        2. Write pointer: write compressed result
        3. Count consecutive characters
        4. Write char + count
        
        DRY RUN:
        chars = ['a','a','b','b','c','c','c']
        
        write=0, read=0
        
        Count 'a': 2 occurrences
        Write: chars[0]='a', chars[1]='2', write=2
        
        Count 'b': 2 occurrences  
        Write: chars[2]='b', chars[3]='2', write=4
        
        Count 'c': 3 occurrences
        Write: chars[4]='c', chars[5]='3', write=6
        
        Result: ['a','2','b','2','c','3'] ✓
        
        Time: O(n) | Space: O(1)
        """
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Count consecutive characters
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Write character
            chars[write] = char
            write += 1
            
            # Write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: REVERSE OPERATIONS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Reverse string/array or parts of it using two pointers from both ends.
    
    🔑 KEY INSIGHT:
    Swap elements at left and right, move both toward center.
    
    💡 WHEN TO USE:
    - Reverse entire string/array
    - Reverse words in sentence
    - Reverse substring
    
    ⏱️  Time: O(n) | Space: O(1) if in-place, O(n) for strings
    
    📝 GENERALIZED TEMPLATE:
    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 344. Reverse String ⭐⭐⭐
    ✅ 345. Reverse Vowels of a String ⭐⭐
    ✅ 541. Reverse String II ⭐
    
    Medium:
    ✅ 151. Reverse Words in a String ⭐⭐
    ✅ 186. Reverse Words in a String II ⭐⭐
    """
    
    def reverseString_template(self, s: List[str]) -> None:
        """
        🎯 MASTER TEMPLATE: Reverse String
        
        Reverse string in-place.
        
        Algorithm:
        Two pointers from both ends, swap and move inward.
        
        Args:
            s: Array of characters (modified in-place)
        
        Time: O(n) | Space: O(1)
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 8
    # ═══════════════════════════════════════════════════════════════════════
    
    def reverseString_LC344(self, s: List[str]) -> None:
        """
        LeetCode 344: Reverse String
        
        Reverse string in-place.
        
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        
        DRY RUN:
        s = ['h', 'e', 'l', 'l', 'o']
        
        left=0, right=4: swap 'h' ↔ 'o'
        ['o', 'e', 'l', 'l', 'h']
        
        left=1, right=3: swap 'e' ↔ 'l'
        ['o', 'l', 'l', 'e', 'h']
        
        left=2, right=2: stop
        
        Result: ['o','l','l','e','h'] ✓
        """
        self.reverseString_template(s)
    
    
    def reverseVowels_LC345(self, s: str) -> str:
        """
        LeetCode 345: Reverse Vowels of a String
        
        Reverse only the vowels in string.
        
        Input: s = "hello"
        Output: "holle"
        
        🔑 APPROACH:
        Two pointers, move both to find vowels, swap them.
        
        Time: O(n) | Space: O(n) for result
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left to vowel
            while left < right and s[left] not in vowels:
                left += 1
            
            # Move right to vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 50 MUST-KNOW PROBLEMS (COMPREHENSIVE FAANG LIST)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 ABSOLUTE MUST-KNOW (Top 15 - DO THESE FIRST!):
═══════════════════════════════════════════════════════════════════════════
1. ⭐⭐⭐ LC 1: Two Sum (HashMap, not two pointers but FOUNDATION!)
   - ALL companies | Asked in 90%+ interviews
   
2. ⭐⭐⭐ LC 167: Two Sum II - Input Array Is Sorted
   - Pattern 1 | Companies: ALL | True two pointers foundation
   
3. ⭐⭐⭐ LC 15: 3Sum
   - Pattern 4 | Companies: ALL (TOP 3 MOST ASKED!)
   - Master this and you can solve 3Sum Closest, Smaller, etc.
   
4. ⭐⭐⭐ LC 11: Container With Most Water
   - Pattern 1 | Companies: ALL (TOP 5 MOST ASKED!)
   
5. ⭐⭐⭐ LC 42: Trapping Rain Water
   - Pattern 1 | Companies: Google, Meta, Amazon (HARD BUT CRITICAL!)
   
6. ⭐⭐⭐ LC 283: Move Zeroes
   - Pattern 2 | Companies: ALL | Easy but tests fundamentals
   
7. ⭐⭐⭐ LC 125: Valid Palindrome
   - Pattern 3 | Companies: ALL | Interview starter question
   
8. ⭐⭐⭐ LC 680: Valid Palindrome II
   - Pattern 3 | Companies: Meta, Amazon, Microsoft
   
9. ⭐⭐⭐ LC 75: Sort Colors (Dutch National Flag)
   - Pattern 6 | Companies: ALL | Classic algorithm
   
10. ⭐⭐⭐ LC 88: Merge Sorted Array
    - Pattern 5 | Companies: Microsoft, Meta, Amazon
    
11. ⭐⭐⭐ LC 16: 3Sum Closest
    - Pattern 4 | Companies: Amazon, Bloomberg, Adobe
    
12. ⭐⭐⭐ LC 209: Minimum Size Subarray Sum
    - Pattern 5B | Companies: Meta, Google | Sliding window variant
    
13. ⭐⭐⭐ LC 713: Subarray Product Less Than K
    - Pattern 5B | Companies: Meta, Amazon
    
14. ⭐⭐⭐ LC 560: Subarray Sum Equals K
    - Pattern 5B | Companies: Meta, Google (HashMap, not pure two pointers)
    
15. ⭐⭐⭐ LC 5: Longest Palindromic Substring
    - Pattern 7B | Companies: ALL | Expand around center


🔥🔥 VERY IMPORTANT (Next 15):
═══════════════════════════════════════════════════════════════════════════
16. ⭐⭐ LC 27: Remove Element
17. ⭐⭐ LC 26: Remove Duplicates from Sorted Array
18. ⭐⭐ LC 344: Reverse String
19. ⭐⭐ LC 345: Reverse Vowels of a String
20. ⭐⭐ LC 977: Squares of a Sorted Array
21. ⭐⭐ LC 350: Intersection of Two Arrays II
22. ⭐⭐ LC 392: Is Subsequence
23. ⭐⭐ LC 18: 4Sum
24. ⭐⭐ LC 259: 3Sum Smaller (Premium but important!)
25. ⭐⭐ LC 234: Palindrome Linked List
26. ⭐⭐ LC 647: Palindromic Substrings
27. ⭐⭐ LC 151: Reverse Words in a String
28. ⭐⭐ LC 443: String Compression
29. ⭐⭐ LC 905: Sort Array By Parity
30. ⭐⭐ LC 2149: Rearrange Array Elements by Sign


🔥 IMPORTANT (Complete Your Mastery - Next 20):
═══════════════════════════════════════════════════════════════════════════
31. ⭐ LC 80: Remove Duplicates from Sorted Array II
32. ⭐ LC 349: Intersection of Two Arrays
33. ⭐ LC 986: Interval List Intersections
34. ⭐ LC 454: 4Sum II (HashMap optimization)
35. ⭐ LC 923: 3Sum With Multiplicity
36. ⭐ LC 1099: Two Sum Less Than K (Premium)
37. ⭐ LC 325: Maximum Size Subarray Sum Equals k (Premium)
38. ⭐ LC 524: Longest Word in Dictionary through Deleting
39. ⭐ LC 792: Number of Matching Subsequences
40. ⭐ LC 324: Wiggle Sort II
41. ⭐ LC 186: Reverse Words in a String II (Premium)
42. ⭐ LC 557: Reverse Words in a String III
43. ⭐ LC 541: Reverse String II
44. ⭐ LC 922: Sort Array By Parity II
45. ⭐ LC 653: Two Sum IV - BST
46. ⭐ LC 9: Palindrome Number
47. ⭐ LC 131: Palindrome Partitioning
48. ⭐ LC 457: Circular Array Loop
49. ⭐ LC 643: Maximum Average Subarray I
50. ⭐ LC 862: Shortest Subarray with Sum at Least K


═══════════════════════════════════════════════════════════════════════════
📊 UPDATED 4-WEEK STUDY PLAN (COMPREHENSIVE):
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - FOUNDATIONS (Two Sum, Opposite Direction, Same Direction):
─────────────────────────────────────────────────────────────────────────
Day 1: Two Sum Family
  - LC 1: Two Sum (HashMap) ⚠️ MUST KNOW!
  - LC 167: Two Sum II (Two Pointers) ⚠️ MUST KNOW!
  - LC 1099: Two Sum Less Than K

Day 2: Container & Water Problems
  - LC 11: Container With Most Water ⚠️ TOP 5 MOST ASKED!
  - LC 42: Trapping Rain Water ⚠️ HARD BUT CRITICAL!

Day 3: Same Direction Fast/Slow
  - LC 27: Remove Element
  - LC 283: Move Zeroes
  - LC 26: Remove Duplicates
  - LC 80: Remove Duplicates II

Day 4: Squares & Sorting
  - LC 977: Squares of a Sorted Array
  - LC 905: Sort Array By Parity
  - LC 922: Sort Array By Parity II

Day 5: Practice all Week 1
Day 6-7: Timed practice (20 min each) + review mistakes


WEEK 2 - 3SUM MASTERY & PALINDROMES:
─────────────────────────────────────────────────────────────────────────
Day 1: 3Sum Foundation
  - LC 15: 3Sum ⚠️ MOST IMPORTANT PROBLEM!
  - Review solution 3 times, memorize template

Day 2: 3Sum Variants
  - LC 16: 3Sum Closest ⚠️ CRITICAL!
  - LC 259: 3Sum Smaller
  - LC 923: 3Sum With Multiplicity

Day 3: 4Sum Family
  - LC 18: 4Sum
  - LC 454: 4Sum II (HashMap)

Day 4: Palindrome Checking
  - LC 125: Valid Palindrome
  - LC 680: Valid Palindrome II ⚠️ META FAVORITE!

Day 5: Advanced Palindromes
  - LC 5: Longest Palindromic Substring ⚠️ CRITICAL!
  - LC 647: Palindromic Substrings
  - LC 234: Palindrome Linked List

Day 6-7: Timed practice + mock interview


WEEK 3 - SUBARRAY SUM & MERGE PROBLEMS:
─────────────────────────────────────────────────────────────────────────
Day 1: Subarray Sum (Sliding Window)
  - LC 209: Minimum Size Subarray Sum ⚠️ IMPORTANT!
  - LC 713: Subarray Product Less Than K ⚠️ IMPORTANT!

Day 2: Subarray Sum (HashMap)
  - LC 560: Subarray Sum Equals K ⚠️ META/GOOGLE FAVORITE!
  - LC 325: Maximum Size Subarray Sum = k

Day 3: Merge Operations
  - LC 88: Merge Sorted Array
  - LC 349: Intersection of Two Arrays
  - LC 350: Intersection of Two Arrays II
  - LC 986: Interval List Intersections

Day 4: Dutch National Flag & Partition
  - LC 75: Sort Colors ⚠️ CLASSIC!
  - LC 2149: Rearrange Array Elements by Sign
  - LC 324: Wiggle Sort II

Day 5: Practice all Week 3
Day 6-7: Timed practice + review


WEEK 4 - ADVANCED PATTERNS & MOCK INTERVIEWS:
─────────────────────────────────────────────────────────────────────────
Day 1: Subsequence Problems
  - LC 392: Is Subsequence
  - LC 524: Longest Word in Dictionary
  - LC 792: Number of Matching Subsequences

Day 2: String Manipulation
  - LC 344: Reverse String
  - LC 345: Reverse Vowels
  - LC 151: Reverse Words ⚠️ IMPORTANT!
  - LC 443: String Compression

Day 3: Mixed Practice (Random from Top 30)
  - Simulate interview conditions
  - 45 minutes, solve 2-3 problems

Day 4: Company-Specific Focus
  - If targeting Google: LC 11, 42, 15, 5, 560
  - If targeting Meta: LC 15, 42, 680, 560, 713
  - If targeting Amazon: LC 167, 15, 283, 125, 88

Day 5-6: Full Mock Interviews
  - Day 5: Two 45-min sessions
  - Day 6: Two 45-min sessions

Day 7: Final Review
  - Review ALL top 15 problems
  - Make cheat sheet of templates
  - Practice explaining solutions out loud


═══════════════════════════════════════════════════════════════════════════
💡 ENHANCED PATTERN SELECTION GUIDE:
═══════════════════════════════════════════════════════════════════════════

QUESTION KEYWORDS → PATTERN:
─────────────────────────────────────────────────────────────────────────
"two numbers that add up to X" (sorted)     → Pattern 1 (Opposite)
"maximize area/container"                    → Pattern 1 (Greedy move smaller)
"trap/collect water"                         → Pattern 1 (Track max heights)
"remove element/duplicates in-place"         → Pattern 2 (Fast/slow)
"move zeros to end"                          → Pattern 2 (Fast/slow)
"check if palindrome"                        → Pattern 3 (Both ends)
"longest palindromic substring"              → Pattern 7B (Expand center)
"find triplets/three numbers"                → Pattern 4 (Fix + two pointers)
"find quadruplets/four numbers"              → Pattern 4 (Fix two + two pointers)
"merge sorted arrays"                        → Pattern 5 (Compare merge)
"intersection of sorted arrays"              → Pattern 5 (Two pointers)
"subarray with sum ≥ k" (positive numbers)   → Pattern 5B (Sliding window)
"subarray with sum = k" (any numbers)        → HashMap (not two pointers!)
"subarray product < k"                       → Pattern 5B (Sliding window)
"sort 0s, 1s, 2s"                           → Pattern 6 (Dutch flag)
"partition by condition"                     → Pattern 6 (Three pointers)
"is subsequence"                             → Pattern 7 (Advance on match)
"reverse string/array"                       → Pattern 8 (Swap from ends)
"reverse words"                              → Pattern 8 + string manipulation


═══════════════════════════════════════════════════════════════════════════
🎓 COMPANY-SPECIFIC PROBLEM FREQUENCY:
═══════════════════════════════════════════════════════════════════════════

GOOGLE (Focus on optimization & variants):
─────────────────────────────────────────────────────────────────────────
Must Know: LC 11, 42, 15, 5, 560, 16, 647, 713
Important: LC 209, 454, 986, 259, 131

META/FACEBOOK (Focus on 3Sum, palindromes, subarray):
─────────────────────────────────────────────────────────────────────────
Must Know: LC 15, 42, 680, 560, 713, 11, 5, 647
Important: LC 16, 209, 259, 125, 234, 350

AMAZON (Focus on basics & variations):
─────────────────────────────────────────────────────────────────────────
Must Know: LC 167, 15, 283, 125, 88, 1, 11, 27
Important: LC 16, 26, 680, 344, 75, 977, 392

MICROSOFT (Focus on merge, partition, string):
─────────────────────────────────────────────────────────────────────────
Must Know: LC 88, 167, 75, 283, 344, 125, 15
Important: LC 27, 26, 151, 345, 350, 905, 443

APPLE (Similar to Amazon, focus on fundamentals):
─────────────────────────────────────────────────────────────────────────
Must Know: LC 167, 283, 125, 344, 88, 1, 27
Important: LC 26, 15, 680, 392, 345, 75


═══════════════════════════════════════════════════════════════════════════
⚡ COMPLEXITY CHEAT SHEET (KNOW THESE COLD!):
═══════════════════════════════════════════════════════════════════════════

Two Sum (unsorted):      O(n) time, O(n) space (HashMap)
Two Sum (sorted):        O(n) time, O(1) space (Two Pointers)
3Sum:                    O(n²) time, O(1) space
4Sum:                    O(n³) time, O(1) space
K-Sum:                   O(n^(k-1)) time, O(k) space (recursion)

Container With Most Water: O(n) time, O(1) space
Trapping Rain Water:       O(n) time, O(1) space

Remove Element/Duplicates: O(n) time, O(1) space
Move Zeroes:              O(n) time, O(1) space

Valid Palindrome:         O(n) time, O(1) space
Longest Palindromic:      O(n²) time, O(1) space (expand center)

Merge Sorted Arrays:      O(m+n) time, O(1) space
Intersection:             O(m+n) time, O(1) space

Subarray Sum (sliding):   O(n) time, O(1) space
Subarray Sum (HashMap):   O(n) time, O(n) space

Sort Colors (Dutch):      O(n) time, O(1) space


═══════════════════════════════════════════════════════════════════════════
🎉 FINAL SUCCESS TIPS:
═══════════════════════════════════════════════════════════════════════════

1. ⭐ THE BIG 5 TO MASTER FIRST:
   - LC 1 (Two Sum) - Foundation for everything
   - LC 15 (3Sum) - Most asked, enables all variants
   - LC 11 (Container) - Greedy strategy mastery
   - LC 42 (Trapping Water) - Peak difficulty, huge payoff
   - LC 560 (Subarray Sum K) - HashMap pattern (not pure two pointers)

2. SORTED = TWO POINTERS OPPORTUNITY!
   - If array sorted → Think two pointers first
   - If not sorted → Consider if sorting helps (O(n log n) cost)
   - Exception: Two Sum unsorted → HashMap better (O(n))

3. FOR 3SUM/4SUM - MEMORIZE THIS TEMPLATE:
   ```python
   def threeSum(nums, target):
       nums.sort()  # ALWAYS sort first!
       result = []
       
       for i in range(len(nums) - 2):
           if i > 0 and nums[i] == nums[i-1]:
               continue  # Skip duplicates!
           
           left, right = i + 1, len(nums) - 1
           while left < right:
               # ... two pointers logic
   ```

4. SUBARRAY SUM - KNOW WHEN TO USE WHAT:
   - Positive numbers + sum ≥ k → Sliding window
   - Any numbers + sum = k → HashMap (prefix sum)
   - Product < k → Sliding window

5. PALINDROME - TWO APPROACHES:
   - Check if palindrome → Two pointers from ends
   - Find longest palindrome → Expand around center

6. COMMON BUGS TO AVOID:
   - Forgetting to skip duplicates in 3Sum ❌
   - Using <= instead of < in while loops ❌
   - Not handling empty array edge case ❌
   - Moving wrong pointer (move smaller in container!) ❌

7. INTERVIEW COMMUNICATION:
   - Always ask: "Is array sorted?"
   - Always ask: "Can have duplicates?"
   - Explain: "I'll use two pointers because..."
   - State complexity before coding!

8. PRACTICE PROGRESSION:
   Week 1: Understand each pattern (slow, thorough)
   Week 2: Solve without looking (struggle = learning!)
   Week 3: Speed up (20 min per problem)
   Week 4: Mock interviews (45 min, 2-3 problems)

9. THE 15-MINUTE RULE:
   - Stuck for 15 min? Look at hint, not solution
   - Still stuck? Read solution, then redo tomorrow
   - Never move on without understanding WHY

10. MEASURE YOUR PROGRESS:
    - Can solve Two Sum II blindfolded? ✓
    - Can solve 3Sum in <25 min? ✓
    - Can explain Container greedy choice? ✓
    - Can derive Trapping Water logic? ✓
    - Can code any pattern without template? ✓

YOU'RE READY FOR INTERVIEWS WHEN:
✅ Top 15 problems < 20 min each
✅ Can explain pattern selection for any problem
✅ Write code with no syntax errors
✅ Explain time/space complexity instantly
✅ Handle follow-up variations confidently

Good luck! Master these 50 problems and two pointers becomes your superpower! 🚀

Remember: Two pointers is asked in 40%+ of FAANG interviews.
These patterns will save you countless times! 💪
"""