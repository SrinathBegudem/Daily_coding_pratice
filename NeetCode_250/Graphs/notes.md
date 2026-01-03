# What “mastery” actually means

You’re ready when you can do all of these without thinking:

Build adjacency list fast (directed vs undirected)

BFS template with dist and parent (shortest path + path reconstruction)

DFS template with states (cycle detection in directed)

Grid BFS/DFS with bounds and visited

Topo sort both ways (Kahn + DFS postorder)

Dijkstra with heap + “skip outdated heap entries” pattern

Union Find with path compression + union by rank

If any of these still feels like “I need to look up the code,” it’s not mastered yet.

A clean graph practice path (in the right order)

Do these in this exact order and don’t move on until each feels easy.

Phase 1: BFS/DFS basics

733 Flood Fill

200 Number of Islands

695 Max Area of Island

994 Rotting Oranges (multi-source BFS)

Phase 2: shortest path (unweighted)

1091 Shortest Path in Binary Matrix

542 01 Matrix (multi-source BFS dist grid)

752 Open the Lock

Phase 3: topo + directed cycle

207 Course Schedule

210 Course Schedule II

Phase 4: bipartite + components + DSU

785 Is Graph Bipartite?

323 Number of Connected Components

684 Redundant Connection

Phase 5: weighted graphs

743 Network Delay Time (Dijkstra)

1631 Path With Minimum Effort (Dijkstra variant)

Phase 6: “Google-style harder BFS”

127 Word Ladder (BFS state space)

Add MST

1584 Min Cost to Connect All Points (Prim or Kruskal)

That’s a strong graph set for new grad.

The fastest way to improve in Python

Two habits make a huge difference:

Always define what a “node” is (vertex, cell, word, state). Many graph problems are disguised state graphs.

Always decide the algorithm from the requirement:

“minimum steps” and unweighted → BFS

“any path / explore” → DFS

“dependencies ordering” → topo

“weighted shortest” → Dijkstra

“min cost connect all” → MST

“dynamic connectivity” → Union Find

One Python-specific warning

Recursive DFS can hit recursion depth on big grids or deep graphs. Be comfortable switching to iterative DFS or BFS when constraints are large

----------------------
# graph grid problems vs normal graph problems 

Totally normal confusion, because a grid problem is literally a graph problem in disguise.

The clean way to remove the confusion is to stop thinking “matrix vs graph” and start thinking:

What are the nodes, and how do I get the neighbors?

That’s the only real difference.

1) Grid problems are “implicit graphs”

In a grid, the nodes are cells like (r, c).

The edges are not given to you. They are implied by geometry:

4-direction neighbors: up, down, left, right

sometimes 8-direction neighbors (also diagonals)

sometimes “knight moves” etc.

So your neighbor generation always looks like “try directions”.

Example: Number of Islands (LC 200)

Node: a land cell '1'

Neighbor: adjacent land cells (4-dir)

Task: count connected components

Example: Shortest Path in Binary Matrix (LC 1091)

Node: a cell

Neighbor: 8-dir moves

Task: shortest path, so BFS

So grid traversal code always has:

rows, cols

a directions list

bounds check

visited check

2) Graph problems are “explicit graphs”

In normal graph problems, nodes are usually:

integers 0..n-1 (courses, people, cities)

or objects (clone graph)

Edges are given to you explicitly:

edge list like [[u,v], ...]

prerequisites like [a, b] meaning b -> a

adjacency list already provided

So neighbor generation is:

for nei in graph[node]:

Example: Course Schedule (LC 207)

Node: course

Edge: prerequisite relation

Neighbor: “next courses” or “prereq courses” depending how you build it

Task: detect cycle in directed graph

Example: Is Graph Bipartite? (LC 785)

Node: vertex

Neighbors: adjacency list

Task: 2-coloring using BFS/DFS

So normal graph traversal code usually starts with:

build adjacency list from edges (if not given)

then BFS/DFS over nodes

3) Not every matrix problem is a graph problem

This is the big trap. Some matrix problems are not about connectivity or paths at all. They are about scanning, simulation, DP, or prefix sums.

Example: Spiral Matrix (LC 54)

You are not exploring neighbors by rules

You are following a fixed spiral order

Example: Rotate Image (LC 48) or Set Matrix Zeroes (LC 73)

Not about reachability, no BFS/DFS needed

So if you keep applying grid BFS/DFS to every matrix problem, you’ll overcomplicate.

4) Quick way to decide what it is

Ask these two questions:

Am I moving from one position/state to another through “allowed moves”?

Yes → it’s a graph traversal problem (grid is a graph here)

Do I need shortest steps, minimum moves, or reachability?

Yes → BFS/DFS/Dijkstra type thinking

If the problem is more like “compute something for every cell” or “transform the matrix”, it might not be graph traversal.

5) Concrete examples to lock this in
Grid-graph (use directions)

LC 200 Number of Islands (components)

LC 695 Max Area of Island (components + size)

LC 994 Rotting Oranges (multi-source BFS)

LC 1091 Shortest Path in Binary Matrix (BFS shortest path)

LC 542 01 Matrix (multi-source BFS distances)

LC 130 Surrounded Regions (boundary-connected components)

Normal graph (use adjacency list)

LC 207 Course Schedule (directed cycle)

LC 210 Course Schedule II (topo sort)

LC 785 Is Graph Bipartite? (2-coloring)

LC 323 Number of Connected Components (components)

LC 684 Redundant Connection (cycle in undirected, DSU)

LC 743 Network Delay Time (Dijkstra weighted graph)

Matrix but NOT traversal

LC 54 Spiral Matrix

LC 48 Rotate Image

LC 73 Set Matrix Zeroes

6) A simple mental model that works every time

Grid BFS/DFS = graph BFS/DFS where:

node = (r,c)

neighbors = generated by directions + bounds
Normal graph BFS/DFS:

node = integer/object

neighbors = already listed in adjacency list

Same algorithm, different neighbor source.

-----------
# dksta vs floyd marshall 
Single-source shortest paths (from one start node to all nodes)

BFS if all edges have the same weight (or unweighted).

Dijkstra if all edge weights are non-negative.

Bellman–Ford if weights can be negative (and you also want to detect negative cycles).

So Dijkstra is for “single source to all nodes” in weighted non-negative graphs, not just “single path”.

All-pairs shortest paths (between every pair of nodes)

Floyd–Warshall: classic all-pairs, simple, O(n^3) time, good when n is small (like a few hundred).

Another common way: run Dijkstra from every node (or BFS from every node if unweighted). This can be faster than Floyd when the graph is sparse.

Let:

V = number of nodes

E = number of edges

Floyd–Warshall

Time: O(V^3)

Space: O(V^2)

Doesn’t care about E (works on adjacency matrix naturally)

Simple, good when V is small (like 200–500 range) and/or graph is dense.

Repeated Dijkstra (run Dijkstra from every node)

Depends on priority queue / representation:

With adjacency list + binary heap:

One Dijkstra: O((E + V) log V) ~ O(E log V)

Repeated for all sources: O(V * E log V)

With adjacency matrix (classic Dijkstra without heap):

One Dijkstra: O(V^2)

Repeated: O(V^3) ✅ same as Floyd in big-O

So when are they “same”?

If you do Dijkstra in the O(V^2) matrix style, then repeated Dijkstra is O(V^3), same big-O as Floyd.

If you do heap-based Dijkstra (common), then repeated Dijkstra is O(V * E log V), which can be much faster than O(V^3) when the graph is sparse (E much smaller than V^2).

Practical intuition

Dense graph (E ~ V^2): repeated heap Dijkstra ≈ O(V^3 log V) (slower than Floyd), Floyd often wins.

Sparse graph (E ~ V): repeated heap Dijkstra ≈ O(V^2 log V) (often faster than Floyd).

If you tell me typical constraints (like V=2000 vs V=200 and whether E is near V or near V^2), I’ll tell you which one is the right pick.