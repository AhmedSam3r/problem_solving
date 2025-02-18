
## RPN problem
[PEP 238 – Changing the Division Operator](https://peps.python.org/pep-0238/)
### Floor division
The result of `x // y` is `-1` because the `//` operator in Python performs **floor division**. Floor division returns the largest integer less than or equal to the result of the division. Let's break it down:

### Calculation Steps:
1. **Normal Division**: \( x \div y = 6 \div -132 \approx -0.0454545 \)
   
2. **Floor Division (`//`)**: The floor division of \( -0.0454545 \) is the greatest integer less than or equal to \( -0.0454545 \). In this case, that integer is \( -1 \).

### Why `-1`?
- **Floor Function Behavior**: The floor of a number is the largest integer less than or equal to that number. Since \( -0.0454545 \) is negative and slightly above \( -1 \), the floor function takes it down to \( -1 \).

### Important Note:
- Floor division always rounds down to the nearest integer, even for negative results. This is different from truncating division, which simply drops the decimal part.

Thus, `6 // -132` results in `-1` because the division results in a negative fraction, and the floor division rounds it down to the next lower integer, which is \( -1 \).


The result of `x // y` is `-1` because the `//` operator in Python performs **floor division**. Floor division returns the largest integer less than or equal to the result of the division. Let's break it down:

### Calculation Steps:
1. **Normal Division**: \( x \div y = 6 \div -132 \approx -0.0454545 \)
   
2. **Floor Division (`//`)**: The floor division of \( -0.0454545 \) is the greatest integer less than or equal to \( -0.0454545 \). In this case, that integer is \( -1 \).

### Why `-1`?
- **Floor Function Behavior**: The floor of a number is the largest integer less than or equal to that number. Since \( -0.0454545 \) is negative and slightly above \( -1 \), the floor function takes it down to \( -1 \).

### Important Note:
- Floor division always rounds down to the nearest integer, even for negative results. This is different from truncating division, which simply drops the decimal part.

Thus, `6 // -132` results in `-1` because the division results in a negative fraction, and the floor division rounds it down to the next lower integer, which is \( -1 \).



### 4 generate paranethes
- mainly it's a backtracking problem
- need to understand how permutations work with a string to generate all the strings, `4_premutations_dummy_ex.py` file 



### 5 daily temperature
what I learned
- be confident in your intuition and try to make it work
- **FOCUS on validating your intuition well step by step**
    - **I did avoid this as I told myself the while loop could cost O(n)**
    - **I'm not fully convinced, why it doesn't cost O(n)**
- FOCUS on the constraints too, it may be an indicator
- **it's similar to sliding window problems**

#### Why while loop isn't quadratic
- **actually its still O(n) even in worst scenario**
- **we can consider it in worst case O(n+n) where the extra n is an item that loops through the whole stack**
  - **In only one iteration it can be O(N) worst case**
- **Key Insight: Total Number of Pushes and Pops**
  - Each index is pushed onto the stack exactly once in the outer loop.
  - Each index is popped from the stack exactly once in the inner loop.
  - This means the total number of stack operations (push + pop) is at most 2n (n pushes and n pops), regardless of the input.



#### Example
- if we have [4,3,2,1], our stack would be [4,3,2,1], 
    however, when we at 3, we know 3 < 4, so we don't have to loop through the whole stack, we simply append it, thats O(1), 
- same for all the other operations, we simply return the res with everything as 0, 
    even if we have something like [4,3,2,1,5], we only process [4,3,2,1] once when we reach 5 (bigger than all of them). thats only O(n),   
- so maximumly, we process each node twice and thats it, imagine we have [4,3,2,1,3], 
  - when we reach the last 3, we process only the [2,1,] from  [4,3,2,1], then we stop, our stack would look like [4,3], the algorithm is done



## 6 car fleet
- **the more you managed to visualize and draw the problem, the better you can understand and reach a solution**
- **Monotonic decreasing stack/queue concept is used 3 times so far in the 4_5, 4_6 and 3_6


## largest histogram
- why `start = prev_index` and `width = len(heights) - prev_index` gives correct results ?
    - as this is a monotonic increasing order stack
    - ex: stack=[(1, 0), (2, 1), (4, 2), (5, 3)], 
    - `width = len(heights) - prev_index` 
        so each item is min height in the stack 
        if extended right to the end as the upcoming values are larger
    - 
- the trick in this question how to check stack in a backward direction
    - we do this by saving the index `start = prev_index`
    - similar to the idea i was thinking about from 4_stack/2_min_stack problem
        where it stores the min value besides the current value
    - so we store the last index we can get back to in backward direction
- we canot store index only as we will get wrong results due to the previous point existence
- similar to  2_two_pointers/5_trap_water problem
- beats 41% in run time
### Part 1: Explanation of `width = i if not stack else i - stack[-1] - 1`

#### Context:
- The **`stack`** stores indices of histogram bars in increasing order of height.
- Whenever a bar at index `i` is shorter than the bar at the top of the stack (or if `i == n`, representing the end of the histogram), the bar at the top of the stack is "popped" because we can no longer extend a rectangle with that height beyond this point.
- The **`width`** of the rectangle with the popped bar's height is determined by how far to the left and right the rectangle can extend.

#### Key Points:
1. **If the stack is empty (`not stack`)**:
   - This means the popped bar extends all the way to the beginning of the histogram (index 0).
   - The width of the rectangle is simply:
     ```python
     width = i
     ```
   - This is because the rectangle spans from index `0` to the current index `i - 1`.

2. **If the stack is not empty**:
   - The stack contains the index of the previous smaller bar (to the left of the popped bar).
   - `stack[-1]` is the index of this previous smaller bar.
   - The rectangle with the popped bar's height starts **right after** this smaller bar (`stack[-1] + 1`) and ends at the current index (`i - 1`).
   - The width is therefore:
     ```python
     width = i - stack[-1] - 1
     ```

---

### Part 2: Why `i - stack[-1] - 1` works correctly every time

#### Key Concept:
The **stack ensures that we always process indices in the correct order, from left to right, and each rectangle is calculated exactly once**. Here's why:

---

#### Step-by-Step Logic:

1. **The Stack Maintains Increasing Order**:
   - The stack stores indices of bars in increasing height order.
   - When a new bar is encountered that is **shorter** than the bar at the top of the stack, the taller bar is popped because the new bar limits its right boundary.
   - Since the stack is processed in increasing order of indices, the **next smaller bar to the left of the popped bar is always at `stack[-1]`**.

---

2. **Why `i - stack[-1] - 1` Always Gives the Correct Width**:
   - When we pop a bar from the stack:
     - Its **right boundary** is the current index `i` (because `heights[i]` is smaller).
     - Its **left boundary** is the index after `stack[-1]` (the previous smaller bar).
   - The width of the rectangle is:
     ```python
     width = (right boundary - left boundary - 1)
            = i - (stack[-1] + 1)
            = i - stack[-1] - 1
     ```

---

#### Why It Works for All Cases:

1. **Case 1: Stack Is Empty (`not stack`)**:
   - If there’s no smaller bar to the left, the rectangle starts from the beginning of the histogram.
   - Width is `i`, which is correct because the rectangle spans from `0` to `i - 1`.

2. **Case 2: Stack Is Not Empty**:
   - The top of the stack (`stack[-1]`) is the nearest smaller bar to the left.
   - Since indices are processed from left to right:
     - All indices in the stack have been processed in increasing order.
     - Thus, the width is correctly calculated as extending from `stack[-1] + 1` to `i - 1`.

---

### Intuition and Guarantee:
- Each bar is processed exactly once (when it's pushed and when it's popped).
- The stack ensures that when a bar is popped, we already know the nearest smaller bars to both its left and right.
- This guarantees that **`i - stack[-1] - 1` always provides the correct width** for the rectangle because:
  - `stack[-1]` is the last index of a bar taller than the current height.
  - The stack never skips indices, ensuring correctness for all bars.

---

### Proof:
For a given bar at index `top` (height `heights[top]`):
1. The **right boundary** of the rectangle is defined by the current index `i` (where `heights[i] < heights[top]`).
2. The **left boundary** of the rectangle is defined by `stack[-1]` (the nearest smaller bar to the left of `top`).
3. The stack ensures:
   - Every index to the left of `top` that has not been popped yet corresponds to bars taller than `heights[top]`.
   - This guarantees that `stack[-1]` correctly identifies the left boundary.

Thus, the width calculation `i - stack[-1] - 1` is valid because:
- It excludes the taller bars to the left (at `stack[-1]`).
- It stops at the first shorter bar on the left.

Let me know if you need further clarification!
