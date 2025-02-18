
def containsDuplicate_set(nums):
    '''
    Time Complexity: O(n) where n is the length of nums, since converting the list to a set requires O(n) time.
    Space Complexity: O(n) for storing the elements in the set.
    Set is built on top of a hash table
    '''
    # unique = set()
    # for num in nums:
    #     if num in unique:
    #         print("num ==>", num)
    #         return True
    #     unique.add(num)
    # more efficient replace it with
    unique = set(nums)
    print(len(unique), len(nums))
    return len(unique) != len(nums)


def containsDuplicate_hashmap(nums):
    unique = {}
    for num in nums:
        if unique.get(num, 0) == 1:
            return True
        unique[num] = 1

    return False


def containsDuplicate_sorting(nums: list):
    '''
    Time Complexity: O(n log n) due to the sorting step.
    Space Complexity: O(1) or O(n) depending on the sorting algorithm used. Some languages use in-place sorting, while others might allocate extra memory.
    '''
    nums.sort()
    for i in range(0, len(nums), 2):
        if nums[i] == nums[i+1]:
            print("nums is ",nums[i])
            return True

    return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums=[1,2,3,1]
r = containsDuplicate_set(nums)
print("r ==> ", r)
nums = [1, 2, 3, 4]
r = containsDuplicate_set(nums)
print("r ==> ", r)


nums = [1, -1, -3, 3, 3, 4, 3, 2, 4, 2]
r = containsDuplicate_hashmap(nums)
print("r ==> ", r)
nums = [1, 2, 3, 4]
r = containsDuplicate_hashmap(nums)
print("r ==> ", r)


nums = [1, -1, -3, 3, 3, 4, 3, 2, 4, 2]
r = containsDuplicate_sorting(nums)
print("SORTING r ==> ", r)
nums = [1, 2, 3, 4]
r = containsDuplicate_sorting(nums)
print("r ==> ", r)
