from typing import List

"""
═══════════════════════════════════════════════════════════════════════════════
                    BINARY SEARCH MASTERY GUIDE
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. INCLUSIVE vs EXCLUSIVE - WHY DOES IT MATTER?

   INCLUSIVE [left, right]:
   - Both boundaries are VALID indices we can access
   - right = n - 1 (last valid index)
   - Loop: while left <= right (check all elements including when left==right)
   - Update: right = mid - 1 (completely exclude mid)
   - Use: When finding if element EXISTS
   
   EXCLUSIVE [left, right):
   - left is valid, right is ONE PAST the valid range
   - right = n (can be outside array!)
   - Loop: while left < right (stop when they meet)
   - Update: right = mid (keep mid as possibility)
   - Use: When finding BOUNDARIES or INSERTION POINTS
   
2. WHY EXCLUSIVE CAN POINT OUTSIDE ARRAY?

   Consider: [1, 3, 5, 7], find insertion point for 8
   
   With EXCLUSIVE:
   - right = 4 (outside array) is VALID answer
   - Means "insert after all elements"
   - left will eventually reach 4, indicating position
   
   With INCLUSIVE:
   - right = 3 (last element)
   - Cannot represent "insert at end"
   - Would need special case handling
   
   EXCLUSIVE naturally handles edge cases!

3. THE GOLDEN RULE:
   - Classic search (exists?) → INCLUSIVE
   - Find boundary/position → EXCLUSIVE

═══════════════════════════════════════════════════════════════════════════════
"""


class BinarySearchMastery:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: CLASSIC BINARY SEARCH (INCLUSIVE)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find if target EXISTS in sorted array (return ANY occurrence)
    
    📊 TEMPLATE: INCLUSIVE [left, right]
    ⏱️  Time: O(log n) | Space: O(1)
    
    🔑 KEY CHARACTERISTICS:
    - right = n - 1 (last valid index)
    - while left <= right (can check when equal)
    - right = mid - 1 (completely exclude mid)
    - Return -1 if not found
    
    📝 DRY RUN EXAMPLE:
    Array: [1, 3, 5, 7, 9], target = 7
    
    Initial: left=0, right=4, range=[1,3,5,7,9]
    
    Step 1: mid = (0+4)//2 = 2
            nums[2] = 5
            5 < 7, so search right half
            left = mid + 1 = 3
            Range: [7,9]
    
    Step 2: left=3, right=4
            mid = (3+4)//2 = 3
            nums[3] = 7 ✓ FOUND!
            return 3
    
    DRY RUN - NOT FOUND:
    Array: [1, 3, 5, 7, 9], target = 6
    
    Initial: left=0, right=4
    
    Step 1: mid=2, nums[2]=5, 5<6 → left=3
    Step 2: left=3, right=4, mid=3, nums[3]=7, 7>6 → right=2
    Step 3: left=3, right=2, left > right → STOP
            return -1 (not found)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 704: Binary Search (easy)
    - LeetCode 374: Guess Number Higher or Lower
    - LeetCode 367: Valid Perfect Square
    - LeetCode 69. Sqrt(x)
    """
    
    def classic_binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # INCLUSIVE: last valid index in array
        
        # Continue while there are elements to check
        # Using <= because we need to check the case when left == right
        while left <= right:
            # Calculate mid (prevents integer overflow in other languages)
            mid = left + (right - left) // 2
            
            # Case 1: Found the target
            if nums[mid] == target:
                return mid
            
            # Case 2: Target is in right half
            elif nums[mid] < target:
                left = mid + 1  # Exclude mid, search right
            
            # Case 3: Target is in left half
            else:  # nums[mid] > target
                right = mid - 1  # Exclude mid, search left (COMPLETELY EXCLUDE)
        
        # Target not found in array
        return -1
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: LOWER BOUND (FIRST OCCURRENCE / LEFT BOUNDARY)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find FIRST occurrence OR insertion position (leftmost boundary)
    
    📊 TEMPLATE: EXCLUSIVE [left, right)
    ⏱️  Time: O(log n) | Space: O(1)
    
    🔑 KEY CHARACTERISTICS:
    - right = n (EXCLUSIVE - one past last index)
    - while left < right (stop when they meet)
    - right = mid (KEEP mid as possible answer)
    - Can return n (insertion point after last element)
    
    🌟 WHY EXCLUSIVE HERE?
    If all elements are < target, answer is n (insert at end)
    Example: [1,2,3], target=5 → should return 3 (insert after all)
    With inclusive (right=2), we can't represent position 3!
    
    📝 DRY RUN EXAMPLE 1 (Target exists):
    Array: [1, 2, 2, 2, 3, 4], target = 2
    
    Goal: Find FIRST occurrence of 2 (index 1)
    
    Initial: left=0, right=6 (EXCLUSIVE - outside array!)
             Search space: [1,2,2,2,3,4]
    
    Step 1: mid = (0+6)//2 = 3
            nums[3] = 2
            2 >= 2 (found, but might not be first!)
            right = mid = 3 (KEEP mid as candidate)
            Search space: [1,2,2] (indices 0,1,2)
    
    Step 2: left=0, right=3
            mid = (0+3)//2 = 1
            nums[1] = 2
            2 >= 2 (still moving left to find first)
            right = mid = 1
            Search space: [1,2] (indices 0,1)
    
    Step 3: left=0, right=1
            mid = (0+1)//2 = 0
            nums[0] = 1
            1 < 2 (not our target)
            left = mid + 1 = 1
            Search space: [2] (index 1)
    
    Step 4: left=1, right=1 → STOP (left == right)
            Check: nums[1] = 2 ✓
            return 1 (first occurrence!)
    
    📝 DRY RUN EXAMPLE 2 (Insert at end):
    Array: [1, 2, 3], target = 5
    
    Goal: Find where to insert 5 (should be index 3 - OUTSIDE ARRAY!)
    
    Initial: left=0, right=3 (EXCLUSIVE)
    
    Step 1: mid = (0+3)//2 = 1
            nums[1] = 2
            2 < 5
            left = mid + 1 = 2
    
    Step 2: left=2, right=3
            mid = (2+3)//2 = 2
            nums[2] = 3
            3 < 5
            left = mid + 1 = 3
    
    Step 3: left=3, right=3 → STOP
            return 3 (insert at end - THIS IS WHY WE USE EXCLUSIVE!)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 35: Search Insert Position (easy) ⭐
    - LeetCode 34: Find First and Last Position (medium) ⭐⭐
    - LeetCode 278: First Bad Version (easy)
    """
    
    def lower_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # EXCLUSIVE: one past the last valid index
        
        # INVARIANT: answer is in [left, right)
        # Stop when left == right (they converge to answer)
        while left < right:
            mid = left + (right - left) // 2
            
            # If current element is less than target
            # Answer must be to the right (exclude mid and left)
            if nums[mid] < target:
                left = mid + 1  # Exclude mid, it's too small
            
            # If current element >= target
            # mid could be the answer (or answer is to the left)
            # KEEP mid in the search space by setting right = mid
            else:  # nums[mid] >= target
                right = mid  # DON'T exclude mid! It might be first occurrence
        
        # At this point, left == right
        # This is the insertion position or first occurrence
        
        # Verify the element exists and matches target
        # (handle case where target doesn't exist)
        if left < len(nums) and nums[left] == target:
            return left  # Found first occurrence
        return -1  # Target doesn't exist (or return left for insertion point)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: UPPER BOUND (LAST OCCURRENCE / RIGHT BOUNDARY)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find LAST occurrence OR position after last occurrence
    
    📊 TEMPLATE: EXCLUSIVE [left, right)
    ⏱️  Time: O(log n) | Space: O(1)
    
    🔑 KEY CHARACTERISTICS:
    - right = n (EXCLUSIVE)
    - while left < right
    - Use <= instead of < in condition
    - Move left PAST target to find boundary
    - Return left - 1 (go back one position)
    
    🌟 THE TRICK:
    Find first element GREATER than target, then go back one step!
    
    📝 DRY RUN EXAMPLE:
    Array: [1, 2, 2, 2, 3, 4], target = 2
    
    Goal: Find LAST occurrence of 2 (index 3)
    
    Initial: left=0, right=6 (EXCLUSIVE)
             Search space: [1,2,2,2,3,4]
    
    Step 1: mid = (0+6)//2 = 3
            nums[3] = 2
            2 <= 2 (found, but might not be last!)
            left = mid + 1 = 4 (MOVE PAST IT!)
            Search space: [3,4] (indices 4,5)
    
    Step 2: left=4, right=6
            mid = (4+6)//2 = 5
            nums[5] = 4
            4 > 2 (too large)
            right = mid = 5
            Search space: [3] (index 4)
    
    Step 3: left=4, right=5
            mid = (4+5)//2 = 4
            nums[4] = 3
            3 > 2 (too large)
            right = mid = 4
    
    Step 4: left=4, right=4 → STOP
            left now points to first element > target
            Last occurrence = left - 1 = 3 ✓
            Check: nums[3] = 2 ✓
            return 3
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 34: Find First and Last Position (medium) ⭐⭐
    - LeetCode 744: Find Smallest Letter Greater Than Target
    - LeetCode 2300: Successful Pairs of Spells and Potions
    - LeetCode 69: Sqrt(x) (easy)
    """
    
    def upper_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # EXCLUSIVE
        
        # Find first element GREATER than target
        while left < right:
            mid = left + (right - left) // 2
            
            # KEY DIFFERENCE: Use <= instead of <
            # This moves us PAST all occurrences of target
            if nums[mid] <= target:  # Even if equal, keep moving right!
                left = mid + 1  # Move past this element
            
            # Found element greater than target
            else:  # nums[mid] > target
                right = mid  # This could be the boundary
        
        # left now points to first element > target
        # So last occurrence is at left - 1
        last_occurrence = left - 1
        
        # Verify it exists and is valid
        if last_occurrence >= 0 and nums[last_occurrence] == target:
            return last_occurrence
        return -1  # Target doesn't exist
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: SEARCH IN ROTATED SORTED ARRAY
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Array rotated at unknown pivot [4,5,6,7,0,1,2]
    
    📊 TEMPLATE: INCLUSIVE [left, right]
    ⏱️  Time: O(log n) | Space: O(1)
    
    🔑 KEY INSIGHT:
    In rotated array, one half is ALWAYS sorted!
    - If left <= mid: left half is sorted
    - Else: right half is sorted
    Then check if target is in the sorted half
    
    📝 DRY RUN EXAMPLE:
    Array: [4, 5, 6, 7, 0, 1, 2], target = 0
    
    Initial: left=0, right=6
    
    Step 1: mid = 3, nums[3] = 7
            nums[0]=4 <= nums[3]=7 → left half [4,5,6,7] is sorted
            Is target 0 in [4,7]? NO (0 < 4)
            Search right half: left = 4
    
    Step 2: left=4, right=6, mid=5
            nums[5] = 1
            nums[4]=0 <= nums[5]=1 → left half [0,1] is sorted  
            Is target 0 in [0,1]? YES! (0 <= 0 < 1)
            Search left half: right = 4
    
    Step 3: left=4, right=4, mid=4
            nums[4] = 0 ✓ FOUND!
            return 4
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 33: Search in Rotated Sorted Array (medium) ⭐⭐
    - LeetCode 81: Search in Rotated Sorted Array II (medium)
    - LeetCode 153: Find Minimum in Rotated Sorted Array (medium)
    - LeetCode 154: Find Minimum in Rotated Sorted Array II (hard)
    """
    
    def search_rotated(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # INCLUSIVE
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Determine which half is properly sorted
            # Check if LEFT half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted: [left...mid] is in order
                
                # Check if target is within sorted left half
                if nums[left] <= target < nums[mid]:
                    # Target is in sorted left half
                    right = mid - 1
                else:
                    # Target is in right half (which contains the rotation)
                    left = mid + 1
            
            # RIGHT half must be sorted
            else:
                # Right half is sorted: [mid...right] is in order
                
                # Check if target is within sorted right half
                if nums[mid] < target <= nums[right]:
                    # Target is in sorted right half
                    left = mid + 1
                else:
                    # Target is in left half (which contains the rotation)
                    right = mid - 1
        
        return -1  # Target not found
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: FIND MINIMUM IN ROTATED ARRAY
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find minimum element in rotated sorted array
    
    📊 TEMPLATE: EXCLUSIVE [left, right)
    ⏱️  Time: O(log n) | Space: O(1)
    
    🔑 KEY INSIGHT:
    - Compare mid with RIGHT boundary
    - If nums[mid] > nums[right]: min is in right half
    - Else: min is in left half (including mid)
    
    📝 DRY RUN EXAMPLE:
    Array: [4, 5, 6, 7, 0, 1, 2]
    
    Goal: Find minimum (0 at index 4)
    
    Initial: left=0, right=6
    
    Step 1: mid = 3, nums[3] = 7, nums[6] = 2
            7 > 2 → minimum is in right half
            left = 4
    
    Step 2: left=4, right=6, mid=5
            nums[5] = 1, nums[6] = 2
            1 < 2 → minimum is in left half (including mid)
            right = 5
    
    Step 3: left=4, right=5, mid=4
            nums[4] = 0, nums[5] = 1
            0 < 1 → minimum is in left half
            right = 4
    
    Step 4: left=4, right=4 → STOP
            return nums[4] = 0 ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 153: Find Minimum in Rotated Sorted Array (medium) ⭐
    - LeetCode 154: Find Minimum in Rotated Sorted Array II (hard)
    """
    
    def find_min_rotated(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1  # Can use inclusive here
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare mid with RIGHT boundary
            # If mid > right, the rotation/minimum is in right half
            if nums[mid] > nums[right]:
                # Minimum is in right half (mid cannot be minimum)
                left = mid + 1
            else:
                # Minimum is in left half or at mid
                # (includes the case where array is not rotated)
                right = mid  # Keep mid as candidate
        
        # left and right converge to minimum
        return nums[left]
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: SEARCH IN 2D MATRIX (Treat as 1D)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Search in row-wise and column-wise sorted matrix
    
    📊 TEMPLATE: INCLUSIVE [left, right]
    ⏱️  Time: O(log(m*n)) | Space: O(1)
    
    🔑 KEY INSIGHT:
    Treat 2D matrix as flattened 1D array!
    - 1D index → 2D: row = idx // cols, col = idx % cols
    - 2D index → 1D: idx = row * cols + col
    
    📝 DRY RUN EXAMPLE:
    Matrix: [[1,  3,  5,  7],    target = 3
             [10, 11, 16, 20],
             [23, 30, 34, 60]]
    
    Treat as: [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
    
    m=3 rows, n=4 cols, total=12 elements
    
    Initial: left=0, right=11
    
    Step 1: mid = 5
            row = 5 // 4 = 1, col = 5 % 4 = 1
            matrix[1][1] = 11
            11 > 3 → search left
            right = 4
    
    Step 2: left=0, right=4, mid=2
            row = 2 // 4 = 0, col = 2 % 4 = 2
            matrix[0][2] = 5
            5 > 3 → search left
            right = 1
    
    Step 3: left=0, right=1, mid=0
            row=0, col=0
            matrix[0][0] = 1
            1 < 3 → search right
            left = 1
    
    Step 4: left=1, right=1, mid=1
            row=0, col=1
            matrix[0][1] = 3 ✓ FOUND!
            return True
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 74: Search a 2D Matrix (medium) ⭐
    - LeetCode 240: Search a 2D Matrix II (medium)
    """
    
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = m * n - 1  # INCLUSIVE: last element in flattened array
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Convert 1D index to 2D coordinates
            row = mid // n  # Which row? (integer division)
            col = mid % n   # Which column? (remainder)
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: FIND PEAK ELEMENT
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find any peak (element greater than neighbors)
    
    📊 TEMPLATE: EXCLUSIVE [left, right)
    ⏱️  Time: O(log n) | Space: O(1)
    
    🔑 KEY INSIGHT:
    If nums[mid] < nums[mid+1]: peak must be in right (upward slope)
    Else: peak is at mid or left (we're at peak or downward slope)
    
    📝 DRY RUN EXAMPLE:
    Array: [1, 2, 1, 3, 5, 6, 4]
                            ↑ peak at index 5
    
    Initial: left=0, right=6
    
    Step 1: mid = 3, nums[3]=3, nums[4]=5
            3 < 5 → upward slope, peak is right
            left = 4
    
    Step 2: left=4, right=6, mid=5
            nums[5]=6, nums[6]=4
            6 > 4 → we found peak!
            right = 5
    
    Step 3: left=5, right=5 → STOP
            return 5 ✓ (6 is greater than both neighbors)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 162: Find Peak Element (medium) ⭐
    - LeetCode 852: Peak Index in a Mountain Array (easy)
    - LeetCode 1095: Find in Mountain Array (hard)
    """
    
    def find_peak_element(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1  # Can use inclusive
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare with next element
            # If going uphill, peak is to the right
            if nums[mid] < nums[mid + 1]:
                # Upward slope → peak is in right half
                left = mid + 1
            else:
                # Downward slope or peak → peak is at mid or left
                right = mid  # Keep mid as candidate
        
        # left and right converge to a peak
        return left


        # 🎯 PEAK ELEMENT: Explicit boundary checking approach
        
        # A peak is where both neighbors are smaller (or don't exist)
        # - If going uphill (right > curr) → peak must be on RIGHT
        # - If going downhill (right < curr) → peak is at curr or LEFT
        
        # Time: O(log n) | Space: O(1)


        def optimal_sol():
            """
            They want us to solve in logn time complexity clear hint of using a binary search, so now instead of doing linear pass lets simple do binary search, but how do we decide to move left or right???? 
            well the trick is upward slope and downward slope.
            so lets say we are at the mid and check left and right if the right side val is high by inutuion the peak element is on right side because
            case 1: if cur mid is less the right then right might be a peak elem if right next ele is less than right
            case 2 : if right next element is not less then that elem might be peak if we keep on going we will either be at the end of the list where the end of list is great and out of bound is always less so it is peak or we find the peak element. 
            similar logic for left too 
            so choose to move on side which is greater than cur mid and it works if monotically increase or non monotically incresaeing 
            """
            n = len(nums)
            lo = 0
            hi = len(nums) - 1
            while lo <= hi: # simple trick if we return inside the while loop then use the lo <= hi code or if we return outside liek return lo we use lo < hi in while loop, bcz you can dry run and see if lo < hi we meet at the result lo == hi == res so we return outside and if we also proceed with lo <= hi so we need to excplitily have return tatement inside the while loop other wise left and right crosses each otehr and creates a bug 
                m = (lo+hi)//2
                #condition if the cur mid is peak return 
                if ((m - 1  < 0 or nums[m-1] < nums[m]) and 
                        (m+1 >= n or nums[m+1] < nums[m])):
                        return m
                #if peak element is on right move right
                elif nums[m] < nums[m+1]:
                    lo = m+ 1
                # if peak is left move left
                else:
                    hi = m - 1
            return -1 #if ans not found 
        return optimal_sol()
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: MINIMIZE/MAXIMIZE - CAPACITY PROBLEMS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find minimum capacity to satisfy constraint
    
    📊 TEMPLATE: EXCLUSIVE [left, right)
    ⏱️  Time: O(n * log(range)) | Space: O(1)
    
    🔑 KEY INSIGHT:
    Binary search on ANSWER SPACE, not array indices!
    - If capacity works → try smaller (minimize)
    - If capacity fails → need larger
    
    📝 PROBLEM: Ship packages within D days
    weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    
    Question: What's the minimum ship capacity needed?
    
    Answer space: [10, 55] (max weight to sum of all)
    
    Initial: left=10 (must fit heaviest), right=55 (fit all)
    
    Step 1: mid = 32
            Can ship with capacity 32 in 5 days?
            Day1: 1+2+3+4+5+6+7+8 = 32 ✗ (exceeds, need new day)
            Simulation: Yes, it works!
            Try smaller: right = 32
    
    Step 2: left=10, right=32, mid=21
            Can ship with 21? Yes!
            right = 21
    
    Step 3: left=10, right=21, mid=15
            Can ship with 15? Yes!
            right = 15
    
    Step 4: left=10, right=15, mid=12
            Can ship with 12? No (10+2 = 12, then 3 alone, too many days)
            left = 13
    
    Continue until left=right=15 (minimum capacity)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 1011: Capacity To Ship Packages Within D Days (medium) ⭐⭐
    - LeetCode 875: Koko Eating Bananas (medium) ⭐⭐
    - LeetCode 1482: Minimum Number of Days to Make m Bouquets (medium)
    - LeetCode 410: Split Array Largest Sum (hard)
    """
    
    def ship_within_days(self, weights: List[int], days: int) -> int:
        # Helper function: can we ship with this capacity?
        def can_ship(capacity):
            days_needed = 1  # Start with day 1
            current_load = 0
            
            for weight in weights:
                # If adding this weight exceeds capacity
                if current_load + weight > capacity:
                    # Need a new day
                    days_needed += 1
                    current_load = weight  # Start new day with this weight
                    
                    # If we exceed allowed days, this capacity fails
                    if days_needed > days:
                        return False
                else:
                    # Add to current day's load
                    current_load += weight
            
            return True  # Successfully shipped in time
        
        # Answer space: [heaviest item, sum of all items]
        left = max(weights)   # Minimum: must fit heaviest item
        right = sum(weights)  # Maximum: fit everything in one day
        
        # Find minimum capacity that works
        while left < right:
            mid = left + (right - left) // 2
            
            # If this capacity works, try smaller
            if can_ship(mid):
                right = mid  # mid works, try smaller
            else:
                # This capacity fails, need larger
                left = mid + 1
        
        return left  # Minimum capacity found
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: KTH ELEMENT IN SORTED MATRIX/RANGE
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find kth smallest in multiplication table or sorted structure
    
    📊 TEMPLATE: EXCLUSIVE [left, right)
    ⏱️  Time: O(m * log(m*n)) | Space: O(1)
    
    🔑 KEY INSIGHT:
    Binary search on VALUE, count how many are <= mid
    
    📝 PROBLEM: Find 3rd smallest in 3x3 multiplication table
    m=3, n=3, k=3
    
    Table: 1  2  3
           2  4  6
           3  6  9
    
    Sorted: [1,2,2,3,3,4,6,6,9]
                  ↑ 3rd smallest = 2
    
    Answer space: [1, 9] (min value to max value)
    
    Helper: count_less_equal(x) = how many values <= x?
    
    Step 1: mid = 5
            count_less_equal(5) = 6 (too many)
            right = 5
    
    Step 2: left=1, right=5, mid=3
            count_less_equal(3) = 4 (still too many)
            right = 3
    
    Step 3: left=1, right=3, mid=2
            count_less_equal(2) = 3 (exactly k!)
            right = 2
    
    Step 4: left=1, right=2, mid=1
            count_less_equal(1) = 1 (too few)
            left = 2
    
    left=2, right=2 → answer = 2 ✓
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 668: Kth Smallest Number in Multiplication Table (hard) ⭐⭐
    - LeetCode 378: Kth Smallest Element in a Sorted Matrix (medium)
    - LeetCode 719: Find K-th Smallest Pair Distance (hard)
    """
    
    def find_kth_in_mult_table(self, m: int, n: int, k: int) -> int:
        # Helper: count numbers <= x in multiplication table
        def count_less_equal(x):
            count = 0
            # For each row i (1 to m)
            for i in range(1, m + 1):
                # In row i: i*1, i*2, i*3, ..., i*n
                # How many are <= x? min(x//i, n)
                count += min(x // i, n)
            return count
        
        # Answer space: [smallest value, largest value]
        left = 1        # Minimum value: 1*1
        right = m * n   # Maximum value: m*n
        
        # Find kth smallest value
        while left < right:
            mid = left + (right - left) // 2
            
            # Count how many values <= mid
            if count_less_equal(mid) < k:
                # Too few, need larger value
                left = mid + 1
            else:
                # Enough values, try smaller
                right = mid
        
        return left
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 10: LONGEST INCREASING SUBSEQUENCE (Binary Search + DP)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 USE CASE: Find length of longest increasing subsequence
    
    📊 TEMPLATE: EXCLUSIVE [left, right) with lower bound
    ⏱️  Time: O(n log n) | Space: O(n)
    
    🔑 KEY INSIGHT:
    Maintain array of smallest tail elements for all LIS lengths
    Use binary search to find insertion position
    
    📝 DRY RUN EXAMPLE:
    Array: [10, 9, 2, 5, 3, 7, 101, 18]
    
    Goal: Find LIS length (answer = 4: [2,3,7,101])
    
    tails = [] (stores smallest tail for each LIS length)
    
    Process 10: tails = [10] (LIS length 1)
    Process 9:  9 < 10, replace → tails = [9]
    Process 2:  2 < 9, replace → tails = [2]
    Process 5:  5 > 2, append → tails = [2, 5]
    Process 3:  2 < 3 < 5, replace 5 → tails = [2, 3]
    Process 7:  7 > 3, append → tails = [2, 3, 7]
    Process 101: 101 > 7, append → tails = [2, 3, 7, 101]
    Process 18:  7 < 18 < 101, replace 101 → tails = [2, 3, 7, 18]
    
    Answer: len(tails) = 4
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 300: Longest Increasing Subsequence (medium) ⭐⭐
    - LeetCode 354: Russian Doll Envelopes (hard)
    - LeetCode 646: Maximum Length of Pair Chain (medium)
    """
    
    def length_of_LIS(self, nums: List[int]) -> int:
        # tails[i] = smallest tail element for LIS of length i+1
        tails = []
        
        for num in nums:
            # Find position to insert/replace using binary search (lower bound)
            left = 0
            right = len(tails)
            
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            # If left == len(tails), append (extending LIS)
            if left == len(tails):
                tails.append(num)
            else:
                # Replace with smaller value (maintains optimal tails)
                tails[left] = num
        
        return len(tails)


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 PRACTICE PROBLEMS BY DIFFICULTY
# ═══════════════════════════════════════════════════════════════════════════
"""
EASY (Master these first):
✅ 704. Binary Search
✅ 35. Search Insert Position  
✅ 278. First Bad Version
✅ 69. Sqrt(x)
✅ 367. Valid Perfect Square
✅ 744. Find Smallest Letter Greater Than Target

MEDIUM (Core interview questions):
🔥 34. Find First and Last Position of Element in Sorted Array
🔥 33. Search in Rotated Sorted Array
🔥 153. Find Minimum in Rotated Sorted Array
🔥 162. Find Peak Element
🔥 74. Search a 2D Matrix
🔥 875. Koko Eating Bananas
🔥 1011. Capacity To Ship Packages Within D Days
🔥 300. Longest Increasing Subsequence

HARD (Advanced patterns):
⭐ 4. Median of Two Sorted Arrays
⭐ 410. Split Array Largest Sum
⭐ 668. Kth Smallest Number in Multiplication Table
⭐ 719. Find K-th Smallest Pair Distance

🎯 STUDY PLAN:
Week 1: Master Classic + Lower/Upper Bound (patterns 1-3)
Week 2: Rotated Arrays + 2D Search (patterns 4-6)
Week 3: Peak + Minimize/Maximize (patterns 7-8)
Week 4: Advanced patterns (9-10) + Hard problems
"""


def test_all_patterns():
    """Run comprehensive tests on all patterns"""
    bs = BinarySearchMastery()
    
    print("🧪 Testing all Binary Search patterns...\n")
    
    # Test 1: Classic
    arr = [1, 3, 5, 7, 9]
    assert bs.classic_binary_search(arr, 7) == 3
    assert bs.classic_binary_search(arr, 6) == -1
    print("✅ Pattern 1 (Classic): Passed")
    
    # Test 2: Lower Bound
    arr = [1, 2, 2, 2, 3, 4]
    assert bs.lower_bound(arr, 2) == 1
    assert bs.lower_bound(arr, 5) == -1
    print("✅ Pattern 2 (Lower Bound): Passed")
    
    # Test 3: Upper Bound
    assert bs.upper_bound(arr, 2) == 3
    print("✅ Pattern 3 (Upper Bound): Passed")
    
    # Test 4: Rotated Array
    rotated = [4, 5, 6, 7, 0, 1, 2]
    assert bs.search_rotated(rotated, 0) == 4
    print("✅ Pattern 4 (Rotated Array): Passed")
    
    # Test 5: Find Min
    assert bs.find_min_rotated(rotated) == 0
    print("✅ Pattern 5 (Find Min Rotated): Passed")
    
    # Test 6: 2D Matrix
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert bs.search_matrix(matrix, 3) == True
    print("✅ Pattern 6 (2D Matrix): Passed")
    
    # Test 7: Peak Element
    arr = [1, 2, 1, 3, 5, 6, 4]
    peak = bs.find_peak_element(arr)
    assert arr[peak] > arr[peak-1] and arr[peak] > arr[peak+1]
    print("✅ Pattern 7 (Peak Element): Passed")
    
    # Test 8: Ship Packages
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert bs.ship_within_days(weights, 5) == 15
    print("✅ Pattern 8 (Ship Packages): Passed")
    
    # Test 9: Kth in Mult Table
    assert bs.find_kth_in_mult_table(3, 3, 5) == 3
    print("✅ Pattern 9 (Kth Element): Passed")
    
    # Test 10: LIS
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    assert bs.length_of_LIS(arr) == 4
    print("✅ Pattern 10 (LIS): Passed")
    
    print("\n🎉 All tests passed! Ready for interviews!")


if __name__ == "__main__":
    test_all_patterns()