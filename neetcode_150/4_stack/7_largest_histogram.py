from typing import List
from collections import deque


class Solution:
    def largestRectangleArea_brute(self, heights: List[int]) -> int:
        largest = float("-inf")
        print(heights)
        for i in range(len(heights)):
            current = heights[i]
            current_min = current
            print("CURRENT ==>", current)
            for j in range(i+1, len(heights)):
                window_size = (j-i) + 1  # calculate total width

                current_min = min(current_min, heights[j])
                largest = max(largest, current_min * window_size)
                print(f"WINDOW SIZE {window_size}, current_min={current_min}, heights[{j}]={heights[j]}, local_area={current_min * window_size}, largest={largest}")
                if heights[j] < current:
                    break

        return largest
    
    def largestRectangleArea_deque(self, heights: List[int]) -> int:
        "it passed 46/99 tests"
        largest = float("-inf")
        # stack = []
        que = deque()
        print(heights)
        for i in range(len(heights)):
            current = heights[i]
            min_current = min(current, que[-1]) if que else current
            print("min current ==>", min_current)
            print(f"current[{i}]={current}, stack={que}, largest={largest}")
            while que and current < que[-1]:
                if que and que[0]:
                    largest = max(largest, que[0] * len(que))
                que.popleft()

            # print(f"current[{i}]={current}, stack={que}, largest={largest}")
            que.append(current)
            largest = max(largest, que[0] * len(que))

        # get remaining elements
        while que:
            que.popleft()
            largest = max(largest, que[0] * len(que)) if que else largest

        min_item = min(heights)
        print("END")
        largest = max(largest, min_item * len(heights))

        return largest

    def largestRectangleArea_stack(self, heights: List[int]) -> int:
        """
        time complexity O(N)
        space complexity O(N)
        - excellent exapalantion `https://www.youtube.com/watch?v=ZGMw8Bvpwd4`
            - The moment we see dip, we process the top of stack item in backward direction.
        - the trick in this question how to check stack in a backward direction
        """
        stack = []
        max_area = float("-inf")
        print(heights)
        for i, height in enumerate(heights):
            start = i

            print(f"height[{i}]={height}, stack={stack}, max_area={max_area}")
            while stack and height < stack[-1][0]:
                h, prev_index = stack.pop()
                width = i - prev_index
                # area = height * width
                max_area = max(max_area, h * width)
                # the trick resides/lies here
                # you want assign the start to the index you can extend to
                # not the height's actual index
                # from this index we can extend to the left to get the max area
                start = prev_index

            stack.append((height, start))
            print(f"V222 height[{i}]={height}, stack={stack}, max_area={max_area}")
        print("STK ==>", stack)
        # get remaining elements
        while stack:
            h, prev_index = stack.pop()
            # len(heights) as we reached to the end of list acts as imaginary index
            width = len(heights) - prev_index
            max_area = max(max_area, h * width)

        return max_area

    def largestRectangleArea_stack_optimized(self, heights: List[int]) -> int:
        """one pass stack"""
        n = len(heights)
        maxArea = 0
        stack = []
        print(heights)
        for i in range(n + 1):
            if i < n:
                print(f"{i}: {heights[i]}==> stack={stack}, max_area={maxArea}")
            while stack and (i == n or heights[i] < heights[stack[-1]]):
                # {heights[i - stack[-1]]} # gives error
                # print(f"index={i} ::: ELEM ==> [{i - stack[-1]}]= vs [{i - stack[-1] - 1}], ")
                height = heights[stack.pop()]
                # acts as start=prev_index, as it gets the earlier element so we can extend backward
                # why stacl
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
            print(f"V222 stack={stack}, max_area={maxArea}")
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.largestRectangleArea_stack(heights)


heights = [2,1,5,6,2,3]
res = Solution().largestRectangleArea(heights)
print(f"RES = {res}")
assert res == 10


heights = [2,4]
res = Solution().largestRectangleArea(heights)
assert res == 4



heights = [0,9]
res = Solution().largestRectangleArea(heights)
assert res == 9


heights = [2,1,2]
res = Solution().largestRectangleArea(heights)
assert res == 3


heights = [5,4,1,2]
res = Solution().largestRectangleArea(heights)
print("RES ==>", res)
assert res == 8

heights = [1,2, 4, 5]
res = Solution().largestRectangleArea(heights)
print("RES ==>", res)
assert res == 8



# heights = [5,4,4,2]
# res = Solution().largestRectangleArea(heights)
# print("RES ==>", res)
# assert res == 12
