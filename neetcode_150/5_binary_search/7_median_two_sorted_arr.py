from typing import List


class Solution:
    """
    we can solve it using two pointers O(M+N)
    """
    def findMedianSortedArrays_v2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        time complexity: O(log(min(M,N)))
        as we're running binary search on the smallest
        space complexity: O(1)
        notes:
        - neetcode really explained it well `https://www.youtube.com/watch?v=q6IEA26hvXc`
        - we can use two pointers approach until we skip number of half_partition
        - passed 2087 / 2096 as it because of an empty list
        - read constraints well, we should handle empty lists
                `0 <= m <= 1000` && `0 <= n <= 1000`


        """
        def median_of_single_list(nums):
            mid = len(nums) // 2
            return nums[mid] if len(nums) % 2 == 1 else (nums[mid - 1] + nums[mid]) / 2 
        print('------------------------------------')
        # base case condition to handle n=0 or m=0
        if not nums1:
            return median_of_single_list(nums2)
        if not nums2:
            return median_of_single_list(nums1)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = len(nums1), len(nums2)
        half_partition = (A+B+1)//2  # +1 to handle floor division in odd/even nums
        left, right = 0, A

        print(f"half_partition={half_partition}\nnums1={nums1}\nnums2={nums2}")
        # while left <= right:  # caused issue in A=[3], B[1,2]
        while True:
            A_partition_idx = (left + right) // 2
            # our right partition contains the remaining of half the size of array
            # Ex. total=13, half=6, A_partition_idx=2(2+1 as zero indexed), B_partition_idx=3
            B_partition_idx = half_partition - (A_partition_idx + 1)

            # handling out of bound elements -inf [...] inf
            # if A_partition_idx > 0 means it's still inbound
            # getting A partition [1,2,3,4]  --> [L(3),R(4)]
            A_left = nums1[A_partition_idx] if (A_partition_idx >= 0) else float("-inf")
            A_right = nums1[A_partition_idx + 1] if (A_partition_idx + 1) < A else float("inf")

            # # getting B partition [1, 2, 3, 4, 5, 6, 7, 8] --> [L(3),R(4)]
            B_left = nums2[B_partition_idx-1] if (B_partition_idx-1) >= 0 else float("-inf")
            B_right = nums2[B_partition_idx] if (B_partition_idx) < B else float("inf")
            print(f"A_left={A_left}, A_right={A_right}, B_left={B_left}, B_right={B_right}")
            print(f"Apartition={A_partition_idx}, B_partition_idx={B_partition_idx}, &&& {A_left} <= {B_right} and {B_left} <= {A_right}, COND={A_left <= B_right}&&{B_left <= A_right}")

            # condition is true satisfies that we found the correct partition
            # do cross checking to check the next element and ensures correct ordering
            if A_left <= B_right and B_left <= A_right:
                if (A + B) % 2 == 0:
                    # max to ensure last element in the left partition
                    # min to ensure first element in the right partition
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                else:
                    return max(A_left, B_left)
            elif A_left > B_right:
                right = A_partition_idx - 1
            else:
                left = A_partition_idx + 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedianSortedArrays_v2(nums1, nums2)





nums1=[1,2,3,4,5,6,7,8]
nums2=[1,2,3,4]
res = Solution().findMedianSortedArrays(nums1, nums2)
print("RES ==>", res)
assert res == 3.5

nums1 = [1,2]
nums2 = [3]
res = Solution().findMedianSortedArrays(nums1, nums2)
print("RES ==>", res)
assert res == 2.0


nums1 = [1,3]
nums2 = [2,4]
res = Solution().findMedianSortedArrays(nums1, nums2)
print("RES ==>", res)
assert res == 2.5

nums1 = []
nums2 = [2,3]
res = Solution().findMedianSortedArrays(nums1, nums2)
print("RES ==>", res)
assert res == 2.50000
