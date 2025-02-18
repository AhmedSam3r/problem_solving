import bisect

def twoSum_brute_force(numbers, target):
    '''
    Your solution must use only constant extra space,
        so it doesn't want us to use hashmap or any storage
    NOOOOTE read the problem well, it mentioned being 1-indexed
    '''
    ptr1 = 0
    while ptr1 < len(numbers):
        ptr2 = ptr1 + 1
        while ptr2 < len(numbers):
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1+1, ptr2+1]
            ptr2 += 1
        ptr1 += 1


def two_sum_binary_search(numbers, target: int):
    '''
    need to understand bisect and how it works
    time complexity O(n log n)
    space complexity o(1)
    ??? 
    '''
    for i in range(len(numbers)):
        complement = target - numbers[i]
        # Perform binary search in the right part of the array (i+1 to end)
        complement_index = bisect.bisect_left(numbers, complement, i + 1)
        if complement_index < len(numbers) and numbers[complement_index] == complement:
            return [i + 1, complement_index + 1]


def binary_search(lst, key):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"left={left}, right={right}, mid={mid}")
        if key == lst[mid]:
            return mid
        if key > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def twoSum_binary_serch(numbers, target):
    '''
    since the array is already sorted we can use binary search
    R===> [2, 5]
    R===> [0, 1]
    R===> [0, 1]
    '''
    print(numbers)
    for i in range(len(numbers)):
        complement = target - numbers[i]
        # print(f"s[i]={numbers[i]}, search for {complement}")
        idx = binary_search(numbers, complement)
        if idx != -1:
            return i, idx
    return [-1, -1]


def two_sum_two_points(numbers, target):
    '''
    similar to using binary search idea
    space complexity O(1)
    space complexity O(n)
    '''
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-indexed result

        elif target > current_sum:
            left += 1

        else:
            right -= 1

def twoSum(*args):
    # r = twoSum_brute_force(*args)
    r = twoSum_binary_serch(*args)
    return r

numbers = [1, 2, 3, 4, 5, 6]
target = 9  # index 2, 5
r = twoSum(numbers, target)
print("R===>", r)

numbers = [-1,0]
target = -1
r = twoSum(numbers, target)
print("R===>", r)

numbers = [2,7,11,15]
target = 9
r = twoSum(numbers, target)
print("R===>", r)

