from typing import List
import heapq
from collections import deque


class Solution:
    """
        explanation video that contains 3 approaches`https://www.youtube.com/watch?v=LiSdD3ljCIE` 
    """
    def maxSlidingWindow_brute_force_v1(self, nums: List[int], k: int) -> List[int]:
        """
        # of windows = n - k + 1
        time complexity O(n* k)
        """
        if k > len(nums):
            return nums
        result = []
        for right in range(len(nums)):
            if right + k > len(nums):
                break
            window = (right + k) - 1
            max_num = max(nums[right: right+k])
            result.append(max_num)

        return result

    def maxSlidingWindow_brute_force_v2(self, nums: List[int], k: int) -> List[int]:
        """
        time complexity O(n*k) => O(n^2)
        space complexity O(1)
        time limit exceeded TLE due to `max_num = max(nums[right: right+k])` create new list every time
        """
        if k > len(nums):
            return nums
        result = []
        left = 0
        for right in range(len(nums)):
            copy_left = left
            max_num = float("-inf")
            window = (right - left) + 1
            print('-----')
            print(f"window={window}, max_num={max_num}, lst={nums[right: right+k]}")
            print(f"left + right + 1 ==>, {copy_left + right + 1}, copy_left={copy_left}, left={left}, right={right}, , k={k}, wind={right - copy_left + 1}, result={result}, cond={(right - copy_left + 1) == k} & {copy_left <= right}")
            while window == k and copy_left <= right:
                max_num = max(max_num, nums[copy_left])
                print(f'copy_left -> {copy_left}, nums[left]={nums[copy_left]}, max_num={max_num}')
                copy_left += 1
            if window == k:
                left += 1
                result.append(max_num)
            print('-----')

        return result

    def maxSlidingWindow_linear(self, nums: List[int], k: int) -> List[int]:
        """
        fails at nums=[1, 1], k=[1]
        if we modified this section to the following, it will fail as it won't be able to track the history of the previous items
            ```
            left += 1
            result.append(max_num)
            max_num = float("-inf")
            ```
        how to remove the element out of the window ?
        """
        if k > len(nums):
            return nums
        result = []
        left = 0
        max_num = float("-inf")
        for right in range(len(nums)):
            window = (right - left) + 1
            max_num = max(max_num, nums[right])
            if window == k:
                left += 1
                result.append(max_num)

        return result

    def maxSlidingWindow_heap(self, nums: List[int], k: int) -> List[int]:
        """
        time complexity: O(n log(k)) or n log(n) if elements in an decreasing order array 4,3,2,1, so popping would never occur
        space complexity O(n) 
    
        - beats 17% in runtime and 7% in memory time
        - how to remove the element out of the window ?
            - by storing the index and checking each iteration if its out of bound
        - window bound [i-k+1, i]
            - left - right + 1 = k, left - k + 1 = right (upper bound)
        - The sliding window covers elements from index i - k + 1 to i. (i = current)
            - i - k is the last index that is outside the current window.
        - heap is min heap  default
        - If max_heap[0][1] <= i - k
            it means that the index of the current maximum element in the heap 
            is no longer within the bounds of the current sliding window (it is to the left of the current window).
            - This element needs to be removed from the heap because it's not valid for the current window.

        """
        if k > len(nums):
            return nums
        result = []
        heap = []
        # create a heap of k size (window size)
        for i in range(k):
            heapq.heappush(heap, (nums[i] * -1, i))

        print(nums)
        for current in range(k-1, len(nums)):
            # pop the root if it's sliding out of the window
            # not interested in other elements since they're not the max element
            while heap and (heap[0][1] <= (current-k)):
                heapq.heappop(heap)
            heapq.heappush(heap, (-1 * nums[current], current))
            # window_size = k - 1, since we're starting from k-1
            # we're sure to get valid window every iteration
            result.append(heap[0][0] * -1)
            print(f"index={current}, current={nums[current]}, heap={heap}, max_num={heap[0][0] * -1}, result={result}")

        return result

    def maxSlidingWindow_deque_v1(self, nums: List[int], k: int) -> List[int]:
        """
        time complexity: O(n)
        space complexity O(n)
        - most optimized approach using monotonic queue
        - ind - left + 1 = k, therefore: ind - k + 1 = left
        - notice here index - k + 1 < deq[0][1] is equivalent to index - k <= deq[0][1]
        double ended queue (DLL) where you maintain element in chronological order where inserting and
        - `while deq and deq[0][1] < (ind - k + 1):` works instead of `if deq and deq[0][1] < (ind - k + 1):`
            in case of nums=[1, -1], k=1, as we add the first element twice
            since we start from k-1 and append elements to the queue
        - this approach will fail at `nums =[9,10,9,-7,-4,-8,2,-6], k=5` since the population isn't done the same as monotonic queue
            instead modify the for loop to follow same style and start from `k` not `k-1`
        - my approach is faster a bit, runtime beats 37%
        - this examples shows better why we keep elements in a descending order `https://youtu.be/DfljaUwZsOk?t=535`
        Algorithm
        1. pop the front of the DLL if the index sliding out of the window
        2. maintain DLL in a descending order (montonic queue)
        3. push current node
        4. include max of curr. window
        """
        deq = deque()
        result = []
        # populating the queue from the k elements
        for i in range(k):
            while deq and nums[i] > deq[-1][0]:
                deq.pop()
            
            deq.append((nums[i], i))
        
        result.append(deq[0][0])
        print(nums)
        # starting from the window (size=k-1)
        for ind in range(k, len(nums)):
            current = nums[ind]
            # print(f"ind={ind}, DEQ ==>{deq} {deq[0][1]} < {ind - k + 1}, cond={deq[0][1] < (ind - k + 1)}")
            # this will remove max of 1 item
            while deq and deq[0][1] < (ind - k + 1):  # 1
                deq.popleft()
                print(f"ind={ind}, TRUE ==> ", deq)
            # print(f"deq={deq}, last={deq[-1]}, cond={deq and deq[-1][0] < current}")
            while deq and deq[-1][0] < current:  # 2
                deq.pop()
            deq.append((current, ind))  # 3
            print(f"ind={ind}, current={current}, cond={current >= k-1:}, deq={deq}, result={result}")
            result.append(deq[0][0])  # 4

        return result

    def maxSlidingWindow_deque_v2(self, nums: List[int], k: int) -> List[int]:
        """
        time complexity: O(n)
        space complexity O(n)
        starting from 0 instead of k-1, more simpler
        beats 28% in runtime
        """
        deq = deque()
        result = []

        for ind in range(0, len(nums)):
            current = nums[ind]

            if deq and deq[0][1] < (ind - k + 1):  # 1
                deq.popleft()

            while deq and deq[-1][0] < current:  # 2
                deq.pop()
            deq.append((current, ind))  # 3

            # window_size = k - 1
            if ind >= k-1:
                result.append(deq[0][0])  # 4
            print(f"ind={ind}, current={current}, cond={current >= k-1:}, deq={deq}, result={result}")

        return result


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.maxSlidingWindow_deque_v1(nums, k)


nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = Solution().maxSlidingWindow(nums, k)
print("RES ==>", res)
assert res == [3,3,5,5,6,7]

nums = [1]
k = 1
res = Solution().maxSlidingWindow(nums, k)
print("RES ==>", res)
assert res == [1]

nums = [1, -1]
k = 1
res = Solution().maxSlidingWindow(nums, k)
print("RES ==>", res)
assert res == [1, -1]


# nums = [1,3,1,2,0,5]
# k = 3
# res = Solution().maxSlidingWindow(nums, k)
# print("RES ==>", res)
# assert res == [3,3,2,5]



nums =[9,10,9,-7,-4,-8,2,-6]
k=5
res = Solution().maxSlidingWindow(nums, k)
print("RES ==>", res)
assert res == [10,10,9,2]
