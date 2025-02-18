# Notes
## longest_substring problem
The key differences between using a Set and a Dictionary (HashMap) in the sliding window approach for finding the longest substring without repeating characters come down to how each handles duplicates and how efficiently they manage the start pointer of the window.

### Using a Set:
- Mechanism: The set approach checks if a character is already in the set to determine duplicates. When a duplicate is found, it removes characters from the start of the window until the duplicate is removed.
- Efficiency Drawback: Each time a duplicate is found, potentially multiple characters are removed from the set, which can take linear time in the worst case (e.g., continuously shrinking the window). This involves a repeated check and deletion process.
- Performance: This approach can be slower because of the repeated operations for removing elements and adjusting the start pointer.
### Using a Dictionary (HashMap):
- Mechanism: The dictionary stores the last seen index of each character. When a duplicate is found, it directly jumps the start pointer to char_index[s[end]] + 1 (the index right after the last occurrence of the current character).
- Efficiency Gain: This jump is direct and efficient. Instead of iterating and removing multiple characters, the start pointer is immediately moved to the correct position, minimizing unnecessary operations.
- Performance: This approach is faster because it avoids the repeated removal process by leveraging the dictionary to efficiently manage the window's boundaries.

## longest substring repeating problem
You're right in noticing some similarities between the brute force and the two-pointer (sliding window) solutions, but there are key differences that affect their time complexity and efficiency:

### Key Differences:

1. **Window Expansion and Shrinking**:
   - **Brute Force**: 
     - It explores every possible starting and ending index of the substring using nested loops.
     - For each start, it calculates the result for every possible end, checking the condition anew for each combination.
     - This results in \(O(n^2)\) time complexity since the inner loop runs independently for each start position.
   - **Two-Pointer (Sliding Window)**:
     - The two-pointer method expands and shrinks the window dynamically.
     - The `end` pointer moves forward to expand the window, while the `start` pointer adjusts only when necessary (when the condition of at most `k` replacements is violated).
     - The key is that the inner logic doesn't restart from every `start` position. Instead, it maintains and updates the window, leading to \(O(n)\) time complexity.

2. **Redundancy**:
   - **Brute Force**:
     - It repeatedly recalculates values for overlapping windows. For example, it recalculates the frequency and max frequency for substrings that are part of larger substrings.
   - **Two-Pointer**:
     - It efficiently reuses calculations from the previous step by only updating the counts as `end` advances or `start` shifts.
     - There's no redundant recalculation for overlapping parts of the string.

3. **Optimized Condition Checking**:
   - **Brute Force**:
     - Checks the condition for each possible window, including many that overlap or are subsets of already checked windows.
   - **Two-Pointer**:
     - Continuously evaluates the same window while expanding or contracting it, reducing redundant checks and unnecessary recalculations.

### Summary of Efficiency:
- **Brute Force**: Expensive because it explores all possible substrings independently.
- **Two-Pointer**: Efficient because it manages and updates a single window dynamically, avoiding the need to re-evaluate overlapping substrings from scratch.


## preumtation in a string

### Shallow Copy vs. Deep Copy

**1. Shallow Copy:**
- A shallow copy creates a new object, but the elements inside it are references to the same objects found in the original.
- For immutable objects (like integers or strings), this works fine since the values can't change.
- For mutable objects (like lists of lists), the shallow copy will point to the same nested objects. Modifying a nested object in one will reflect in the other.

**Example:**
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 9
print(original)  # Output: [[9, 2], [3, 4]] (both are affected)
```

**2. Deep Copy:**
- A deep copy creates a new object and recursively copies all objects found in the original.
- Changes to any part of the deep copy do not affect the original, even for nested objects.

**Example:**
```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 9
print(original)  # Output: [[1, 2], [3, 4]] (original remains unchanged)
```

### Key Differences:
- **Shallow Copy:** 
  - Copies the structure of the object, but not the nested objects.
  - Faster and uses less memory for the initial copy.
  - Changes to nested objects affect both copies.
  
- **Deep Copy:** 
  - Recursively copies all objects and sub-objects.
  - More memory and processing time are required.
  - Changes to any part of the copied object do not affect the original.

In summary, use a deep copy when you need full independence between the original and the copy, especially if there are nested mutable objects. Use a shallow copy when you only need to copy the top-level object and the internal references can remain shared.


## Max sliding window

Let's address why the while-loop:
worst case `nums=[4,5,6,7,8,9,10,11,12]`, `k=3` each element would be added and removed once
```python
while max_heap[0][1] <= i - k:
    heapq.heappop(max_heap)
```

does not make the overall complexity **O(n * k * log n)**:

### Key Points:

1. **Purpose of the While-Loop**:
   - The loop ensures that we remove elements from the heap that are outside the bounds of the current sliding window (`i - k + 1` to `i`).
   - `max_heap[0][1] <= i - k` checks if the maximum element's index (`max_heap[0][1]`) is out of the sliding window.

2. **Maximum Removals Per Element**:
   - Although it seems the loop might run up to `k` times per iteration, the total number of `heappop` operations over the entire process is limited by the number of elements in `nums`.
   - Each element in the array is added to the heap once and removed from the heap at most once.

3. **Amortized Analysis**:
   - Each element can be pushed and popped exactly once, leading to **n push and n pop operations**.
   - Even though in some iterations of the main loop, we might remove more than one element (if multiple elements are out of the window), the overall number of pop operations is still **O(n)**.
   - The key point is that each element is handled exactly twice (pushed once and popped once), and the heap operations (push and pop) are each **O(log k)**.

4. **No Redundant Operations**:
   - The loop only removes elements that are strictly necessary to maintain the heap invariant for the sliding window.
   - Elements are not repeatedly processed in a way that would result in **O(k)** removals per iteration consistently.

### Time Complexity:

- **Heap Operations**:
  - Each push and pop operation is **O(log k)**.
  
- **Total Operations**:
  - **n** push operations (one for each element).
  - **n** pop operations (each element is removed at most once).

- **Overall Complexity**:
  - The total number of heap operations is **2n** (push and pop), each taking **O(log k)**.
  - Therefore, the overall time complexity remains **O(n log k)**.

In summary, while the while-loop might run multiple times in some iterations, the total number of pop operations across all iterations is still **O(n)**, leading to the overall complexity of **O(n log k)**.