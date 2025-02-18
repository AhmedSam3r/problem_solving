from collections import deque


class MinStack:
    """
    time complexity: O(1)
    time complexity: O(2n)=O(n)
    time and memory beats ~30%
    - my solution, using primary and secondary storage for tracking min
    - we can optimize memory using stack instead of deque
    - example
        ```
        def push(self, val: int) -> None:
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)

        def pop(self) -> None:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        ```

    """

    def __init__(self):
        self.stack = list()
        self.deq = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        # = is important to make it work, to avoid adding min elements at the nend
        if self.deq and self.deq[0] >= val:
            self.deq.appendleft(val)
        else:
            self.deq.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.deq and self.deq[0] == popped:
            self.deq.popleft()
        elif self.deq and self.deq[-1] == popped:
            self.deq.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.deq[0]


class MinStackSol2:
    """
    chatgpt solution
    uses only one stack but with pairs to track minimum, 
        where it stores the current minimum along with the value
    explains the min stack approach but he's using an extra DS min stack `https://www.youtube.com/watch?v=RfMroCV17-4`
    Input: 5, 4, -1, 10, -20
    min stack = x=5, [5], x=4, [5,4], x=-1. [5,4,-1] x= 10, [5,4,-1,-1], x=-20, [5,4,-1,-1,-20]
    see how it appends the min to the top value
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))
        print("CURRENT STACK ==>", self.stack)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Ex.1
minStack = MinStack()
assert minStack.stack == []
minStack.push(-2)
assert minStack.stack == [-2]
minStack.push(0)
assert minStack.stack == [-2, 0]
minStack.push(-3)
assert minStack.stack == [-2, 0, -3]
min_val = minStack.getMin()
assert min_val == -3
minStack.pop()
top = minStack.top()
assert top == 0
min_val = minStack.getMin()
assert min_val == -2

# Ex.2
minStack = MinStack()
assert minStack.stack == []
minStack.push(0)
assert minStack.stack == [0]
minStack.push(1)
assert minStack.stack == [0, 1]
minStack.push(0)
assert minStack.stack == [0, 1, 0]


minStack = MinStackSol2()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
min_val = minStack.getMin()
print("MIN VAL ==>", min_val)
minStack.pop()
top = minStack.top()
min_val = minStack.getMin()
print("MIN VAL ==>", min_val)
