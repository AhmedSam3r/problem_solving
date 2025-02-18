from typing import List


class Solution:
    """
    the key solution is understanding how to calculate the water
    we need the left height be always greater than or equal the right height
        : min_height = min(max_left[i], max_right[i]
    to calculate amount of water for each index
        : min_height - height[i]
    refer to:
    https://www.youtube.com/watch?v=ZI2z5pq0TqA explains concept of maxL and maxR arrays so well
    https://youtu.be/4Y7irecfvLM?t=689 this made me understand the idea of how two pointers work here


    """
    def trap(self, height: List[int]) -> int:
        """
        my solution is failing when left has higher bars than right and there is any gap in between,
        it cannot calculate water `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
            in this part [3,2,1,2], can't calculate water at index whose value=1
        i was trying to use slide
        """
        left, right = 0, 1
        total_water = 0
        max_left = left
        while (left < right < len(height)):
            if height[left] == 0:
                left += 1
                right += 1
                continue
            elif height[right] == 0:
                right += 1
                continue
            print(f"heigh[{left}]={height[left]} && height[{right}]={height[right]}")
            max_left = max(max_left, left)
            if (
                height[right] >= height[left]
                # or (height[right] == height[left] and height[right-1] == 0)
            ):
                # calculate area
                # print("TOT==>", (min(height[left], height[right]) * (right - left - 1)))
                temp_l, temp_r = right-1, right
                temp_max = min(height[left], height[right])
                while temp_l > left:
                    print(f"height[{temp_l}]={height[temp_l]} && height[{temp_r}]={height[temp_r]}, temp_max={temp_max}, total={(temp_max - height[temp_l])}")
                    total_water += (temp_max - height[temp_l])
                    temp_l -= 1
                left = right
                right = left + 1
            else:
                right += 1

            print("TOTAL WATER ==>", total_water)
            print('--------------------------------')
        return total_water

    def trap_extra_memory(self, height: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)
        beats:
            beats 12% in runtime and beats 20% in memory
        (1) get max left array
        (2) get max right array
        (3&4) for the current index calculate:
            the min of (the greatest left height and the greatest right height)
            this will get us the height that can trap water
            then subtract the current of height to know the amount of water trapped
                min(max_left[i], max_right[i]) - height[i]

        """
        max_left, max_right = ([0] * len(height)), ([0] * len(height))
        for i in range(1, len(height)):
            max_left[i] = max(height[i-1], max_left[i-1])
        print("height    ==>", height)
        print("MAX LEFT  ==>", max_left)
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(height[i+1], max_right[i+1])
        print("MAX right ==>", max_right)
        total = 0
        for i in range(len(height)):
            total += max(0, min(max_left[i], max_right[i]) - height[i])

        return total

    def trap_two_pointers(self, height: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        beats:
            beats 43% in runtime and beats 31% in memory
        Notes:
            - two pointer solution is confusing as we can miss some heights, so how does it work ?
            - unlike the maxL and maxR array which compute every index based on the previous maxL and maxR values
            - this made me understand the idea of how two pointers work here https://youtu.be/4Y7irecfvLM?t=689
            - if you're bounded by a left boundar and a right boundary, you can take things greedily 
                as you know for sure, water can be trapper, i don't care about the next element
                    i care about my current position. this the crux of the problem


        """
        left = total = 0
        right = len(height) - 1
        left_max = right_max = 0

        while left < right:
            
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # since left smaller, try increment hoping find better height
            if left_max <= right_max:
                current = left
                left += 1
            else:  # left_max > right_max
                current = right
                right -= 1
            # to calculate amount of water trapped
            min_height = min(left_max, right_max)
            # taking max ensure that our result will be > the current so result will be > 0
            total += min_height - height[current]

        return total

# height = [4, 2, 0, 3, 2, 5]
# res = Solution().trap_extra_memory(height)
# print("RES ==>", res)


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# res = Solution().trap_extra_memory(height)
# print("RES ==>", res)


height = [4, 2, 0, 3, 2, 5]
res = Solution().trap_two_pointers(height)
print("RES ==>", res)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = Solution().trap_two_pointers(height)
print("RES ==>", res)

