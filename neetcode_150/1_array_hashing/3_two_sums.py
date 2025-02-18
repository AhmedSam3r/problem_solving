from typing import List

# how to search in a smart way
# how to utilize hashmap in searching
# hint target is the total sum two numbers, complement = target - other_number


def twoSum_brute_force(nums: List[int], target: int) -> List[int]:
    '''
    Time Complexity: O(n²) — You check all pairs.
    Space Complexity: O(1) — No extra space needed.
    '''
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return -1, -1


def twoSum_hashmap(nums: List[int], target: int) -> List[int]:
    '''
    Time Complexity: O(n) — One pass through the array.
    Space Complexity: O(n) — Additional space for the hash map.
    be careful of when to save complement and when to search by num
    '''
    # [3,2,4]
    result = {}
    for ind, num in enumerate(nums):
        complement = target - num
        # to avoid 0 indexed being discarded
        if result.get(num, None) is not None: 
            return [ind, result[num]]
        result[complement] = ind

    return []


def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    twoSum is different from twoSum_hashmap in the way of choosing 
    which key to save and how to search by complement
    '''
    prev_map = {}

    for i in range(len(nums)):
        num = nums[i]
        key = target - num
        print(prev_map)
        if prev_map.get(key, None) is not None:
            print(prev_map)
            return [prev_map[key], i]
        prev_map[num] = i
    return []


def binary_search(nums, left, right, target):
    while left < right:
        mid = (left+(right-left))//2
        if nums[mid][0] == target:
            return mid
        elif nums[mid][0] >= left:
            mid = left + 1
        else:
            mid = right - 1

        return -1


def two_sum_binary_search(nums, target):
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()  # Sort based on the numbers

    for i in range(len(indexed_nums)):
        complement = target - indexed_nums[i][0]
        # Perform binary search on the right part of the array
        j = binary_search(indexed_nums, i + 1, len(indexed_nums) - 1, complement)
        if j != -1:
            return [indexed_nums[i][1], indexed_nums[j][1]]

    return []  # Return an empty list if no solution is found


# nums = [2,7,11,15]
# target = 9
# r = twoSum_brute_force(nums, target)
# print("r = ", r)

# nums = [2, 3, 4]
# target = 6
# r = twoSum_brute_force(nums, target)
# print("r = ", r)



# nums = [2,7,11,15]
# target = 9
# r = twoSum_hashmap(nums, target)
# print("hashmap r = ", r)

nums = [2, 3, 4]
target = 6
r = twoSum(nums, target)
print("hashmap r = ", r)


