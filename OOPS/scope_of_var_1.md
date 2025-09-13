# Python Variable Scope & Mutability Guide

## 🎯 The Core Problem

When writing nested functions (like DFS in tree problems), you'll encounter scope issues. Understanding **variable scope** and **mutability** is crucial for avoiding `UnboundLocalError` and writing clean code.

---

## 📚 Variable Scope Rules (LEGB)

Python follows the **LEGB** rule to resolve variable names:

1. **L**ocal - Inside the current function
2. **E**nclosing - In the parent function (nested functions)
3. **G**lobal - At the module level
4. **B**uilt-in - Python built-ins (print, len, etc.)

```python
x = "global"          # Global scope

def outer():
    x = "enclosing"   # Enclosing scope
    
    def inner():
        x = "local"   # Local scope
        print(x)      # Prints "local"
    
    inner()
    print(x)          # Prints "enclosing"

outer()
print(x)              # Prints "global"
```

---

## 🔧 The `self` Keyword

### What is `self`?
- **Instance reference** - refers to the current object
- **Not a keyword** - just a convention (could be named anything)
- **Automatically passed** as first parameter in instance methods

### Instance Variables vs Local Variables
```python
class Solution:
    def __init__(self):
        self.instance_var = 0  # Instance variable - accessible across methods
    
    def method1(self):
        local_var = 10         # Local variable - only in this method
        self.instance_var = 5  # Modify instance variable
    
    def method2(self):
        print(self.instance_var)  # ✅ Can access - instance variable
        # print(local_var)        # ❌ Error - local_var doesn't exist here
```

### Why Use `self` in Tree Problems?
```python
class Solution:
    def maxDepth(self, root):
        self.max_depth = 0  # ✅ Accessible in nested functions
        
        def dfs(node, depth):
            if not node:
                return
            self.max_depth = max(self.max_depth, depth)  # ✅ Works
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return self.max_depth
```

---

## 🔄 The `nonlocal` Keyword

### What is `nonlocal`?
- Allows **modification** of variables in the **enclosing scope**
- Creates a **binding** to the parent function's variable
- Only works with **enclosing scope** (not global)

### Example: Without `nonlocal` (Error)
```python
def outer():
    count = 0  # Enclosing scope variable
    
    def inner():
        count = count + 1  # ❌ UnboundLocalError!
        # Python thinks you're creating a NEW local variable
        # But you're trying to read it before assignment
    
    inner()

outer()  # Crashes!
```

### Example: With `nonlocal` (Fixed)
```python
def outer():
    count = 0  # Enclosing scope variable
    
    def inner():
        nonlocal count  # ✅ Tell Python to use enclosing scope
        count = count + 1  # ✅ Now works!
    
    inner()
    print(count)  # Prints 1

outer()
```

### Tree Problem with `nonlocal`
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        max_diameter = 0  # Local to diameterOfBinaryTree
        
        def dfs(node):
            nonlocal max_diameter  # ✅ Bind to enclosing scope
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            max_diameter = max(max_diameter, diameter)  # ✅ Can modify
            return 1 + max(left, right)
        
        dfs(root)
        return max_diameter
```

---

## 📦 Mutable vs Immutable Types

### Immutable Types (Cannot Change In-Place)
```python
# Numbers, strings, tuples, frozensets
x = 5        # int
y = "hello"  # string  
z = (1, 2)   # tuple

# These create NEW objects:
x = x + 1    # New int object
y = y + "!"  # New string object
```

### Mutable Types (Can Change In-Place)
```python
# Lists, dicts, sets, custom objects
arr = [1, 2, 3]      # list
d = {"a": 1}         # dict
s = {1, 2, 3}        # set

# These modify the SAME object:
arr.append(4)        # Same list object, just modified
d["b"] = 2           # Same dict object, just modified
```

---

## ⚡ Scope + Mutability Interactions

### The Key Rule
> **Reading** a variable works from any scope.
> **Modifying** a variable requires it to be in the correct scope.

### Case 1: Immutable Types (Numbers, Strings)

#### ❌ Problem: Trying to Modify Immutable in Nested Function
```python
def outer():
    count = 0  # Immutable int
    
    def inner():
        # count = count + 1  # ❌ UnboundLocalError!
        # Python sees assignment (=) and thinks you want a NEW local variable
        # But you're trying to read the old value first - ERROR!
        pass
    
    inner()
```

#### ✅ Solution 1: Use `nonlocal`
```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # ✅ Explicitly bind to enclosing scope
        count = count + 1  # ✅ Now works
    
    inner()
    print(count)  # Prints 1
```

#### ✅ Solution 2: Use `self` (in class methods)
```python
class Solution:
    def some_method(self):
        self.count = 0  # Instance variable
        
        def inner():
            self.count = self.count + 1  # ✅ Works - self is always accessible
        
        inner()
        print(self.count)  # Prints 1
```

### Case 2: Mutable Types (Lists, Dicts)

#### ✅ Mutable Types Work Without `nonlocal`
```python
def outer():
    result = []  # Mutable list
    count_dict = {"val": 0}  # Mutable dict
    
    def inner():
        # ✅ These work because we're NOT reassigning the variable
        result.append(1)        # Modifying same list object
        count_dict["val"] += 1  # Modifying same dict object
    
    inner()
    print(result)      # [1]
    print(count_dict)  # {"val": 1}
```

#### ❌ But Reassignment Still Needs `nonlocal`
```python
def outer():
    result = []
    
    def inner():
        # result.append(1)     # ✅ Works - modifying same object
        # result = [1, 2, 3]   # ❌ UnboundLocalError - reassignment!
        pass
    
    inner()
```

---

## 🌳 Tree Problem Case Study

Let's analyze the diameter problem with different approaches:

### Approach 1: Using `self` (Instance Variable)
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0  # ✅ Instance variable - accessible everywhere
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            self.max_diameter = max(self.max_diameter, diameter)  # ✅ Works
            return 1 + max(left, right)
        
        dfs(root)
        return self.max_diameter
```

**Pros:**
- ✅ Simple and clean
- ✅ No scope issues
- ✅ Common in LeetCode solutions

**Cons:**
- ❌ Modifies object state
- ❌ Not purely functional

### Approach 2: Using `nonlocal`
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        max_diameter = 0  # Local variable
        
        def dfs(node):
            nonlocal max_diameter  # ✅ Bind to enclosing scope
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            max_diameter = max(max_diameter, diameter)  # ✅ Works
            return 1 + max(left, right)
        
        dfs(root)
        return max_diameter
```

**Pros:**
- ✅ More functional approach
- ✅ Doesn't modify object state
- ✅ Variable scope is explicit

**Cons:**
- ❌ Slightly more verbose
- ❌ Need to remember `nonlocal`

### Approach 3: Using Mutable Container
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        result = [0]  # ✅ Mutable list - no nonlocal needed
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            result[0] = max(result[0], diameter)  # ✅ Modifying list content
            return 1 + max(left, right)
        
        dfs(root)
        return result[0]
```

**Pros:**
- ✅ No `nonlocal` needed
- ✅ No instance variable pollution

**Cons:**
- ❌ Awkward syntax `result[0]`
- ❌ Less readable than other approaches

### Approach 4: Return Multiple Values (Most Functional)
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0, 0  # (height, max_diameter)
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)
            
            current_diameter = left_height + right_height
            max_diameter = max(left_diameter, right_diameter, current_diameter)
            height = 1 + max(left_height, right_height)
            
            return height, max_diameter
        
        _, diameter = dfs(root)
        return diameter
```

**Pros:**
- ✅ Purely functional - no side effects
- ✅ No scope issues at all
- ✅ Most elegant solution

**Cons:**
- ❌ Slightly more complex logic
- ❌ Returns extra information

---

## 🚨 Common Scope Errors & Solutions

### Error 1: UnboundLocalError
```python
# ❌ This crashes:
def func():
    x = 10
    def nested():
        x = x + 1  # UnboundLocalError!
    nested()

# ✅ Solutions:
def func():
    x = 10
    def nested():
        nonlocal x  # Solution 1
        x = x + 1
    nested()

# Or:
class Solution:
    def func(self):
        self.x = 10  # Solution 2
        def nested():
            self.x = self.x + 1
        nested()
```

### Error 2: Modifying vs Reassigning
```python
def func():
    lst = []
    count = 0
    
    def nested():
        # ✅ These work:
        lst.append(1)       # Modifying mutable object
        
        # ❌ These need nonlocal:
        # count = count + 1   # Reassigning immutable
        # lst = [1, 2, 3]     # Reassigning mutable variable
    
    nested()
```

---

## 📋 Decision Matrix: When to Use What?

| Scenario | Use `self` | Use `nonlocal` | Use Mutable Container | Return Values |
|----------|------------|----------------|----------------------|---------------|
| **LeetCode problems** | ✅ Common | ✅ Good | ❌ Awkward | ✅ Best |
| **Single value tracking** | ✅ Simple | ✅ Clean | ❌ Verbose | ✅ Pure |
| **Multiple values** | ✅ Easy | ✅ OK | ❌ Complex | ✅ Natural |
| **Functional style** | ❌ Side effects | ⚠️ Better | ⚠️ Better | ✅ Perfect |
| **Performance** | ✅ Fast | ✅ Fast | ✅ Fast | ✅ Fast |
| **Readability** | ✅ Clear | ✅ Clear | ❌ Confusing | ✅ Clear |

---

## 🎯 Best Practices

### 1. **Choose Based on Context**
```python
# For LeetCode/Interview - use self (simple & common)
class Solution:
    def problem(self, root):
        self.result = 0
        # ... nested function uses self.result

# For production code - prefer functional approach
def problem(root):
    def helper(node):
        # Return multiple values instead of modifying external state
        return value1, value2
    return helper(root)
```

### 2. **Be Explicit About Scope**
```python
# ✅ Good - explicit nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count  # Clear intent
        count += 1
    inner()

# ❌ Avoid - mutable container trick
def outer():
    count = [0]  # Confusing - why a list?
    def inner():
        count[0] += 1
    inner()
```

### 3. **Document Scope Decisions**
```python
class Solution:
    def complexProblem(self, root):
        # Using instance variable for simplicity in interview setting
        self.max_val = 0
        
        def dfs(node):
            # Could use nonlocal, but self.max_val is clearer
            self.max_val = max(self.max_val, node.val)
        
        dfs(root)
        return self.max_val
```

---

## 🔥 Quick Reference

### Scope Resolution
```python
# Reading variables: LEGB order (Local → Enclosing → Global → Built-in)
# Modifying variables: Must be in correct scope

def outer():
    x = 1              # Enclosing scope
    def inner():
        print(x)       # ✅ Reading works from any scope
        # x = x + 1     # ❌ Modifying needs nonlocal
        nonlocal x     # ✅ Now modification works
        x = x + 1
    inner()
```

### Instance Variables
```python
class MyClass:
    def method(self):
        self.var = 1   # ✅ Accessible in all methods & nested functions
        
        def nested():
            self.var += 1  # ✅ Always works with self
        
        nested()
```

### Immutable vs Mutable
```python
# Immutable: int, str, tuple - assignment creates new object
count = 0
count = count + 1  # New object

# Mutable: list, dict, set - methods modify same object  
lst = []
lst.append(1)      # Same object, modified
```

### Error Patterns
```python
# ❌ UnboundLocalError pattern:
def func():
    x = 0
    def nested():
        x = x + 1  # Error - local x not defined
    nested()

# ✅ Solutions:
def func():
    x = 0
    def nested():
        nonlocal x      # Solution 1
        x = x + 1
    nested()

# Or in class:
class Solution:
    def func(self):
        self.x = 0      # Solution 2
        def nested():
            self.x = self.x + 1
        nested()
```

---

## 💡 Memory Aids

**"LEGB"** - **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in

**"Modify = Scope"** - If you're modifying a variable, make sure it's in the right scope

**"self Always Works"** - Instance variables with `self` are accessible everywhere

**"nonlocal for Numbers"** - Use `nonlocal` when modifying immutable types in nested functions

**"Return > Modify"** - Returning values is often cleaner than modifying external state