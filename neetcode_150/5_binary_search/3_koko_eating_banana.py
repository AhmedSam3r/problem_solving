from typing import List
import math
import heapq


class Solution:
    def minEatingSpeed_brute(self, piles: List[int], h: int) -> int:
        """
        time complexity(O(n^2))
        space complexity O(1)
        it 
        """
        min_val = float("inf")
        print(piles)
        for i in range(len(piles)):
            current = piles[i]  # (number of piles / hour)
            total_hrs = 0
            for j in range(len(piles)):
                total_hrs += math.ceil(piles[j]/current)
            print(f"piles[{i}]={piles[i]} TOTAL HOURS >> {total_hrs}, min_val={min_val}")
            if total_hrs <= h:
                min_val = min(0, current)

        return min_val

    def minEatingSpeed_binary_search_v1(self, piles: List[int], h: int) -> int:
        """
        time compleity O(Nxlog(M))
            - where n is the length of input array piles and
                m is the maximum number of bananas in a pile max(piles)
        time compleity O(N)
        notes:
            - tricky and smart question on how to use binary search
            - the crux of the problem is that we're sure that the rate of eating bannanas will be <= max(piles)
            - when we find that the total hours > h,
                that means our rate of eating is slow (small) so we have to shift to larger values
                `left = mid + 1`
            - we can brute force solution from 1 to max(piles) that would be O(n)
        """
        upper_limit = max(piles)
        rate_list = list(range(1, upper_limit+1))
        print(piles)
        print(rate_list)
        left, right = 0, len(rate_list) - 1
        min_speed = float("inf")
        while left <= right:
            mid = (left + right) // 2
            total_hrs = 0
            current_rate = rate_list[mid]
            for j in range(len(piles)):
                total_hrs += math.ceil(piles[j]/current_rate)

            if total_hrs <= h:
                min_speed = min(min_speed, current_rate)
            print(f"CURR={current_rate}, rate_listL[{left}]={rate_list[left]}, mid[{mid}]={rate_list[mid]}, rate_listR[{right}]={rate_list[right]}, total_hours={total_hrs}, h={h}, min_speed={min_speed}")
            if total_hrs <= h:
                right = mid - 1
            else:
                left = mid + 1

        return min_speed
    
    def minEatingSpeed_binary_search_v2(self, piles: List[int], h: int) -> int:
        """
        time compleity O(Nxlog(M))
             - where n is the length of input array piles and
                m is the maximum number of bananas in a pile max(piles)
        time compleity O(1)
        notes:
            - no need for rate list array, optimized in space
            - ensure that left=1 && `right=max(piles)` not `max(piles)-1`
            - this gives better runtime and memory 
                `mid = (left + right) // 2` than `l + ((r - l) // 2)` (wierd to me)
        """
        left, right = 1, max(piles)
        min_speed = float("inf")
        while left <= right:
            mid = (left + right) // 2
            total_hrs = 0
            current_rate = mid
            for j in range(len(piles)):
                total_hrs += math.ceil(piles[j]/current_rate)

            if total_hrs <= h:
                min_speed = min(min_speed, current_rate)
            if total_hrs <= h:
                right = mid - 1
            else:
                left = mid + 1

        return min_speed

    def minEatingSpeedHeap(self, piles, h):
        """
        - this approach flawed and does not work correctly
            - It prioritizes the largest pile at each step but does not globally minimize k.
            - The binary search method guarantees the smallest possible k, while this method does not always find it.
            - Thus, Binary Search is the best approach for solving this problem correctly.
        """
        max_heap = [-p for p in piles]  # Max heap (negative values)
        heapq.heapify(max_heap)
        print(piles)
        print("HEAP ==>", max_heap)
        while h > 0:
            largest = -1 * (heapq.heappop(max_heap))  # Get the largest pile
            k = math.ceil(largest / h)  # Compute minimum speed needed
            print(f"HEAP={max_heap}, largest={largest}, x={largest - k}")
            heapq.heappush(max_heap, -1 * (largest - k))  # Reduce and push back
            h -= 1  # Decrease hours left
        return -max_heap[0]  # Return the smallest speed needed

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.minEatingSpeedHeap(piles, h)



# piles = [3, 6, 7, 11]
# h = 8
# res = Solution().minEatingSpeed(piles, h)
# print("RES ==>", res)
# assert res == 4


piles = [1, 4, 3, 2]
h = 9
res = Solution().minEatingSpeed(piles, h)
print("RES ==>", res)
assert res == 2

piles = [25, 10, 23, 4]
h = 4
res = Solution().minEatingSpeed(piles, h)
assert res == 25
