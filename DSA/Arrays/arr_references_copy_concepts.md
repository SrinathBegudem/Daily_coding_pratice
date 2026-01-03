# References vs Copies in Python  
Understanding how Python handles variables, lists, and copying.

---

## 1️⃣ Assignment does NOT copy

When you write:

```python
a = [1, 2, 3]
b = a
No new list is created.

Both names point to the same object:

python
Copy code
b[0] = 99
# a -> [99, 2, 3]
# b -> [99, 2, 3]
Think: two labels on the same box.

2️⃣ Shallow copy copies only the outer container
Ways to make a shallow copy:

python
Copy code
b = a[:]          # slicing
b = list(a)       # constructor
import copy
b = copy.copy(a)  # shallow copy
This creates a new outer list, but its elements still reference the same inner objects:

python
Copy code
a = [[1], [2]]
b = a[:]          # shallow copy

b[0].append(99)
Result:

lua
Copy code
a = [[1, 99], [2]]
b = [[1, 99], [2]]
Shallow copy is usually safe only when items inside are immutable
(ints, strings, tuples, etc.).

3️⃣ Deep copy duplicates everything recursively
python
Copy code
import copy
b = copy.deepcopy(a)
Now:

python
Copy code
b[0].append(99)
Result:

lua
Copy code
a = [[1], [2]]
b = [[1, 99], [2]]
Use when working with nested mutable structures.

4️⃣ Slicing pitfalls (why rotate() broke)
Slicing creates a new list, not an in-place view:

python
Copy code
y = nums[:k]   # copy
So:

python
Copy code
reverse(nums[:k])
reverses a temporary copy and throws it away.

To modify in-place, work with indexes, not slices:

python
Copy code
reverse(0, k-1)
reverse(k, n-1)
5️⃣ Mutability matters
Immutable (safe to share):

int

float

bool

str

tuple

Mutable (dangerous to share unintentionally):

list

dict

set

most custom objects

6️⃣ Quick cheat sheet
Same list (no copy)

python
Copy code
b = a
Shallow copy

python
Copy code
b = a[:]
Deep copy

python
Copy code
import copy
b = copy.deepcopy(a)
In-place algorithm rule

Avoid arr[:] when you actually want to modify.
Prefer functions that take indices.

7️⃣ Mental model that never fails
Variables are arrows, not boxes:

pgsql
Copy code
name  ───► object
Assignment moves the arrow.
Copying creates a new object.

8️⃣ Common pitfalls
modifying shared lists by accident

slicing and assuming “in-place” behavior

shallow copy sharing inner elements

forgetting nested data requires deepcopy

default mutable function arguments like:

python
Copy code
def foo(x=[]):   # bad
9️⃣ Best practices
✔ be explicit when copying
✔ prefer immutables when possible
✔ clearly document when functions mutate inputs
✔ use deep copy only when you truly need it
✔ test nested structures carefully

Summary
Operation	New object?	Inner objects copied?
b = a	❌ No	❌ No
b = a[:]	✅ Yes	❌ No
copy.copy(a)	✅ Yes	❌ No
copy.deepcopy(a)	✅ Yes	✅ Yes

Save, revisit, and practice — this concept unlocks a LOT of debugging wins.

yaml
Copy code

---

If you want, I can also add:

• diagrams  
• exercises  
• LeetCode examples that specifically break when copies go wrong  

Just say the word.






