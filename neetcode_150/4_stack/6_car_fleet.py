from typing import List


class Solution:
    """
    - great expalanation for the problem here `https://www.youtube.com/watch?v=Pr6T-3yB9RM`
    - drawing the problem make the solution more clear
    """
    def carFleet_dummy(self, target: int, position: List[int], speed: List[int]) -> int:
        """dummy initital not working solution"""
        res = {}
        length = len(position)
        catch = {}
        for i in range(length):
            # t = d / s
            timee = (target - position[i]) // speed[i]
            res[timee] = res.get(timee, 0) + 1
            catch[position[i] + speed[i]] = 1  # catch.get(position[i] + speed[i], 0)  + 1

        print(f"catch={catch}, values={sum(catch.values())}")
        print(res)

        return sum(catch.values())

    def carFleet_counter(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time complexity: O(nlogn + n) = O(nlogn)
        space complexity O(n)

        notes:
            - in run time beats 99%, in memory beats 42%
            - two conditions when met then one fleet is formed else new fleet is added +1
                - if the position of the car is a head (>) of the previous car
                    (that's why we sort descindgly)
                - if the time of the previous car is less (<) the ahead car
        """
        lst = list(zip(position, speed))
        # start from right is better to make sure if a car is ahead of another car 
        # and interesect the earlier/previous cars will move with the same speed is the ahead car
        # sort by positiong desc
        lst.sort(key=lambda item: item[0], reverse=True)
        total_fleet = 0
        prev_arrival_time = -1
        print(lst)
        for pos, spd in lst:
            cur_arrival_time = (target - pos) / spd  # t = distance/speed
            print(f"pos={pos}, speed={speed}, curr={cur_arrival_time}, prev={prev_arrival_time}")
            if cur_arrival_time > prev_arrival_time:
                total_fleet += 1
                prev_arrival_time = cur_arrival_time

        return total_fleet

    def carFleet_stack(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time complexity: O(nlogn + n) = O(nlogn)
        space complexity O(n)

        notes:
            - in run time beats 91% (surprisngly good) and in memory beats 42%
            - using a decreasing monotonic stack
            - two conditions when met then one fleet is formed else new fleet is added +1
                - if the position of the car is ahead (>) of the previous car
                    (that's why we sort descindgly) or (start comparing from the second/ahead car to the previous one)
                - if the time of the previous car is less (<=) the ahead/next car,
                    that means it arrived earlier so they intersect at some point

        """
        lst = list(zip(position, speed))
        lst.sort(key=lambda item: item[0], reverse=False)
        stack = []
        print(lst)
        for pos, spd in lst:
            cur_arrival_time = (target - pos) / spd  # t = distance/speed
            print(f"pos={pos}, speed={spd}, curr={cur_arrival_time}, stack={stack}")
            while stack and stack[-1] <= cur_arrival_time:
                stack.pop()  # leaving the ahead car as if two cars intersect, the fleet moves with the speed of the ahead/leading car
            stack.append(cur_arrival_time)

        return len(stack)


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return self.carFleet_stack(target, position, speed)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
res = Solution().carFleet(target, position, speed)
print("RES ==>", res)
assert res == 3

target = 100
position = [0,2,4]
speed = [4,2,1]
res = Solution().carFleet(target, position, speed)
print("RES ==>", res)
assert res == 1
