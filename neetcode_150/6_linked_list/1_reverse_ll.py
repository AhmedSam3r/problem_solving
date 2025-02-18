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
    """
    time complexity: O(N)
    space complexity O(1)
    check `https://www.youtube.com/watch?v=G0_I-ZF0S38`

    """
    def reverseList_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity O(n)
        space complexity O(1)
        notes:
            - it worked yaay
            - it's considered two pointers problem
            - there's a simpler version
        """
        if not head or not head.next:
            return head
        new_head = ListNode(-1)
        while head and head.next:
            cur = head.next
            next = cur.next
            cur.next = ListNode(head.val)  # to avoid cyclic LL
            print(f"prev={head}, cur={cur}. next={next}")
            new_head_next = new_head.next
            # print(f"new_head_next={new_head_next}")
            new_head.next = cur
            # print(f"new_head.next={new_head.next}")
            # new_head.next= 4->3
            # cur.next.next= 4->3->(Here)
            # 4->3->(2->1) since they're pairs so it worked
            cur.next.next = new_head_next
            head = next

        if head:
            prev = new_head.next
            new_head.next = head
            new_head.next.next=prev

        print("new_head=>", new_head.next.next.next)
        return new_head.next

    def reverseList_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            print(f"V1 prev={prev}, cur={cur}. next={next}")
            cur.next = prev
            prev = cur
            cur = next
            print(f"V2 prev={prev}, cur={cur}. next={next}")

        print("HORRAY", prev)
        return prev

    def reverseList_recursive_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """a bit confusing """
        def reverse(cur, prev):
            if cur is None:
                return prev
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

        return reverse(head, None)

    def reverseList_recursive_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - this is a better exaplanation `https://www.youtube.com/watch?v=MRe3UsRadKw`
            clearing confusion of head.next.next and head.next code
        - current.next.next is the node pointer that's one in front of your current node. 
            When you say head.next.next = current, this is the "reversing" part. 
        - When you say head.next = null, this is deleting the old forward reference
            to prevent it from cyclic head
        - knowing that prev has the last head pointer that contains the new reversed list
            - example 1->2->3->4->5
            - return 5
            - 5->4
            - 5->4->3 and so on ...
        """
        if head is None or head.next is None:
            return head  # Base case: return the last node as new head

        # Recursive call to reverse the rest of the list
        new_head = self.reverseList_recursive_v2(head.next)

        # Reverse the two nodes
        head.next.next = head  # Make the next node point to current node
        head.next = None  # Disconnect current node from the rest

        return new_head  # Return new head of the reversed list

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseList_recursive_v2(head)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head.display()
print('---------------')
res = Solution().reverseList(head)
print('------------')
res.display()
print('------------')


# head2 = ListNode(1, ListNode(2))
# res = Solution().reverseList(head2)
# print('------------')
# res.display()


# head2 = ListNode(1)
# res = Solution().reverseList(head2)
# print('------------')
# res.display()
