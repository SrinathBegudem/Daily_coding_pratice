"""
═══════════════════════════════════════════════════════════════════════════════
                    ARRAY PATTERNS MASTERY GUIDE - COMPLETE
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. ARRAY MANIPULATION PATTERNS (This Guide):
   ✅ In-place modification (remove duplicates, rotation)
   ✅ Product patterns (except self, subarray products)
   ✅ Matrix traversal (spiral, diagonal, rotation)
   ✅ Kadane's algorithm (maximum subarray)
   ✅ Boyer-Moore voting (majority element)
   ✅ Merging and rearrangement
   ✅ Next permutation and combinatorics
   ✅ Missing/duplicate number detection

2. EXCLUDED PATTERNS (Separate Guides):
   ❌ Prefix Sum → Separate guide
   ❌ Sliding Window → Separate guide
   ❌ Two Pointers → Separate guide
   ❌ HashMap patterns → Separate guide
   ❌ Binary Search on arrays → Already covered

3. 14 ESSENTIAL ARRAY PATTERNS COVERED:
   ✅ Pattern 1: Remove Duplicates (In-Place with index pointer) ✅
   ✅ Pattern 2: Array Rotation (Reversal method)
   ✅ Pattern 3: Product Except Self (Left-Right product arrays)
   ✅ Pattern 4: Spiral Matrix Traversal (Boundary shrinking)
   ✅ Pattern 5: Set Matrix Zeroes (First row/col as markers)
   ✅ Pattern 6: Pascal's Triangle (DP generation)
   ✅ Pattern 7: Next Permutation (Two-pass modification)
   ✅ Pattern 8: Find Missing/Duplicate (Math/Cyclic sort)
   ✅ Pattern 9: Kadane's Algorithm (Maximum subarray)
   ✅ Pattern 10: Stock Buy/Sell (State machine DP)
   ✅ Pattern 11: Jump Game (Greedy/DP reach)
   ✅ Pattern 12: Boyer-Moore Voting (Majority element)
   ✅ Pattern 13: Merge Sorted Arrays (Two pointers merge)
   ✅ Pattern 14: Array Rearrangement (Cyclic, positive-negative)
   ✅ Pattern 15: Bucket sort ✅
        LC Sort Characters By Frequency ✅
        LC Top K Frequent Elements using bucket sort ✅
        LC Maximum Gap 
        LC Contains Duplicate III
        Example patterns:
        You care about frequency, not exact ordering
        “top k frequent”
        “sort by frequency”
        “group by frequency”
        “count occurrences and output sorted by count”

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Optional

class ArrayPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: REMOVE DUPLICATES (In-Place Modification)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Use write pointer (index) to track where to place next valid element.
    Read pointer scans through array.
    
    🔑 KEY INSIGHT:
    For keeping at most k duplicates:
    - First k elements are always valid (place directly)
    - After that, compare current with element k positions back
    - If different OR within first k → place it
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def removeDuplicates(nums, k):
        index = 0
        for num in nums:
            if index < k or num != nums[index - k]:
                nums[index] = num
                index += 1
        return index
    
    💡 WHY THIS WORKS:
    - index < k: First k elements auto-placed
    - num != nums[index - k]: Current differs from k positions back
      → Safe to add (won't create k+1 duplicates)
    
    📊 PATTERN VARIATIONS:
    k=1: Keep unique only (LC 26)
    k=2: Keep at most 2 of each (LC 80)
    k=3: Keep at most 3 of each
    val removal: Different pattern (LC 27)
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 26. Remove Duplicates from Sorted Array ⭐⭐⭐
    ✅ 27. Remove Element ⭐⭐
    ✅ 283. Move Zeroes ⭐⭐⭐
    
    Medium:
    ✅ 80. Remove Duplicates from Sorted Array II ⭐⭐
    """
    
    def removeDuplicates_generalized(self, nums: List[int], k: int) -> int:
        """
        🎯 MASTER TEMPLATE: Keep at most k occurrences
        
        This is the ONE template to rule them all!
        Memorize this and you can solve ALL duplicate removal problems.
        
        Args:
            nums: Sorted array
            k: Maximum occurrences allowed
        
        Returns:
            New length after removing excess duplicates
        
        Examples:
            k=1, [1,1,2] → [1,2] (length 2)
            k=2, [1,1,1,2,2,3] → [1,1,2,2,3] (length 5)
            k=3, [1,1,1,1,2] → [1,1,1,2] (length 4)
        
        Time: O(n) | Space: O(1)
        """
        index = 0
        
        for num in nums:
            # First k elements OR current differs from k positions back
            if index < k or num != nums[index - k]:
                nums[index] = num
                index += 1
        
        return index
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 1
    # ═══════════════════════════════════════════════════════════════════════
    
    def removeDuplicates_LC26(self, nums: List[int]) -> int:
        """
        LeetCode 26: Remove Duplicates from Sorted Array (Keep 1)
        
        Remove duplicates so each element appears only once.
        
        Input: nums = [1,1,2,2,3]
        Output: 2, nums = [1,2,3,_,_]
        
        🔑 APPROACH: k=1 in general template
        
        DRY RUN:
        nums = [1,1,2,2,3]
        
        index=0: num=1, index<1 → place → [1], index=1
        index=1: num=1, 1==nums[0] → SKIP
        index=1: num=2, 2!=nums[0] → place → [1,2], index=2
        index=2: num=2, 2==nums[1] → SKIP
        index=2: num=3, 3!=nums[1] → place → [1,2,3], index=3
        
        Result: [1,2,3] ✓
        """
        return self.removeDuplicates_generalized(nums, k=1)
    
    
    def removeDuplicates_LC80(self, nums: List[int]) -> int:
        """
        LeetCode 80: Remove Duplicates from Sorted Array II (Keep 2)
        
        Keep at most 2 occurrences of each element.
        
        Input: nums = [1,1,1,2,2,3]
        Output: 5, nums = [1,1,2,2,3,_]
        
        🔑 APPROACH: k=2 in general template
        
        DRY RUN:
        nums = [1,1,1,2,2,3]
        
        index=0: num=1, index<2 → place → [1], index=1
        index=1: num=1, index<2 → place → [1,1], index=2
        index=2: num=1, 1==nums[0] → SKIP (3rd occurrence)
        index=2: num=2, 2!=nums[0] → place → [1,1,2], index=3
        index=3: num=2, 2!=nums[1] → place → [1,1,2,2], index=4
        index=4: num=3, 3!=nums[2] → place → [1,1,2,2,3], index=5
        
        Result: [1,1,2,2,3] ✓
        """
        return self.removeDuplicates_generalized(nums, k=2)
    
    
    def removeElement_LC27(self, nums: List[int], val: int) -> int:
        """
        LeetCode 27: Remove Element
        
        Remove all instances of a specific value.
        
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        
        🔑 DIFFERENT PATTERN: Not about consecutive duplicates!
        Simply filter out all occurrences of val.
        
        Time: O(n) | Space: O(1)
        """
        k = 0
        
        for num in nums:
            if num != val:  # Keep if NOT equal to val
                nums[k] = num
                k += 1
        
        return k
    
    
    def moveZeroes_LC283(self, nums: List[int]) -> None:
        """
        LeetCode 283: Move Zeroes
        
        Move all zeros to end, maintain relative order of non-zeros.
        
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        
        🔑 APPROACH: Two-pass
        1. Move all non-zeros to front (like removeElement)
        2. Fill remaining positions with zeros
        
        Time: O(n) | Space: O(1)
        """
        k = 0  # Position for next non-zero
        
        # Pass 1: Move all non-zeros to front
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        
        # Pass 2: Fill remaining with zeros
        for i in range(k, len(nums)):
            nums[i] = 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: ARRAY ROTATION (Reversal Method)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Rotate array by k positions using THREE reversals.
    
    🔑 KEY INSIGHT (Right Rotation by k):
    Original: [1,2,3,4,5,6,7], k=3
    
    Step 1: Reverse entire array
    [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
    
    Step 2: Reverse first k elements
    [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
    
    Step 3: Reverse remaining n-k elements
    [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4] ✓
    
    💡 WHY THIS WORKS:
    - Reversing entire array moves last k to front (but reversed)
    - Reversing first k fixes their order
    - Reversing rest fixes remaining order
    
    📊 VARIATIONS:
    - Right rotation: reverse(0,n-1), reverse(0,k-1), reverse(k,n-1)
    - Left rotation: reverse(0,k-1), reverse(k,n-1), reverse(0,n-1)
    - Left by k = Right by (n-k)
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def rotate(nums, k):
        n = len(nums)
        k = k % n  # Handle k > n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 189. Rotate Array ⭐⭐⭐
    
    Medium:
    ✅ 48. Rotate Image (90° clockwise) ⭐⭐
    ✅ 151. Reverse Words in a String
    """
    
    def rotate_right(self, nums: List[int], k: int) -> None:
        """
        🎯 MASTER TEMPLATE: Rotate array right by k positions
        
        This is THE template for array rotation!
        
        Algorithm:
        1. Reverse entire array
        2. Reverse first k elements
        3. Reverse remaining n-k elements
        
        Args:
            nums: Array to rotate
            k: Number of positions to rotate right
        
        Example:
            nums = [1,2,3,4,5,6,7], k = 3
            → [5,6,7,1,2,3,4]
        
        Time: O(n) | Space: O(1)
        """
        n = len(nums)
        k = k % n  # Handle k > n
        
        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Three reversals
        reverse(0, n - 1)      # Reverse entire
        reverse(0, k - 1)      # Reverse first k
        reverse(k, n - 1)      # Reverse remaining
    
    
    def rotate_left(self, nums: List[int], k: int) -> None:
        """
        🎯 VARIANT: Rotate array left by k positions
        
        Left rotation by k = Right rotation by (n-k)
        OR different reversal order
        
        Time: O(n) | Space: O(1)
        """
        n = len(nums)
        k = k % n
        
        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # For left rotation: different order
        reverse(0, k - 1)      # Reverse first k
        reverse(k, n - 1)      # Reverse remaining
        reverse(0, n - 1)      # Reverse entire
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 2
    # ═══════════════════════════════════════════════════════════════════════
    
    def rotate_LC189(self, nums: List[int], k: int) -> None:
        """
        LeetCode 189: Rotate Array
        
        Rotate array to the right by k steps.
        
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        
        DRY RUN:
        nums = [1,2,3,4,5,6,7], k = 3
        
        Step 1: Reverse entire [1,2,3,4,5,6,7]
        → [7,6,5,4,3,2,1]
        
        Step 2: Reverse first 3 [7,6,5]
        → [5,6,7,4,3,2,1]
        
        Step 3: Reverse last 4 [4,3,2,1]
        → [5,6,7,1,2,3,4] ✓
        """
        self.rotate_right(nums, k)
    
    
    def rotate_image_LC48(self, matrix: List[List[int]]) -> None:
        """
        LeetCode 48: Rotate Image (90° clockwise)
        
        Rotate n×n matrix 90 degrees clockwise.
        
        Input:          Output:
        [1,2,3]        [7,4,1]
        [4,5,6]   →    [8,5,2]
        [7,8,9]        [9,6,3]
        
        🔑 APPROACH: Two steps
        1. Transpose matrix (swap matrix[i][j] with matrix[j][i])
        2. Reverse each row
        
        WHY THIS WORKS:
        Transpose: rows become columns
        [1,2,3]    [1,4,7]
        [4,5,6] →  [2,5,8]
        [7,8,9]    [3,6,9]
        
        Reverse each row: columns reverse
        [1,4,7]    [7,4,1]
        [2,5,8] →  [8,5,2]
        [3,6,9]    [9,6,3] ✓
        
        Time: O(n²) | Space: O(1)
        """
        n = len(matrix)
        
        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: PRODUCT OF ARRAY EXCEPT SELF
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Calculate product of all elements except self WITHOUT division.
    
    🔑 KEY INSIGHT:
    For each index i, answer[i] = (product of all before i) × (product of all after i)
    
    Use LEFT and RIGHT product arrays:
    - left[i] = product of all elements before i
    - right[i] = product of all elements after i
    - answer[i] = left[i] × right[i]
    
    💡 SPACE OPTIMIZATION:
    Instead of separate left/right arrays:
    1. Build left products directly in output array
    2. Multiply with right products on the fly (single variable)
    
    📝 EXAMPLE:
    nums = [1, 2, 3, 4]
    
    Left products:  [1, 1, 2, 6]
    Right products: [24, 12, 4, 1]
    Answer:         [24, 12, 8, 6]
    
    Explanation:
    answer[0] = 2×3×4 = 24 = left[0]×right[0] = 1×24
    answer[1] = 1×3×4 = 12 = left[1]×right[1] = 1×12
    answer[2] = 1×2×4 = 8  = left[2]×right[2] = 2×4
    answer[3] = 1×2×3 = 6  = left[3]×right[3] = 6×1
    
    ⏱️  Time: O(n) | Space: O(1) excluding output
    
    📝 GENERALIZED TEMPLATE:
    def productExceptSelf(nums):
        n = len(nums)
        result = [1] * n
        
        # Build left products
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # Multiply with right products on the fly
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 238. Product of Array Except Self ⭐⭐⭐
    ✅ 1656. Design an Ordered Stream
    ✅ 2155. All Divisions With the Highest Score of a Binary Array
    """
    
    def productExceptSelf_optimized(self, nums: List[int]) -> List[int]:
        """
        🎯 MASTER TEMPLATE: Product of array except self
        
        Space-optimized solution using output array for left products
        and single variable for right products.
        
        Algorithm:
        1. Build left products in result array
        2. Multiply with right products on the fly
        
        Args:
            nums: Input array
        
        Returns:
            Array where result[i] = product of all except nums[i]
        
        Example:
            nums = [1,2,3,4]
            result = [24,12,8,6]
        
        Time: O(n) | Space: O(1) excluding output
        """
        n = len(nums)
        result = [1] * n
        
        # Step 1: Build left products in result
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Step 2: Multiply with right products on the fly
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 3
    # ═══════════════════════════════════════════════════════════════════════
    
    def productExceptSelf_LC238(self, nums: List[int]) -> List[int]:
        """
        LeetCode 238: Product of Array Except Self
        
        Return array where answer[i] is product of all elements except nums[i].
        Cannot use division.
        
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        
        DRY RUN:
        nums = [1, 2, 3, 4]
        
        Step 1: Build left products
        result[0] = 1 (no elements before)
        result[1] = 1 × nums[0] = 1 × 1 = 1
        result[2] = 1 × nums[1] = 1 × 2 = 2
        result[3] = 2 × nums[2] = 2 × 3 = 6
        result = [1, 1, 2, 6]
        
        Step 2: Multiply with right products
        right = 1
        i=3: result[3] *= 1 → result[3] = 6, right = 4
        i=2: result[2] *= 4 → result[2] = 8, right = 12
        i=1: result[1] *= 12 → result[1] = 12, right = 24
        i=0: result[0] *= 24 → result[0] = 24, right = 24
        
        result = [24, 12, 8, 6] ✓
        """
        return self.productExceptSelf_optimized(nums)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: SPIRAL MATRIX TRAVERSAL
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Traverse 2D matrix in spiral order (clockwise from outside to inside).
    
    🔑 KEY INSIGHT:
    Use 4 boundaries that shrink inward:
    - top, bottom (row boundaries)
    - left, right (column boundaries)
    
    In each iteration, traverse 4 sides:
    1. Top row: left → right (then top++)
    2. Right column: top → bottom (then right--)
    3. Bottom row: right → left (then bottom--)
    4. Left column: bottom → top (then left++)
    
    💡 EDGE CASES:
    - After traversing top/right, check if top <= bottom before bottom row
    - After traversing bottom, check if left <= right before left column
    - This handles single row/column matrices
    
    📝 VISUALIZATION:
    [1  2  3  4]
    [5  6  7  8]
    [9 10 11 12]
    
    Order: 1→2→3→4→8→12→11→10→9→5→6→7
    
    Iteration 1:
    Top: 1,2,3,4 (top++)
    Right: 8,12 (right--)
    Bottom: 11,10,9 (bottom--)
    Left: 5 (left++)
    
    Iteration 2:
    Top: 6,7 (top++)
    Done!
    
    ⏱️  Time: O(m×n) | Space: O(1) excluding output
    
    📝 GENERALIZED TEMPLATE:
    def spiralOrder(matrix):
        result = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        
        while top <= bottom and left <= right:
            # Top row
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top += 1
            
            # Right column
            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right -= 1
            
            # Bottom row (if exists)
            if top <= bottom:
                for col in range(right, left-1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # Left column (if exists)
            if left <= right:
                for row in range(bottom, top-1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 54. Spiral Matrix ⭐⭐⭐
    ✅ 59. Spiral Matrix II ⭐⭐
    ✅ 885. Spiral Matrix III
    ✅ 2326. Spiral Matrix IV
    """
    
    def spiralOrder_template(self, matrix: List[List[int]]) -> List[int]:
        """
        🎯 MASTER TEMPLATE: Spiral matrix traversal
        
        Traverse matrix in spiral order using boundary shrinking.
        
        Algorithm:
        1. Initialize 4 boundaries: top, bottom, left, right
        2. While boundaries valid:
           - Traverse top row (left→right)
           - Traverse right column (top→bottom)
           - Traverse bottom row (right→left) if valid
           - Traverse left column (bottom→top) if valid
           - Shrink boundaries inward
        
        Args:
            matrix: 2D matrix
        
        Returns:
            Elements in spiral order
        
        Time: O(m*n) | Space: O(1)
        """
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse top row (left → right)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # 2. Traverse right column (top → bottom)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 3. Traverse bottom row (right → left) if exists
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # 4. Traverse left column (bottom → top) if exists
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 4
    # ═══════════════════════════════════════════════════════════════════════
    
    def spiralOrder_LC54(self, matrix: List[List[int]]) -> List[int]:
        """
        LeetCode 54: Spiral Matrix
        
        Return all elements in spiral order.
        
        Input:
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
        
        Output: [1,2,3,6,9,8,7,4,5]
        
        DRY RUN:
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
        
        Initial: top=0, bottom=2, left=0, right=2
        
        Iteration 1:
        1. Top row (0,0→0,2): [1,2,3], top=1
        2. Right col (1,2→2,2): [1,2,3,6,9], right=1
        3. Bottom row (2,1→2,0): [1,2,3,6,9,8,7], bottom=1
        4. Left col (1,0→1,0): [1,2,3,6,9,8,7,4], left=1
        
        Iteration 2:
        1. Top row (1,1→1,1): [1,2,3,6,9,8,7,4,5], top=2
        2. top > bottom, exit
        
        Result: [1,2,3,6,9,8,7,4,5] ✓
        """
        return self.spiralOrder_template(matrix)
    
    
    def generateMatrix_LC59(self, n: int) -> List[List[int]]:
        """
        LeetCode 59: Spiral Matrix II
        
        Generate n×n matrix filled 1 to n² in spiral order.
        
        Input: n = 3
        Output:
        [[1,2,3],
         [8,9,4],
         [7,6,5]]
        
        🔑 APPROACH: Same boundaries, but FILL instead of READ
        
        Time: O(n²) | Space: O(1)
        """
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        
        while top <= bottom and left <= right:
            # Top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # Right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # Bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # Left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
        
        return matrix
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: SET MATRIX ZEROES
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    If matrix[i][j] == 0, set entire row i and column j to 0.
    Do this in-place with O(1) space.
    
    🔑 KEY INSIGHT:
    Use FIRST ROW and FIRST COLUMN as markers!
    
    Algorithm:
    1. Check if first row/col themselves have zeros (need flags)
    2. Use first row/col to mark which rows/cols need zeroing
       - If matrix[i][j] == 0:
         * Mark matrix[i][0] = 0 (row i needs zeroing)
         * Mark matrix[0][j] = 0 (col j needs zeroing)
    3. Set zeros based on markers (skip first row/col)
    4. Handle first row and column separately using flags
    
    💡 WHY THIS WORKS:
    - First row/col store information about other rows/cols
    - Separate flags preserve original first row/col state
    - Process inner matrix first, then edges
    
    📝 VISUALIZATION:
    Original:        After marking:   After setting:
    [1,1,1]         [1,0,1]          [1,0,1]
    [1,0,1]    →    [0,0,1]     →    [0,0,0]
    [1,1,1]         [1,0,1]          [1,0,1]
    
    matrix[1][1]=0 → mark matrix[1][0]=0, matrix[0][1]=0
    Then set row 1 and col 1 to zero
    
    ⏱️  Time: O(m×n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def setZeroes(matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Mark using first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row/col
        if first_row_zero:
            for j in range(n): matrix[0][j] = 0
        if first_col_zero:
            for i in range(m): matrix[i][0] = 0
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 73. Set Matrix Zeroes ⭐⭐⭐
    ✅ 289. Game of Life
    ✅ 1582. Special Positions in a Binary Matrix
    """
    
    def setZeroes_template(self, matrix: List[List[int]]) -> None:
        """
        🎯 MASTER TEMPLATE: Set matrix zeroes in O(1) space
        
        Use first row and column as markers.
        
        Algorithm:
        1. Check if first row/col have zeros (flags)
        2. Use first row/col to mark zeros in rest of matrix
        3. Set zeros based on markers
        4. Handle first row/col separately
        
        Args:
            matrix: 2D matrix (modified in-place)
        
        Time: O(m*n) | Space: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Step 1: Check if first row/col have zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Step 2: Use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column
        
        # Step 3: Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Handle first row and column
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 5
    # ═══════════════════════════════════════════════════════════════════════
    
    def setZeroes_LC73(self, matrix: List[List[int]]) -> None:
        """
        LeetCode 73: Set Matrix Zeroes
        
        If element is 0, set its entire row and column to 0.
        
        Input:
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
        
        Output:
        [[1,0,1],
         [0,0,0],
         [1,0,1]]
        
        DRY RUN:
        matrix = [[1,1,1],
                  [1,0,1],
                  [1,1,1]]
        
        Step 1: Check first row/col
        first_row_zero = False (no zeros)
        first_col_zero = False (no zeros)
        
        Step 2: Mark zeros
        matrix[1][1] = 0 → mark matrix[1][0]=0, matrix[0][1]=0
        matrix = [[1,0,1],
                  [0,0,1],
                  [1,1,1]]
        
        Step 3: Set zeros based on markers
        Row 1: matrix[1][0]=0 → set entire row 1 to 0
        Col 1: matrix[0][1]=0 → set entire col 1 to 0
        matrix = [[1,0,1],
                  [0,0,0],
                  [1,0,1]] ✓
        """
        self.setZeroes_template(matrix)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: PASCAL'S TRIANGLE
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Generate Pascal's triangle where each number is sum of two numbers above it.
    
    🔑 KEY INSIGHT:
    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    Each row starts and ends with 1.
    
    💡 PATTERN:
    Row 0:           1
    Row 1:         1   1
    Row 2:       1   2   1
    Row 3:     1   3   3   1
    Row 4:   1   4   6   4   1
    
    Building row 4:
    [1] (edge)
    [1, 1+3=4] (triangle[3][0] + triangle[3][1])
    [1, 4, 3+3=6] (triangle[3][1] + triangle[3][2])
    [1, 4, 6, 3+1=4] (triangle[3][2] + triangle[3][3])
    [1, 4, 6, 4, 1] (edge)
    
    📝 OPTIMIZATION FOR SINGLE ROW:
    Instead of building entire triangle, generate row directly using formula:
    row[j] = row[j-1] * (i-j+1) / j
    
    Or iteratively update previous row.
    
    ⏱️  Time: O(n²) for n rows | Space: O(n²)
    
    📝 GENERALIZED TEMPLATE:
    def generate(numRows):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 118. Pascal's Triangle ⭐⭐
    ✅ 119. Pascal's Triangle II ⭐⭐
    
    Medium:
    ✅ 1396. Design Underground System
    """
    
    def generate_pascals_triangle(self, numRows: int) -> List[List[int]]:
        """
        🎯 MASTER TEMPLATE: Generate Pascal's Triangle
        
        Build triangle row by row, each element is sum of two above.
        
        Algorithm:
        1. For each row i (0 to numRows-1):
           - Create row of size i+1 filled with 1s
           - For middle elements: row[j] = prev_row[j-1] + prev_row[j]
           - Append to triangle
        
        Args:
            numRows: Number of rows to generate
        
        Returns:
            Pascal's triangle as list of lists
        
        Time: O(n²) | Space: O(n²)
        """
        triangle = []
        
        for i in range(numRows):
            # Create row of size i+1, all 1s
            row = [1] * (i + 1)
            
            # Fill middle elements
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
        
        return triangle
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 6
    # ═══════════════════════════════════════════════════════════════════════
    
    def generate_LC118(self, numRows: int) -> List[List[int]]:
        """
        LeetCode 118: Pascal's Triangle
        
        Generate first numRows of Pascal's triangle.
        
        Input: numRows = 5
        Output:
        [[1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]]
        
        DRY RUN:
        numRows = 4
        
        i=0: row = [1]
        triangle = [[1]]
        
        i=1: row = [1,1]
        triangle = [[1], [1,1]]
        
        i=2: row = [1,1,1]
        j=1: row[1] = triangle[1][0] + triangle[1][1] = 1+1 = 2
        row = [1,2,1]
        triangle = [[1], [1,1], [1,2,1]]
        
        i=3: row = [1,1,1,1]
        j=1: row[1] = triangle[2][0] + triangle[2][1] = 1+2 = 3
        j=2: row[2] = triangle[2][1] + triangle[2][2] = 2+1 = 3
        row = [1,3,3,1]
        triangle = [[1], [1,1], [1,2,1], [1,3,3,1]] ✓
        """
        return self.generate_pascals_triangle(numRows)
    
    
    def getRow_LC119(self, rowIndex: int) -> List[int]:
        """
        LeetCode 119: Pascal's Triangle II
        
        Return the rowIndex-th row (0-indexed).
        
        Input: rowIndex = 3
        Output: [1,3,3,1]
        
        🔑 SPACE OPTIMIZED: Generate row in-place
        Update from right to left to avoid overwriting values we need.
        
        Time: O(n²) | Space: O(n)
        """
        row = [1]
        
        for i in range(rowIndex):
            # Add 1 at end
            row.append(1)
            
            # Update from right to left
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: NEXT PERMUTATION
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Find next lexicographically greater permutation of array.
    If not possible, return smallest permutation (sorted array).
    
    🔑 KEY INSIGHT (Two-pass algorithm):
    
    Example: [1,3,5,4,2] → [1,4,2,3,5]
    
    Step 1: Find rightmost ascending pair (pivot)
    Scan from right: 2<4 ✗, 4>5 ✗, 5>3 ✗, 3>1 ✓
    Pivot at index 1 (value 3)
    
    Step 2: Find smallest element greater than pivot (from right)
    From right in [5,4,2]: find element > 3
    Found 4 at index 3
    
    Step 3: Swap pivot with this element
    [1,3,5,4,2] → [1,4,5,3,2]
    
    Step 4: Reverse suffix after pivot
    Reverse [5,3,2] → [2,3,5]
    Result: [1,4,2,3,5] ✓
    
    💡 WHY THIS WORKS:
    - Pivot is rightmost position where we can increase value
    - Swapping with next greater ensures minimal increase
    - Reversing suffix makes it smallest possible
    
    📝 EDGE CASE:
    If no ascending pair found (array is descending):
    [5,4,3,2,1] → reverse entire → [1,2,3,4,5]
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def nextPermutation(nums):
        n = len(nums)
        
        # Step 1: Find pivot (rightmost i where nums[i] < nums[i+1])
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find smallest nums[j] > nums[i] from right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse suffix
        nums[i+1:] = reversed(nums[i+1:])
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 31. Next Permutation ⭐⭐⭐
    ✅ 46. Permutations
    ✅ 47. Permutations II
    ✅ 60. Permutation Sequence
    """
    
    def nextPermutation_template(self, nums: List[int]) -> None:
        """
        🎯 MASTER TEMPLATE: Find next permutation
        
        Rearrange numbers into next lexicographically greater permutation.
        If not possible, return lowest permutation.
        
        Algorithm:
        1. Find pivot: rightmost i where nums[i] < nums[i+1]
        2. If pivot exists:
           a. Find smallest nums[j] > nums[i] from right
           b. Swap nums[i] and nums[j]
        3. Reverse suffix after pivot
        
        Args:
            nums: Array to permute (modified in-place)
        
        Example:
            [1,3,5,4,2] → [1,4,2,3,5]
        
        Time: O(n) | Space: O(1)
        """
        n = len(nums)
        
        # Step 1: Find pivot (rightmost ascending pair)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find smallest element > pivot from right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse suffix (makes it smallest)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 7
    # ═══════════════════════════════════════════════════════════════════════
    
    def nextPermutation_LC31(self, nums: List[int]) -> None:
        """
        LeetCode 31: Next Permutation
        
        Rearrange numbers into next lexicographically greater permutation.
        
        Input: nums = [1,2,3]
        Output: [1,3,2]
        
        Input: nums = [3,2,1]
        Output: [1,2,3] (wrap around)
        
        DRY RUN:
        nums = [1,3,5,4,2]
        
        Step 1: Find pivot
        i=3: nums[3]=4 >= nums[4]=2 ✗
        i=2: nums[2]=5 >= nums[3]=4 ✗
        i=1: nums[1]=3 < nums[2]=5 ✓ (pivot found)
        
        Step 2: Find smallest > pivot from right
        j=4: nums[4]=2 <= nums[1]=3 ✗
        j=3: nums[3]=4 > nums[1]=3 ✓
        
        Step 3: Swap
        nums[1]=3 ↔ nums[3]=4
        nums = [1,4,5,3,2]
        
        Step 4: Reverse suffix [5,3,2]
        nums = [1,4,2,3,5] ✓
        """
        self.nextPermutation_template(nums)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: FIND MISSING/DUPLICATE NUMBERS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Find missing or duplicate numbers in array [1..n] with O(1) space.
    
    🔑 KEY TECHNIQUES:
    
    1. MATH APPROACH (for single missing):
       Sum formula: sum(1 to n) = n*(n+1)/2
       Missing = expected_sum - actual_sum
    
    2. XOR APPROACH (for single missing):
       XOR all numbers 1 to n with array elements
       Duplicates cancel out, leaving missing number
    
    3. CYCLIC SORT (for multiple missing/duplicate):
       Place each number at its correct index: nums[i] should be at index i-1
       Numbers not at correct position are missing/duplicate
    
    4. INDEX MARKING (negative marking):
       Use array indices as hash: mark nums[abs(nums[i])-1] as negative
       Positive indices indicate missing, duplicates cause double-negative
    
    💡 EXAMPLE (Cyclic Sort):
    nums = [4,3,2,7,8,2,3,1]
    Goal: Each nums[i] should equal i+1
    
    Process:
    [4,3,2,7,8,2,3,1]
    nums[0]=4 → swap with nums[3]
    [7,3,2,4,8,2,3,1]
    nums[0]=7 → swap with nums[6]
    [3,3,2,4,8,2,7,1]
    nums[0]=3 → swap with nums[2]
    [2,3,3,4,8,2,7,1]
    nums[0]=2 → swap with nums[1]
    [3,2,3,4,8,2,7,1]
    nums[0]=3 already at nums[2], skip (duplicate!)
    ... continue ...
    
    Final: [1,2,3,4,?,?,7,8]
    Missing: 5,6 (positions with duplicates)
    Duplicates: 2,3
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 TEMPLATES:
    
    # Math approach (single missing)
    def findMissing(nums):
        n = len(nums) + 1
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
    
    # Cyclic sort approach
    def cyclicSort(nums):
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 268. Missing Number ⭐⭐⭐
    ✅ 448. Find All Numbers Disappeared in an Array ⭐⭐
    ✅ 136. Single Number (XOR variant)
    
    Medium:
    ✅ 287. Find the Duplicate Number ⭐⭐⭐
    ✅ 442. Find All Duplicates in an Array ⭐⭐
    ✅ 645. Set Mismatch
    """
    
    def findMissing_math(self, nums: List[int]) -> int:
        """
        🎯 TEMPLATE 1: Math approach for single missing number
        
        Use sum formula: missing = expected_sum - actual_sum
        
        Args:
            nums: Array of n-1 numbers from [1..n]
        
        Returns:
            The missing number
        
        Time: O(n) | Space: O(1)
        """
        n = len(nums) + 1  # n numbers, but array has n-1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    
    def findMissing_xor(self, nums: List[int]) -> int:
        """
        🎯 TEMPLATE 2: XOR approach for single missing number
        
        XOR has property: a ⊕ a = 0, a ⊕ 0 = a
        XOR all numbers 1 to n with all array elements.
        Duplicates cancel, leaving missing number.
        
        Args:
            nums: Array of n-1 numbers from [1..n]
        
        Returns:
            The missing number
        
        Time: O(n) | Space: O(1)
        """
        xor_all = 0
        n = len(nums)
        
        # XOR with indices 0 to n
        for i in range(n + 1):
            xor_all ^= i
        
        # XOR with array elements
        for num in nums:
            xor_all ^= num
        
        return xor_all
    
    
    def cyclicSort_template(self, nums: List[int]) -> None:
        """
        🎯 TEMPLATE 3: Cyclic sort for finding missing/duplicates
        
        Place each number at its correct index: nums[i] should be i+1
        
        Algorithm:
        1. For each position, swap until correct number is there
        2. Skip if number already at correct position (duplicate)
        3. After sorting, positions with wrong numbers indicate missing
        
        Args:
            nums: Array to sort cyclically
        
        Time: O(n) | Space: O(1)
        """
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1  # nums[i] should be at index i-1
            
            # Swap if not at correct position
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1  # Move on (either correct or duplicate)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 8
    # ═══════════════════════════════════════════════════════════════════════
    
    def missingNumber_LC268(self, nums: List[int]) -> int:
        """
        LeetCode 268: Missing Number
        
        Find missing number in array [0..n].
        
        Input: nums = [3,0,1]
        Output: 2
        
        DRY RUN (Math):
        nums = [3,0,1], n = 3
        expected_sum = 3 * 4 / 2 = 6
        actual_sum = 3 + 0 + 1 = 4
        missing = 6 - 4 = 2 ✓
        
        DRY RUN (XOR):
        xor_all = 0
        XOR with 0,1,2,3: xor_all = 0⊕1⊕2⊕3
        XOR with array [3,0,1]: xor_all = 0⊕1⊕2⊕3⊕3⊕0⊕1
        Simplify: 2 (pairs cancel) ✓
        """
        # Math approach
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)
    
    
    def findDuplicate_LC287(self, nums: List[int]) -> int:
        """
        LeetCode 287: Find the Duplicate Number
        
        Array contains n+1 numbers from [1..n], one number repeated.
        Find the duplicate without modifying array.
        
        Input: nums = [1,3,4,2,2]
        Output: 2
        
        🔑 APPROACH: Floyd's Cycle Detection (Tortoise & Hare)
        
        Treat array as linked list:
        - nums[i] points to nums[nums[i]]
        - Duplicate creates a cycle
        
        WHY IT WORKS:
        If duplicate is d, two indices point to d → cycle!
        
        Phase 1: Detect cycle (slow and fast meet)
        Phase 2: Find cycle start (that's the duplicate)
        
        Time: O(n) | Space: O(1)
        """
        # Phase 1: Find meeting point
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find cycle start (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
    
    def findDisappearedNumbers_LC448(self, nums: List[int]) -> List[int]:
        """
        LeetCode 448: Find All Numbers Disappeared in an Array
        
        Find all numbers in [1..n] that don't appear.
        
        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [5,6]
        
        🔑 APPROACH: Index marking (negative marking)
        
        Algorithm:
        1. For each nums[i], mark nums[abs(nums[i])-1] as negative
        2. Positive indices indicate missing numbers
        
        Time: O(n) | Space: O(1)
        """
        # Mark indices as negative
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        
        # Find positive indices
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
    
    
    def findDuplicates_LC442(self, nums: List[int]) -> List[int]:
        """
        LeetCode 442: Find All Duplicates in an Array
        
        Find all numbers that appear twice.
        Numbers in [1..n], array size n.
        
        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [2,3]
        
        🔑 APPROACH: Index marking
        When we see nums[i], mark nums[abs(nums[i])-1] as negative.
        If already negative → duplicate!
        
        Time: O(n) | Space: O(1)
        """
        result = []
        
        for num in nums:
            idx = abs(num) - 1
            
            if nums[idx] < 0:
                # Already negative → duplicate
                result.append(abs(num))
            else:
                # Mark as negative
                nums[idx] = -nums[idx]
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: KADANE'S ALGORITHM (Maximum Subarray)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Find contiguous subarray with maximum sum.
    
    🔑 KEY INSIGHT (Kadane's Algorithm):
    At each position, decide:
    - Extend current subarray (current_sum + nums[i])
    - Start new subarray (nums[i])
    
    Choose whichever is larger!
    
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)
    
    💡 WHY THIS WORKS:
    If current_sum becomes negative, it only hurts future sums.
    Better to start fresh from current element.
    
    📝 EXAMPLE:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    i=0: current=-2, max=-2
    i=1: current=max(1, -2+1)=1, max=1
    i=2: current=max(-3, 1-3)=-2, max=1
    i=3: current=max(4, -2+4)=4, max=4
    i=4: current=max(-1, 4-1)=3, max=4
    i=5: current=max(2, 3+2)=5, max=5
    i=6: current=max(1, 5+1)=6, max=6 ✓
    i=7: current=max(-5, 6-5)=1, max=6
    i=8: current=max(4, 1+4)=5, max=6
    
    Maximum sum = 6 (subarray [4,-1,2,1])
    
    📊 VARIATIONS:
    - Standard: Find maximum sum
    - Circular: Array is circular (can wrap around)
    - Product: Maximum product subarray (different handling for negatives)
    - k times: Can delete at most k elements
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 GENERALIZED TEMPLATE:
    def maxSubArray(nums):
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 53. Maximum Subarray ⭐⭐⭐ (MOST ASKED!)
    
    Medium:
    ✅ 152. Maximum Product Subarray ⭐⭐⭐
    ✅ 918. Maximum Sum Circular Subarray ⭐⭐
    ✅ 1749. Maximum Absolute Sum of Any Subarray
    ✅ 1191. K-Concatenation Maximum Sum
    """
    
    def maxSubArray_kadane(self, nums: List[int]) -> int:
        """
        🎯 MASTER TEMPLATE: Kadane's Algorithm
        
        Find maximum sum of contiguous subarray.
        
        Algorithm:
        At each position, decide:
        - Extend current subarray
        - Start new subarray
        Keep track of maximum seen.
        
        Args:
            nums: Input array
        
        Returns:
            Maximum subarray sum
        
        Example:
            nums = [-2,1,-3,4,-1,2,1,-5,4]
            output = 6 (subarray [4,-1,2,1])
        
        Time: O(n) | Space: O(1)
        """
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            # Extend or start new
            current_sum = max(num, current_sum + num)
            
            # Update maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 9
    # ═══════════════════════════════════════════════════════════════════════
    
    def maxSubArray_LC53(self, nums: List[int]) -> int:
        """
        LeetCode 53: Maximum Subarray
        
        Find contiguous subarray with largest sum.
        
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has sum 6
        
        DRY RUN:
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        
        i=0: current=-2, max=-2
        i=1: current=max(1, -2+1)=1, max=1
        i=2: current=max(-3, 1-3)=-2, max=1
        i=3: current=max(4, -2+4)=4, max=4
        i=4: current=max(-1, 4-1)=3, max=4
        i=5: current=max(2, 3+2)=5, max=5
        i=6: current=max(1, 5+1)=6, max=6
        i=7: current=max(-5, 6-5)=1, max=6
        i=8: current=max(4, 1+4)=5, max=6
        
        Result: 6 ✓
        """
        return self.maxSubArray_kadane(nums)
    
    
    def maxProduct_LC152(self, nums: List[int]) -> int:
        """
        LeetCode 152: Maximum Product Subarray
        
        Find contiguous subarray with largest product.
        
        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has product 6
        
        🔑 APPROACH: Track both max and min
        
        Negatives can flip max to min and vice versa!
        
        current_max = max(num, max_so_far * num, min_so_far * num)
        current_min = min(num, max_so_far * num, min_so_far * num)
        
        Time: O(n) | Space: O(1)
        """
        if not nums:
            return 0
        
        max_so_far = min_so_far = result = nums[0]
        
        for num in nums[1:]:
            # Save max before updating (min depends on old max)
            temp_max = max_so_far
            
            # Update max and min
            max_so_far = max(num, temp_max * num, min_so_far * num)
            min_so_far = min(num, temp_max * num, min_so_far * num)
            
            # Update result
            result = max(result, max_so_far)
        
        return result
    
    
    def maxSubarraySumCircular_LC918(self, nums: List[int]) -> int:
        """
        LeetCode 918: Maximum Sum Circular Subarray
        
        Array is circular (can wrap around).
        
        Input: nums = [1,-2,3,-2]
        Output: 3
        Explanation: [3] (or [3,-2,1] wrapping = 2, but [3] is better)
        
        Input: nums = [5,-3,5]
        Output: 10
        Explanation: [5,5] wrapping around
        
        🔑 APPROACH: Two cases
        
        Case 1: Maximum subarray doesn't wrap
        → Standard Kadane's
        
        Case 2: Maximum subarray wraps around
        → Total sum - minimum subarray
        (wrapping max = remove minimum from middle)
        
        Answer = max(case1, case2)
        
        EDGE CASE: If all negative, case2 would remove everything.
        Use case1 in this scenario.
        
        Time: O(n) | Space: O(1)
        """
        def kadane_max(nums):
            current = max_sum = nums[0]
            for num in nums[1:]:
                current = max(num, current + num)
                max_sum = max(max_sum, current)
            return max_sum
        
        def kadane_min(nums):
            current = min_sum = nums[0]
            for num in nums[1:]:
                current = min(num, current + num)
                min_sum = min(min_sum, current)
            return min_sum
        
        max_kadane = kadane_max(nums)
        total_sum = sum(nums)
        min_kadane = kadane_min(nums)
        
        # If all negative, max_kadane is best
        if max_kadane < 0:
            return max_kadane
        
        # Otherwise, compare normal max vs circular max
        max_circular = total_sum - min_kadane
        
        return max(max_kadane, max_circular)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 10: STOCK BUY/SELL (State Machine DP)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Maximize profit from buying and selling stocks with constraints.
    
    🔑 KEY INSIGHT:
    Model as state machine with states:
    - HOLDING: Currently own stock
    - NOT_HOLDING: Don't own stock
    
    Transitions:
    - Buy: NOT_HOLDING → HOLDING (cost = price)
    - Sell: HOLDING → NOT_HOLDING (profit = price)
    
    💡 STATE MACHINE APPROACH:
    
    For each day i, track:
    - cash[i]: Max profit if NOT holding stock
    - hold[i]: Max profit if HOLDING stock
    
    Transitions:
    - cash[i] = max(cash[i-1], hold[i-1] + price[i])  # Don't buy OR sell
    - hold[i] = max(hold[i-1], cash[i-1] - price[i])  # Keep holding OR buy
    
    📊 VARIATIONS:
    
    1. ONE TRANSACTION (LC 121):
       - Buy once, sell once
       - Track min price seen, max profit
    
    2. UNLIMITED TRANSACTIONS (LC 122):
       - Buy and sell as many times as you want
       - Sum all positive differences
    
    3. AT MOST K TRANSACTIONS (LC 188):
       - Use DP with states for each transaction count
    
    4. WITH COOLDOWN (LC 309):
       - After selling, must rest 1 day before buying again
       - Add COOLDOWN state
    
    5. WITH TRANSACTION FEE (LC 714):
       - Pay fee on each transaction
       - Subtract fee from profit on sell
    
    ⏱️  Time: O(n) or O(n*k) | Space: O(1) or O(k)
    
    📝 TEMPLATES:
    
    # Template 1: Unlimited transactions (greedy)
    def maxProfit(prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    # Template 2: State machine (general)
    def maxProfit(prices):
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price)
            hold = max(hold, cash - price)
        return cash
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 121. Best Time to Buy and Sell Stock ⭐⭐⭐
    
    Medium:
    ✅ 122. Best Time to Buy and Sell Stock II ⭐⭐⭐
    ✅ 309. Best Time to Buy/Sell Stock with Cooldown ⭐⭐
    ✅ 714. Best Time to Buy/Sell Stock with Fee ⭐⭐
    
    Hard:
    ✅ 123. Best Time to Buy and Sell Stock III
    ✅ 188. Best Time to Buy and Sell Stock IV
    """
    
    def maxProfit_one_transaction(self, prices: List[int]) -> int:
        """
        🎯 TEMPLATE 1: One transaction (buy once, sell once)
        
        Track minimum price seen so far.
        For each price, calculate profit if we sell today.
        
        Args:
            prices: Stock prices
        
        Returns:
            Maximum profit
        
        Time: O(n) | Space: O(1)
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
    
    
    def maxProfit_unlimited(self, prices: List[int]) -> int:
        """
        🎯 TEMPLATE 2: Unlimited transactions (greedy)
        
        Buy and sell as many times as you want.
        Sum all positive price differences.
        
        Intuition: Buy today, sell tomorrow if profitable.
        
        Args:
            prices: Stock prices
        
        Returns:
            Maximum profit
        
        Time: O(n) | Space: O(1)
        """
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
    
    
    def maxProfit_state_machine(self, prices: List[int]) -> int:
        """
        🎯 TEMPLATE 3: State machine (general approach)
        
        Model as state machine:
        - cash: Max profit when NOT holding stock
        - hold: Max profit when HOLDING stock
        
        Transitions:
        - cash = max(stay_cash, sell_stock)
        - hold = max(stay_hold, buy_stock)
        
        Args:
            prices: Stock prices
        
        Returns:
            Maximum profit
        
        Time: O(n) | Space: O(1)
        """
        cash, hold = 0, -prices[0]
        
        for price in prices[1:]:
            cash = max(cash, hold + price)  # Don't buy OR sell
            hold = max(hold, cash - price)  # Keep holding OR buy
        
        return cash
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 10
    # ═══════════════════════════════════════════════════════════════════════
    
    def maxProfit_LC121(self, prices: List[int]) -> int:
        """
        LeetCode 121: Best Time to Buy and Sell Stock
        
        Buy once, sell once. Maximize profit.
        
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy at 1, sell at 6, profit = 5
        
        DRY RUN:
        prices = [7, 1, 5, 3, 6, 4]
        
        i=0: min=7, profit=max(0, 7-7)=0
        i=1: min=1, profit=max(0, 1-1)=0
        i=2: min=1, profit=max(0, 5-1)=4
        i=3: min=1, profit=max(4, 3-1)=4
        i=4: min=1, profit=max(4, 6-1)=5
        i=5: min=1, profit=max(5, 4-1)=5
        
        Result: 5 ✓
        """
        return self.maxProfit_one_transaction(prices)
    
    
    def maxProfit_LC122(self, prices: List[int]) -> int:
        """
        LeetCode 122: Best Time to Buy and Sell Stock II
        
        Unlimited transactions. Maximize profit.
        
        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy at 1, sell at 5 (profit 4).
                     Buy at 3, sell at 6 (profit 3).
                     Total = 7
        
        DRY RUN:
        prices = [7, 1, 5, 3, 6, 4]
        
        i=1: 1 < 7, no profit
        i=2: 5 > 1, profit += 4, total = 4
        i=3: 3 < 5, no profit
        i=4: 6 > 3, profit += 3, total = 7
        i=5: 4 < 6, no profit
        
        Result: 7 ✓
        """
        return self.maxProfit_unlimited(prices)
    
    
    def maxProfit_LC309(self, prices: List[int]) -> int:
        """
        LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
        
        After selling, must cooldown 1 day before buying again.
        
        Input: prices = [1,2,3,0,2]
        Output: 3
        Explanation: Buy at 1, sell at 2, cooldown, buy at 0, sell at 2
        
        🔑 APPROACH: 3 states
        - HOLDING: Own stock
        - SOLD: Just sold (cooldown next day)
        - RESET: Can buy again
        
        Transitions:
        hold[i] = max(hold[i-1], reset[i-1] - price)
        sold[i] = hold[i-1] + price
        reset[i] = max(reset[i-1], sold[i-1])
        
        Time: O(n) | Space: O(1)
        """
        if not prices:
            return 0
        
        hold = -prices[0]  # Bought first stock
        sold = 0           # Can't sell on day 0
        reset = 0          # Didn't buy
        
        for price in prices[1:]:
            prev_sold = sold
            
            sold = hold + price           # Sell today
            hold = max(hold, reset - price)  # Keep or buy today
            reset = max(reset, prev_sold)    # Rest or was resting
        
        return max(sold, reset)
    
    
    def maxProfit_LC714(self, prices: List[int], fee: int) -> int:
        """
        LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee
        
        Pay fee on each transaction.
        
        Input: prices = [1,3,2,8,4,9], fee = 2
        Output: 8
        Explanation: Buy at 1, sell at 8 (profit 7-2=5).
                     Buy at 4, sell at 9 (profit 5-2=3).
                     Total = 8
        
        🔑 APPROACH: State machine with fee
        Subtract fee when selling.
        
        Time: O(n) | Space: O(1)
        """
        cash, hold = 0, -prices[0]
        
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)  # Sell with fee
            hold = max(hold, cash - price)        # Buy
        
        return cash
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 11: JUMP GAME (Greedy Reachability)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Determine if you can reach the end from start, or minimum jumps needed.
    
    🔑 KEY INSIGHT (Greedy):
    Track the farthest position reachable from current position.
    
    max_reach = max(max_reach, i + nums[i])
    
    If at any point i > max_reach → can't proceed (false)
    If max_reach >= last_index → can reach end (true)
    
    💡 FOR MINIMUM JUMPS:
    Use BFS-like approach with levels:
    - Current level: positions reachable with current jump count
    - Next level: positions reachable with one more jump
    - Track farthest reach of current level
    
    📝 EXAMPLE (Can Jump):
    nums = [2,3,1,1,4]
    
    i=0: nums[0]=2, max_reach = max(0, 0+2) = 2
    i=1: nums[1]=3, max_reach = max(2, 1+3) = 4 ✓ (reached end!)
    
    Can reach end: True
    
    📝 EXAMPLE (Minimum Jumps):
    nums = [2,3,1,1,4]
    
    Jump 0: At index 0, can reach [0,2]
            Farthest = 2
    
    Jump 1: From [1,2], can reach up to:
            From 1: 1+3=4 ✓ (reached end!)
    
    Minimum jumps = 1
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 TEMPLATES:
    
    # Can Jump (greedy)
    def canJump(nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
    
    # Minimum Jumps (BFS-like)
    def jump(nums):
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 55. Jump Game ⭐⭐⭐
    ✅ 45. Jump Game II ⭐⭐⭐
    ✅ 1306. Jump Game III
    ✅ 1345. Jump Game IV
    
    Hard:
    ✅ 1871. Jump Game VII
    """
    
    def canJump_greedy(self, nums: List[int]) -> bool:
        """
        🎯 TEMPLATE 1: Can reach end (greedy)
        
        Track farthest reachable position.
        If current position > farthest → stuck.
        
        Args:
            nums: Array where nums[i] is max jump from index i
        
        Returns:
            True if can reach last index
        
        Time: O(n) | Space: O(1)
        """
        max_reach = 0
        
        for i in range(len(nums)):
            # Can't reach this position
            if i > max_reach:
                return False
            
            # Update farthest reachable
            max_reach = max(max_reach, i + nums[i])
            
            # Already can reach end
            if max_reach >= len(nums) - 1:
                return True
        
        return True
    
    
    def jump_minimum(self, nums: List[int]) -> int:
        """
        🎯 TEMPLATE 2: Minimum jumps to reach end
        
        Use BFS-like approach with levels.
        Each level represents positions reachable with current jump count.
        
        Args:
            nums: Array where nums[i] is max jump from index i
        
        Returns:
            Minimum number of jumps
        
        Time: O(n) | Space: O(1)
        """
        jumps = 0
        current_end = 0  # End of current level
        farthest = 0     # Farthest reachable in next level
        
        for i in range(len(nums) - 1):
            # Update farthest reachable from positions in current level
            farthest = max(farthest, i + nums[i])
            
            # Reached end of current level → need another jump
            if i == current_end:
                jumps += 1
                current_end = farthest  # Move to next level
        
        return jumps
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 11
    # ═══════════════════════════════════════════════════════════════════════
    
    def canJump_LC55(self, nums: List[int]) -> bool:
        """
        LeetCode 55: Jump Game
        
        Determine if you can reach the last index.
        
        Input: nums = [2,3,1,1,4]
        Output: True
        Explanation: Jump 1 step from 0 to 1, then 3 steps to last
        
        DRY RUN:
        nums = [2, 3, 1, 1, 4]
        
        i=0: max_reach = max(0, 0+2) = 2
        i=1: max_reach = max(2, 1+3) = 4 (>= len-1=4) ✓
        
        Result: True ✓
        """
        return self.canJump_greedy(nums)
    
    
    def jump_LC45(self, nums: List[int]) -> int:
        """
        LeetCode 45: Jump Game II
        
        Return minimum number of jumps to reach last index.
        Guaranteed to be reachable.
        
        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: Jump 1 step from 0 to 1, then 3 steps to last
        
        DRY RUN:
        nums = [2, 3, 1, 1, 4]
        
        Level 0 (jumps=0):
        i=0: farthest = max(0, 0+2) = 2
        i=0 == current_end=0 → jumps=1, current_end=2
        
        Level 1 (jumps=1):
        i=1: farthest = max(2, 1+3) = 4
        i=2: farthest = max(4, 2+1) = 4
        i=2 == current_end=2 → jumps=2, current_end=4
        
        i=3: reached len-1, done
        
        Result: 2 ✓
        """
        return self.jump_minimum(nums)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 12: BOYER-MOORE VOTING (Majority Element)
    # ═══════════════════════════════════════════════════════════════════════
# COMMON PATTERN TO SOLVE BOTH MAJORITY ELEMENT 1 and MAJORITY ELEMENT 2 USING HASHMAP
        # def findMajorityElements(nums, k):
        #     """
        #     Find all elements appearing > n/k times
        #     k=2 for >n/2 (Majority Element I) -> only one possible element
        #     k=3 for >n/3 (Majority Element II) -> 2 possible elements
        #     """
        #     counts = Counter(nums)
        #     result = []
        #     threshold = len(nums) // k

        #     for key, val in counts.items():
        #         if val > threshold:
        #             result.append(key)

        #     return result
    """
    🎯 CORE CONCEPT:
    Find element that appears more than ⌊n/2⌋ or ⌊n/3⌋ times with O(1) space.
    
    🔑 KEY INSIGHT (Boyer-Moore Voting):
    Maintain candidate(s) and counter(s).
    
    For majority (> n/2):
    - If count == 0, set current element as candidate
    - If current == candidate, increment count
    - Else decrement count
    
    Intuition: Cancel out pairs of different elements.
    Majority element survives!
    
    💡 WHY THIS WORKS:
    If element appears > n/2 times:
    - Even if all other elements "vote against" it
    - It still has net positive votes
    
    📝 EXAMPLE:
    nums = [2,2,1,1,1,2,2]
    
    i=0: candidate=2, count=1
    i=1: 2==candidate, count=2
    i=2: 1!=candidate, count=1
    i=3: 1!=candidate, count=0
    i=4: count=0, candidate=1, count=1
    i=5: 2!=candidate, count=0
    i=6: count=0, candidate=2, count=1
    
    Candidate = 2 ✓ (appears 4 times > 7/2)
    
    📊 EXTENSION (> n/3):
    Can have at most 2 elements appearing > n/3 times.
    Use TWO candidates and TWO counters!
    
    ⏱️  Time: O(n) | Space: O(1)
    
    📝 TEMPLATE:
    def majorityElement(nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate  # If guaranteed to exist
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 169. Majority Element ⭐⭐⭐
    
    Medium:
    ✅ 229. Majority Element II ⭐⭐
    ✅ 1150. Check If a Number Is Majority Element
    """
    
    def majorityElement_template(self, nums: List[int]) -> int:
        """
        🎯 MASTER TEMPLATE: Boyer-Moore Voting Algorithm
        
        Find element appearing more than ⌊n/2⌋ times.
        
        Algorithm:
        1. Maintain candidate and count
        2. For each element:
           - If count == 0: set as candidate
           - If matches candidate: increment count
           - Else: decrement count
        3. Candidate is the majority element
        
        Args:
            nums: Array (majority element guaranteed to exist)
        
        Returns:
            Majority element
        
        Time: O(n) | Space: O(1)
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            count += (1 if num == candidate else -1)
        
        return candidate
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 12
    # ═══════════════════════════════════════════════════════════════════════
    
    def majorityElement_LC169(self, nums: List[int]) -> int:
        """
        LeetCode 169: Majority Element
        
        Find element appearing more than ⌊n/2⌋ times.
        Guaranteed to exist.
        
        Input: nums = [3,2,3]
        Output: 3
        
        DRY RUN:
        nums = [2, 2, 1, 1, 1, 2, 2]
        
        i=0: count=0 → candidate=2, count=1
        i=1: 2==2 → count=2
        i=2: 1!=2 → count=1
        i=3: 1!=2 → count=0
        i=4: count=0 → candidate=1, count=1
        i=5: 2!=1 → count=0
        i=6: count=0 → candidate=2, count=1
        
        Result: 2 ✓
        """
        return self.majorityElement_template(nums)
    
    
    def majorityElement_II_LC229(self, nums: List[int]) -> List[int]:
        """
        LeetCode 229: Majority Element II
        
        Find all elements appearing more than ⌊n/3⌋ times.
        At most 2 such elements can exist.
        
        Input: nums = [3,2,3]
        Output: [3]
        
        🔑 APPROACH: Two candidates, two counters
        
        Phase 1: Find candidates using voting
        Phase 2: Verify candidates actually appear > n/3 times
        
        Time: O(n) | Space: O(1)
        """
        # Phase 1: Find candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify candidates
        result = []
        threshold = len(nums) // 3
        
        for candidate in [candidate1, candidate2]:
            if candidate is not None and nums.count(candidate) > threshold:
                result.append(candidate)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 13: MERGE SORTED ARRAYS (Two Pointers Merge)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Merge two sorted arrays efficiently.
    
    🔑 KEY INSIGHT:
    Use two pointers, compare elements, place smaller one.
    
    💡 IN-PLACE MERGE (nums1 has extra space):
    Merge from RIGHT to LEFT to avoid overwriting!
    
    Why right to left?
    - nums1 has empty space at end
    - Filling from right preserves unmerged elements
    
    📝 EXAMPLE (In-place):
    nums1 = [1,2,3,0,0,0], m=3
    nums2 = [2,5,6], n=3
    
    Pointers: p1=2 (last of nums1), p2=2 (last of nums2), p=5 (last position)
    
    Step 1: nums1[2]=3 vs nums2[2]=6 → 6 larger
            Place 6 at position 5
            nums1 = [1,2,3,0,0,6], p2=1, p=4
    
    Step 2: nums1[2]=3 vs nums2[1]=5 → 5 larger
            nums1 = [1,2,3,0,5,6], p2=0, p=3
    
    Step 3: nums1[2]=3 vs nums2[0]=2 → 3 larger
            nums1 = [1,2,3,3,5,6], p1=1, p=2
    
    Step 4: nums1[1]=2 vs nums2[0]=2 → equal, take nums2
            nums1 = [1,2,2,3,5,6], p2=-1, p=1
    
    Step 5: Copy remaining nums1
            nums1 = [1,2,2,3,5,6] ✓
    
    ⏱️  Time: O(m+n) | Space: O(1) in-place, O(m+n) with extra array
    
    📝 TEMPLATE:
    def merge(nums1, m, nums2, n):
        p1, p2, p = m-1, n-1, m+n-1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining nums2 (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 88. Merge Sorted Array ⭐⭐⭐
    ✅ 21. Merge Two Sorted Lists (LinkedList variant)
    
    Medium:
    ✅ 986. Interval List Intersections
    """
    
    def merge_template(self, nums1: List[int], m: int, 
                       nums2: List[int], n: int) -> None:
        """
        🎯 MASTER TEMPLATE: Merge sorted arrays in-place
        
        Merge nums2 into nums1 (nums1 has size m+n).
        Fill from right to left to avoid overwriting.
        
        Algorithm:
        1. Three pointers: p1 (last of nums1), p2 (last of nums2), p (last position)
        2. Compare nums1[p1] vs nums2[p2], place larger at p
        3. Copy remaining elements from nums2 if any
        
        Args:
            nums1: First sorted array with extra space
            m: Number of elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        
        Time: O(m+n) | Space: O(1)
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # Merge from right to left
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining elements from nums2 (if any)
        # No need to copy remaining nums1 (already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # LEETCODE PROBLEMS - PATTERN 13
    # ═══════════════════════════════════════════════════════════════════════
    
    def merge_LC88(self, nums1: List[int], m: int, 
                   nums2: List[int], n: int) -> None:
        """
        LeetCode 88: Merge Sorted Array
        
        Merge nums2 into nums1 as one sorted array.
        nums1 has length m+n.
        
        Input: nums1 = [1,2,3,0,0,0], m = 3
               nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        
        DRY RUN:
        nums1 = [1,2,3,0,0,0], m=3
        nums2 = [2,5,6], n=3
        
        p1=2, p2=2, p=5
        
        Step 1: nums1[2]=3 vs nums2[2]=6
                6 > 3 → nums1[5]=6, p2=1, p=4
        
        Step 2: nums1[2]=3 vs nums2[1]=5
                5 > 3 → nums1[4]=5, p2=0, p=3
        
        Step 3: nums1[2]=3 vs nums2[0]=2
                3 > 2 → nums1[3]=3, p1=1, p=2
        
        Step 4: nums1[1]=2 vs nums2[0]=2
                2 == 2 → nums1[2]=2, p2=-1, p=1
        
        Step 5: p2 < 0, done
        
        Result: [1,2,2,3,5,6] ✓
        """
        self.merge_template(nums1, m, nums2, n)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 14: ARRAY REARRANGEMENT
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Rearrange array elements according to specific pattern.
    
    🔑 COMMON PATTERNS:
    
    1. SEPARATE POSITIVE/NEGATIVE:
       - Two pointers: left (negative), right (positive)
       - Partition like quicksort
    
    2. ALTERNATE POSITIVE/NEGATIVE:
       - Separate first, then interleave
       - Or use extra space to build directly
    
    3. CYCLIC ROTATION:
       - Place each element at its correct position
       - Swap until cycle completes
    
    💡 TECHNIQUE: Dutch National Flag
    For partitioning into 3 categories (0s, 1s, 2s):
    - low pointer: boundary of 0s
    - high pointer: boundary of 2s
    - mid pointer: current element
    
    📝 EXAMPLE (Sort Colors - Dutch Flag):
    nums = [2,0,2,1,1,0]
    
    low=0, mid=0, high=5
    
    Step 1: nums[0]=2 → swap with high
            [0,0,2,1,1,2], high=4
    
    Step 2: nums[0]=0 → swap with low
            [0,0,2,1,1,2], low=1, mid=1
    
    Step 3: nums[1]=0 → swap with low
            [0,0,2,1,1,2], low=2, mid=2
    
    Step 4: nums[2]=2 → swap with high
            [0,0,1,1,2,2], high=3
    
    Step 5: nums[2]=1 → correct, mid++
    Step 6: nums[3]=1 → correct, mid++
    Step 7: mid > high, done
    
    Result: [0,0,1,1,2,2] ✓
    
    ⏱️  Time: O(n) | Space: O(1)
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 75. Sort Colors (Dutch National Flag) ⭐⭐⭐
    ✅ 2149. Rearrange Array Elements by Sign ⭐⭐
    ✅ 324. Wiggle Sort II
    ✅ 280. Wiggle Sort
    """
    
    def sortColors_dutch_flag(self, nums: List[int]) -> None:
        """
        🎯 TEMPLATE: Dutch National Flag Algorithm
        
        Sort array of 0s, 1s, 2s in one pass.
        
        Algorithm:
        - low: boundary of 0s
        - high: boundary of 2s
        - mid: current element
        
        If nums[mid] == 0: swap with low, move both
        If nums[mid] == 1: move mid
        If nums[mid] == 2: swap with high, move high down
        
        Args:
            nums: Array of 0s, 1s, 2s (modified in-place)
        
        Time: O(n) | Space: O(1)
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap with low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Correct position, move on
                mid += 1
            else:  # nums[mid] == 2
                # Swap with high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Don't move mid (need to check swapped element)
    
    
    def rearrangeArray_LC2149(self, nums: List[int]) -> List[int]:
        """
        LeetCode 2149: Rearrange Array Elements by Sign
        
        Rearrange so every consecutive pair has opposite signs.
        Equal positive and negative numbers.
        
        Input: nums = [3,1,-2,-5,2,-4]
        Output: [3,-2,1,-5,2,-4]
        
        🔑 APPROACH: Two pointers for positive/negative positions
        
        Time: O(n) | Space: O(n)
        """
        n = len(nums)
        result = [0] * n
        pos_idx, neg_idx = 0, 1  # Positive at even, negative at odd
        
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
        
        return result


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 30 MUST-KNOW PROBLEMS (RANKED BY IMPORTANCE)
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 ABSOLUTE MUST-KNOW (Top 10):
═══════════════════════════════════════════════════════════════════════════
1. ⭐⭐⭐ LC 26: Remove Duplicates from Sorted Array
   - Pattern 1 | Companies: ALL
   
2. ⭐⭐⭐ LC 189: Rotate Array
   - Pattern 2 | Companies: Microsoft, Amazon, Google
   
3. ⭐⭐⭐ LC 238: Product of Array Except Self
   - Pattern 3 | Companies: Amazon, Microsoft, Facebook, Apple
   
4. ⭐⭐⭐ LC 54: Spiral Matrix
   - Pattern 4 | Companies: Amazon, Microsoft, Google
   
5. ⭐⭐⭐ LC 73: Set Matrix Zeroes
   - Pattern 5 | Companies: Amazon, Microsoft, Apple
   
6. ⭐⭐⭐ LC 53: Maximum Subarray (Kadane's)
   - Pattern 9 | Companies: ALL (most asked!)
   
7. ⭐⭐⭐ LC 121: Best Time to Buy and Sell Stock
   - Pattern 10 | Companies: ALL
   
8. ⭐⭐⭐ LC 55: Jump Game
   - Pattern 11 | Companies: Amazon, Google, Microsoft
   
9. ⭐⭐⭐ LC 169: Majority Element
   - Pattern 12 | Companies: Google, Facebook, Amazon
   
10. ⭐⭐⭐ LC 88: Merge Sorted Array
    - Pattern 13 | Companies: Microsoft, Amazon, Facebook


🔥🔥 VERY IMPORTANT (Next 10):
═══════════════════════════════════════════════════════════════════════════
11. ⭐⭐ LC 80: Remove Duplicates from Sorted Array II
12. ⭐⭐ LC 48: Rotate Image (Matrix 90°)
13. ⭐⭐ LC 118: Pascal's Triangle
14. ⭐⭐ LC 31: Next Permutation
15. ⭐⭐ LC 268: Missing Number
16. ⭐⭐ LC 287: Find the Duplicate Number
17. ⭐⭐ LC 152: Maximum Product Subarray
18. ⭐⭐ LC 122: Best Time to Buy and Sell Stock II
19. ⭐⭐ LC 45: Jump Game II
20. ⭐⭐ LC 75: Sort Colors (Dutch Flag)


🔥 IMPORTANT (Complete Foundation):
═══════════════════════════════════════════════════════════════════════════
21. ⭐ LC 27: Remove Element
22. ⭐ LC 283: Move Zeroes
23. ⭐ LC 59: Spiral Matrix II
24. ⭐ LC 119: Pascal's Triangle II
25. ⭐ LC 448: Find All Numbers Disappeared
26. ⭐ LC 442: Find All Duplicates
27. ⭐ LC 918: Maximum Sum Circular Subarray
28. ⭐ LC 309: Best Time to Buy/Sell Stock with Cooldown
29. ⭐ LC 714: Best Time to Buy/Sell Stock with Fee
30. ⭐ LC 229: Majority Element II


═══════════════════════════════════════════════════════════════════════════
📊 4-WEEK STUDY PLAN:
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - In-Place Modification & Rotation:
Day 1: Pattern 1 (Remove Duplicates) - LC 26, 80, 27, 283
Day 2: Pattern 2 (Rotation) - LC 189, 48
Day 3: Pattern 3 (Product Except Self) - LC 238
Day 4: Practice all Week 1 problems
Day 5: Timed practice (30 min per problem)
Day 6-7: Review and redo mistakes

WEEK 2 - Matrix Patterns & Combinatorics:
Day 1: Pattern 4 (Spiral) - LC 54, 59
Day 2: Pattern 5 (Set Zeroes) - LC 73
Day 3: Pattern 6 (Pascal's Triangle) - LC 118, 119
Day 4: Pattern 7 (Next Permutation) - LC 31
Day 5: Practice all Week 2 problems
Day 6-7: Review and redo mistakes

WEEK 3 - Missing/Duplicate & Kadane's:
Day 1: Pattern 8 (Missing/Duplicate) - LC 268, 287, 448, 442
Day 2: Pattern 9 (Kadane's) - LC 53, 152, 918
Day 3: Pattern 10 (Stock Problems) - LC 121, 122, 309, 714
Day 4: Practice all Week 3 problems
Day 5: Timed practice
Day 6-7: Review and redo mistakes

WEEK 4 - Advanced Patterns & Mock Interviews:
Day 1: Pattern 11 (Jump Game) - LC 55, 45
Day 2: Pattern 12 (Boyer-Moore) - LC 169, 229
Day 3: Pattern 13-14 (Merge & Rearrange) - LC 88, 75, 2149
Day 4: Mixed practice (all patterns)
Day 5-6: Timed mock interviews (45 min each)
Day 7: Review weak areas


═══════════════════════════════════════════════════════════════════════════
💡 INTERVIEW TIPS:
═══════════════════════════════════════════════════════════════════════════

✅ ALWAYS DO THESE:
1. Ask about modifying in-place vs creating new array
2. Clarify if array is sorted (many patterns require this)
3. Check for edge cases: empty array, single element, all same
4. State time/space complexity before coding

❌ NEVER DO THESE:
1. Modify input without permission
2. Use extra space when O(1) is possible
3. Forget to handle negative numbers (especially in product/sum problems)
4. Ignore integer overflow in product calculations

🎯 PATTERN SELECTION CHEAT SHEET:
═══════════════════════════════════════════════════════════════════════════
Remove duplicates in-place      → Pattern 1 (index pointer)
Rotate array                    → Pattern 2 (reversal)
Product without division        → Pattern 3 (left-right products)
Traverse matrix spirally        → Pattern 4 (boundary shrinking)
Set entire row/col to zero      → Pattern 5 (first row/col markers)
Generate Pascal's triangle      → Pattern 6 (DP generation)
Next lexicographic permutation  → Pattern 7 (two-pass swap)
Find missing/duplicate          → Pattern 8 (math/cyclic/XOR)
Maximum subarray sum            → Pattern 9 (Kadane's)
Stock buy/sell optimization     → Pattern 10 (state machine)
Can reach end / min jumps       → Pattern 11 (greedy reachability)
Majority element                → Pattern 12 (Boyer-Moore voting)
Merge sorted arrays             → Pattern 13 (two pointers)
Rearrange/partition elements    → Pattern 14 (Dutch flag)


═══════════════════════════════════════════════════════════════════════════
🎓 FINAL TIPS FOR SUCCESS:
═══════════════════════════════════════════════════════════════════════════

1. Master the templates - they are universal!
2. Practice dry runs on paper (builds intuition)
3. Time yourself - aim for 25-30 minutes per medium
4. Understand WHY patterns work, not just HOW
5. Review mistakes immediately after solving
6. Do problems multiple times until pattern recognition is instant
7. Focus on Top 10 first - they cover 80% of interviews

Good luck! 🚀
"""