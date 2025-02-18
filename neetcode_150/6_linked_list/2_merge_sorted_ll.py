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
            print(f"current={temp}")
            temp = temp.next
        print("--------------DISPLAY-----------------------------")

    def __str__(self):
        if self.val:
            return str(self.val)
        return "EMPTY"


class Solution:
    def mergeTwoLists_v1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = head = ListNode(-1)

        # list1.display()
        # list2.display()
        while list1 and list2:
            # print(f"head={head}, list1={list1}, list2={list2}")
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 if list1 else list2
        return prev.next

    def mergeTwoLists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        explain recursive in details `https://www.youtube.com/watch?v=bdWOmYL5d1g`
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeTwoLists_recursive(list1, list2)




head1 = ListNode(1, ListNode(2, ListNode(4)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
res = Solution().mergeTwoLists(head1, head2)
res.display()


# head1 = ListNode(1, ListNode(2))
# head2 = ListNode(1)
# res = Solution().mergeTwoLists(head1, head2)
# res.display()

# head1 = ListNode(1)
# head2 = None
# res = Solution().mergeTwoLists(head1, head2)
# res.display()


