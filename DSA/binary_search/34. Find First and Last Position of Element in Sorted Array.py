class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        This can be solve using left most and right most occurrence but we have to run the algorithm twice (need to think single pass). so after solving got to know this cannot be solved wihtout 2 passes 
        """
        """
        Time: O(log n) - two binary searches
        Space: O(1)
        
        Optimization: Early exit if target doesn't exist
        """
        n = len(nums)
        
        # Edge case: empty array
        if n == 0:
            return [-1, -1]
        
        # === LOWER BOUND: Find first occurrence ===
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        left = lo
        
        # ✅ OPTIMIZATION: Early exit if target doesn't exist
        # If left is out of bounds OR element isn't target, no need to search further
        if left >= n or nums[left] != target:
            return [-1, -1]
        
        # === UPPER BOUND: Find last occurrence ===
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        
        right = lo - 1
        
        return [left, right]

        def first_try():
            n = len(nums)
            if n == 0:
                return [-1,-1]
            def lower_bound():
                lo = 0
                hi = n
                while lo < hi:
                    mid = (lo+hi)//2
                    if nums[mid] < target:
                        lo = mid+1
                    else:
                        hi = mid 
                return lo
            
            def upper_bound():
                lo = 0
                hi = n
                while lo < hi:
                    mid = (lo+hi)//2
                    if nums[mid] <= target:
                        lo = mid+1
                    else:
                        hi = mid 
                return lo-1
            left = lower_bound()
            right = upper_bound()
            
            # Validate: check if indices are valid AND equal target
            # Check bounds first to avoid index out of range!
            if left < n and left >= 0 and nums[left] == target:
                return [left, right]
            
            return [-1, -1]


            