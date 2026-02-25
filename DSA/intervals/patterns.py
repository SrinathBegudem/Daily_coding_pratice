"""
═══════════════════════════════════════════════════════════════════════════════
                    INTERVAL PATTERNS MASTERY GUIDE
              THE MOST ASKED PATTERN IN FAANG INTERVIEWS!
═══════════════════════════════════════════════════════════════════════════════

🎯 WHY INTERVALS ARE CRITICAL:

1. APPEARS IN 20-30% OF FAANG CODING INTERVIEWS!
   - Google: 35% of interviews have interval problems
   - Amazon: 25% of interviews
   - Meta: 30% of interviews
   - Microsoft: 20% of interviews
   - Bloomberg: 40% of interviews (loves intervals!)

2. TESTS MULTIPLE SKILLS:
   ✅ Sorting algorithms
   ✅ Greedy thinking
   ✅ Edge case handling
   ✅ Data structure selection (heap, sweep line, etc.)
   ✅ Time/Space optimization

3. ONE PATTERN → SOLVE 20+ PROBLEMS!
   Master the universal template and you can solve:
   - Meeting Rooms (all variants)
   - Merge/Insert Intervals
   - Non-overlapping problems
   - Scheduling problems
   - Event processing
   - And more!

═══════════════════════════════════════════════════════════════════════════════
🔑 THE UNIVERSAL INTERVAL FRAMEWORK
═══════════════════════════════════════════════════════════════════════════════

STEP 1: IDENTIFY THE INTERVAL PROBLEM TYPE
────────────────────────────────────────────────────────────────────────────

Ask yourself these questions:

1️⃣ "Do I need to CHECK overlap/count overlaps?"
   → Pattern 1: Overlap Detection
   → Examples: Meeting Rooms I, Can Attend All Appointments

2️⃣ "Do I need to COUNT maximum simultaneous intervals?"
   → Pattern 2: Maximum Overlapping (Heap or Sweep Line)
   → Examples: Meeting Rooms II, Min Platforms, Car Pooling

3️⃣ "Do I need to MERGE overlapping intervals?"
   → Pattern 3: Merge Intervals
   → Examples: Merge Intervals, Insert Interval

4️⃣ "Do I need to SELECT maximum non-overlapping intervals?"
   → Pattern 4: Activity Selection (Greedy)
   → Examples: Non-overlapping Intervals, Min Arrows

5️⃣ "Do I need to PROCESS intervals by events?"
   → Pattern 5: Event-based Processing (Sweep Line)
   → Examples: My Calendar, Skyline Problem

6️⃣ "Do I need to FIND gaps or intersections?"
   → Pattern 6: Interval Algebra
   → Examples: Interval Intersection, Employee Free Time


STEP 2: CHOOSE THE RIGHT APPROACH
────────────────────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────────────────┐
│                    INTERVAL DECISION TREE                               │
└─────────────────────────────────────────────────────────────────────────┘

                        START: Got Interval Problem?
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
              Can overlap?                    Must be separate?
                    │                               │
        ┌───────────┴───────────┐          ┌───────┴───────┐
        │                       │          │               │
   Just check?           Count/Optimize?  Select max?   Remove min?
        │                       │          │               │
    Pattern 1              Pattern 2    Pattern 4       Pattern 4
    (Sort once)         (Heap/Sweep)   (Greedy)        (Greedy)
        │                       │          │               │
   O(n log n)            O(n log n)   O(n log n)      O(n log n)
        │                       │          │               │
    ┌───┴────┐            ┌────┴────┐    └───────────────┘
    │        │            │         │
 Merge?   Insert?      Heap?   Sweep Line?
    │        │            │         │
Pattern 3  Pattern 3  Pattern 2  Pattern 5


STEP 3: APPLY THE UNIVERSAL TEMPLATE
────────────────────────────────────────────────────────────────────────────

🔥 MASTER TEMPLATE (Works for 80% of problems!):

```python
def solve_interval_problem(intervals):
    # STEP 1: Edge cases
    if not intervals:
        return []  # or appropriate default
    
    # STEP 2: Sort intervals
    # Choose sort key based on problem type:
    #   - Most cases: sort by START time
    #   - Activity selection: sort by END time
    #   - Custom: sort by custom key
    intervals.sort()  # or intervals.sort(key=lambda x: x[1])
    
    # STEP 3: Initialize result
    result = []  # or count = 0, or heap = []
    
    # STEP 4: Process intervals one by one
    for current in intervals:
        # Pattern-specific logic:
        # - Overlap check: compare with previous
        # - Merge: extend or add
        # - Heap: push/pop based on condition
        # - Greedy: select or skip
        pass
    
    # STEP 5: Return result
    return result
```

═══════════════════════════════════════════════════════════════════════════════
"""

from typing import List, Optional
import heapq
from collections import defaultdict

class IntervalPatterns:
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 1: OVERLAP DETECTION (Can Attend All?)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 PROBLEM TYPE: Check if ANY two intervals overlap
    
    🔑 KEY INSIGHT:
    After sorting by START time:
    - If intervals[i].start < intervals[i-1].end → OVERLAP!
    - One pass is enough!
    
    ⏱️  Time: O(n log n) | Space: O(1)
    
    🎓 GENERIC TEMPLATE:
    
    def has_overlap(intervals):
        intervals.sort()  # Sort by start time
        
        for i in range(1, len(intervals)):
            # If current starts before previous ends
            if intervals[i][0] < intervals[i-1][1]:
                return True  # Overlap found!
        
        return False  # No overlaps
    
    
    📝 DETAILED DRY RUN:
    ═══════════════════════════════════════════════════════════════════════
    
    Problem: Can person attend all meetings?
    Input: intervals = [[0,30], [5,10], [15,20]]
    Output: False
    
    Visualization:
    Timeline: 0----5----10----15----20----30
    Meeting1: [=============================]  (0-30)
    Meeting2:      [====]                      (5-10)
    Meeting3:               [====]             (15-20)
                   ↑
              OVERLAP! (Meeting1 and Meeting2 overlap)
    
    Step-by-step:
    
    Initial: intervals = [[0,30], [5,10], [15,20]]
    After sort: [[0,30], [5,10], [15,20]] (already sorted)
    
    i=1: Check [5,10] vs [0,30]
         current.start = 5
         previous.end = 30
         5 < 30? YES → OVERLAP DETECTED ✗
         Return False
    
    Another Example (No Overlap):
    Input: intervals = [[1,4], [5,8], [9,12]]
    
    Timeline: 0--1--4--5--8--9--12
    Meeting1:    [==]              (1-4)
    Meeting2:         [==]         (5-8)
    Meeting3:              [==]    (9-12)
              No overlap!
    
    After sort: [[1,4], [5,8], [9,12]]
    
    i=1: 5 < 4? NO ✓
    i=2: 9 < 8? NO ✓
    Return True (can attend all)
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 252: Meeting Rooms (easy) ⭐⭐⭐
    - LeetCode 1229: Meeting Scheduler (medium) ⭐⭐
    - LeetCode 495: Teemo Attacking (medium) ⭐
    """
    
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        LeetCode 252: Meeting Rooms
        
        FOUNDATION PROBLEM - MASTER THIS FIRST!
        
        Can a person attend all meetings?
        
        Input: [[0,30],[5,10],[15,20]]
        Output: False (0-30 overlaps with 5-10)
        """
        if not intervals:
            return True
        
        # Sort by start time
        intervals.sort()
        
        # Check each adjacent pair
        for i in range(1, len(intervals)):
            # If current starts before previous ends
            if intervals[i][0] < intervals[i-1][1]:
                return False  # Overlap detected
        
        return True  # No overlaps
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 2: MAXIMUM OVERLAPPING (Meeting Rooms II)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 PROBLEM TYPE: Find MAXIMUM number of overlapping intervals at any time
    
    🔑 KEY INSIGHT:
    Need to track "active" intervals at each point in time.
    
    THREE APPROACHES:
    
    APPROACH 1: MIN-HEAP (BEST for interviews!)
    ────────────────────────────────────────────────────────────────────
    - Sort by start time
    - Use heap to track end times
    - When new meeting starts:
      → If earliest ending meeting is done (heap[0] <= start): reuse room
      → Else: need new room
    - Heap size = rooms needed
    
    Time: O(n log n) | Space: O(n)
    
    
    APPROACH 2: SEPARATE ARRAYS (Most Elegant!)
    ────────────────────────────────────────────────────────────────────
    - Separate start and end times
    - Sort both independently
    - Use two pointers:
      → Start event: rooms++
      → End event: rooms--
    - Track maximum
    
    Time: O(n log n) | Space: O(n)
    
    
    APPROACH 3: SWEEP LINE (Most Powerful!)
    ────────────────────────────────────────────────────────────────────
    - Create events: (time, +1 for start, -1 for end)
    - Sort events
    - Sweep through, tracking active count
    
    Time: O(n log n) | Space: O(n)
    
    
    📝 DETAILED DRY RUN - HEAP APPROACH:
    ═══════════════════════════════════════════════════════════════════════
    
    Problem: Minimum meeting rooms needed?
    Input: intervals = [[0,30], [5,10], [15,20]]
    Output: 2
    
    Visualization:
    Timeline: 0----5----10----15----20----30
    Room 1:   [=============================]  (0-30)
    Room 2:        [====]     [====]           (5-10, 15-20)
                   ↑          ↑
              Need 2nd    Reuse Room 2
    
    Algorithm with Heap:
    
    Step 1: Sort by start time
    intervals = [[0,30], [5,10], [15,20]]
    
    Step 2: Initialize
    heap = []  (stores end times of active meetings)
    max_rooms = 0
    
    Step 3: Process each meeting
    
    Meeting 1: [0, 30]
      - Heap is empty, add new room
      - heap = [30]
      - Rooms in use: 1
      - max_rooms = 1
      
      Interpretation: Room 1 is occupied until time 30
    
    Meeting 2: [5, 10]
      - Check if any room is free
      - Earliest ending: heap[0] = 30
      - Start time: 5
      - Is 5 >= 30? NO (room not free yet)
      - Need NEW room
      - heap = [10, 30]  (min-heap: 10 is at top)
      - Rooms in use: 2
      - max_rooms = 2
      
      Interpretation: Room 1 occupied until 30, Room 2 until 10
    
    Meeting 3: [15, 20]
      - Check if any room is free
      - Earliest ending: heap[0] = 10
      - Start time: 15
      - Is 15 >= 10? YES (Room 2 is free!)
      - REUSE Room 2
      - Remove 10, add 20
      - heap = [20, 30]
      - Rooms in use: 2
      - max_rooms = 2 (no change)
      
      Interpretation: Room 1 still until 30, Room 2 now until 20
    
    Final Answer: max_rooms = 2 ✓
    
    
    📝 DETAILED DRY RUN - TWO ARRAYS APPROACH:
    ═══════════════════════════════════════════════════════════════════════
    
    Same problem: [[0,30], [5,10], [15,20]]
    
    Step 1: Separate and sort
    starts = [0, 5, 15]   (sorted start times)
    ends   = [10, 20, 30] (sorted end times)
    
    Step 2: Initialize two pointers
    i = 0  (pointer for starts)
    j = 0  (pointer for ends)
    rooms = 0
    max_rooms = 0
    
    Step 3: Process events
    
    Event 1: starts[0] = 0 vs ends[0] = 10
      - 0 < 10 → Meeting STARTS
      - rooms = 1
      - max_rooms = 1
      - i = 1
      
      Interpretation: First meeting starts at 0
    
    Event 2: starts[1] = 5 vs ends[0] = 10
      - 5 < 10 → Meeting STARTS
      - rooms = 2
      - max_rooms = 2
      - i = 2
      
      Interpretation: Second meeting starts before first ends
    
    Event 3: starts[2] = 15 vs ends[0] = 10
      - 15 >= 10 → Meeting ENDS
      - rooms = 1
      - j = 1
      
      Interpretation: First meeting to end (at 10) frees a room
    
    Event 4: starts[2] = 15 vs ends[1] = 20
      - 15 < 20 → Meeting STARTS
      - rooms = 2
      - i = 3 (done with starts)
      
      Interpretation: Third meeting starts
    
    Final Answer: max_rooms = 2 ✓
    
    
    🎓 WHY THIS WORKS:
    
    KEY INSIGHT: We don't care WHICH room is which!
    We only care about the COUNT of active meetings.
    
    - When a meeting starts: count++
    - When a meeting ends: count--
    - Maximum count = rooms needed
    
    By sorting start/end times separately:
    - We process all events in chronological order
    - But we prioritize ends over starts at same time
      (that's why we use < instead of <=)
    
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 253: Meeting Rooms II (medium) ⭐⭐⭐ MOST ASKED!
    - LeetCode 1094: Car Pooling (medium) ⭐⭐⭐
    - LeetCode 1893: Check Coverage (easy) ⭐
    - LeetCode 2848: Points That Intersect (easy) ⭐
    """
    
    def minMeetingRooms_heap(self, intervals: List[List[int]]) -> int:
        """
        LeetCode 253: Meeting Rooms II
        
        APPROACH 1: MIN-HEAP
        
        THE MOST ASKED INTERVAL PROBLEM IN FAANG!
        
        Master this completely - appears in 30% of Google interviews!
        """
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort()
        
        # Min-heap to track end times
        heap = []
        
        for start, end in intervals:
            # If earliest ending meeting is done, reuse room
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # Add current meeting's end time
            heapq.heappush(heap, end)
        
        # Heap size = max rooms needed
        return len(heap)
    
    
    def minMeetingRooms_twoArrays(self, intervals: List[List[int]]) -> int:
        """
        LeetCode 253: Meeting Rooms II
        
        APPROACH 2: TWO ARRAYS
        
        More intuitive once you understand the concept!
        """
        if not intervals:
            return 0
        
        # Separate start and end times
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        rooms = max_rooms = 0
        i = j = 0
        
        # Process all start events
        while i < len(starts):
            # If meeting starts before earliest ends
            if starts[i] < ends[j]:
                # New meeting starts, need room
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                # Meeting ends, free room
                rooms -= 1
                j += 1
        
        return max_rooms
    
    
    def minMeetingRooms_sweepLine(self, intervals: List[List[int]]) -> int:
        """
        LeetCode 253: Meeting Rooms II
        
        APPROACH 3: SWEEP LINE
        
        Most powerful for complex problems!
        """
        # Create events: (time, type)
        # type: +1 for start, -1 for end
        events = []
        
        for start, end in intervals:
            events.append((start, 1))   # Meeting starts
            events.append((end, -1))    # Meeting ends
        
        # Sort events
        # If same time, process ends before starts
        events.sort(key=lambda x: (x[0], x[1]))
        
        rooms = max_rooms = 0
        
        for time, delta in events:
            rooms += delta
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms
    
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        LeetCode 1094: Car Pooling
        
        Same as Meeting Rooms II, but checking capacity!
        
        trips[i] = [numPassengers, from, to]
        
        🔑 INSIGHT: This is meeting rooms with weights!
        
        Input: trips = [[2,1,5],[3,3,7]], capacity = 4
        Output: False
        
        Timeline:  1----3----5----7
        Trip 1:    2ppl [======]
        Trip 2:         3ppl [======]
                        ↑
                   At time 3: 2+3=5 > 4 ✗
        """
        # Sweep line approach
        events = []
        
        for passengers, start, end in trips:
            events.append((start, passengers))   # Pick up
            events.append((end, -passengers))    # Drop off
        
        # Sort by time, drop-offs before pick-ups
        events.sort()
        
        current_passengers = 0
        
        for time, delta in events:
            current_passengers += delta
            
            if current_passengers > capacity:
                return False
        
        return True
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 3: MERGE/INSERT INTERVALS
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 PROBLEM TYPE: Merge overlapping intervals
    
    🔑 KEY INSIGHT:
    After sorting by START:
    - If intervals[i].start <= last_merged.end → MERGE
    - Else → Add as new interval
    
    ⏱️  Time: O(n log n) | Space: O(n)
    
    🎓 GENERIC TEMPLATE:
    
    def merge_intervals(intervals):
        intervals.sort()  # Sort by start time
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
    
    
    📝 DETAILED DRY RUN - MERGE INTERVALS:
    ═══════════════════════════════════════════════════════════════════════
    
    Problem: Merge overlapping intervals
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    
    Visualization:
    Timeline: 0--1--2--3--6--8--10--15--18
    Original:    [====]              (1-3)
                   [========]        (2-6)
                            [==]     (8-10)
                                 [==](15-18)
    
    After merge:
                 [=========]         (1-6)  MERGED!
                            [==]     (8-10)
                                 [==](15-18)
    
    Step-by-step:
    
    Step 1: Sort by start (already sorted)
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    
    Step 2: Initialize with first interval
    merged = [[1,3]]
    
    Step 3: Process remaining intervals
    
    i=1: Process [2,6]
      - current.start = 2
      - last_merged.end = 3
      - 2 <= 3? YES → OVERLAP!
      - Merge: extend end to max(3, 6) = 6
      - merged = [[1,6]]
      
      Interpretation: [1,3] and [2,6] overlap, become [1,6]
    
    i=2: Process [8,10]
      - current.start = 8
      - last_merged.end = 6
      - 8 <= 6? NO → No overlap
      - Add new: merged = [[1,6], [8,10]]
      
      Interpretation: Gap between 6 and 8, separate interval
    
    i=3: Process [15,18]
      - current.start = 15
      - last_merged.end = 10
      - 15 <= 10? NO → No overlap
      - Add new: merged = [[1,6], [8,10], [15,18]]
      
      Interpretation: Gap between 10 and 15, separate interval
    
    Final Answer: [[1,6], [8,10], [15,18]] ✓
    
    
    📝 DETAILED DRY RUN - INSERT INTERVAL:
    ═══════════════════════════════════════════════════════════════════════
    
    Problem: Insert newInterval into sorted intervals
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
    
    Visualization:
    Timeline: 0--1--2--3--5--6--9
    Original:    [====]         (1-3)
                           [==] (6-9)
    New:           [====]       (2-5)
    
    After insert:
                 [========]     (1-5)  MERGED!
                           [==] (6-9)
    
    THREE PHASES:
    
    Phase 1: Add all intervals that END before newInterval STARTS
    Phase 2: Merge all overlapping intervals
    Phase 3: Add all intervals that START after newInterval ENDS
    
    Step-by-step:
    
    intervals = [[1,3], [6,9]]
    newInterval = [2,5]
    result = []
    
    i = 0
    
    Phase 1: Non-overlapping intervals BEFORE newInterval
    ────────────────────────────────────────────────────────
    
    Check [1,3]:
      - Does [1,3] end before [2,5] starts?
      - 3 < 2? NO
      - So [1,3] may overlap, move to Phase 2
    
    Phase 2: Merge overlapping intervals
    ────────────────────────────────────────────────────────
    
    Check [1,3]:
      - Does [1,3] overlap with [2,5]?
      - Is 1 <= 5? YES
      - Merge: newInterval = [min(1,2), max(3,5)] = [1,5]
      - i = 1
    
    Check [6,9]:
      - Does [6,9] overlap with [1,5]?
      - Is 6 <= 5? NO
      - Stop merging, move to Phase 3
    
    Add merged interval: result = [[1,5]]
    
    Phase 3: Non-overlapping intervals AFTER newInterval
    ────────────────────────────────────────────────────────
    
    Add remaining: result = [[1,5], [6,9]]
    
    Final Answer: [[1,5], [6,9]] ✓
    
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 56: Merge Intervals (medium) ⭐⭐⭐
    - LeetCode 57: Insert Interval (medium) ⭐⭐⭐
    - LeetCode 986: Interval List Intersections (medium) ⭐⭐⭐
    - LeetCode 759: Employee Free Time (hard) ⭐⭐
    """
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        LeetCode 56: Merge Intervals
        
        FUNDAMENTAL INTERVAL PROBLEM!
        
        Master this template - it appears EVERYWHERE!
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort()
        
        # Initialize with first interval
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # If current overlaps with last merged
            if intervals[i][0] <= merged[-1][1]:
                # Merge by extending end
                # Use max because intervals might be: [1,5], [2,3]
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # No overlap, add as new interval
                merged.append(intervals[i])
        
        return merged
    
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        LeetCode 57: Insert Interval
        
        Insert into sorted intervals and merge.
        
        🔑 THREE PHASES APPROACH:
        
        Phase 1: Add intervals that end BEFORE newInterval starts
        Phase 2: Merge all overlapping intervals  
        Phase 3: Add intervals that start AFTER newInterval ends
        """
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Phase 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            # Merge: extend newInterval to cover current interval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged interval
        result.append(newInterval)
        
        # Phase 3: Add all intervals after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
    
    
    def intervalIntersection(self, firstList: List[List[int]], 
                            secondList: List[List[int]]) -> List[List[int]]:
        """
        LeetCode 986: Interval List Intersections
        
        Find intersection of two sorted interval lists.
        
        Input: firstList = [[0,2],[5,10],[13,23],[24,25]]
               secondList = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        
        🔑 TWO POINTERS:
        
        For each pair of intervals:
        - Intersection exists if: max(start1, start2) <= min(end1, end2)
        - Intersection = [max(start1, start2), min(end1, end2)]
        - Move pointer of interval that ends first
        
        📝 DRY RUN:
        
        firstList =  [[0,2], [5,10], [13,23], [24,25]]
        secondList = [[1,5], [8,12], [15,24], [25,26]]
        
        i=0, j=0: [0,2] vs [1,5]
          Intersection: [max(0,1), min(2,5)] = [1,2] ✓
          [0,2] ends first, i++
        
        i=1, j=0: [5,10] vs [1,5]
          Intersection: [max(5,1), min(10,5)] = [5,5] ✓
          [1,5] ends first, j++
        
        i=1, j=1: [5,10] vs [8,12]
          Intersection: [max(5,8), min(10,12)] = [8,10] ✓
          [5,10] ends first, i++
        
        Continue...
        """
        result = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            # Find intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            # If valid intersection
            if start <= end:
                result.append([start, end])
            
            # Move pointer of interval that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return result
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 4: ACTIVITY SELECTION (Greedy)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 PROBLEM TYPE: Select maximum non-overlapping intervals
    
    🔑 KEY INSIGHT:
    GREEDY: Always pick interval that ENDS earliest!
    
    Why? By finishing early, we leave most room for future intervals.
    This is PROVABLY optimal!
    
    ⏱️  Time: O(n log n) | Space: O(1)
    
    🎓 GENERIC TEMPLATE:
    
    def max_non_overlapping(intervals):
        # CRITICAL: Sort by END time!
        intervals.sort(key=lambda x: x[1])
        
        count = 1  # First interval always selected
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If no overlap with previous
            if intervals[i][0] >= prev_end:
                count += 1
                prev_end = intervals[i][1]
        
        return count
    
    
    📝 DETAILED DRY RUN:
    ═══════════════════════════════════════════════════════════════════════
    
    Problem: Remove minimum intervals to make rest non-overlapping
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1 (remove [1,3])
    
    Visualization:
    Timeline: 0--1--2--3--4
    Original: [==]           (1-2)
                 [==]        (2-3)
                    [==]     (3-4)
              [=====]        (1-3) ← REMOVE THIS!
    
    After sort by END time:
    intervals = [[1,2], [2,3], [1,3], [3,4]]
                  end=2  end=3  end=3  end=4
    
    Activity Selection (select maximum non-overlapping):
    
    Select [1,2] (ends earliest)
      prev_end = 2
      count = 1
    
    Check [2,3]:
      start = 2 >= prev_end = 2? YES → Select!
      prev_end = 3
      count = 2
    
    Check [1,3]:
      start = 1 >= prev_end = 3? NO → Skip!
      count = 2
    
    Check [3,4]:
      start = 3 >= prev_end = 3? YES → Select!
      prev_end = 4
      count = 3
    
    Selected: 3 intervals ([1,2], [2,3], [3,4])
    Total: 4 intervals
    Remove: 4 - 3 = 1 ✓
    
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 435: Non-overlapping Intervals (medium) ⭐⭐⭐
    - LeetCode 452: Minimum Number of Arrows (medium) ⭐⭐⭐
    - LeetCode 646: Maximum Length of Pair Chain (medium) ⭐⭐
    - LeetCode 1353: Maximum Events (medium) ⭐⭐
    """
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        LeetCode 435: Non-overlapping Intervals
        
        Remove minimum intervals to make rest non-overlapping.
        
        🔑 INSIGHT: This is activity selection!
        - Find max non-overlapping intervals
        - Remove = total - max
        """
        if not intervals:
            return 0
        
        # Sort by END time (CRITICAL!)
        intervals.sort(key=lambda x: x[1])
        
        count = 1  # First interval always selected
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If no overlap with previous selected
            if intervals[i][0] >= prev_end:
                count += 1
                prev_end = intervals[i][1]
        
        # Total - selected = removed
        return len(intervals) - count
    
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        LeetCode 452: Minimum Number of Arrows to Burst Balloons
        
        Each balloon covers [start, end].
        Arrow at x bursts all balloons where start <= x <= end.
        Find minimum arrows needed.
        
        Input: points = [[10,16],[2,8],[1,6],[7,12]]
        Output: 2
        
        🔑 INSIGHT: This is interval grouping!
        
        Sort by end, shoot arrow at end of first balloon.
        This bursts maximum balloons!
        
        📝 DRY RUN:
        
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
        """
        if not points:
            return 0
        
        # Sort by end position
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]  # Shoot at end of first balloon
        
        for i in range(1, len(points)):
            # If balloon starts after arrow position
            if points[i][0] > arrow_pos:
                # Need new arrow
                arrows += 1
                arrow_pos = points[i][1]
        
        return arrows



    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 5: EVENT-BASED PROCESSING (Sweep Line Advanced)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 PROBLEM TYPE: Calendar problems, event processing
    
    🔑 KEY INSIGHT:
    Track intervals dynamically, check overlaps on insertion
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 729: My Calendar I (medium) ⭐⭐
    - LeetCode 731: My Calendar II (medium) ⭐⭐
    - LeetCode 732: My Calendar III (hard) ⭐⭐
    """
    
    def book_MyCalendar(self, calendar: List[List[int]], start: int, end: int) -> bool:
        """
        LeetCode 729: My Calendar I
        
        Book event [start, end) if no overlap with existing events.
        
        🔑 APPROACH: Check each existing interval for overlap
        
        Overlap condition: start1 < end2 AND start2 < end1
        """
        for s, e in calendar:
            # Check if overlaps
            if start < e and s < end:
                return False
        
        # No overlap, add to calendar
        calendar.append([start, end])
        return True
    
    
    # ═══════════════════════════════════════════════════════════════════════
    # PATTERN 6: INTERVAL ALGEBRA (Gaps & Intersections)
    # ═══════════════════════════════════════════════════════════════════════
    """
    🎯 PROBLEM TYPE: Find gaps, intersections, free time
    
    🔑 KEY INSIGHT:
    - Gaps: Areas NOT covered by any interval
    - Intersections: Areas covered by ALL intervals
    
    💡 LEETCODE PROBLEMS:
    - LeetCode 759: Employee Free Time (hard) ⭐⭐⭐
    - LeetCode 1272: Remove Interval (medium) ⭐⭐
    """
    
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        """
        LeetCode 759: Employee Free Time
        
        Find common free time across all employees.
        
        Input: schedule = [[[1,3],[4,6]], [[2,4]], [[2,5],[9,12]]]
        Output: [[6,9]]
        
        🔑 APPROACH:
        1. Flatten all intervals
        2. Merge intervals
        3. Gaps between merged = free time
        
        📝 DRY RUN:
        
        All intervals: [1,3], [4,6], [2,4], [2,5], [9,12]
        Sort: [1,3], [2,4], [2,5], [4,6], [9,12]
        
        Merge:
        [1,3] + [2,4] + [2,5] = [1,5]
        [1,5] + [4,6] = [1,6]
        [9,12] stays separate
        
        Merged: [1,6], [9,12]
        
        Gaps: between 6 and 9 → [[6,9]] ✓
        """
        # Flatten all intervals
        intervals = []
        for emp_schedule in schedule:
            intervals.extend(emp_schedule)
        
        # Sort and merge
        intervals.sort()
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        # Find gaps
        free_time = []
        for i in range(1, len(merged)):
            free_time.append([merged[i-1][1], merged[i][0]])
        
        return free_time


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 TOP 30 INTERVAL PROBLEMS - RANKED BY IMPORTANCE
# ═══════════════════════════════════════════════════════════════════════════
"""
🔥🔥🔥 TIER 1: ABSOLUTE MUST-KNOW (Top 10)
═══════════════════════════════════════════════════════════════════════════

1. ⭐⭐⭐ LC 253: Meeting Rooms II
   - Pattern: Maximum Overlapping
   - Approaches: Heap, Two Arrays, Sweep Line
   - Why: #1 MOST ASKED INTERVAL PROBLEM!
   - Companies: Google (35%), Amazon (25%), Meta (30%)
   - Difficulty: 10/10 importance

2. ⭐⭐⭐ LC 56: Merge Intervals  
   - Pattern: Merge
   - Why: Foundation for many other problems
   - Companies: ALL FAANG
   - Difficulty: 10/10 importance

3. ⭐⭐⭐ LC 57: Insert Interval
   - Pattern: Insert & Merge
   - Why: Extension of merge, very common
   - Companies: Google, Amazon, Meta
   - Difficulty: 9/10 importance

4. ⭐⭐⭐ LC 435: Non-overlapping Intervals
   - Pattern: Activity Selection (Greedy)
   - Why: Classic greedy, tests understanding
   - Companies: Google, Meta, Microsoft
   - Difficulty: 9/10 importance

5. ⭐⭐⭐ LC 252: Meeting Rooms
   - Pattern: Overlap Detection
   - Why: Warmup for Meeting Rooms II
   - Companies: Amazon, Microsoft
   - Difficulty: 8/10 importance

6. ⭐⭐⭐ LC 452: Minimum Arrows to Burst Balloons
   - Pattern: Activity Selection
   - Why: Variant of non-overlapping
   - Companies: Amazon, Microsoft
   - Difficulty: 8/10 importance

7. ⭐⭐⭐ LC 986: Interval List Intersections
   - Pattern: Two Pointers
   - Why: Tests interval algebra
   - Companies: Google, Meta
   - Difficulty: 8/10 importance

8. ⭐⭐⭐ LC 1094: Car Pooling
   - Pattern: Maximum Overlapping with Capacity
   - Why: Real-world application
   - Companies: Uber, Lyft, Amazon
   - Difficulty: 8/10 importance

9. ⭐⭐⭐ LC 759: Employee Free Time
   - Pattern: Gaps between Intervals
   - Why: Tests merge + gap finding
   - Companies: Google, Meta
   - Difficulty: 7/10 importance

10. ⭐⭐⭐ LC 646: Maximum Length of Pair Chain
    - Pattern: Activity Selection
    - Why: Another activity selection variant
    - Companies: Google, Amazon
    - Difficulty: 7/10 importance


🔥🔥 TIER 2: VERY IMPORTANT (Next 10)
═══════════════════════════════════════════════════════════════════════════

11. ⭐⭐ LC 729: My Calendar I
12. ⭐⭐ LC 731: My Calendar II
13. ⭐⭐ LC 732: My Calendar III
14. ⭐⭐ LC 1353: Maximum Number of Events That Can Be Attended
15. ⭐⭐ LC 1229: Meeting Scheduler
16. ⭐⭐ LC 1288: Remove Covered Intervals
17. ⭐⭐ LC 1272: Remove Interval
18. ⭐⭐ LC 495: Teemo Attacking
19. ⭐⭐ LC 2848: Points That Intersect With Cars
20. ⭐⭐ LC 1893: Check if All Integers in Range Are Covered


🔥 TIER 3: GOOD TO KNOW (Final 10)
═══════════════════════════════════════════════════════════════════════════

21. ⭐ LC 228: Summary Ranges
22. ⭐ LC 163: Missing Ranges
23. ⭐ LC 352: Data Stream as Disjoint Intervals
24. ⭐ LC 715: Range Module
25. ⭐ LC 2276: Count Integers in Intervals
26. ⭐ LC 218: The Skyline Problem (very hard)
27. ⭐ LC 850: Rectangle Area II (very hard)
28. ⭐ LC 1851: Minimum Interval to Include Each Query
29. ⭐ LC 2406: Divide Intervals Into Minimum Groups
30. ⭐ LC 2054: Two Best Non-Overlapping Events


═══════════════════════════════════════════════════════════════════════════
📚 THE 5 UNIVERSAL INTERVAL TEMPLATES
═══════════════════════════════════════════════════════════════════════════

TEMPLATE 1: OVERLAP DETECTION (Meeting Rooms I)
──────────────────────────────────────────────────────────────────────────
"""
def has_overlap(intervals: List[List[int]]) -> bool:
    """
    Check if ANY two intervals overlap.
    
    Time: O(n log n) | Space: O(1)
    
    Use for:
    - LC 252: Meeting Rooms
    - LC 1229: Meeting Scheduler
    - Any "can attend all" problem
    """
    if not intervals:
        return False
    
    # Sort by start time
    intervals.sort()
    
    # Check each adjacent pair
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return True  # Overlap found
    
    return False  # No overlaps

"""
TEMPLATE 2: MAXIMUM OVERLAPPING (Meeting Rooms II)
──────────────────────────────────────────────────────────────────────────
"""
def max_overlapping_heap(intervals: List[List[int]]) -> int:
    """
    Find MAXIMUM simultaneous intervals.
    
    Time: O(n log n) | Space: O(n)
    
    Use for:
    - LC 253: Meeting Rooms II (MOST IMPORTANT!)
    - LC 1094: Car Pooling
    - Any "minimum resources needed" problem
    """
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort()
    
    # Min-heap for end times
    heap = []
    
    for start, end in intervals:
        # Remove ended intervals
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current interval
        heapq.heappush(heap, end)
    
    # Heap size = max simultaneous
    return len(heap)


def max_overlapping_sweep(intervals: List[List[int]]) -> int:
    """
    Same problem, different approach (often more intuitive!)
    
    Time: O(n log n) | Space: O(n)
    """
    if not intervals:
        return 0
    
    # Separate and sort start/end times
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    rooms = max_rooms = 0
    i = j = 0
    
    while i < len(starts):
        if starts[i] < ends[j]:
            # Meeting starts
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            # Meeting ends
            rooms -= 1
            j += 1
    
    return max_rooms

"""
TEMPLATE 3: MERGE INTERVALS
──────────────────────────────────────────────────────────────────────────
"""
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.
    
    Time: O(n log n) | Space: O(n)
    
    Use for:
    - LC 56: Merge Intervals
    - LC 759: Employee Free Time (merge first)
    - Any "consolidate overlaps" problem
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort()
    
    # Initialize with first interval
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        # If overlaps with last merged interval
        if intervals[i][0] <= merged[-1][1]:
            # Merge by extending end
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            # No overlap, add new
            merged.append(intervals[i])
    
    return merged

"""
TEMPLATE 4: INSERT INTERVAL
──────────────────────────────────────────────────────────────────────────
"""
def insert_interval(intervals: List[List[int]], 
                    newInterval: List[int]) -> List[List[int]]:
    """
    Insert into sorted intervals and merge.
    
    Time: O(n) | Space: O(n)
    
    THREE PHASES:
    1. Add intervals ending BEFORE newInterval
    2. Merge overlapping intervals
    3. Add intervals starting AFTER newInterval
    
    Use for:
    - LC 57: Insert Interval
    - Any "add and merge" problem
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Phase 1: Before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Phase 2: Merge overlapping
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    result.append(newInterval)
    
    # Phase 3: After newInterval
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

"""
TEMPLATE 5: ACTIVITY SELECTION (Non-overlapping)
──────────────────────────────────────────────────────────────────────────
"""
def max_non_overlapping(intervals: List[List[int]]) -> int:
    """
    Select MAXIMUM non-overlapping intervals.
    
    Time: O(n log n) | Space: O(1)
    
    CRITICAL: Sort by END time! (not start)
    
    Use for:
    - LC 435: Non-overlapping Intervals
    - LC 452: Minimum Arrows
    - LC 646: Maximum Pair Chain
    - Any "activity selection" problem
    """
    if not intervals:
        return 0
    
    # CRITICAL: Sort by END time!
    intervals.sort(key=lambda x: x[1])
    
    count = 1
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        # If no overlap
        if intervals[i][0] >= prev_end:
            count += 1
            prev_end = intervals[i][1]
    
    return count


"""
═══════════════════════════════════════════════════════════════════════════
🎯 4-WEEK MASTERY PLAN
═══════════════════════════════════════════════════════════════════════════

WEEK 1 - FOUNDATIONS:
────────────────────────────────────────────────────────────────────────

Day 1: Theory + LC 252 (Meeting Rooms)
  □ Understand overlap condition
  □ Master Template 1
  □ Practice dry runs

Day 2: LC 56 (Merge Intervals) ⚠️ CRITICAL!
  □ Master Template 3
  □ Understand merge logic
  □ Handle edge cases

Day 3: LC 57 (Insert Interval) ⚠️ CRITICAL!
  □ Master Template 4
  □ Three phases approach
  □ Practice both approaches

Day 4: Review Week 1
  □ Redo all 3 problems
  □ Time yourself
  □ Explain out loud

Day 5-7: Practice variations
  □ LC 228: Summary Ranges
  □ LC 495: Teemo Attacking
  □ LC 2848: Points Intersect


WEEK 2 - MEETING ROOMS (MOST IMPORTANT WEEK!)
────────────────────────────────────────────────────────────────────────

Day 1-2: LC 253 (Meeting Rooms II) ⚠️⚠️⚠️
  □ SPEND 2 FULL DAYS HERE!
  □ Master ALL three approaches:
    - Heap approach
    - Two arrays approach
    - Sweep line approach
  □ Practice explaining each
  □ This is THE most asked problem!

Day 3: LC 1094 (Car Pooling)
  □ Apply Meeting Rooms II with capacity
  □ Understand the variant

Day 4: LC 2406 (Divide Intervals Into Groups)
  □ Another Meeting Rooms II variant
  □ Solidify the pattern

Day 5: Review all Meeting Rooms
  □ Can you solve LC 253 in 15 minutes?
  □ Know all three approaches?
  □ Explain why each works?

Day 6-7: Calendar problems
  □ LC 729: My Calendar I
  □ LC 731: My Calendar II
  □ LC 732: My Calendar III


WEEK 3 - ACTIVITY SELECTION & GREEDY:
────────────────────────────────────────────────────────────────────────

Day 1: LC 435 (Non-overlapping) ⚠️⚠️
  □ Master Template 5
  □ Understand why sort by END
  □ Practice proof

Day 2: LC 452 (Minimum Arrows) ⚠️⚠️
  □ Apply activity selection
  □ Explain greedy choice

Day 3: LC 646 (Pair Chain)
  □ Another activity selection
  □ Solidify pattern

Day 4: LC 1353 (Maximum Events)
  □ Advanced activity selection
  □ Use heap + greedy

Day 5-7: Advanced problems
  □ LC 986: Interval Intersections
  □ LC 759: Employee Free Time
  □ LC 1288: Remove Covered


WEEK 4 - REVIEW & COMPANY-SPECIFIC:
────────────────────────────────────────────────────────────────────────

Day 1: Review TOP 10 (Tier 1)
  □ Solve all without hints
  □ Time yourself
  □ Aim for <20 min each

Day 2: Google Focus
  □ LC 253, 56, 57, 435, 986, 759
  □ Practice explaining

Day 3: Amazon Focus
  □ LC 252, 253, 56, 452, 1094
  □ Speed practice

Day 4: Meta Focus
  □ LC 253, 56, 986, 759, 435
  □ Mock interview

Day 5: Microsoft Focus
  □ LC 252, 253, 56, 435, 452
  □ Template review

Day 6: Mock Interview Day
  □ Pick 3 random from Tier 1
  □ 45 minutes total
  □ Explain out loud

Day 7: Rest & Template Memorization
  □ Review all 5 templates
  □ Quick practice run


═══════════════════════════════════════════════════════════════════════════
🔑 PATTERN RECOGNITION CHEAT SHEET
═══════════════════════════════════════════════════════════════════════════

QUESTION KEYWORDS → PATTERN → TEMPLATE
──────────────────────────────────────────────────────────────────────────

"Can attend all meetings?"
  → Pattern 1: Overlap Detection
  → Template 1 (sort by start, check adjacent)
  → O(n log n)

"Minimum rooms/platforms/resources needed?"
  → Pattern 2: Maximum Overlapping
  → Template 2 (heap OR two arrays)
  → O(n log n)

"Merge overlapping intervals"
  → Pattern 3: Merge
  → Template 3 (sort, extend end)
  → O(n log n)

"Insert interval into sorted list"
  → Pattern 3: Insert & Merge
  → Template 4 (three phases)
  → O(n)

"Remove minimum intervals" / "Maximum non-overlapping"
  → Pattern 4: Activity Selection
  → Template 5 (sort by END!)
  → O(n log n)

"Find intersections" / "Common free time"
  → Pattern 6: Interval Algebra
  → Merge first, then find gaps
  → O(n log n)

"Book/schedule with capacity"
  → Pattern 2: Overlapping with Limit
  → Sweep line with capacity check
  → O(n log n)


SORT DECISION:
──────────────────────────────────────────────────────────────────────────

Sort by START when:
✅ Checking overlap
✅ Merging intervals
✅ Inserting intervals
✅ Finding intersections
→ 90% of problems!

Sort by END when:
✅ Activity selection
✅ Maximum non-overlapping
✅ Minimum to remove
→ Only greedy problems!


═══════════════════════════════════════════════════════════════════════════
🏢 COMPANY-SPECIFIC BREAKDOWN
═══════════════════════════════════════════════════════════════════════════

GOOGLE (35% of interviews have intervals!)
────────────────────────────────────────────────────────────────────────
Must Master:
  1. LC 253: Meeting Rooms II (appears in 1/3 of interviews!)
  2. LC 56: Merge Intervals
  3. LC 57: Insert Interval
  4. LC 435: Non-overlapping Intervals
  5. LC 986: Interval Intersections
  6. LC 759: Employee Free Time

Focus: All patterns, emphasize heap approach for LC 253


AMAZON (25% of interviews)
────────────────────────────────────────────────────────────────────────
Must Master:
  1. LC 252: Meeting Rooms
  2. LC 253: Meeting Rooms II
  3. LC 56: Merge Intervals
  4. LC 452: Minimum Arrows
  5. LC 1094: Car Pooling

Focus: Practical problems, two-array approach for LC 253


META/FACEBOOK (30% of interviews)
────────────────────────────────────────────────────────────────────────
Must Master:
  1. LC 253: Meeting Rooms II
  2. LC 56: Merge Intervals
  3. LC 986: Interval Intersections
  4. LC 759: Employee Free Time
  5. LC 435: Non-overlapping

Focus: Interval algebra, intersection problems


MICROSOFT (20% of interviews)
────────────────────────────────────────────────────────────────────────
Must Master:
  1. LC 252: Meeting Rooms
  2. LC 253: Meeting Rooms II
  3. LC 56: Merge Intervals
  4. LC 435: Non-overlapping
  5. LC 452: Minimum Arrows

Focus: Fundamentals, clear explanations


BLOOMBERG (40% of interviews!)
────────────────────────────────────────────────────────────────────────
Must Master:
  ALL TOP 10 problems!
  Bloomberg LOVES interval problems!

Special focus:
  - Calendar problems (LC 729, 731, 732)
  - Advanced variants
  - Multiple approaches


═══════════════════════════════════════════════════════════════════════════
🚨 COMMON MISTAKES & HOW TO AVOID THEM
═══════════════════════════════════════════════════════════════════════════

MISTAKE 1: Wrong Sort Key
❌ Sorting by start for activity selection
✅ ALWAYS sort by END for activity selection!

MISTAKE 2: Wrong Overlap Condition
❌ if start1 <= start2 and end1 >= end2:  # WRONG!
✅ if start1 < end2 and start2 < end1:    # CORRECT!

MISTAKE 3: Not Using Heap for Meeting Rooms II
❌ Trying complex logic without heap
✅ Use min-heap to track end times

MISTAKE 4: Forgetting Edge Cases
❌ Not checking empty arrays
❌ Not handling single interval
❌ Not considering equal endpoints
✅ Always test: [], [[1,2]], [[1,2],[2,3]]

MISTAKE 5: Modifying Input
❌ Sorting intervals in-place might cause issues
✅ Consider if you need to preserve original

MISTAKE 6: Off-by-One in Overlap
❌ Treating [1,2] and [2,3] as overlapping
✅ Remember: intervals are often [start, end)
   Check problem statement!

MISTAKE 7: Using Wrong Data Structure
❌ Using array when heap is needed (LC 253)
❌ Using heap when array suffices (LC 252)
✅ Match data structure to problem pattern


═══════════════════════════════════════════════════════════════════════════
✅ YOU'RE INTERVIEW-READY WHEN:
═══════════════════════════════════════════════════════════════════════════

□ Can solve LC 253 in under 15 minutes
□ Can explain ALL three approaches for LC 253
□ Know when to sort by START vs END
□ Can recognize pattern from problem description in <1 minute
□ Have all 5 templates memorized
□ Can handle edge cases without hints
□ Understand why greedy works for activity selection
□ Can explain overlap condition clearly
□ Completed all Tier 1 problems (TOP 10)
□ Can solve any Tier 2 problem with template


═══════════════════════════════════════════════════════════════════════════
💡 FINAL TIPS FOR INTERVIEW SUCCESS
═══════════════════════════════════════════════════════════════════════════

1. THE GOLDEN RULE:
   "When in doubt, sort by START and use merge template!"
   This solves 70% of interval problems.

2. MEETING ROOMS II IS KING:
   If you only learn ONE interval problem thoroughly,
   make it LC 253 (Meeting Rooms II).
   Know heap, two-array, and sweep line approaches.

3. PROVE YOUR GREEDY:
   For activity selection, ALWAYS explain why sorting by
   END time is optimal. Interviewers love this proof!

4. DRAW IT OUT:
   Always visualize intervals on a timeline.
   This catches bugs and clarifies logic.

5. MASTER THE OVERLAP FORMULA:
   start1 < end2 AND start2 < end1
   Write this down at start of every interval problem!

6. TEMPLATE FIRST, OPTIMIZE LATER:
   Start with working solution using templates.
   Then optimize if needed. Don't over-engineer!

7. PRACTICE EXPLAINING:
   Can you explain your approach in 30 seconds?
   Practice this - it's what interviewers want to hear!

8. TIME MANAGEMENT:
   - Easy interval: 10-15 min
   - Medium interval: 15-20 min  
   - Hard interval (LC 253): 20-25 min

9. COMPANY PREPARATION:
   - Google: Master LC 253 with all approaches!
   - Amazon: Focus on practical problems
   - Meta: Emphasize interval algebra
   - Bloomberg: Practice advanced variants

10. THE ULTIMATE TEST:
    Can you solve these 5 back-to-back in under 90 min?
    - LC 252 (Meeting Rooms)
    - LC 253 (Meeting Rooms II)
    - LC 56 (Merge Intervals)
    - LC 57 (Insert Interval)
    - LC 435 (Non-overlapping)
    
    If YES → You're 100% ready! 🎉


═══════════════════════════════════════════════════════════════════════════
📊 QUICK REFERENCE CARD
═══════════════════════════════════════════════════════════════════════════

OVERLAP FORMULA:
start1 < end2 AND start2 < end1

MERGE CONDITION:
intervals[i][0] <= merged[-1][1]

ACTIVITY SELECTION:
Sort by END time, greedy select!

MEETING ROOMS II:
Heap size = max rooms needed

TEMPLATES:
1. Overlap → sort by start, check adjacent
2. Max overlap → heap or two arrays
3. Merge → sort, extend end
4. Insert → three phases
5. Activity → sort by END!


Good luck! Master these patterns and intervals become your superpower! 💪
"""


if __name__ == "__main__":
    # Test all interval patterns
    ip = IntervalPatterns()
    
    print("🧪 Testing Interval Patterns...\n")
    
    # Pattern 1: Overlap Detection
    assert ip.canAttendMeetings([[0,30],[5,10],[15,20]]) == False
    assert ip.canAttendMeetings([[1,4],[5,8],[9,12]]) == True
    print("✅ Pattern 1 (Overlap Detection): Passed")
    
    # Pattern 2: Maximum Overlapping
    assert ip.minMeetingRooms_heap([[0,30],[5,10],[15,20]]) == 2
    assert ip.minMeetingRooms_twoArrays([[0,30],[5,10],[15,20]]) == 2
    assert ip.minMeetingRooms_sweepLine([[0,30],[5,10],[15,20]]) == 2
    print("✅ Pattern 2 (Meeting Rooms II - All Approaches): Passed")
    
    # Pattern 3: Merge
    assert ip.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    print("✅ Pattern 3 (Merge Intervals): Passed")
    
    assert ip.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    print("✅ Pattern 3 (Insert Interval): Passed")
    
    # Pattern 4: Activity Selection
    assert ip.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert ip.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    print("✅ Pattern 4 (Activity Selection): Passed")
    
    # Pattern 6: Intersection
    result = ip.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], 
                                     [[1,5],[8,12],[15,24],[25,26]])
    assert result == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print("✅ Pattern 6 (Interval Intersections): Passed")
    
    print("\n🎉 All interval patterns tested successfully!")
    print("\n📚 PRIORITY LEARNING ORDER:")
    print("   Week 1: LC 252 → 56 → 57")
    print("   Week 2: LC 253 (ALL 3 APPROACHES!) ⚠️⚠️⚠️")
    print("   Week 3: LC 435 → 452 → 986")
    print("   Week 4: LC 759 + Review all")
    print("\n🎯 INTERVIEW READY: Master LC 253 completely!")
    print("   - This ONE problem appears in 30% of Google interviews!")
    print("   - Know heap, two-array, AND sweep line approaches")