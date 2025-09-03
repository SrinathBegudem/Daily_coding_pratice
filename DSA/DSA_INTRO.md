# Complete Data Structures Guide - From Basics to Advanced

## 🎯 The Learning Ladder

This guide follows a **progressive ladder approach** - each data structure solves specific pain points of the previous ones. Learn when to "upgrade" from one to another.

---

## 1️⃣ Static Array (Fixed-Size)

### What It Is
- **Contiguous memory block** with fixed length
- Elements stored side-by-side in memory
- Size determined at creation time

### Time Complexities
```
✅ Index Access:    O(1)    // arr[5] 
✅ Update:          O(1)    // arr[5] = 10
❌ Insert Middle:   O(n)    // Shift all elements
❌ Delete Middle:   O(n)    // Shift all elements  
❌ Append:          N/A     // Fixed size!
```

### Why Use Static Arrays
- **Smallest memory footprint** - no extra overhead
- **Best cache locality** - contiguous memory = fast access
- **Predictable performance** - no surprise allocations

### Pain Points
- **Cannot resize** - stuck with initial size
- **Expensive middle operations** - O(n) shifts required
- **Memory waste** if you don't use full capacity

### When to Use
- Fixed-size data (chess board, image pixels)
- Embedded systems with tight memory
- Performance-critical code with known bounds

---

## 2️⃣ Dynamic Array (Python `list`)

### What It Is
- **Resizable array** that grows automatically
- **Over-allocates memory** (grows by factor ~1.5-2x)
- Amortizes the cost of resizing

### Time Complexities
```
✅ Index Access:    O(1)    // arr[5]
✅ Update:          O(1)    // arr[5] = 10  
✅ Append:          O(1)*   // *amortized
✅ Pop End:         O(1)    // arr.pop()
❌ Insert Middle:   O(n)    // arr.insert(5, val)
❌ Delete Middle:   O(n)    // arr.pop(5)
❌ Pop Front:       O(n)    // arr.pop(0)
```

### Why Upgrade from Static Array
- **Need flexible size** with unknown final length
- **Want fast random access** by index
- **Frequent appends** to the end

### Pain Points
- **Middle operations still O(n)** - have to shift elements
- **Occasional resize costs** - copying entire array
- **Memory overhead** - over-allocation wastes space
- **Front operations expensive** - `arr.pop(0)` is O(n)

### Python Examples
```python
# ✅ Good uses
nums = [1, 2, 3]
nums.append(4)           # O(1) amortized
last = nums.pop()        # O(1)
nums[2] = 10            # O(1)

# ❌ Avoid these
nums.insert(0, 0)       # O(n) - shifts everything
nums.pop(0)             # O(n) - shifts everything
```

---

## 3️⃣ Linked List (Singly/Doubly)

### What It Is
- **Nodes with pointers** - not stored contiguously
- Each node contains data + pointer to next node
- Doubly linked has pointers in both directions

### Time Complexities
```
✅ Insert at Known Node:    O(1)    // If you have the node pointer
✅ Delete at Known Node:    O(1)    // If you have the node pointer  
✅ Head Operations:         O(1)    // Insert/delete at start
✅ Tail Operations:         O(1)    // If you maintain tail pointer
❌ Search by Value:         O(n)    // Must traverse
❌ Access by Index:         O(n)    // No random access
```

### Why Upgrade from Dynamic Array
- **Many insert/delete operations** not at the end
- **Don't need random access** by index
- **Want O(1) insertions** at known positions

### Pain Points
- **Poor cache locality** - nodes scattered in memory
- **Extra memory overhead** - storing pointers
- **Slow search** - must traverse sequentially
- **No random access** - can't jump to arr[100]

### When to Use
```python
# Good for:
# - Implementing stacks/queues
# - Undo functionality (each node = state)
# - Music playlists (easy insert/remove songs)
# - Browser history (back/forward navigation)
```

---

## 4️⃣ Stacks, Queues, Deques

Built on top of arrays or linked lists for specific access patterns.

### Stack (LIFO - Last In, First Out)
```python
# ✅ Python: Use list with append/pop at END
stack = []
stack.append(1)    # Push - O(1)
stack.append(2)    # Push - O(1)  
top = stack.pop()  # Pop - O(1), returns 2
```

### Queue (FIFO - First In, First Out) 
```python
# ✅ Python: Use collections.deque
from collections import deque
queue = deque()
queue.append(1)        # Enqueue - O(1)
queue.append(2)        # Enqueue - O(1)
first = queue.popleft() # Dequeue - O(1), returns 1

# ❌ Don't use list for queues
queue = []
queue.append(1)
first = queue.pop(0)   # O(n) - shifts entire array!
```

### Deque (Double-Ended Queue)
```python
# ✅ O(1) operations at BOTH ends
from collections import deque
dq = deque()
dq.append(1)        # Add to right - O(1)
dq.appendleft(0)    # Add to left - O(1)  
dq.pop()            # Remove from right - O(1)
dq.popleft()        # Remove from left - O(1)
```

**Key Rule:** Use `deque` over `list` for any front operations (`popleft`, `appendleft`).

---

## 5️⃣ Hash Table / Hash Set (Python `dict`/`set`)

### What It Is
- **Key → Bucket mapping** via hash function
- Average O(1) operations due to direct addressing
- Python 3.7+ `dict` maintains insertion order (but NOT sorted)

### Time Complexities
```
✅ Insert:          O(1) avg    // dict[key] = val
✅ Lookup:          O(1) avg    // val = dict[key]
✅ Delete:          O(1) avg    // del dict[key]
✅ Membership:      O(1) avg    // key in dict
❌ Worst Case:      O(n)        // Rare hash collisions
❌ Ordered Ops:     N/A         // No sorted iteration
```

### Why Upgrade from Arrays/Lists
- **Need fast membership testing** - "is X in the collection?"
- **Need fast lookup by key** - associate keys with values
- **Frequent insert/delete** with fast access

### Pain Points
- **No inherent order** - can't get "next largest" key
- **Memory overhead** - hash table structure + load factor
- **Rare worst-case O(n)** - when hash collisions cluster

### Python Examples
```python
# ✅ Hash Set - fast membership
seen = set()
seen.add(5)
if 5 in seen:       # O(1) avg
    print("Found!")

# ✅ Hash Map - key-value lookup  
counts = {}
counts["apple"] = 3
if "apple" in counts:   # O(1) avg
    print(counts["apple"])

# ✅ Frequency counting
from collections import Counter
freq = Counter([1,2,2,3])  # {1:1, 2:2, 3:1}
```

---

## 6️⃣ Binary Heap / Priority Queue (Python `heapq`)

### What It Is
- **Min-heap** implemented as array-backed binary tree
- Parent is always ≤ children (min-heap property)  
- NOT fully sorted - only root is guaranteed minimum

### Time Complexities
```
✅ Push:            O(log n)    // heappush(heap, item)
✅ Pop Min:         O(log n)    // heappop(heap)
✅ Peek Min:        O(1)        // heap[0]
❌ Arbitrary Delete: O(n)       // Find + delete specific item
❌ Search:          O(n)        // Must check all elements
```

### Why Upgrade from Hash Table
- **Always need smallest/largest item next** 
- **Priority-based processing** (Dijkstra's algorithm)
- **Top-K problems** (find K largest/smallest)

### Pain Points
- **No fast arbitrary delete/update** - must find item first
- **Not sorted iteration** - popping gives sorted order, but heap itself isn't
- **Only gives min/max** - can't efficiently get "2nd smallest"

### Python Examples
```python
import heapq

# ✅ Min-heap (default)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)  
heapq.heappush(heap, 2)
min_val = heapq.heappop(heap)  # Returns 1

# ✅ Max-heap trick - negate values
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
max_val = -heapq.heappop(max_heap)  # Returns 3

# ✅ For complex objects
tasks = [(1, "high"), (3, "low"), (2, "medium")]  # (priority, task)
heapq.heapify(tasks)
next_task = heapq.heappop(tasks)  # (1, "high")
```

---

## 7️⃣ Binary Search Tree (BST)

### What It Is
- **Binary tree** where left < parent < right
- **Unbalanced**: Can degrade to linked list O(n)
- **Balanced** (AVL, Red-Black): Self-balancing, guaranteed O(log n)

### Time Complexities
```
Unbalanced BST:
✅ Average Case:     O(log n)   // search/insert/delete
❌ Worst Case:       O(n)       // Skewed tree

Balanced BST:  
✅ All Operations:   O(log n)   // search/insert/delete
✅ Ordered Iteration: O(n)      // In-order traversal
✅ Range Queries:    O(log n + k) // k = results
```

### Why Upgrade from Heap
- **Need sorted order** with efficient search
- **Need predecessor/successor** operations
- **Need range queries** (find all values between X and Y)
- **Want ordered set/map** functionality

### Pain Points
- **More complex** than hash tables - rotations, balancing
- **Usually need libraries** - C++ `std::map`, Java `TreeMap`
- **Higher constant factors** than hash tables

### Python Note
```python
# Python doesn't have built-in balanced BST
# Alternatives:
# 1. sorted() + bisect for static sorted data
# 2. Use sortedcontainers library: SortedDict, SortedSet
# 3. Implement your own (interview scenarios)

import bisect
sorted_list = [1, 3, 5, 7, 9]
bisect.insort(sorted_list, 4)  # Maintains sorted order
index = bisect.bisect_left(sorted_list, 5)  # Binary search
```

---

## 8️⃣ Trie (Prefix Tree)

### What It Is
- **Tree structure over characters/strings**
- Each path from root represents a word/prefix
- Nodes can mark "end of word"

### Time Complexities
```
✅ Insert Word:         O(L)    // L = word length
✅ Search Word:         O(L)    // L = word length  
✅ Prefix Search:       O(L)    // Check if prefix exists
✅ All with Prefix:     O(L + k) // k = number of results
❌ Memory Usage:        High    // Many nodes
```

### Why Upgrade from Hash Set
- **Prefix-based queries** - autocomplete, spell check
- **Wildcard pattern matching** 
- **Dictionary operations** with prefix enumeration
- **Space efficiency** for large dictionaries with common prefixes

### Pain Points
- **Memory-heavy** - many nodes for large alphabets
- **Alphabet fan-out** - each node may have 26+ children
- **Not cache-friendly** - pointer chasing

### Python Implementation
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

---

## 9️⃣ Union-Find (Disjoint Set)

### What It Is
- **Track connected components** in a collection
- **Path compression** + **Union by rank** optimizations
- Near-constant amortized time complexity

### Time Complexities
```
✅ Find:            O(α(n))    // α = inverse Ackermann (≈ constant)
✅ Union:           O(α(n))    // Same amortized bound
✅ Connected:       O(α(n))    // Check if same component
```

### Why Use Union-Find
- **Connectivity queries** - "Are A and B connected?"
- **Dynamic connectivity** - connections change over time
- **Kruskal's MST algorithm**
- **Grouping/clustering** problems

### Pain Points
- **No inherent ordering** - can't iterate components easily
- **Not for general search** - only connectivity
- **Specialized use case** - limited to union/find operations

### Python Implementation
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

---

## 🔟 Fenwick Tree (BIT) / Segment Tree

### What It Is
- **Trees over array indices** for range aggregate queries
- **Fenwick Tree**: Prefix sums with point updates
- **Segment Tree**: General range queries with range updates

### Time Complexities
```
Fenwick Tree (Binary Indexed Tree):
✅ Point Update:     O(log n)    // Update single element
✅ Prefix Sum:       O(log n)    // Sum from 0 to i
✅ Range Sum:        O(log n)    // Sum from i to j

Segment Tree:
✅ Range Query:      O(log n)    // Min/Max/Sum in range
✅ Point Update:     O(log n)    // Update single element  
✅ Range Update:     O(log n)    // Update entire range
```

### Why Upgrade from Arrays
- **Frequent range queries** with updates
- **Array changes dynamically** - can't precompute
- **Multiple query types** - sum, min, max over ranges

### Pain Points
- **More complex code** than simple arrays
- **Higher memory usage** - tree structure overhead
- **Not for arbitrary searches** - specialized for range queries

### Python Fenwick Tree Example
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        i += 1  # 1-indexed internally
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Add lowest set bit
    
    def prefix_sum(self, i):
        i += 1  # 1-indexed internally  
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)  # Remove lowest set bit
        return result
    
    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
```

---

## 1️⃣1️⃣ Graph Representations

### Adjacency List
```python
# Most common representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],  
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Or with weights
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('D', 2)]
}
```

**Properties:**
- **Space**: O(n + m) where n = nodes, m = edges
- **Edge Check**: O(degree) - must search neighbors
- **Best for**: Sparse graphs, BFS/DFS traversal

### Adjacency Matrix
```python
# 2D array representation
n = 4  # Number of nodes
graph = [[0] * n for _ in range(n)]
graph[0][1] = 1  # Edge from node 0 to node 1
graph[1][0] = 1  # Undirected edge
```

**Properties:**
- **Space**: O(n²) - always full matrix
- **Edge Check**: O(1) - direct array access
- **Best for**: Dense graphs, frequent edge queries

---

## 🚀 When to Switch? (Decision Tree)

Follow this decision tree to choose the right data structure:

```
Need random index access + resizable?
├─ YES → Dynamic Array (list)
└─ NO → Continue...

Many front operations (pop(0), insert(0))?  
├─ YES → collections.deque
└─ NO → Continue...

Many middle insert/delete at known positions?
├─ YES → Linked List  
└─ NO → Continue...

Need fast membership/lookup by key?
├─ YES → dict/set (Hash Table)
└─ NO → Continue...

Always need min/max element next?
├─ YES → heapq (Priority Queue)
└─ NO → Continue...

Need sorted order + predecessor/successor?
├─ YES → Balanced BST (use sortedcontainers)
└─ NO → Continue...

Need prefix operations on strings?
├─ YES → Trie
└─ NO → Continue...

Need connectivity merges/queries?  
├─ YES → Union-Find
└─ NO → Continue...

Need range queries with updates?
├─ YES → Fenwick/Segment Tree
└─ NO → Continue...

Need graph algorithms?
├─ YES → Adjacency List (usually)
└─ NO → Back to basics!
```

---

## 📋 Quick Reference Table

| Data Structure | Access Index | Search Value | Insert End | Insert Mid | Delete Mid | Ordered? | Typical Use Case |
|----------------|-------------|--------------|------------|------------|------------|----------|------------------|
| **Static Array** | O(1) | O(n) | N/A | O(n) | O(n) | Index | Fixed-size, tight memory |
| **Dynamic Array** | O(1) | O(n) | O(1)* | O(n) | O(n) | Index | General-purpose |
| **Linked List** | O(n) | O(n) | O(1)** | O(1)** | O(1)** | Insertion | Many inserts/deletes |
| **Deque** | O(n) | O(n) | O(1) | — | — | Ends only | Queues, sliding window |
| **Hash Map/Set** | — | O(1) avg | O(1) | — | O(1) | Unordered*** | Membership, maps |
| **Heap** | — | O(n) | O(log n) | — | — | Heap | Min/Max next |
| **Balanced BST** | O(log n) | O(log n) | O(log n) | O(log n) | O(log n) | Sorted | Ordered sets/maps |
| **Trie** | — | O(L) | O(L) | — | — | Lexicographic | Prefix queries |
| **Fenwick/SegTree** | — | — | — | — | — | Index | Range queries + updates |

**Notes:**
- `*` = amortized
- `**` = if you have the node pointer  
- `***` = Python dict keeps insertion order but not sorted order

---

## 🎯 Python Interview Cheat Sheet

### Essential Data Structures
```python
# Dynamic Array
arr = [1, 2, 3]
arr.append(4)        # O(1) amortized
arr.pop()            # O(1) - from end only!

# Deque (for queues)
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)     # O(1)
dq.popleft()         # O(1)

# Hash Map/Set  
counts = {}
seen = set()
counts['key'] = 1    # O(1) avg
'key' in counts      # O(1) avg

# Priority Queue (Min-Heap)
import heapq
heap = [3, 1, 4, 2]
heapq.heapify(heap)  # O(n)
heapq.heappush(heap, 0)  # O(log n)
min_val = heapq.heappop(heap)  # O(log n)

# For max-heap, negate values
max_heap = [-3, -1, -4, -2]
heapq.heapify(max_heap)
max_val = -heapq.heappop(max_heap)
```

### Common Patterns
```python
# Two pointers (arrays/strings)
left, right = 0, len(arr) - 1
while left < right:
    # Process arr[left] and arr[right]
    left += 1
    right -= 1

# Sliding window (substring problems)  
window = {}
left = 0
for right in range(len(s)):
    window[s[right]] = window.get(s[right], 0) + 1
    while window_condition_violated:
        window[s[left]] -= 1
        left += 1

# Frequency counting
from collections import Counter
freq = Counter(arr)  # {element: count}

# Stack (monotonic patterns)
stack = []
for num in nums:
    while stack and stack[-1] > num:
        stack.pop()
    stack.append(num)
```

---

## 📚 Step-by-Step Learning Path

### Level 1: Foundation
1. **Arrays & Strings** 
   - Two pointers, sliding window
   - Array manipulation, string processing

2. **Stacks & Queues**
   - Monotonic stack/queue patterns
   - Expression parsing, matching brackets

### Level 2: Core Structures  
3. **Hash Tables**
   - Maps/sets, frequency counting
   - Deduplication, fast lookups

4. **Heaps** 
   - Top-K problems, priority queues
   - K-way merge, streaming data

### Level 3: Tree Structures
5. **Binary Trees**
   - Traversals (BFS, DFS)
   - Tree properties, recursion vs iteration

6. **Binary Search Trees**
   - BST validation, search operations
   - Balanced vs unbalanced

### Level 4: Specialized Structures
7. **Tries**
   - Prefix problems, autocomplete
   - Word search, dictionary operations  

8. **Union-Find**
   - Connected components
   - Graph connectivity problems

### Level 5: Advanced
9. **Fenwick/Segment Trees**
   - Range queries with updates
   - Competitive programming problems

10. **Graph Algorithms** 
    - BFS, DFS, topological sort
    - Shortest path, minimum spanning tree

---

## 🔥 Key Takeaways

1. **Start simple, upgrade when you feel the pain** - don't over-engineer
2. **Each structure solves specific pain points** of the previous ones  
3. **Python favorites**: `list`, `deque`, `dict`/`set`, `heapq`
4. **Time complexity matters** - but so does simplicity and readability
5. **Practice the upgrade decisions** - knowing when to switch is crucial

Remember: **The best data structure is the simplest one that meets your performance requirements!**