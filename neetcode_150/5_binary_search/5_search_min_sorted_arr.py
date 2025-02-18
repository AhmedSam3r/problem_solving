from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        time complexity O(2log(N)) = O(log(N))
        space complexity O(1)
        notes:
            - the problem says algorithm O(log(N)) so its binary search we go to
            - usually the brute solution for that is O(n) and you will be asked to improve it
            - two pass solution
            - it's a complex problem as it contains two sub problems
                - using binary search to find the pivot element at index k (where items before/after pivot are sorted  ascendingly nums[k-1]<=pivot<=)
                - using binary search to find the target at index i (mid)
            - what made the problem solvable to me is the previous problem
            - this made the solutions works `target > nums[pivot_index]` and `target <= nums[-1]:`
                - in cases such as the following where array the target and the pivot in opposite directions
                    so you have to make sure of the array boundaries to move in the right direction
                    nums=[3,1], target=3, pivot=nums[1]=1 and target=3
                    nums=[5,1,3], target=5, pivot=nums[1]=1 and target=5
            - solution beats 100% in runtime
        """
        def findMin(nums: List[int]) -> int:
            rotated = nums[0] > nums[-1]
            if not rotated:
                return 0
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == nums[right]:
                    return mid
                elif nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
        
        print(f"nums={nums}, target={target}")
        if len(nums) == 1:
            idx = 0
            return idx if nums[idx] == target else -1

        pivot_index = findMin(nums)
        print("pivot_index ==>", pivot_index)
        if nums[pivot_index] == target:
            return pivot_index
        elif target > nums[pivot_index] and target <= nums[-1]:
            left = pivot_index
            right = len(nums) - 1
        else:  # target < nums[pivot_index]:
            left = 0
            right = pivot_index
        print(f"nums[{left}]={nums[left]},, nums[{right}]={nums[right]}")
        while left <= right:
            mid = (left + right) // 2
            print(f"numsL[{left}]={nums[left]},, numsR[{right}]={nums[right]},, numsM[{mid}]={nums[mid]}")
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search_another_sol(self, nums: List[int], target: int) -> int:
        """
        not my solutin but i was thinking of sth like that as the sol has 4 conditions giving all the possibilities per each step
        confusing and not easy to digiest
        """
        l, r = 0, len(nums)-1
        
        # checks to move: ex. [4,5,6,7,0,1,2]
        # if on left sorted:
        # then on your left you should have only smaller points
        # and on your right you either have larger OR smaller than the leftmost

        # if on right: 
        # then on your left you have either smaller OR larger than rightmost
        # on your right you have only larger points

        while l <= r:
            m = (r+l) // 2 # avoid overflow
            print(l,m,r)
            #tip: don't forget equals sign
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1 


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = Solution().search(nums, target)
assert res == 4


nums = [4,5,6,7,0,1,2]
target = 3
res = Solution().search(nums, target)
assert res == -1

nums = [1]
target = 0
res = Solution().search(nums, target)
assert res == -1


nums = [1,2,3,4,5]
target = 4
res = Solution().search(nums, target)
print("REs ==>", res)
assert res == 3

nums = [3,1]
target = 3
res = Solution().search(nums, target)
print("REs ==>", res)
assert res == 0


nums=[5,1,3]
target = 5
res = Solution().search(nums, target)
print("REs ==>", res)
assert res == 0


