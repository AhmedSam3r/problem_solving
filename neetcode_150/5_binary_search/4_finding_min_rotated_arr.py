from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """"
        time complexity O(log(N))
        space complexity O(1)
        notes:
            - passes 100% in runtime, i'm happy with my solution
            - it uses lower bound approach
            - `right = mid` this part what make the solution correct, why ?
                - as there're cases where mid is the answer so we don't want to skip that index
                - ex [3, 1, 2] 
                    - numsL[0]=3 numsR[2]=2, mid[1]=1,
                    - numsL[0]=3 numsR[1]=1, mid[0]=3,
                    - numsL[1]=1 numsR[1]=1, mid[1]=1,
            - also instead of `nums[mid] == nums[right]` 
                - we can replace it with condition `left < right` 
                - and returns nums[left] (or nums[right])
        """
        rotated = nums[0] > nums[-1]
        if not rotated:
            return nums[0]
        left, right = 0, len(nums) - 1
        print(nums)
        while left <= right:
            mid = (left + right) // 2
            print(f"nums[{left}]={nums[left]} numsR[{right}]={nums[right]}, mid[{mid}]={nums[mid]},")
            if nums[mid] == nums[right]:
                return nums[mid]
            # in case nums[mid] > nums[right]
            # we are sure that the left sorted array has values greater than the right sorted array
            # that means at least nums[mid] > nums[right], so nums[mid] will never be the minimum
            # so it's safe to skip mid + 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: # nums[mid] < nums[right]
                right = mid  # this make the upper bound works

    def findMin_binary_search(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res



nums = [3,4,5,1,2]
res = Solution().findMin(nums)
assert res == 1


nums = [4,5,6,7,0,1,2]
res = Solution().findMin(nums)
assert res == 0


nums = [11,13,15,17]
res = Solution().findMin(nums)
assert res == 11

nums = [3,1,2]
res = Solution().findMin(nums)
assert res == 1

