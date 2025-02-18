from typing import List
import math

class Solution:
    """
    notes:
        - an array of distinct integers
        - sorted in ascending order
        - solution must run in O(logn) time
        - left <= right the equality here,
            along with &`mid-1` or `mid+1` is important since mid is already used
        - if number is close to 2^31, adding two numbers with these values could overflow (not in python)
            - mid is recommended to calculate it through 
                `(left+(right-left))//2` to avoid overflow
        - log2(n) = x, 2^x=n,
            ex: 16->8->4->2->1, 2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^8=16
    """
    def search_iterative(self, nums: List[int], target: int) -> int:
        """
        """
        left, right = 0, len(nums) - 1
        print(nums)
        while left <= right:
            mid = ((left + right) // 2)
            print(f"target={target}, L[{left}]={nums[left]}, MID[{mid}]={nums[mid]}, R[{right}]={nums[right]}")
            current = nums[mid]
            if target == current:
                return mid
            elif target > current:
                left = mid + 1
            else:  # target < mid
                right = mid - 1
            print(f"V222  left={left}, right={right}")
        print('-------------------------------------------')

        return -1

    def binary_search_recursive(self, l: int, r: int,
                                nums: List[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binary_search_recursive(m + 1, r, nums, target)
        return self.binary_search_recursive(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search_recursive(0, len(nums) - 1, nums, target)


    def search(self, nums: List[int], target: int) -> int:
        return self.search_iterative(nums)


nums = [-1,0,2,4,6,8]
target = 4
res = Solution().search(nums, target)
print("RES ==>", res)
assert res == 3

nums = [-1,0,2,4,6,8]
target = 3
res = Solution().search(nums, target)
assert res == -1


nums=[5,6]
target=5
res = Solution().search(nums, target)
assert res == 0

nums=[5]
target=5
res = Solution().search(nums, target)
assert res == 0

nums=[-1,0,3,5,9,12]
target=0
res = Solution().search(nums, target)
assert res == 1

