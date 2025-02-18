from typing import List


class Solution:
    """
    what I learned
    - be confident in your intuition and try to make it work
    - FOCUS on validating your intuition well step by step
        - I did avoid this as I told myself the while loop could cost O(n)
        - I'm not fully convinced, why it doesn't cost O(n)
    - FOCUS on the constraints too, it may be an indicator
    """
    def dailyTemperatures_brute(self, temperatures: List[int]) -> List[int]:
        """
        time complexity O(n^2)
        space complexity O(1)
        TLE
        """
        result = []
        for i in range(len(temperatures)):
            days = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    days = j - i
                    break

            result.append(days)

        return result

    def dailyTemperatures_stack(self, temperatures: List[int]) -> List[int]:
        """
        time complexity O(n)
        space complexity O(n)
        run time beats 30% and space beats 23%
        notes:
            - montonic decreasing stack problem similar to max_windo_slide monotonic deque problem
            - does this adds extra time complexity `while stack and current > stack[-1][0]:` ?
                - it shouldn't as max number of iteration in one element could be O(n),
            - `result = [0] * len(temperatures)` stack is LIFO, 
                so when popping last item we have to put in the equivalent index, this way we can access the index directly
                Ex. temperatures = [73,74,75,71,69,72,76,73], this part [71,69,72], 
                    69 is first in stack but is second in result list
            - similar to sliding window right is current, left is previous 
            - you don't need store the (key, index) pair. You can just store the index in the queue
            - montonic dec. stack Ex:
                temp[0]=4, stack=[], result=[0, 0, 0, 0]
                temp[1]=3, stack=[(4, 0)], result=[0, 0, 0, 0]
                temp[2]=2, stack=[(4, 0), (3, 1)], result=[0, 0, 0, 0]
                temp[3]=1, stack=[(4, 0), (3, 1), (2, 2)], result=[0, 0, 0, 0]
            - `for idx in range(len(temperatures) - 1):` the `-1` part would lead to wrong results, why ?
                - as we compare current element with the previous ones
                - Ex: [30, 60, 90], temp[2]=90, stack=[(60, 1)], result=[1, 0, 0], 
                - in this last iteration 60 will be removed as current=90 and current > stack[-1][0]
            
        """
        stack = []
        result = [0] * len(temperatures)
        days = 0
        print(temperatures)
        for idx in range(len(temperatures)):
            current = temperatures[idx]
            print(f"temp[{idx}]={current}, stack={stack}, result={result}")
            while stack and current > stack[-1][0]:
                prev_idx = stack[-1][1]
                days = idx - prev_idx
                result[prev_idx] = days
                # print(f"inside temp[{idx}]={current}, prev_idx={prev_idx}, days={days}, last={stack[-1][0]}, stack={stack}, result={result}") # before popping
                stack.pop()

            stack.append((current, idx))

        return result

    def dailyTemperatures_stack_v2(self, temperatures: List[int]) -> List[int]:
        """using index only to save space since we are sure that it's a decreasing monotonic stack
        getting index by idx=stack[-1] and value=temperatures[idx] """
        ans = [0] * len(temperatures)

        stack = []

        for day, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:

                last_day = stack.pop()

                ans[last_day] = day - last_day
            stack.append(day)

        return ans

    def dailyTemperaturesReverse(self, temperatures):
        """dynamic programming approach, will leave it now and check it later"""
        n = len(temperatures)
        result = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = n  # No warmer day found
                else:
                    j += result[j]
            if j < n:
                result[i] = j - i

        return result


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.dailyTemperatures_stack(temperatures)


temperatures = [73,74,75,71,69,72,76,73]
res = Solution().dailyTemperatures(temperatures)
print("RES ==>", res)
assert res == [1,1,4,2,1,1,0,0]


temperatures = [30,40,50,60]
res = Solution().dailyTemperatures(temperatures)
print("RES ==>", res)
assert res == [1,1,1,0]


temperatures = [30,60,90]
res = Solution().dailyTemperatures(temperatures)
assert res == [1,1,0]


temperatures = [4, 3, 2, 1]
res = Solution().dailyTemperatures(temperatures)
assert res == [0, 0, 0, 0]

