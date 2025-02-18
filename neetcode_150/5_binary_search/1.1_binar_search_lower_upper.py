from typing import List


class Solution:
    """
    - In case of a repeated number `https://www.youtube.com/watch?v=6-15eccc6ek`
    - explaining the concept of lower and upper bound using binary search
    """
    def search_lower_bound(self, nums: List[int], target: int) -> int:
        """finds the first index of the target"""
        lo, hi = 0, len(nums)

        while lo < hi:
            m = lo + ((hi - lo) // 2)
            if nums[m] >= target:  # notice that nums[m] > target greatehi than and equal both
                hi = m
            else:
                lo = m + 1
        return lo if (lo < len(nums) and nums[lo] == target) else -1

    def search_upper_bound(self, nums: List[int], target: int) -> int:
        """
        finds the last index of the target
        why lo -1 ?
        - `lo` points to the first index greater than target. 
        - To get the index of the last occurrence of the target, we need to check the element just before l, i.e., l - 1.
            - Ex [-1, 0, 2, 4, 6, 8], target=4 lo=4, nums[4]=6, nums[4-1]=4 == target
        """
        lo, hi = 0, len(nums)

        while lo < hi:
            m = lo + ((hi - lo) // 2)
            if nums[m] > target:  # notice that nums[m] > target greatehi than only
                hi = m
            else:
                lo = m + 1

        return lo - 1 if (lo and nums[lo - 1] == target) else -1


nums = [-1,0,2,4,6,8]
target = 4
res = Solution().search_lower_bound(nums, target)
print("RES ==>", res)
assert res == 3


nums = [-1,0,2,4,6,8]
target = 4
# upper is failing, maybe work return lo-1 if (lo and nums[lo-1] == target) else -1
res = Solution().search_lower_bound(nums, target)
print("RES ==>", res)
assert res == 3

nums = [-1,0,2,4,6,8]
target = 4
# upper is failing, maybe work return lo-1 if (lo and nums[lo-1] == target) else -1
res = Solution().search_upper_bound(nums, target)
print("RES ==>", res)
assert res == 3
