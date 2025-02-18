from typing import List


def productExceptSelf_brute(nums):
    result = []
    print("nums", nums)
    for i in range(len(nums)):
        product = 1
        for j in range(0, len(nums)):
            if j == i:
                continue
            print(f"i={i} nums[i] = {nums[i]}, j={j}, nums[j] ", nums[j])
            product *= nums[j]
        print("PRDUCT = ", product)
        result.append(product)
    return result


def productExceptSelf_error_try(nums):
    product = 1
    has_zero = False
    exist = False
    for num in nums:
        if num == 0:
            has_zero = True
            continue
        exist = True
        product *= num

    # means only zeros
    if exist is False:
        product = 0
    print("PROD ==>", product)
    for i in range(len(nums)):
        print("i==>", i)
        if has_zero and nums[i] != 0:
            nums[i] = 0
        elif has_zero and nums[i] == 0:
            nums[i] = product
        else:
            nums[i] = product // nums[i]

    return nums

class Solution:
    def productExceptSelf_brute_force(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            temp = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue
                temp *= nums[j]
            res.append(temp)

        return res
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time complexity:
            O(n)
        space complexity:
            O(n), in this case the output array isn't considered as an extra space
        how it works?
            nums   = [1,  2, 3, 4]
            prefix = [1,  1, 2, 6]
                - start_index=0 populate it from left to right
                - first index value will be 1, since the prefix of index 0 doesnot exist so prefix=1
            suffix = [24, 12, 4, 1]
                - start_index=3 populate it from right to left
                - last index value will be 1, since the suffix of index 3 doesnot exist so suffix=1
            result = [1*24, 1*12, 2*4, 6*1]
            result = [24, 12, 8, 6]
        Notes:
            the tricky part in this problem that we can't use division or extra space
            so we compress prefix and suffix into one array

        """
        result = []
        prefix = 1
        for i in range(0, len(nums)):
            result.append(prefix)
            prefix = prefix * nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]
            print(f"arr:{nums[i]} & res:{result[i]} and suffix is {suffix}")
        
        print("prefix ==>", result)
        return  result
    
    def product_except_self_divison(selfnums):
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        output = [0] * len(nums)
        # if we've more than one zero therefore we will have all the array to be mutliplied by 0
        if zero_count > 1:
            return output

        for i in range(len(nums)):
            # if zero_count > 0, so multiplications will be 0
            # our array is populated with 0 already
            if zero_count == 0:
                output[i] = total_product // nums[i]
            elif nums[i] == 0:
                output[i] = total_product

        return output




# nums = [-1,0,1,2,3]
# r = productExceptSelf_brute(nums)
# print("r ==>", r)

nums = [1, 2, 4, 6]
r = productExceptSelf_brute(nums)
print("r ==>", r)

nums = [0, 8, 0]  # fails
r = productExceptSelf_brute(nums)
print("r ==>", r)
