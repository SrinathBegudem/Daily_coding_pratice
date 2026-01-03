# Recursion, DP, and Backtracking – How to Think (Clean Notes)

## 0. How to think about recursion (this comes first)

Before DP or backtracking, recursion itself needs the right mindset.

When writing recursion, do **only these three things**:

1. **Define the function in English**  
   Example:  
   `solve(i, cap)` returns the best value using items from index `i` onward with capacity `cap`.

2. **Trust the function contract**  
   Assume recursive calls magically return the correct answer.  
   Do NOT try to simulate the full call stack in your head.

3. **Think in relationships, not execution**  
   You describe how a bigger problem depends on smaller ones.  
   The language runtime handles call order for you.

---

## 1. Core recursion template (mental model)

Every recursive solution follows this structure:

- **Base case**: when nothing can be done anymore  
- **Choices**: what options are available at this state  
- **Combine**: how results from choices are used  

You never control recursion with loops.  
You only define how states depend on smaller states.

---

## 2. When recursion becomes DP

DP always **starts as recursion**.

Recursion becomes DP when:
- the same subproblem appears again
- the function is called multiple times with the same arguments

At that point:

> recursion + storage (memoization) = DP

The logic stays the same.  
Only caching is added.

---

## 3. What DP really is

DP is **not** about tables first.

DP is about:
- defining a state
- returning an answer for that state
- combining answers from smaller states

Bottom-up tables are just an optimization of this idea.

---

## 4. About “number of choices”

DP does **not** mean exactly two choices.

Correct rule:
> DP has a small, fixed set of choices per state.

Examples:
- Knapsack → take / skip
- Grid DP → right / down
- Coin change → try each coin
- LIS → compare with previous indices

Two choices is common, but not required.

---

## 5. When it is backtracking

Backtracking is used when:
- all possibilities must be generated
- paths or combinations are built explicitly
- append / pop is used
- visited arrays are required
- order of elements matters

Backtracking explores **possibilities**.  
DP computes **results**.

---

## 6. How to identify recursion vs DP vs backtracking

Ask these questions:

- Does the function return a value, not a list?
  - Yes → recursion / DP
  - No → backtracking

- Do subproblems repeat?
  - Yes → DP
  - No → plain recursion

- Are paths or combinations being built?
  - Yes → backtracking

- Is the problem asking for min / max / best / count?
  - Yes → DP

---

## 7. One-line mental shortcut

**Backtracking:**  
"What are all the ways?"

**DP:**  
"What is the best answer?"

---

## 8. Final takeaway

- Always start with recursion
- Define the subproblem clearly
- Trust recursive calls
- If subproblems repeat, store results
- That recursion + storage is DP
- If paths are generated, it is backtracking
