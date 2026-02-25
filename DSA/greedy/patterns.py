"""
═══════════════════════════════════════════════════════════════════════════════
                    GREEDY ALGORITHM MASTERY GUIDE
            The Most Asked Pattern in FAANG Interviews!
═══════════════════════════════════════════════════════════════════════════════

🎯 FUNDAMENTAL CONCEPTS:

1. WHAT IS GREEDY?
   - Make the LOCALLY OPTIMAL choice at each step
   - Hope that these local choices lead to GLOBAL OPTIMUM
   - No backtracking - commit to each choice!
   
   Example: Making change with coins
   - Always pick the largest coin that fits
   - $0.67 with coins [25¢, 10¢, 5¢, 1¢]
   - Greedy: 25¢ + 25¢ + 10¢ + 5¢ + 1¢ + 1¢ = 6 coins ✓
   - This is OPTIMAL for standard US coins!

2. WHEN DOES GREEDY WORK?
   ✅ Greedy Choice Property: Local optimum → Global optimum
   ✅ Optimal Substructure: Optimal solution contains optimal subsolutions
   
   Classic Examples Where Greedy WORKS:
   - Activity Selection (intervals)
   - Huffman Coding
   - Minimum Spanning Tree (Kruskal's, Prim's)
   - Dijkstra's Shortest Path
   - Fractional Knapsack
   
   Classic Examples Where Greedy FAILS:
   - 0/1 Knapsack (need DP!)
   - Longest Common Subsequence (need DP!)
   - Coin change with arbitrary coins (need DP!)
   
3. HOW TO RECOGNIZE GREEDY PROBLEMS?
   🔑 KEYWORDS in problem description:
   - "maximize" or "minimize"
   - "optimal"
   - "intervals" or "meetings"
   - "schedule" or "arrange"
   - "earliest" or "latest"
   - "fewest" or "most"
   
   🔑 CHARACTERISTICS:
   - Local choice affects future choices
   - Sorting often helps
   - Making the "best" choice at each step
   - No need to reconsider past decisions

4. GREEDY VS DYNAMIC PROGRAMMING?
   
   Use GREEDY when:
   ✅ Local optimum = Global optimum
   ✅ Can prove greedy choice property
   ✅ O(n) or O(n log n) solution exists
   ✅ No need to try all possibilities
   
   Use DP when:
   ❌ Greedy fails (counterexample exists)
   ❌ Need to explore multiple choices
   ❌ Overlapping subproblems
   ❌ Need to track previous states
   
   Example: Jump Game
   - Jump Game I: Can reach end? → GREEDY works! O(n)
   - Jump Game II: Min jumps to reach end? → GREEDY works! O(n)
   - But if asking "count all paths"? → Need DP!

5. 10 ESSENTIAL GREEDY PATTERNS:
   ✅ Pattern 1: Interval Problems (Meeting Rooms, Non-overlapping)
   ✅ Pattern 2: Two Pointer Greedy (Container, Gas Station)
   ✅ Pattern 3: Sorting + Greedy (Assign Cookies, Maximum Units)
   ✅ Pattern 4: Stack-based Greedy (Remove K Digits, Smallest Subsequence)
   ✅ Pattern 5: Jump Game Family (Greedy Choice Property)
   ✅ Pattern 6: Greedy + Heap (Task Scheduler, Minimum Cost)
   ✅ Pattern 7: Greedy String (Partition Labels, Reorganize String)
   ✅ Pattern 8: Array Rearrangement (Wiggle Sort, Array Partition)
   ✅ Pattern 9: Stock Buy/Sell (Multiple variants)
   ✅ Pattern 10: Greedy Math (Gas Station, Water/Candy variants)

6. THE GREEDY DECISION TREE:
   
   See "intervals" or "meetings"? → Pattern 1
   See "maximize/minimize" + can sort? → Pattern 3
   See "remove K items" or "smallest/largest"? → Pattern 4
   See "jump" or "reach"? → Pattern 5
   See "schedule tasks" or "minimum time"? → Pattern 6
   See "partition" or "reorganize"? → Pattern 7
   See "rearrange" or "wiggle"? → Pattern 8
   See "buy/sell stock"? → Pattern 9
   See "gas" or "candy" or "water"? → Pattern 10

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Optional
import heapq
from collections import Counter, defaultdict

class GreedyPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: INTERVAL PROBLEMS (Most Asked!)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    When dealing with intervals, SORTING is key!
    Usually sort by start time or end time, then make greedy choice.
    
    🔑 KEY INSIGHT - WHY GREEDY WORKS:
    For activity selection: Choose meeting that ends earliest!
    - Leaves most room for future meetings
    - This is the greedy choice property
    
    Common Interval Patterns:
    1. Sort by END time → Select non-overlapping (Activity Selection)
    2. Sort by START time → Count overlaps (Meeting Rooms II)
    3. Sort by START, then merge → Merge Intervals
    
    ⏱️  Time: O(n log n) for sorting | Space: O(1) to O(n)
    
    📝 DRY RUN - ACTIVITY SELECTION:
    Intervals: [[1,3], [2,4], [3,5], [0,6], [5,7], [8,9]]
    
    Goal: Select maximum non-overlapping intervals
    
    Step 1: Sort by END time
    Sorted: [[1,3], [2,4], [3,5], [0,6], [5,7], [8,9]]
    
    Step 2: Greedy selection
    - Select [1,3] (ends earliest)
    - Skip [2,4] (starts at 2, overlaps with [1,3])
    - Select [3,5] (starts at 3, no overlap with [1,3])
    - Skip [0,6] (overlaps)
    - Select [5,7] (starts at 5, no overlap)
    - Select [8,9] (no overlap)
    
    Result: 4 intervals selected ✓
    
    🔑 WHY THIS GREEDY CHOICE?
    By always picking the interval that ends earliest:
    - We free up time for future intervals ASAP
    - Maximizes flexibility for remaining choices
    - This is PROVABLY optimal!
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 252. Meeting Rooms ⭐⭐⭐
    
    Medium:
    ✅ 253. Meeting Rooms II ⭐⭐⭐ (MOST ASKED!)
    ✅ 435. Non-overlapping Intervals ⭐⭐⭐
    ✅ 452. Minimum Number of Arrows to Burst Balloons ⭐⭐⭐
    ✅ 56. Merge Intervals ⭐⭐⭐
    ✅ 57. Insert Interval ⭐⭐
    ✅ 1353. Maximum Number of Events That Can Be Attended ⭐⭐
    
    Hard:
    ✅ 759. Employee Free Time ⭐⭐
    """
    
    def canAttendMeetings_LC252(self, intervals: List[List[int]]) -> bool:
        """
        LeetCode 252: Meeting Rooms
        
        Can attend all meetings? (No overlap)
        
        Input: [[0,30],[5,10],[15,20]]
        Output: False (0-30 overlaps with 5-10)
        
        🔑 APPROACH: Sort by start, check for overlaps
        
        DRY RUN:
        intervals = [[0,30], [5,10], [15,20]]
        After sort: [[0,30], [5,10], [15,20]]
        
        Check [0,30] vs [5,10]:
        - prev_end = 30, curr_start = 5
        - 5 < 30 → OVERLAP! ✗
        
        Return False ✓
        
        Time: O(n log n) | Space: O(1)
        """
        if not intervals:
            return True
        
        # Sort by start time
        intervals.sort()
        
        for i in range(1, len(intervals)):
            # If current starts before previous ends → overlap
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True
    
    
    def minMeetingRooms_LC253(self, intervals: List[List[int]]) -> int:
        """
        LeetCode 253: Meeting Rooms II
        
        THE MOST ASKED INTERVAL PROBLEM!
        Find minimum meeting rooms needed.
        
        Input: [[0,30],[5,10],[15,20]]
        Output: 2 (need 2 rooms at most)
        
        🔑 APPROACH 1: Sort + Heap (BEST for interviews!)
        
        Algorithm:
        1. Sort meetings by start time
        2. Use min-heap to track room end times
        3. For each meeting:
           - If earliest ending room is free (end <= start) → reuse it
           - Else → need new room
        4. Heap size = rooms needed
        
        DRY RUN:
        intervals = [[0,30], [5,10], [15,20]]
        After sort: [[0,30], [5,10], [15,20]]
        
        heap = []  (stores end times)
        
        Meeting [0,30]:
          heap empty, add room
          heap = [30]
          rooms = 1
        
        Meeting [5,10]:
          heap top = 30
          5 < 30 (not free), need new room
          heap = [10, 30]
          rooms = 2
        
        Meeting [15,20]:
          heap top = 10
          15 >= 10 (free!), reuse room
          Remove 10, add 20
          heap = [20, 30]
          rooms = 2 (max seen)
        
        Result: 2 rooms ✓
        
        Time: O(n log n) | Space: O(n)
        """
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort()
        
        # Min-heap to track end times
        heap = []
        
        for start, end in intervals:
            # If earliest room is free, reuse it
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # Add this meeting's end time
            heapq.heappush(heap, end)
        
        # Heap size = max rooms needed
        return len(heap)
    
    
    def minMeetingRooms_approach2(self, intervals: List[List[int]]) -> int:
        """
        🔑 APPROACH 2: Separate Start/End Arrays (Elegant!)
        
        Algorithm:
        1. Separate all start and end times
        2. Sort both arrays
        3. Use two pointers:
           - When meeting starts → need room (rooms++)
           - When meeting ends → free room (rooms--)
        4. Track maximum rooms needed
        
        DRY RUN:
        intervals = [[0,30], [5,10], [15,20]]
        
        starts = [0, 5, 15]
        ends = [10, 20, 30]
        
        i=0, j=0, rooms=0, max_rooms=0
        
        starts[0]=0 < ends[0]=10:
          meeting starts, rooms=1, max_rooms=1
          i=1
        
        starts[1]=5 < ends[0]=10:
          meeting starts, rooms=2, max_rooms=2
          i=2
        
        starts[2]=15 > ends[0]=10:
          meeting ends, rooms=1
          j=1
        
        starts[2]=15 < ends[1]=20:
          meeting starts, rooms=2, max_rooms=2
          i=3 (done with starts)
        
        Result: 2 rooms ✓
        
        Time: O(n log n) | Space: O(n)
        """
        if not intervals:
            return 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        rooms = max_rooms = 0
        i = j = 0
        
        while i < len(starts):
            # If meeting starts before earliest ends
            if starts[i] < ends[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                # Meeting ends, free up room
                rooms -= 1
                j += 1
        
        return max_rooms
    
    
    def eraseOverlapIntervals_LC435(self, intervals: List[List[int]]) -> int:
        """
        LeetCode 435: Non-overlapping Intervals
        
        Remove minimum intervals to make rest non-overlapping.
        
        Input: [[1,2],[2,3],[3,4],[1,3]]
        Output: 1 (remove [1,3])
        
        🔑 KEY INSIGHT: 
        This is EXACTLY activity selection!
        - Find max non-overlapping intervals
        - Remove the rest!
        
        Greedy: Sort by END time, select earliest ending!
        
        DRY RUN:
        intervals = [[1,2], [2,3], [3,4], [1,3]]
        Sort by end: [[1,2], [2,3], [1,3], [3,4]]
        
        Select [1,2] (end=2)
        Select [2,3] (start=2, end=3, no overlap)
        Skip [1,3] (start=1 < prev_end=3, overlap!)
        Select [3,4] (start=3, end=4, no overlap)
        
        Selected: 3 intervals
        Remove: 4 - 3 = 1 ✓
        
        Time: O(n log n) | Space: O(1)
        """
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 1  # First interval always selected
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If no overlap, select this interval
            if intervals[i][0] >= prev_end:
                count += 1
                prev_end = intervals[i][1]
        
        # Total - selected = removed
        return len(intervals) - count
    
    
    def findMinArrowShots_LC452(self, points: List[List[int]]) -> int:
        """
        LeetCode 452: Minimum Number of Arrows to Burst Balloons
        
        Each balloon covers [start, end].
        Arrow at x bursts all balloons where start <= x <= end.
        Find minimum arrows needed.
        
        Input: [[10,16],[2,8],[1,6],[7,12]]
        Output: 2
        
        🔑 KEY INSIGHT:
        This is interval overlap problem!
        - Sort by END position
        - Shoot arrow at end of first balloon
        - This bursts maximum balloons
        
        DRY RUN:
        points = [[10,16], [2,8], [1,6], [7,12]]
        Sort by end: [[1,6], [2,8], [7,12], [10,16]]
        
        Arrow 1 at position 6:
          Bursts [1,6] ✓
          Bursts [2,8]? 2 <= 6 <= 8 ✓
          Bursts [7,12]? 7 <= 6? ✗
        
        Arrow 2 at position 12:
          Bursts [7,12] ✓
          Bursts [10,16]? 10 <= 12 <= 16 ✓
        
        Total: 2 arrows ✓
        
        Time: O(n log n) | Space: O(1)
        """
        if not points:
            return 0
        
        # Sort by end position
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]  # Shoot at end of first balloon
        
        for i in range(1, len(points)):
            # If balloon starts after arrow, need new arrow
            if points[i][0] > arrow_pos:
                arrows += 1
                arrow_pos = points[i][1]
        
        return arrows
    
    
    def merge_LC56(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        LeetCode 56: Merge Intervals
        
        Merge all overlapping intervals.
        
        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        
        🔑 APPROACH: Sort by start, then merge
        
        DRY RUN:
        intervals = [[1,3], [2,6], [8,10], [15,18]]
        Already sorted by start
        
        result = []
        
        Process [1,3]:
          result = [[1,3]]
        
        Process [2,6]:
          2 <= 3? Yes, merge!
          result = [[1,6]]
        
        Process [8,10]:
          8 <= 6? No, add new
          result = [[1,6], [8,10]]
        
        Process [15,18]:
          15 <= 10? No, add new
          result = [[1,6], [8,10], [15,18]] ✓
        
        Time: O(n log n) | Space: O(n)
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort()
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # If overlaps with last merged interval
            if intervals[i][0] <= merged[-1][1]:
                # Merge by extending end
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # No overlap, add new interval
                merged.append(intervals[i])
        
        return merged
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: TWO POINTER GREEDY
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Combine greedy with two pointers for optimization problems.
    
    🔑 KEY PROBLEMS:
    - Container With Most Water (already in Two Pointers guide)
    - Gas Station (circular array + greedy)
    - Trapping Rain Water (already in Two Pointers guide)
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 455. Assign Cookies ⭐⭐
    
    Medium:
    ✅ 134. Gas Station ⭐⭐⭐ (MOST ASKED!)
    ✅ 11. Container With Most Water ⭐⭐⭐
    ✅ 42. Trapping Rain Water ⭐⭐⭐
    """
    
    def canCompleteCircuit_LC134(self, gas: List[int], cost: List[int]) -> int:
        """
        LeetCode 134: Gas Station
        
        THE MOST IMPORTANT GREEDY TWO-POINTER PROBLEM!
        
        Circular route with gas stations.
        gas[i] = gas at station i
        cost[i] = cost to travel from i to i+1
        
        Find starting station to complete circuit, or -1.
        
        Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3 (start at station 3)
        
        🔑 KEY INSIGHTS:
        1. If total_gas < total_cost → impossible
        2. If possible, there's exactly ONE valid start
        3. Greedy: If can't reach j from i, then can't reach j from any k in [i,j)!
        
        Why Insight 3?
        - If fail at j starting from i:
        - tank[i→j] < 0
        - For any k in (i,j): tank[k→j] < tank[i→j] < 0
        - So k also fails!
        - Next candidate must be j+1!
        
        DRY RUN:
        gas =  [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        diff = [-2,-2,-2, 3, 3]
        
        total_gas = 15, total_cost = 15 → possible ✓
        
        start = 0, tank = 0
        
        i=0: tank = 0 + (-2) = -2 < 0
             Failed! Try next
             start = 1, tank = 0
        
        i=1: tank = 0 + (-2) = -2 < 0
             start = 2, tank = 0
        
        i=2: tank = 0 + (-2) = -2 < 0
             start = 3, tank = 0
        
        i=3: tank = 0 + 3 = 3 ✓
        
        i=4: tank = 3 + 3 = 6 ✓
        
        Return start = 3 ✓
        
        Time: O(n) | Space: O(1)
        """
        total_tank = 0
        curr_tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            # If can't reach next station
            if curr_tank < 0:
                # Try starting from next station
                start = i + 1
                curr_tank = 0
        
        # If total gas >= total cost, solution exists
        return start if total_tank >= 0 else -1
    
    
    def findContentChildren_LC455(self, g: List[int], s: List[int]) -> int:
        """
        LeetCode 455: Assign Cookies
        
        g[i] = greed factor of child i
        s[j] = size of cookie j
        
        Cookie s[j] satisfies child g[i] if s[j] >= g[i].
        Maximize satisfied children.
        
        Input: g = [1,2,3], s = [1,1]
        Output: 1
        
        🔑 GREEDY: Give smallest cookie that satisfies each child
        
        Sort both arrays, use two pointers!
        
        Time: O(n log n + m log m) | Space: O(1)
        """
        g.sort()
        s.sort()
        
        child = cookie = 0
        
        while child < len(g) and cookie < len(s):
            # If cookie satisfies child
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: SORTING + GREEDY
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Sort first, then make greedy choices based on sorted order.
    
    🔑 KEY INSIGHT:
    Sorting reveals the optimal order for greedy choices!
    
    Common Patterns:
    1. Sort by value, pick greedily
    2. Sort by ratio/priority, pick greedily
    3. Sort by size, assign greedily
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 455. Assign Cookies ⭐⭐
    ✅ 860. Lemonade Change ⭐⭐
    
    Medium:
    ✅ 1663. Smallest String With A Given Numeric Value ⭐⭐
    ✅ 1710. Maximum Units on a Truck ⭐⭐
    ✅ 406. Queue Reconstruction by Height ⭐⭐⭐
    ✅ 621. Task Scheduler ⭐⭐⭐
    """
    
    def maxUnitsOnTruck_LC1710(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        LeetCode 1710: Maximum Units on a Truck
        
        boxTypes[i] = [numBoxes, unitsPerBox]
        Pick boxes to maximize units (capacity = truckSize)
        
        Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
        Output: 8
        
        🔑 GREEDY: Pick boxes with most units per box first!
        
        DRY RUN:
        boxTypes = [[1,3], [2,2], [3,1]], truckSize = 4
        Sort by units (descending): [[1,3], [2,2], [3,1]]
        
        Take 1 box with 3 units: total = 3, truck = 3
        Take 2 boxes with 2 units: total = 7, truck = 1
        Take 1 box with 1 unit: total = 8, truck = 0 ✓
        
        Time: O(n log n) | Space: O(1)
        """
        # Sort by units per box (descending)
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for numBoxes, unitsPerBox in boxTypes:
            # Take as many boxes as possible
            boxes_to_take = min(numBoxes, truckSize)
            total_units += boxes_to_take * unitsPerBox
            truckSize -= boxes_to_take
            
            if truckSize == 0:
                break
        
        return total_units
    
    
    def reconstructQueue_LC406(self, people: List[List[int]]) -> List[List[int]]:
        """
        LeetCode 406: Queue Reconstruction by Height
        
        people[i] = [h, k] where:
        - h = height
        - k = number of people in front with height >= h
        
        Reconstruct queue.
        
        Input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        
        🔑 GREEDY STRATEGY:
        1. Sort by height DESC, then by k ASC
        2. Insert each person at index k
        
        Why this works?
        - Tallest people don't care about shorter ones
        - Insert tallest first at their k position
        - Shorter people fit in between!
        
        DRY RUN:
        people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        Sort: [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
        
        result = []
        
        Insert [7,0] at index 0: [[7,0]]
        Insert [7,1] at index 1: [[7,0], [7,1]]
        Insert [6,1] at index 1: [[7,0], [6,1], [7,1]]
        Insert [5,0] at index 0: [[5,0], [7,0], [6,1], [7,1]]
        Insert [5,2] at index 2: [[5,0], [7,0], [5,2], [6,1], [7,1]]
        Insert [4,4] at index 4: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]] ✓
        
        Time: O(n²) | Space: O(n)
        """
        # Sort by height DESC, k ASC
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []
        for person in people:
            # Insert at index k
            result.insert(person[1], person)
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: STACK-BASED GREEDY
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Use stack to build optimal solution by keeping/removing elements.
    
    🔑 KEY INSIGHT:
    Monotonic stack + greedy removal creates optimal result!
    
    Common Patterns:
    1. Remove K digits → smallest number
    2. Remove duplicate letters → smallest lexicographical
    3. Largest number after removal
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 402. Remove K Digits ⭐⭐⭐ (IMPORTANT!)
    ✅ 316. Remove Duplicate Letters ⭐⭐⭐
    ✅ 1081. Smallest Subsequence of Distinct Characters ⭐⭐⭐
    ✅ 321. Create Maximum Number ⭐⭐
    
    Hard:
    ✅ 1673. Find Most Competitive Subsequence ⭐⭐
    """
    
    def removeKdigits_LC402(self, num: str, k: int) -> str:
        """
        LeetCode 402: Remove K Digits
        
        MOST IMPORTANT STACK-BASED GREEDY!
        
        Remove k digits to get smallest possible number.
        
        Input: num = "1432219", k = 3
        Output: "1219"
        
        🔑 GREEDY STRATEGY:
        Use monotonic increasing stack!
        - If current < stack top: pop (remove larger digit)
        - This creates smallest number
        
        DRY RUN:
        num = "1432219", k = 3
        
        stack = [], k_remaining = 3
        
        '1': stack = ['1'], k = 3
        
        '4': 4 > 1, stack = ['1','4'], k = 3
        
        '3': 3 < 4, pop '4'!
             stack = ['1','3'], k = 2
        
        '2': 2 < 3, pop '3'!
             stack = ['1','2'], k = 1
        
        '2': 2 = 2, stack = ['1','2','2'], k = 1
        
        '1': 1 < 2, pop '2'!
             stack = ['1','2','1'], k = 0
        
        '9': k = 0, just append
             stack = ['1','2','1','9']
        
        Result: "1219" ✓
        
        Time: O(n) | Space: O(n)
        """
        stack = []
        
        for digit in num:
            # Remove larger digits while we can
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining k digits from end
        if k > 0:
            stack = stack[:-k]
        
        # Build result, remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'
    
    
    def removeDuplicateLetters_LC316(self, s: str) -> str:
        """
        LeetCode 316: Remove Duplicate Letters
        
        Remove duplicates to get smallest lexicographical order.
        Each letter appears exactly once.
        
        Input: s = "bcabc"
        Output: "abc"
        
        🔑 GREEDY STRATEGY:
        1. Track last occurrence of each character
        2. Use stack + set (in_stack)
        3. Pop larger characters if they appear later!
        
        DRY RUN:
        s = "bcabc"
        last = {'b':3, 'c':4, 'a':2}
        
        stack = [], in_stack = set()
        
        i=0, 'b':
          stack = ['b'], in_stack = {'b'}
        
        i=1, 'c':
          stack = ['b','c'], in_stack = {'b','c'}
        
        i=2, 'a':
          'a' < 'c' and last['c']=4 > 2 (appears later!)
          Pop 'c'!
          'a' < 'b' and last['b']=3 > 2 (appears later!)
          Pop 'b'!
          stack = ['a'], in_stack = {'a'}
        
        i=3, 'b':
          'b' not in stack
          stack = ['a','b'], in_stack = {'a','b'}
        
        i=4, 'c':
          'c' not in stack
          stack = ['a','b','c'], in_stack = {'a','b','c'}
        
        Result: "abc" ✓
        
        Time: O(n) | Space: O(1) (26 letters max)
        """
        # Track last occurrence
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        in_stack = set()
        
        for i, char in enumerate(s):
            # If already in result, skip
            if char in in_stack:
                continue
            
            # Remove larger characters that appear later
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)
            
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: JUMP GAME FAMILY (Greedy Choice Property)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Can reach end? Minimum jumps? Use greedy!
    
    🔑 KEY INSIGHT:
    Track furthest reachable position!
    - Jump Game I: Can reach end?
    - Jump Game II: Minimum jumps to reach end?
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 55. Jump Game ⭐⭐⭐ (MUST KNOW!)
    ✅ 45. Jump Game II ⭐⭐⭐ (MUST KNOW!)
    ✅ 1306. Jump Game III ⭐⭐
    ✅ 1345. Jump Game IV ⭐⭐
    
    Hard:
    ✅ 1871. Jump Game VII ⭐⭐
    """
    
    def canJump_LC55(self, nums: List[int]) -> bool:
        """
        LeetCode 55: Jump Game
        
        MOST ASKED GREEDY PROBLEM!
        
        nums[i] = max jump length from position i
        Can reach last index?
        
        Input: nums = [2,3,1,1,4]
        Output: True
        
        🔑 GREEDY: Track furthest reachable position!
        
        DRY RUN:
        nums = [2, 3, 1, 1, 4]
        goal = 4 (last index)
        
        max_reach = 0
        
        i=0: max_reach = max(0, 0+2) = 2
             0 <= 2 ✓ (can reach)
        
        i=1: max_reach = max(2, 1+3) = 4
             1 <= 4 ✓
        
        i=2: max_reach = max(4, 2+1) = 4
             2 <= 4 ✓
        
        i=3: max_reach = max(4, 3+1) = 4
             3 <= 4 ✓
        
        i=4: 4 <= 4 ✓
        
        max_reach >= goal? 4 >= 4 ✓
        Return True ✓
        
        Time: O(n) | Space: O(1)
        """
        max_reach = 0
        
        for i in range(len(nums)):
            # If current position unreachable
            if i > max_reach:
                return False
            
            # Update furthest reach
            max_reach = max(max_reach, i + nums[i])
        
        return max_reach >= len(nums) - 1
    
    
    def jump_LC45(self, nums: List[int]) -> int:
        """
        LeetCode 45: Jump Game II
        
        Find MINIMUM jumps to reach end.
        
        Input: nums = [2,3,1,1,4]
        Output: 2 (jump 1 step from index 0 to 1, then 3 steps to last)
        
        🔑 GREEDY: BFS-like approach!
        - Track current jump range
        - Track furthest for next jump
        - When current range ends, jump!
        
        DRY RUN:
        nums = [2, 3, 1, 1, 4]
        
        jumps = 0
        current_end = 0 (end of current jump range)
        furthest = 0 (furthest from current range)
        
        i=0:
          furthest = max(0, 0+2) = 2
          i=0 == current_end? Yes! Jump!
          jumps = 1, current_end = 2
        
        i=1:
          furthest = max(2, 1+3) = 4
          i=1 < current_end=2, no jump yet
        
        i=2:
          furthest = max(4, 2+1) = 4
          i=2 == current_end? Yes! Jump!
          jumps = 2, current_end = 4
        
        Reached end! Return 2 ✓
        
        Time: O(n) | Space: O(1)
        """
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        furthest = 0
        
        for i in range(len(nums) - 1):
            # Update furthest reachable
            furthest = max(furthest, i + nums[i])
            
            # If reached end of current jump
            if i == current_end:
                jumps += 1
                current_end = furthest
        
        return jumps
    
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: GREEDY + HEAP (Priority Queue)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Use heap to always process most optimal element!
    
    🔑 KEY INSIGHT:
    Heap gives us the "greedy choice" in O(log n)!
    - Min-heap: Always get smallest
    - Max-heap: Always get largest
    
    Common Patterns:
    1. Task scheduling with cooldown
    2. Minimum cost problems
    3. K-way merge problems
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 621. Task Scheduler ⭐⭐⭐ (MOST ASKED!)
    ✅ 767. Reorganize String ⭐⭐⭐
    ✅ 1405. Longest Happy String ⭐⭐
    ✅ 1337. The K Weakest Rows in a Matrix ⭐⭐
    
    Hard:
    ✅ 358. Rearrange String k Distance Apart ⭐⭐
    """
    
    def leastInterval_LC621(self, tasks: List[str], n: int) -> int:
        """
        LeetCode 621: Task Scheduler
        
        THE MOST IMPORTANT GREEDY + HEAP PROBLEM!
        
        tasks = list of tasks, n = cooldown period
        Same task must be separated by at least n intervals.
        Find minimum intervals needed.
        
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8 (A -> B -> idle -> A -> B -> idle -> A -> B)
        
        🔑 GREEDY STRATEGY:
        Always schedule most frequent task first!
        Use max-heap to track frequencies.
        
        DRY RUN:
        tasks = ["A","A","A","B","B","B"], n = 2
        
        freq = {'A': 3, 'B': 3}
        heap = [-3, -3]  (max-heap using negative)
        
        Time 0: Schedule A (freq=3)
                heap = [-3, -2], cooldown = {A: 2}
        
        Time 1: Schedule B (freq=3)
                heap = [-2, -2], cooldown = {A: 1, B: 2}
        
        Time 2: Both A,B in cooldown, IDLE
                cooldown = {A: 0, B: 1}
        
        Time 3: Schedule A (freq=2)
                heap = [-2, -1], cooldown = {A: 2, B: 0}
        
        Time 4: Schedule B (freq=2)
                heap = [-1, -1], cooldown = {A: 1, B: 2}
        
        Time 5: IDLE
        
        Time 6: Schedule A (freq=1)
                heap = [-1], cooldown = {A: 2, B: 0}
        
        Time 7: Schedule B (freq=1)
                heap = [], cooldown = {A: 1, B: 2}
        
        Total: 8 intervals ✓
        
        Time: O(n) | Space: O(1) (26 letters max)
        """
        # Count frequencies
        freq = Counter(tasks)
        
        # Max-heap (use negative for max)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        
        time = 0
        
        while heap:
            temp = []
            
            # Process n+1 tasks (one cycle)
            for _ in range(n + 1):
                if heap:
                    # Get most frequent task
                    count = heapq.heappop(heap)
                    if count < -1:
                        temp.append(count + 1)
                    time += 1
                elif temp:
                    # Still tasks left but in cooldown
                    time += 1  # Idle
            
            # Add back tasks for next cycle
            for count in temp:
                heapq.heappush(heap, count)
        
        return time
    
    
    def leastInterval_formula(self, tasks: List[str], n: int) -> int:
        """
        🔑 MATHEMATICAL APPROACH (More elegant!)
        
        Formula:
        max_freq = frequency of most common task
        max_count = number of tasks with max_freq
        
        Answer = max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_count
        )
        
        Why?
        - Most frequent task creates (max_freq - 1) gaps
        - Each gap needs (n + 1) slots
        - Last occurrence has max_count tasks
        
        DRY RUN:
        tasks = ["A","A","A","B","B","B"], n = 2
        
        max_freq = 3 (A and B both appear 3 times)
        max_count = 2 (both A and B have max freq)
        
        Slots needed = (3-1) * (2+1) + 2
                    = 2 * 3 + 2
                    = 8 ✓
        
        Time: O(n) | Space: O(1)
        """
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for f in freq.values() if f == max_freq)
        
        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_count
        )
    
    
    def reorganizeString_LC767(self, s: str) -> str:
        """
        LeetCode 767: Reorganize String
        
        Rearrange so no two adjacent characters are same.
        Return "" if impossible.
        
        Input: s = "aab"
        Output: "aba"
        
        🔑 GREEDY: Use max-heap, always place most frequent!
        
        Impossible when: max_freq > (n + 1) / 2
        
        DRY RUN:
        s = "aab"
        freq = {'a': 2, 'b': 1}
        heap = [(-2,'a'), (-1,'b')]
        
        Step 1: Pop 'a' (freq=2)
                result = "a"
                prev = ('a', -1)
        
        Step 2: Pop 'b' (freq=1)
                Add prev 'a' back: heap = [(-1,'a')]
                result = "ab"
                prev = ('b', 0)
        
        Step 3: Pop 'a' (freq=1)
                result = "aba" ✓
        
        Time: O(n log k) where k = unique chars | Space: O(k)
        """
        # Count frequencies
        freq = Counter(s)
        
        # Check if possible
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # Max-heap
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        
        result = []
        prev = None
        
        while heap:
            # Get most frequent
            count, char = heapq.heappop(heap)
            result.append(char)
            
            # Add previous back to heap
            if prev:
                heapq.heappush(heap, prev)
            
            # Update previous
            if count < -1:
                prev = (count + 1, char)
            else:
                prev = None
        
        return ''.join(result)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 7: GREEDY STRING PROBLEMS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    String manipulation using greedy choices.
    
    🔑 KEY PROBLEMS:
    - Partition Labels
    - Split String
    - String transformation
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Medium:
    ✅ 763. Partition Labels ⭐⭐⭐ (IMPORTANT!)
    ✅ 1047. Remove All Adjacent Duplicates ⭐⭐
    ✅ 1209. Remove All Adjacent Duplicates II ⭐⭐
    ✅ 678. Valid Parenthesis String ⭐⭐⭐
    """
    
    def partitionLabels_LC763(self, s: str) -> List[int]:
        """
        LeetCode 763: Partition Labels
        
        Partition into max parts where each letter appears in at most one part.
        
        Input: s = "ababcbacadefegdehijhklij"
        Output: [9,7,8]
        
        🔑 GREEDY:
        1. Track last occurrence of each character
        2. Extend partition to include all occurrences
        
        DRY RUN:
        s = "ababcbacadefegdehijhklij"
        
        last = {'a':8, 'b':5, 'c':7, 'd':14, 'e':15, ...}
        
        start=0, end=0
        
        i=0, 'a': last['a']=8, end=8
        i=1, 'b': last['b']=5, end=8 (no change)
        i=2, 'a': last['a']=8, end=8
        ...
        i=8, 'a': i==end! Partition: [0,8] length=9
        
        start=9, end=9
        i=9, 'd': last['d']=14, end=14
        ...
        i=15, 'e': i==end! Partition: [9,15] length=7
        
        Continue...
        Result: [9, 7, 8] ✓
        
        Time: O(n) | Space: O(1) (26 letters)
        """
        # Track last occurrence
        last = {char: i for i, char in enumerate(s)}
        
        result = []
        start = end = 0
        
        for i, char in enumerate(s):
            # Extend partition to include this char's last occurrence
            end = max(end, last[char])
            
            # If reached end of partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result
    
    
    def checkValidString_LC678(self, s: str) -> bool:
        """
        LeetCode 678: Valid Parenthesis String
        
        '(' = open, ')' = close, '*' = empty/open/close
        Is string valid?
        
        Input: s = "(*)"
        Output: True
        
        🔑 GREEDY: Track min and max possible open brackets!
        
        min_open = minimum open brackets
        max_open = maximum open brackets
        
        '(': min++, max++
        ')': min--, max--
        '*': min-- (treat as close), max++ (treat as open)
        
        Valid if min_open <= 0 and max_open >= 0 at each step
        
        Time: O(n) | Space: O(1)
        """
        min_open = max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # '*'
                min_open -= 1  # Treat as close
                max_open += 1  # Treat as open
            
            # Too many close brackets
            if max_open < 0:
                return False
            
            # Negative min doesn't make sense
            min_open = max(min_open, 0)
        
        # All open brackets matched
        return min_open == 0
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 8: ARRAY REARRANGEMENT
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Rearrange array to satisfy certain properties.
    
    🔑 KEY PROBLEMS:
    - Wiggle Sort
    - Array Partition
    - Maximize sum/product
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 561. Array Partition ⭐⭐
    
    Medium:
    ✅ 280. Wiggle Sort ⭐⭐
    ✅ 324. Wiggle Sort II ⭐⭐⭐
    ✅ 1323. Maximum 69 Number ⭐
    """
    
    def arrayPairSum_LC561(self, nums: List[int]) -> int:
        """
        LeetCode 561: Array Partition
        
        Pair elements to maximize sum of minimums.
        
        Input: nums = [1,4,3,2]
        Output: 4 (pairs: (1,2), (3,4), min sum = 1+3=4)
        
        🔑 GREEDY: Sort and pair adjacent elements!
        
        Why? After sorting, pairing adjacent gives max sum.
        
        Time: O(n log n) | Space: O(1)
        """
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))
    
    
    def wiggleSort_LC280(self, nums: List[int]) -> None:
        """
        LeetCode 280: Wiggle Sort (Premium)
        
        Rearrange so nums[0] <= nums[1] >= nums[2] <= nums[3]...
        
        Input: nums = [3,5,2,1,6,4]
        Output: [3,5,1,6,2,4] (one possible answer)
        
        🔑 GREEDY: One pass, swap when needed!
        
        For even i: nums[i] <= nums[i+1]
        For odd i: nums[i] >= nums[i+1]
        
        If violated, swap!
        
        DRY RUN:
        nums = [3, 5, 2, 1, 6, 4]
        
        i=0 (even): 3 <= 5? Yes ✓
        i=1 (odd): 5 >= 2? Yes ✓
        i=2 (even): 2 <= 1? No! Swap
                nums = [3, 5, 1, 2, 6, 4]
        i=3 (odd): 2 >= 6? No! Swap
                nums = [3, 5, 1, 6, 2, 4]
        i=4 (even): 2 <= 4? Yes ✓
        
        Result: [3, 5, 1, 6, 2, 4] ✓
        
        Time: O(n) | Space: O(1)
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or \
               (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 9: STOCK BUY/SELL (Complete Family!)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Different transaction limits require different greedy strategies.
    
    🔑 ALL VARIANTS:
    - Buy/Sell once → Track min price
    - Buy/Sell unlimited → Sum all increases
    - Buy/Sell with cooldown → Skip day after sell
    - Buy/Sell with fee → Subtract fee
    - Buy/Sell k times → DP (not greedy!)
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 121. Best Time to Buy and Sell Stock ⭐⭐⭐
    
    Medium:
    ✅ 122. Best Time to Buy and Sell Stock II ⭐⭐⭐
    ✅ 714. Best Time to Buy and Sell Stock with Fee ⭐⭐⭐
    ✅ 309. Best Time to Buy and Sell Stock with Cooldown ⭐⭐
    
    Hard:
    ✅ 123. Best Time to Buy and Sell Stock III ⭐⭐ (DP)
    ✅ 188. Best Time to Buy and Sell Stock IV ⭐⭐ (DP)
    """
    
    def maxProfit_LC121(self, prices: List[int]) -> int:
        """
        LeetCode 121: Best Time to Buy and Sell Stock
        
        Buy ONCE, sell ONCE.
        Maximize profit.
        
        Input: prices = [7,1,5,3,6,4]
        Output: 5 (buy at 1, sell at 6)
        
        🔑 GREEDY: Track minimum price seen so far!
        
        DRY RUN:
        prices = [7, 1, 5, 3, 6, 4]
        
        min_price = ∞, max_profit = 0
        
        Day 0: price=7
               min_price = 7
               profit = 7-7 = 0
        
        Day 1: price=1
               min_price = 1
               profit = 1-1 = 0
        
        Day 2: price=5
               min_price = 1
               profit = 5-1 = 4, max_profit = 4
        
        Day 3: price=3
               profit = 3-1 = 2
        
        Day 4: price=6
               profit = 6-1 = 5, max_profit = 5 ✓
        
        Day 5: price=4
               profit = 4-1 = 3
        
        Result: 5 ✓
        
        Time: O(n) | Space: O(1)
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum price
            min_price = min(min_price, price)
            
            # Calculate profit if sold today
            profit = price - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit
    
    
    def maxProfit_LC122(self, prices: List[int]) -> int:
        """
        LeetCode 122: Best Time to Buy and Sell Stock II
        
        Buy/Sell UNLIMITED times (but must sell before buying again).
        
        Input: prices = [7,1,5,3,6,4]
        Output: 7 (buy 1, sell 5: +4, buy 3, sell 6: +3)
        
        🔑 GREEDY: Sum ALL increases!
        
        Why? Every increase is a profit opportunity!
        
        DRY RUN:
        prices = [7, 1, 5, 3, 6, 4]
        
        Day 1: 1 < 7? No profit
        Day 2: 5 > 1? Profit = 5-1 = 4
        Day 3: 3 < 5? No profit
        Day 4: 6 > 3? Profit = 6-3 = 3
        Day 5: 4 < 6? No profit
        
        Total: 4 + 3 = 7 ✓
        
        Time: O(n) | Space: O(1)
        """
        profit = 0
        
        for i in range(1, len(prices)):
            # If price increases, add the increase
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
    
    
    def maxProfit_LC714(self, prices: List[int], fee: int) -> int:
        """
        LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee
        
        Unlimited transactions, but pay fee per transaction.
        
        Input: prices = [1,3,2,8,4,9], fee = 2
        Output: 8 (buy 1, sell 8: +5, buy 4, sell 9: +3)
        
        🔑 GREEDY: Track cash and stock states!
        
        cash = max profit if currently not holding stock
        stock = max profit if currently holding stock
        
        Time: O(n) | Space: O(1)
        """
        cash = 0  # Not holding stock
        stock = -prices[0]  # Holding stock (bought at prices[0])
        
        for price in prices[1:]:
            # Update cash: either keep not holding, or sell today
            cash = max(cash, stock + price - fee)
            
            # Update stock: either keep holding, or buy today
            stock = max(stock, cash - price)
        
        return cash
    
    
    def maxProfit_LC309(self, prices: List[int]) -> int:
        """
        LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
        
        After selling, must cooldown for 1 day.
        
        Input: prices = [1,2,3,0,2]
        Output: 3 (buy 1, sell 2: +1, cooldown, buy 0, sell 2: +2)
        
        🔑 GREEDY with states:
        
        sold = max profit after selling today
        hold = max profit while holding stock
        rest = max profit while resting (cooldown)
        
        Time: O(n) | Space: O(1)
        """
        if len(prices) < 2:
            return 0
        
        sold = 0
        hold = -prices[0]
        rest = 0
        
        for price in prices[1:]:
            prev_sold = sold
            
            # Sell today (was holding)
            sold = hold + price
            
            # Buy today (was resting)
            hold = max(hold, rest - price)
            
            # Rest today (was sold yesterday)
            rest = max(rest, prev_sold)
        
        return max(sold, rest)
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 10: GREEDY MATH (Tricky Greedy Problems)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 CORE CONCEPT:
    Mathematical insights lead to greedy solutions.
    
    🔑 KEY PROBLEMS:
    - Candy distribution
    - Water container
    - Minimum moves
    
    💡 LEETCODE PRACTICE PROBLEMS:
    Easy:
    ✅ 860. Lemonade Change ⭐⭐
    
    Medium:
    ✅ 135. Candy ⭐⭐⭐ (HARD but IMPORTANT!)
    ✅ 11. Container With Most Water ⭐⭐⭐
    ✅ 881. Boats to Save People ⭐⭐
    
    Hard:
    ✅ 42. Trapping Rain Water ⭐⭐⭐
    """
    
    def candy_LC135(self, ratings: List[int]) -> int:
        """
        LeetCode 135: Candy
        
        VERY TRICKY GREEDY PROBLEM!
        
        Children in line with ratings.
        Rules:
        1. Each child gets at least 1 candy
        2. Higher rating gets more candy than neighbors
        
        Minimize total candies.
        
        Input: ratings = [1,0,2]
        Output: 5 (candies = [2,1,2])
        
        🔑 GREEDY: Two passes!
        
        Pass 1 (left to right): Satisfy left neighbor rule
        Pass 2 (right to left): Satisfy right neighbor rule
        
        DRY RUN:
        ratings = [1, 0, 2]
        
        Pass 1 (left to right):
        candies = [1, 1, 1]
        
        i=1: ratings[1]=0 < ratings[0]=1? No change
        i=2: ratings[2]=2 > ratings[1]=0? candies[2] = candies[1]+1 = 2
        candies = [1, 1, 2]
        
        Pass 2 (right to left):
        i=1: ratings[1]=0 < ratings[2]=2? No change
        i=0: ratings[0]=1 > ratings[1]=0? 
             candies[0] = max(1, candies[1]+1) = max(1, 2) = 2
        candies = [2, 1, 2]
        
        Total: 5 ✓
        
        Time: O(n) | Space: O(n)
        """
        n = len(ratings)
        candies = [1] * n
        
        # Left to right: satisfy left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left: satisfy right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
    
    
    def lemonadeChange_LC860(self, bills: List[int]) -> bool:
        """
        LeetCode 860: Lemonade Change
        
        Lemonade costs $5.
        Customers pay with $5, $10, or $20.
        Can provide correct change?
        
        Input: bills = [5,5,5,10,20]
        Output: True
        
        🔑 GREEDY: Keep track of bills, prioritize giving larger bills as change!
        
        For $10: Give one $5
        For $20: Give one $10 + one $5, OR three $5
        
        Time: O(n) | Space: O(1)
        """
        five = ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # $20
                # Prefer giving $10 + $5 over three $5
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
    
    
    def numRescueBoats_LC881(self, people: List[int], limit: int) -> int:
        """
        LeetCode 881: Boats to Save People
        
        Boat can carry at most 2 people with weight <= limit.
        Find minimum boats needed.
        
        Input: people = [3,2,2,1], limit = 3
        Output: 3 (boats: [1,2], [2], [3])
        
        🔑 GREEDY: Pair lightest with heaviest!
        
        Sort array, use two pointers.
        - If lightest + heaviest <= limit: pair them
        - Else: heaviest goes alone
        
        DRY RUN:
        people = [3, 2, 2, 1], limit = 3
        Sort: [1, 2, 2, 3]
        
        left=0, right=3, boats=0
        
        people[0]+people[3] = 1+3 = 4 > 3
        Boat: [3] alone, boats=1, right=2
        
        people[0]+people[2] = 1+2 = 3 <= 3
        Boat: [1,2], boats=2, left=1, right=1
        
        people[1]+people[1] = 2+2 = 4 > 3
        (left==right, just one person)
        Boat: [2], boats=3, left=2
        
        Result: 3 boats ✓
        
        Time: O(n log n) | Space: O(1)
        """
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If lightest and heaviest can share boat
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 60 GREEDY PROBLEMS - COMPREHENSIVE FAANG LIST
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 TIER 1: ABSOLUTE MUST-KNOW (Top 15 - MASTER THESE FIRST!)
═══════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LC 55: Jump Game
   - Pattern: Jump Game / Greedy Choice Property
   - Why: #1 MOST ASKED GREEDY PROBLEM!
   - Company: ALL FAANG
   - Difficulty: 10/10 importance

2. ⭐⭐⭐ LC 45: Jump Game II
   - Pattern: Jump Game / BFS-like Greedy
   - Why: Follow-up to #1, very common
   - Company: Google, Meta, Amazon
   - Difficulty: 10/10 importance

3. ⭐⭐⭐ LC 253: Meeting Rooms II
   - Pattern: Intervals / Heap
   - Why: MOST ASKED INTERVAL PROBLEM!
   - Company: ALL FAANG (especially Google, Amazon)
   - Difficulty: 10/10 importance

4. ⭐⭐⭐ LC 435: Non-overlapping Intervals
   - Pattern: Intervals / Activity Selection
   - Why: Classic greedy, proves understanding
   - Company: Google, Meta, Microsoft
   - Difficulty: 9/10 importance

5. ⭐⭐⭐ LC 121: Best Time to Buy and Sell Stock
   - Pattern: Stock / Greedy Math
   - Why: Most common stock problem
   - Company: ALL (especially Amazon, Microsoft)
   - Difficulty: 9/10 importance

6. ⭐⭐⭐ LC 122: Best Time to Buy and Sell Stock II
   - Pattern: Stock / Sum All Increases
   - Why: Extension of #5
   - Company: Bloomberg, Amazon, Meta
   - Difficulty: 8/10 importance

7. ⭐⭐⭐ LC 134: Gas Station
   - Pattern: Two Pointer Greedy / Circular Array
   - Why: Tricky greedy insight
   - Company: Amazon, Google, Meta
   - Difficulty: 9/10 importance

8. ⭐⭐⭐ LC 621: Task Scheduler
   - Pattern: Greedy + Heap
   - Why: MOST ASKED HEAP + GREEDY!
   - Company: Meta, Google, Amazon
   - Difficulty: 9/10 importance

9. ⭐⭐⭐ LC 763: Partition Labels
   - Pattern: Greedy String
   - Why: Beautiful greedy solution
   - Company: Amazon, Bloomberg
   - Difficulty: 8/10 importance

10. ⭐⭐⭐ LC 452: Minimum Arrows to Burst Balloons
    - Pattern: Intervals
    - Why: Variant of activity selection
    - Company: Amazon, Microsoft
    - Difficulty: 8/10 importance

11. ⭐⭐⭐ LC 56: Merge Intervals
    - Pattern: Intervals
    - Why: FUNDAMENTAL interval problem
    - Company: ALL FAANG
    - Difficulty: 9/10 importance

12. ⭐⭐⭐ LC 402: Remove K Digits
    - Pattern: Stack Greedy / Monotonic Stack
    - Why: MOST IMPORTANT STACK GREEDY!
    - Company: Google, Meta
    - Difficulty: 8/10 importance

13. ⭐⭐⭐ LC 316: Remove Duplicate Letters
    - Pattern: Stack Greedy
    - Why: Classic stack greedy
    - Company: Google, Meta, Amazon
    - Difficulty: 8/10 importance

14. ⭐⭐⭐ LC 767: Reorganize String
    - Pattern: Greedy + Heap
    - Why: Important heap greedy
    - Company: Google, Amazon
    - Difficulty: 7/10 importance

15. ⭐⭐⭐ LC 135: Candy
    - Pattern: Greedy Math
    - Why: HARDEST GREEDY but very important!
    - Company: Google, Meta
    - Difficulty: 7/10 importance


🔥🔥 TIER 2: VERY IMPORTANT (Next 20)
═══════════════════════════════════════════════════════════════════════════

16. ⭐⭐ LC 252: Meeting Rooms
17. ⭐⭐ LC 57: Insert Interval
18. ⭐⭐ LC 714: Best Time to Buy and Sell Stock with Fee
19. ⭐⭐ LC 309: Best Time to Buy and Sell Stock with Cooldown
20. ⭐⭐ LC 678: Valid Parenthesis String
21. ⭐⭐ LC 455: Assign Cookies
22. ⭐⭐ LC 1710: Maximum Units on a Truck
23. ⭐⭐ LC 406: Queue Reconstruction by Height
24. ⭐⭐ LC 860: Lemonade Change
25. ⭐⭐ LC 881: Boats to Save People
26. ⭐⭐ LC 1047: Remove All Adjacent Duplicates
27. ⭐⭐ LC 1209: Remove All Adjacent Duplicates II
28. ⭐⭐ LC 561: Array Partition
29. ⭐⭐ LC 280: Wiggle Sort
30. ⭐⭐ LC 11: Container With Most Water (in Two Pointers guide)
31. ⭐⭐ LC 42: Trapping Rain Water (in Two Pointers guide)
32. ⭐⭐ LC 1405: Longest Happy String
33. ⭐⭐ LC 1353: Maximum Number of Events
34. ⭐⭐ LC 1663: Smallest String With Given Value
35. ⭐⭐ LC 1323: Maximum 69 Number


🔥 TIER 3: IMPORTANT (Complete Foundation - Next 15)
═══════════════════════════════════════════════════════════════════════════

36. ⭐ LC 1306: Jump Game III
37. ⭐ LC 1345: Jump Game IV  
38. ⭐ LC 1871: Jump Game VII
39. ⭐ LC 759: Employee Free Time
40. ⭐ LC 321: Create Maximum Number
41. ⭐ LC 1081: Smallest Subsequence (same as 316)
42. ⭐ LC 1673: Find Most Competitive Subsequence
43. ⭐ LC 358: Rearrange String k Distance Apart
44. ⭐ LC 324: Wiggle Sort II
45. ⭐ LC 1337: The K Weakest Rows
46. ⭐ LC 630: Course Schedule III
47. ⭐ LC 649: Dota2 Senate
48. ⭐ LC 991: Broken Calculator
49. ⭐ LC 1328: Break a Palindrome
50. ⭐ LC 1647: Minimum Deletions for Unique Frequencies


TIER 4: ADVANCED (After Mastering Basics - Final 10)
═══════════════════════════════════════════════════════════════════════════

51. LC 123: Best Time to Buy/Sell Stock III (DP, not greedy)
52. LC 188: Best Time to Buy/Sell Stock IV (DP, not greedy)
53. LC 738: Monotone Increasing Digits
54. LC 757: Set Intersection Size At Least Two
55. LC 936: Stamping The Sequence
56. LC 1505: Minimum Possible Integer
57. LC 1578: Minimum Deletion Cost
58. LC 1653: Minimum Deletions to Make String Balanced
59. LC 1689: Partitioning Into Minimum Number Of Deci-Binary
60. LC 1775: Equal Sum Arrays With Minimum Operations


═══════════════════════════════════════════════════════════════════════════
📊 PROBLEM BREAKDOWN BY PATTERN:
═══════════════════════════════════════════════════════════════════════════

Pattern 1 - Intervals (Most Important!): 12 problems
- LC 252, 253, 435, 452, 56, 57, 759, 1353, 630, etc.

Pattern 2 - Two Pointer Greedy: 5 problems
- LC 11, 42, 134, 455, 881

Pattern 3 - Sorting + Greedy: 7 problems
- LC 406, 455, 1710, 1663, 1323, 561, etc.

Pattern 4 - Stack Greedy: 8 problems
- LC 402, 316, 1081, 321, 1673, 1047, 1209, etc.

Pattern 5 - Jump Game: 5 problems
- LC 55, 45, 1306, 1345, 1871

Pattern 6 - Greedy + Heap: 6 problems
- LC 621, 767, 1405, 1337, 358, 253

Pattern 7 - Greedy String: 8 problems
- LC 763, 678, 1047, 1209, 1663, 1328, etc.

Pattern 8 - Array Rearrangement: 5 problems
- LC 561, 280, 324, etc.

Pattern 9 - Stock Problems: 6 problems
- LC 121, 122, 714, 309, 123, 188

Pattern 10 - Greedy Math: 8 problems
- LC 135, 860, 881, 991, 738, etc.


═══════════════════════════════════════════════════════════════════════════
🎯 6-WEEK COMPREHENSIVE STUDY PLAN:
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - JUMP GAME & FUNDAMENTALS:
────────────────────────────────────────────────────────────────────────
Day 1: Theory + LC 55 (Jump Game) ⚠️ CRITICAL!
  - Read all pattern descriptions
  - Understand greedy vs DP
  - Master LC 55 completely

Day 2: LC 45 (Jump Game II) ⚠️ CRITICAL!
  - BFS-like greedy
  - Practice explaining the intuition

Day 3: LC 121 (Stock I) + LC 122 (Stock II)
  - Track min price strategy
  - Sum all increases strategy

Day 4: LC 714 (Stock with Fee) + LC 309 (Cooldown)
  - State machine approach
  - Practice both

Day 5: Review all Jump + Stock problems
Day 6-7: Redo Week 1 problems for speed


WEEK 2 - INTERVALS (MOST IMPORTANT WEEK!):
────────────────────────────────────────────────────────────────────────
Day 1: LC 252 (Meeting Rooms) + LC 253 (Meeting Rooms II) ⚠️⚠️⚠️
  - SPEND EXTRA TIME ON 253!
  - Master both heap and two-array approaches
  - This is THE most asked interval problem!

Day 2: LC 435 (Non-overlapping) + LC 452 (Arrows) ⚠️⚠️
  - Activity selection pattern
  - Sort by end time strategy

Day 3: LC 56 (Merge Intervals) + LC 57 (Insert) ⭐⭐
  - Fundamental merging
  - Edge cases

Day 4: LC 1353 (Max Events) + LC 759 (Employee Free Time)
  - Advanced interval problems

Day 5: Review ALL interval problems
  - Practice explaining sort choice
  - Master the pattern

Day 6-7: Redo all Week 2 under time pressure


WEEK 3 - GREEDY + HEAP & STACK:
────────────────────────────────────────────────────────────────────────
Day 1: LC 621 (Task Scheduler) ⚠️⚠️⚠️
  - MOST IMPORTANT HEAP PROBLEM!
  - Master both heap and formula approaches

Day 2: LC 767 (Reorganize String) + LC 1405 (Happy String)
  - Heap greedy pattern
  - Impossible case detection

Day 3: LC 402 (Remove K Digits) ⚠️⚠️⚠️
  - MOST IMPORTANT STACK GREEDY!
  - Monotonic stack pattern

Day 4: LC 316 (Remove Duplicates) + LC 1081 (Smallest Subseq)
  - Stack + last occurrence
  - Very tricky!

Day 5: LC 1047 + LC 1209 (Adjacent Duplicates)
  - Stack applications

Day 6-7: Review + practice all heap/stack problems


WEEK 4 - STRING & ARRAY REARRANGEMENT:
────────────────────────────────────────────────────────────────────────
Day 1: LC 763 (Partition Labels) ⚠️
  - Beautiful greedy problem
  - Last occurrence technique

Day 2: LC 678 (Valid Parenthesis String) ⚠️
  - Min/max open brackets
  - Tricky greedy

Day 3: LC 406 (Queue Reconstruction) ⚠️
  - Sort + insert strategy
  - Practice dry run

Day 4: LC 561 (Array Partition) + LC 280 (Wiggle)
  - Pairing strategies
  - One-pass wiggle

Day 5: LC 324 (Wiggle II) (harder variant)
Day 6-7: Review all string/array problems


WEEK 5 - GREEDY MATH & TRICKY PROBLEMS:
────────────────────────────────────────────────────────────────────────
Day 1: LC 134 (Gas Station) ⚠️⚠️⚠️
  - CRITICAL PROBLEM!
  - Understand the greedy insight
  - Practice proof

Day 2: LC 135 (Candy) ⚠️⚠️⚠️
  - HARDEST GREEDY PROBLEM!
  - Two-pass technique
  - Spend extra time!

Day 3: LC 860 (Lemonade) + LC 881 (Boats)
  - Greedy choices
  - Two pointer + greedy

Day 4: LC 455 (Cookies) + LC 1710 (Max Units)
  - Sorting + greedy
  - Simple but important

Day 5: LC 1663 (Smallest String) + LC 1323 (Max 69)
  - Greedy construction

Day 6-7: Review all greedy math


WEEK 6 - COMPREHENSIVE REVIEW & MOCK:
────────────────────────────────────────────────────────────────────────
Day 1: Review TOP 15 problems (Tier 1)
  - Redo all without looking
  - Time yourself

Day 2: Company-specific focus
  - Google: 55, 45, 253, 621, 402, 135
  - Meta: 55, 253, 621, 316, 767, 678
  - Amazon: 55, 253, 121, 134, 763, 452

Day 3: Mock interview - Intervals
  - Pick 2-3 random interval problems
  - 45 min time limit
  - Explain out loud

Day 4: Mock interview - Mixed patterns
  - Random problems from different patterns
  - Practice pattern recognition

Day 5: Weak areas
  - Identify your weakest pattern
  - Do 5+ problems from that pattern

Day 6: Final review - Templates
  - Memorize all master templates
  - Review pattern selection guide

Day 7: Rest & confidence building
  - Review notes
  - Quick run through Tier 1


═══════════════════════════════════════════════════════════════════════════
💡 MASTER TEMPLATES (MEMORIZE THESE!):
═══════════════════════════════════════════════════════════════════════════

TEMPLATE 1: Activity Selection (Intervals)
──────────────────────────────────────────────────────────────────────────
# Sort by END time
intervals.sort(key=lambda x: x[1])

count = 1
prev_end = intervals[0][1]

for i in range(1, len(intervals)):
    if intervals[i][0] >= prev_end:
        count += 1
        prev_end = intervals[i][1]

return count


TEMPLATE 2: Meeting Rooms II (Min Rooms)
──────────────────────────────────────────────────────────────────────────
# Approach 1: Heap
intervals.sort()
heap = []

for start, end in intervals:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

return len(heap)

# Approach 2: Two arrays
starts = sorted([i[0] for i in intervals])
ends = sorted([i[1] for i in intervals])

rooms = max_rooms = 0
i = j = 0

while i < len(starts):
    if starts[i] < ends[j]:
        rooms += 1
        max_rooms = max(max_rooms, rooms)
        i += 1
    else:
        rooms -= 1
        j += 1

return max_rooms


TEMPLATE 3: Jump Game
──────────────────────────────────────────────────────────────────────────
# Jump Game I: Can reach?
max_reach = 0

for i in range(len(nums)):
    if i > max_reach:
        return False
    max_reach = max(max_reach, i + nums[i])

return max_reach >= len(nums) - 1

# Jump Game II: Min jumps
jumps = 0
current_end = 0
furthest = 0

for i in range(len(nums) - 1):
    furthest = max(furthest, i + nums[i])
    
    if i == current_end:
        jumps += 1
        current_end = furthest

return jumps


TEMPLATE 4: Stack Greedy (Remove K Digits)
──────────────────────────────────────────────────────────────────────────
stack = []

for digit in num:
    # Remove larger digits while possible
    while k > 0 and stack and stack[-1] > digit:
        stack.pop()
        k -= 1
    stack.append(digit)

# Remove remaining k from end
if k > 0:
    stack = stack[:-k]

result = ''.join(stack).lstrip('0')
return result if result else '0'


TEMPLATE 5: Stack Greedy (Remove Duplicates)
──────────────────────────────────────────────────────────────────────────
last_occurrence = {char: i for i, char in enumerate(s)}

stack = []
in_stack = set()

for i, char in enumerate(s):
    if char in in_stack:
        continue
    
    # Remove larger chars that appear later
    while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
        removed = stack.pop()
        in_stack.remove(removed)
    
    stack.append(char)
    in_stack.add(char)

return ''.join(stack)


TEMPLATE 6: Greedy + Heap (Task Scheduler)
──────────────────────────────────────────────────────────────────────────
# Heap approach
freq = Counter(tasks)
heap = [-count for count in freq.values()]
heapq.heapify(heap)

time = 0

while heap:
    temp = []
    
    for _ in range(n + 1):
        if heap:
            count = heapq.heappop(heap)
            if count < -1:
                temp.append(count + 1)
            time += 1
        elif temp:
            time += 1  # Idle
    
    for count in temp:
        heapq.heappush(heap, count)

return time

# Formula approach
max_freq = max(freq.values())
max_count = sum(1 for f in freq.values() if f == max_freq)

return max(
    len(tasks),
    (max_freq - 1) * (n + 1) + max_count
)


TEMPLATE 7: Stock Buy/Sell
──────────────────────────────────────────────────────────────────────────
# Stock I: One transaction
min_price = float('inf')
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(max_profit, profit)

return max_profit

# Stock II: Unlimited transactions
profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        profit += prices[i] - prices[i-1]

return profit


TEMPLATE 8: Greedy String (Partition Labels)
──────────────────────────────────────────────────────────────────────────
last = {char: i for i, char in enumerate(s)}

result = []
start = end = 0

for i, char in enumerate(s):
    end = max(end, last[char])
    
    if i == end:
        result.append(end - start + 1)
        start = i + 1

return result


═══════════════════════════════════════════════════════════════════════════
🎓 PATTERN RECOGNITION GUIDE:
═══════════════════════════════════════════════════════════════════════════

KEYWORDS → PATTERN:
──────────────────────────────────────────────────────────────────────────

"intervals" / "meetings" / "overlapping"
→ Pattern 1: Intervals
→ Sort by end time for activity selection
→ Use heap for multiple resources

"jump" / "reach" / "can reach end"
→ Pattern 5: Jump Game
→ Track furthest reachable position

"buy/sell stock" / "profit" / "transaction"
→ Pattern 9: Stock
→ Identify variant (once/unlimited/fee/cooldown)

"remove K" / "smallest/largest number"
→ Pattern 4: Stack Greedy
→ Monotonic stack approach

"schedule" / "tasks" / "cooldown"
→ Pattern 6: Greedy + Heap
→ Use max-heap for frequencies

"partition" / "reorganize" / "rearrange"
→ Pattern 7: Greedy String OR Pattern 8: Array
→ Last occurrence or sorting

"minimum" / "maximum" + can sort
→ Pattern 3: Sorting + Greedy
→ Sort first, then greedy choice

"candy" / "gas station" / "change"
→ Pattern 10: Greedy Math
→ Mathematical insight needed


WHEN TO USE GREEDY VS DP:
──────────────────────────────────────────────────────────────────────────

Use GREEDY when:
✅ Can prove greedy choice property
✅ Local optimum = global optimum
✅ No overlapping subproblems
✅ Can make irreversible decisions

Examples:
- Activity Selection ✓
- Huffman Coding ✓
- Fractional Knapsack ✓
- Jump Game I, II ✓

Use DP when:
❌ Greedy has counterexample
❌ Need to explore all possibilities
❌ Overlapping subproblems exist
❌ State depends on previous states

Examples:
- 0/1 Knapsack ✗
- Longest Common Subsequence ✗
- Stock IV (k transactions) ✗


═══════════════════════════════════════════════════════════════════════════
🏢 COMPANY-SPECIFIC FOCUS:
═══════════════════════════════════════════════════════════════════════════

GOOGLE (Loves intervals, heap, hard greedy):
────────────────────────────────────────────────────────────────────────
Must Know: 55, 45, 253, 435, 621, 402, 135, 316, 767
Important: 56, 452, 763, 134, 678

META/FACEBOOK (Balanced across patterns):
────────────────────────────────────────────────────────────────────────
Must Know: 55, 253, 621, 316, 767, 763, 678, 134
Important: 435, 45, 402, 56, 1405

AMAZON (Focus on intervals, stock, arrays):
────────────────────────────────────────────────────────────────────────
Must Know: 55, 253, 121, 122, 134, 452, 763, 1710
Important: 435, 56, 57, 860, 455, 406

MICROSOFT (Balanced, loves stock problems):
────────────────────────────────────────────────────────────────────────
Must Know: 121, 122, 55, 253, 56, 435, 860
Important: 455, 881, 1710, 561, 252

BLOOMBERG (Loves stock, intervals):
────────────────────────────────────────────────────────────────────────
Must Know: 121, 122, 714, 309, 253, 435, 763
Important: 56, 621, 452, 134


═══════════════════════════════════════════════════════════════════════════
🚨 COMMON MISTAKES TO AVOID:
═══════════════════════════════════════════════════════════════════════════

1. ❌ Using DP when greedy works
   - Waste time on complex solution
   - Jump Game doesn't need DP!

2. ❌ Not sorting when needed
   - Intervals MUST be sorted
   - Greedy often needs sorted input

3. ❌ Wrong sort key
   - Activity selection: sort by END time!
   - Not start time!

4. ❌ Forgetting edge cases
   - Empty array
   - Single element
   - All same values

5. ❌ Not proving greedy choice
   - In interview, explain WHY greedy works
   - Give counterexample if it doesn't

6. ❌ Using wrong data structure
   - Heap for Meeting Rooms II (not array)
   - Stack for Remove K Digits (not greedy removal)

7. ❌ Overcomplicating simple problems
   - Stock II: just sum increases!
   - Don't overthink

8. ❌ Not considering impossible cases
   - Task Scheduler: max_freq too high
   - Reorganize String: frequency > (n+1)/2


═══════════════════════════════════════════════════════════════════════════
✅ PROGRESS CHECKLIST:
═══════════════════════════════════════════════════════════════════════════

Week 1 - Jump & Stock:
□ 55: Jump Game ⚠️⚠️⚠️
□ 45: Jump Game II ⚠️⚠️⚠️
□ 121: Stock I ⚠️⚠️
□ 122: Stock II ⚠️⚠️
□ 714: Stock with Fee
□ 309: Stock with Cooldown

Week 2 - Intervals:
□ 252: Meeting Rooms
□ 253: Meeting Rooms II ⚠️⚠️⚠️ CRITICAL!
□ 435: Non-overlapping ⚠️⚠️⚠️
□ 452: Arrows ⚠️⚠️
□ 56: Merge Intervals ⚠️⚠️
□ 57: Insert Interval ⚠️

Week 3 - Heap & Stack:
□ 621: Task Scheduler ⚠️⚠️⚠️ CRITICAL!
□ 767: Reorganize String ⚠️⚠️
□ 1405: Happy String
□ 402: Remove K Digits ⚠️⚠️⚠️ CRITICAL!
□ 316: Remove Duplicates ⚠️⚠️⚠️
□ 1047, 1209: Adjacent Duplicates

Week 4 - String & Array:
□ 763: Partition Labels ⚠️⚠️
□ 678: Valid Parenthesis ⚠️⚠️
□ 406: Queue Reconstruction ⚠️
□ 561: Array Partition
□ 280: Wiggle Sort
□ 324: Wiggle Sort II

Week 5 - Greedy Math:
□ 134: Gas Station ⚠️⚠️⚠️ CRITICAL!
□ 135: Candy ⚠️⚠️⚠️ HARDEST!
□ 860: Lemonade
□ 881: Boats
□ 455: Cookies
□ 1710: Max Units

Week 6 - Review & Mock:
□ Redo all Tier 1 problems
□ Company-specific practice
□ Mock interviews
□ Template mastery


═══════════════════════════════════════════════════════════════════════════
🎯 YOU'RE READY FOR INTERVIEWS WHEN:
═══════════════════════════════════════════════════════════════════════════

✅ Can solve LC 55 in under 5 minutes
✅ Can solve LC 253 with both approaches
✅ Know when to use greedy vs DP
✅ Can explain greedy choice property
✅ Recognize interval patterns instantly
✅ Master stack greedy (LC 402, 316)
✅ Comfortable with heap greedy (LC 621)
✅ Know all stock variants (121, 122, 714, 309)
✅ Can solve LC 134 and explain the insight
✅ Survived LC 135 (Candy) 😅
✅ Memorized all master templates
✅ Can pattern-match in <1 minute


═══════════════════════════════════════════════════════════════════════════
🔑 FINAL SUCCESS TIPS:
═══════════════════════════════════════════════════════════════════════════

1. ⭐ THE BIG 5 TO MASTER ABSOLUTELY:
   - LC 55 (Jump Game) - Foundation
   - LC 253 (Meeting Rooms II) - Intervals
   - LC 621 (Task Scheduler) - Heap Greedy
   - LC 402 (Remove K Digits) - Stack Greedy
   - LC 134 (Gas Station) - Greedy Insight

2. PATTERN RECOGNITION IS KEY:
   - See "intervals"? → Sort by end time
   - See "jump"? → Track max reach
   - See "remove K"? → Monotonic stack
   - See "schedule"? → Heap

3. PROVE THE GREEDY CHOICE:
   - Always explain WHY greedy works
   - Give brief proof or intuition
   - Show counterexample for DP if needed

4. INTERVALS ARE EVERYWHERE:
   - 20%+ of greedy problems
   - Master LC 253 thoroughly
   - Know both heap and two-array solutions

5. PRACTICE EXPLAINING OUT LOUD:
   - "I'll use greedy because..."
   - "The greedy choice is..."
   - "This works because..."

6. MEMORIZE TEMPLATES:
   - Don't reinvent the wheel
   - Interval template
   - Stack greedy template
   - Jump game template

7. TIME MANAGEMENT:
   - Easy greedy: 10-15 min
   - Medium greedy: 20-25 min
   - Hard greedy (135): 30+ min ok!

8. WHEN STUCK:
   - Try sorting first
   - Consider heap if multiple choices
   - Think about local vs global
   - Can I prove greedy works?

9. COMPANY PREPARATION:
   - Google: Focus on intervals + hard greedy
   - Meta: Balanced, know heap well
   - Amazon: Intervals + arrays + stock
   - Microsoft: Stock problems + basics

10. THE ULTIMATE TEST:
    Can you solve LC 55, 253, 621, 402, 134 without hints?
    If YES → You're interview-ready! 🎉


═══════════════════════════════════════════════════════════════════════════
📚 FINAL WORDS:
═══════════════════════════════════════════════════════════════════════════

Greedy is the MOST PRACTICAL algorithm pattern:
- Appears in 30-40% of coding interviews
- Often O(n) or O(n log n) - very efficient
- Tests problem-solving creativity
- Proves algorithmic maturity

MASTER THE PATTERNS:
✅ Intervals (Pattern 1) - MOST IMPORTANT!
✅ Jump Game (Pattern 5) - MOST ASKED!
✅ Stack Greedy (Pattern 4) - MOST CLEVER!
✅ Greedy + Heap (Pattern 6) - MOST PRACTICAL!

Remember: Greedy is about making the BEST local choice!
Sometimes it's obvious (Jump Game)
Sometimes it's tricky (Gas Station, Candy)
But once you see it, you can't unsee it! 💡

Good luck! You've got this! 🚀
Master these 60 problems and greedy becomes your superpower! 💪

P.S. If you can solve LC 135 (Candy), you can solve ANYTHING! 😎
"""


if __name__ == "__main__":
    # Test the greedy patterns
    gp = GreedyPatterns()
    
    print("🧪 Testing Greedy Patterns...\n")
    
    # Test intervals
    assert gp.canAttendMeetings_LC252([[0,30],[5,10],[15,20]]) == False
    print("✅ Meeting Rooms: Passed")
    
    assert gp.minMeetingRooms_LC253([[0,30],[5,10],[15,20]]) == 2
    print("✅ Meeting Rooms II: Passed")
    
    assert gp.eraseOverlapIntervals_LC435([[1,2],[2,3],[3,4],[1,3]]) == 1
    print("✅ Non-overlapping Intervals: Passed")
    
    # Test jump game
    assert gp.canJump_LC55([2,3,1,1,4]) == True
    assert gp.canJump_LC55([3,2,1,0,4]) == False
    print("✅ Jump Game: Passed")
    
    assert gp.jump_LC45([2,3,1,1,4]) == 2
    print("✅ Jump Game II: Passed")
    
    # Test gas station
    assert gp.canCompleteCircuit_LC134([1,2,3,4,5], [3,4,5,1,2]) == 3
    print("✅ Gas Station: Passed")
    
    # Test stock
    assert gp.maxProfit_LC121([7,1,5,3,6,4]) == 5
    print("✅ Stock I: Passed")
    
    assert gp.maxProfit_LC122([7,1,5,3,6,4]) == 7
    print("✅ Stock II: Passed")
    
    # Test stack greedy
    assert gp.removeKdigits_LC402("1432219", 3) == "1219"
    print("✅ Remove K Digits: Passed")
    
    assert gp.removeDuplicateLetters_LC316("bcabc") == "abc"
    print("✅ Remove Duplicate Letters: Passed")
    
    # Test partition labels
    assert gp.partitionLabels_LC763("ababcbacadefegdehijhklij") == [9,7,8]
    print("✅ Partition Labels: Passed")
    
    # Test candy
    assert gp.candy_LC135([1,0,2]) == 5
    print("✅ Candy: Passed")
    
    print("\n🎉 All greedy patterns tested successfully!")
    print("\n📚 FOCUS AREAS:")
    print("   1. Master LC 55 & 45 (Jump Game)")
    print("   2. Master LC 253 (Meeting Rooms II) - MOST ASKED!")
    print("   3. Master LC 621 (Task Scheduler)")
    print("   4. Master LC 402 & 316 (Stack Greedy)")
    print("   5. Master LC 134 & 135 (Gas, Candy)")
    print("\n⏰ Recommended: 6 weeks, 1-1.5 hours daily")
    print("🎯 Week 2 (Intervals) is MOST important for interviews!")