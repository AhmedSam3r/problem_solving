from typing import List


class Solution:
    def findDuplicate_v1(self, nums: List[int]) -> int:
        """doesn't completely work with large solutions give O(N)"""
        if len(nums) == 2:
            return nums[0]

        slow_idx, fast_idx = 0, 2
        print("hE")
        i, j = 0, 1
        while True:
            if slow_idx >= len(nums):
                slow_idx = i
                i += 1
                if i >= len(nums):
                    i = 0

            if fast_idx >= len(nums):
                fast_idx = j
                j += 1
                if j >= len(nums):
                    j = 0
            slow = nums[slow_idx]
            fast = nums[fast_idx]
            print(f"slow[{slow_idx}]={slow}, fast[{fast_idx}]={fast}")
            if slow == fast and slow_idx!=fast_idx:
                print(f"FOUND {slow}={fast}, slow_idx={slow_idx} & fast_idx={fast_idx}")
                break
            slow_idx += 1
            fast_idx += 2
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return fast


    def findDuplicate_v2(self, nums: List[int]) -> int:
        """
        time complexity O(N)

        space complexity O(1)
        notes:
            - this solution will only works if array values between 1 and N which is size of array
            - this problem requires linear time and constant complexity,
                so we can't use dictionnary
            - it's called Floyd's Tortoise and Hare (Cycle Detection)
            - to create a linkedlist we take the number as an index to next pointer
                and same applies to fast
                - ex [1, 3, 4, 2, 2], slow=0
                - nums[0] = 1
                - nums[1] = 3
                - nums[3] = 2
                - nums[4] = 2
            - excellent video expalantion `https://www.youtube.com/watch?v=wjYnzkAhcNk`
                - For the graph starting from 2:32, I think the outgoing pointer from node 0 should point at node 1 first. 
                And then node 1 will point to node 3.
                - Skipping the node that is pointed by 0 will struggle at the situation that element in 0 index is already the anwser.

        """
        # fast is a must to be equals 0 at the beginning
        slow = fast = 0
        while True:
            slow = nums[slow]
            # fast moves 2 time faster
            # fast = nums[fast]
            # fast = nums[fast]
            fast = nums[nums[fast]]
            print(f"slow={slow}, fast={fast}")
            if slow == fast:
                break
        
        slow2 = 0
        print("@@@@@@@@@")
        print(f"slow1={slow}, slow2={slow2}")
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            print(f"slow1={slow}, slow2={slow2}")
            if slow == slow2:
                return slow


    def findDuplicate(self, nums: List[int]) -> int:
        return self.findDuplicate_v2(nums)


nums = [1,3,4,2,2]
res = Solution().findDuplicate(nums)
assert res == 2

# nums = [3,1,3,4,2]
# res = Solution().findDuplicate(nums)
# assert res == 3

# nums = [3,3,3,3,3]
# res = Solution().findDuplicate(nums)
# assert res == 3

# nums = [8,1,1,9,5,4,2,7,3,6]
# res = Solution().findDuplicate(nums)
# assert res == 1


# nums = [1,1,2]
# res = Solution().findDuplicate(nums)
# assert res == 1

