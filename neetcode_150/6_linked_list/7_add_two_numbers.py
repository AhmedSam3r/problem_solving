import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self):
        temp = self
        print("--------------DISPLAY-----------------------------")
        while temp:
            print(f"current={temp}, address={id(temp)}")
            temp = temp.next
        print("--------------DISPLAY-----------------------------")

    def __str__(self):
        if self.val is not None:
            return str(self.val)
        return "EMPTY"


class Solution:
    def combine_digits(self, x, y):
        result = x * 10 + y
        return result

    def addTwoNumbers_multiple_pass(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity O(N)

        space complexity O(N)

        notes:
            - this solution worked but beats 5% in runtime

        """
        def reverse_head_recusive(head, num):
            if not head or not head.next:
                num[0] = self.combine_digits(num[0], head.val)
                return head, num

            _, num = reverse_head_recusive(head.next, num)
            num[0] = self.combine_digits(num[0], head.val)
            head.next.next = head  # this line was the missing line for me. why it works ?
            head.next = None
            return _, num

        # prev1, num1 = reverse_head(l1, [0])
        # prev2, num2 = reverse_head(l2, [0])
        prev1, num1 = reverse_head_recusive(l1, [0])
        prev2, num2 = reverse_head_recusive(l2, [0])
        res = num1[0] + num2[0]

        if res == 0:
            return ListNode(0)
        dummy = cur = ListNode(-1)
        while res > 0:
            num = res % 10
            cur.next = ListNode(num)
            res //= 10
            cur = cur.next

        print(f"n1={num1}, n2={num2}, res={res}")
        return dummy.next

    def addTwoNumbers_forward(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity O(max(m, n))

        space complexity O(1)

        notes:
            - 243+456=342+654
            - carry condition to consider last element carry in case of 
                last two elements summation >= 10
        """
        dummy = cur = ListNode(-1)

        carry = 0
        # carry condition to consider last element carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_val = val1 + val2 + carry
            res = total_val % 10
            carry = total_val // 10

            print(f"v1={val1}, v2={val2}, carry={carry}, res={res}")
            cur.next = ListNode(res)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def addTwoNumbers_recursion(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)

        next_node = self.addTwoNumbers_recursion(
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )
        return ListNode(val, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbers_forward(l1, l2)


def combine_digits(digits):
    result = 0
    for digit in digits:
        result = result * 10 + digit  # Shift left and add digit
    return result


# def combine_digits_reduce(digts):
#     from functools import reduce
#     number = reduce(lambda x, y: print(f"x={x}, y={y}, result={x * 10 + y}") or x * 10 + y, digits)
#     print("number", number)  # Output: 342


# l = [3, 4, 2]
# res = combine_digits(l)
# print("res==>", res)


# head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head1 = ListNode(2, ListNode(4, ListNode(7)))
head2 = ListNode(5, ListNode(6, ListNode(7)))
res = Solution().addTwoNumbers(head1, head2)
res.display()
