

def threeSum_brute_force(nums):
    '''
    combining our knowledge of two sum and two sum sorted we can solve it
    '''
    length = len(nums)
    result = set()
    idx = list()
    result_list=[]
    print(nums)
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                res = nums[i] + nums[j] + nums[k]
                triplet = [nums[i], nums[j], nums[k]]
                triplet.sort()
                # https://stackoverflow.com/questions/13675296/how-to-overcome-typeerror-unhashable-type-list
                # since list is unhashable type, requires to be hashable (immutable)
                triplet = tuple(triplet)
                if res == 0 and triplet not in result:
                    result.add(triplet)
                    result_list.append(triplet)
                    idx.append((i, j, k))

    # print(list(zip(result_list, idx)))
    return list(result)


def threeSum(nums):
    """
    time complexity:
      O(n*n) + O(nxlogn) = O(n^2)
    space complexity:
        O(1) or O(n) if sorting create new array
    Notes:
        - a + b + c = 0
            i ==> nums[i] = a, so we don't want b to be similar to a, since a already is taken, we don't want duplicates
        - neetcode solution doesn't work because of the condition of nums[left]+nums[right] (> or <) 0 he made
        - it works when we compare three_sum: nums[i]+nums[left]+nums[right] (> or <) 0
        - since three_sum a+b+c=0 is valid comparison, or b+c (< or >) -a
        - in our case -a or 0 is target like two sum sorted problem

        - what about the case where you have an array like [-3,-3,0,3,6] ?
            In this case, both [-3,-3,6] and [-3,0,3] are valid. (if case we ignored duplicates) as he mentioned https://www.youtube.com/watch?v=jzZsG8n2R9A
            If you skip the second -3, you will miss out on [-3,0,3] as one of the triplets.
            but the idea yo
        - you ignore duplicates after complete iteration with i over nums[i], so every combination is selected with l & r
        -  `while nums[left] == nums[left-1] and left < right:`
                it works without the following optimization `while nums[right] == nums[right+1] and left < right`
                why without ? as it's guranteed to avoid duplicates since left is incremented, so every combination is uniue
        - combining our knowledge of two sum and two sum sorted we can solve it
                i delayed the problem as i thought there was a better solution
                be confident the length you noticed that its small 3 <= nums.length <= 3000
                so you could safely assume that it could be of n*n as you thought earlier        


    """
    length = len(nums)
    nums.sort()
    result = []
    # print("nums::", nums)
    for i in range(length):
        left, right = i + 1, length - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # print(f"{i}. nums[i]={nums[i]}")
        # print(f"combinations {result}")
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            # print(f"left={left}: {nums[left]}, right={right}: {nums[right]}")
            # print("three_sum ==>", three_sum)
            if three_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1  # neetcode didn't add this one but it made sense and it was correct
                # print("WEEEEEEEEE")
                # to handle case like nums:: [-2, 0, 0, 2, 2]
                # since already uniqe combination of i, l is taken
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                # it works without the following optimization
                # but it's guranteed to avoid duplicates since l is updated
                # so every combination is uniue
                # while nums[right] == nums[right+1] and left < right:
                    # right -= 1
            elif three_sum > 0:
                right -= 1
            else:
                left += 1
    return result


# nums = [-1, 0, 1, 2, -1, -4]
# r = threeSum(nums)
# print("r ==>", r)

# nums = [-2,0,0,2,2]
# r = threeSum(nums)
# print("r ==>", r)

nums =[-1,0,1,2,-1,-4,-2,-3,3,0,4]
r = threeSum(nums)
print("r ==>", r)



nums = [-3,-3,0,3,6]
r = threeSum(nums)
print("r ==>", r)


nums = [0,1,1]
r = threeSum(nums)
print("r ==>", r)


nums = [0,0,0]
r = threeSum(nums)
print("r ==>", r)


