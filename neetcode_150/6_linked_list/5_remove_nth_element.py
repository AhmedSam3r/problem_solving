
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
    def removeNthFromEnd_two_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        time complexity: O(N)
        
        space compelxity: O(1)

        notes:
            - special case when index=0
            - beats 100% in runtime
        
        """
        def get_nth_index(head, n):
            cur, count = head, 0
            while cur:
                count += 1
                cur = cur.next
            return count - n
        index, nth = 0, get_nth_index(head, n)
        prev = cur = head
        while cur:
            print(f"index={index}, nth={nth}, prev={prev}, cur={cur}")
            # special case
            if nth == index and index == 0:
                print(f"SPEC ==> cur={cur}, prev={prev}")
                head = head.next
                print(f"SPEC ==> cur={cur}")
                break
            elif nth == index:
                prev.next = cur.next
                break
            else:
                index += 1
                prev = cur
                cur = cur.next
        return head

    def removeNthFromEnd_one_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        notes:
            - video expalanation `https://www.youtube.com/watch?v=XVuQxVej6y8`
        """
        dummy = ListNode(-1, head)
        left, right = dummy, dummy.next
        # notice that we skip by so if n=3 it's like passing over 4 indexes (n+1)
        # n to keep distance between left and right = n
        # +1 to skip the dummy note
        while n > 0 and right:
            right = right.next
            n -= 1
        print(f"RIGHT={right}")

        while right:
            left, right = left.next, right.next
        print(f"left={left}, right={right}")
        # remove nth element
        left.next = left.next.next
        # why we use dummy.next ?
        # in case of index = 0 to remove the head of LL
        return dummy.next

    def remove_recursion(self, head: ListNode, n: list):
        if not head:
            return None

        head.next = self.remove_recursion(head.next, n)
        n[0] -= 1
        if n[0] == 0:
            return head.next
        return head

    def removeNthFromEnd_recursion(self, head, n):
        """
        we pass it as a list to pass the element by reference
        """
        return self.remove_recursion(head, [n])

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.removeNthFromEnd_recursion(head, n)

head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n=2
res = Solution().removeNthFromEnd(head1, n)
res.display()

# not working
head1 = ListNode(1, ListNode(2))
n=2
print("NOOOT WORKING")
res = Solution().removeNthFromEnd(head1, n)
res.display()

head1 = ListNode(1, ListNode(2, ListNode(3)))
n=2
res = Solution().removeNthFromEnd(head1, n)
# res.display()

head1 = ListNode(1, ListNode(2, ListNode(3)))
n=3
print("NOOOT WORKING")
res = Solution().removeNthFromEnd(head1, n)
# res.display()



head1 = ListNode(1, ListNode(2))
n=1
res = Solution().removeNthFromEnd(head1, n)
# res.display()


head1 = ListNode(1)
n=1
res = Solution().removeNthFromEnd(head1, n)
assert res is None
