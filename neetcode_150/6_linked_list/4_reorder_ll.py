
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
    def reorderList_v1(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        time complexity: O(n)

        space complexity: O(n)

        notes:
            - this solution worked
            - runtime
                - runtime in commented while loop beats 25%
                    - Extra Write Operation `next=head.next`
                    - Breaking the Linked List Adds Overhead `head.next=None`
                    - Extra Variable `next`
                - when i changed the first while loop, it beats 100%

            - the concept of pointers and LL needs more practice of me as I forgot
              how to move pointer correctly

            - what made it work is the following:
                - `prev = head = ListNode(-1)`
                - then every time you state that `head.next=something`
                - then you move `head = head.next`
                - then you satet that `head.next=somethingelse`
                - so in that way you're moving head to the right location 
                    and store the value you want into its next location.
                    that makes the solution works correctly and prev keeps track of the next items

        """
        if not head.next:
            return head
        save = list()

        while head:
            # next = head.next
            # head.next = None  # Breaking the linked list connections
            save.append(head)
            # head = next  # Move to the next node
            head = head.next

        i, j = 0, len(save) - 1
        if i == j:
            return head
        prev = head = ListNode(-1)
        while i <= j:
            print(f"head={save[i]}, tail={save[j]}")
            head.next = save[i]
            head = head.next

            if i != j:
                head.next = save[j]
                head = head.next

            i += 1
            j -= 1

        head.next = None

        print(f"prev={prev} ,,, head={head}")
        head = prev.next
        return head

    def reorderList_recurse_v1(self, head: Optional[ListNode]) -> None:
        def recurse(tail, head):
            if not tail.next:
                print(f"RETURN HERE={tail}")
                return tail
            

            new_tail = recurse(tail.next, head)
            print(f"head={head}, tail={tail}", end=' ')
            next = head.next
            head.next = new_tail
            print(f", next={next}")
            head = head.next  # it doesn't take effect, each time head addr is going to be sent
            head = tail
            
            return head
        # prev = head = ListNode(-1)
        dummy = ListNode(-1)
        dummy.next = head
        res = recurse(head, head)
        print(f"--- FINAL ---, head={head}, res={res}, dummy={dummy.next}")
        return dummy.next

    def reorderList_inplace(self, head: Optional[ListNode]) -> None:
        """
        time complexity: O(n)

        space complexity: O(1)
        notes:
            - beats 50% in runtime using my solution `cur.next.next` (slow than the previous one)
            - beats 30% in runtime using the neetcode suggest approachs (slower than my solution) but better memory
            - using slow fast technique
            - it's a complex problem divided into 3 sub-problems
            - it worked yaaay, after 4 days of trying to make it work 
        """
        # (1) find a mid point
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(f"slow={slow}, fast={fast}")

        # (2) reverse the second partition after mid
        second = slow.next
        prev = None
        while second:
            cur = second  # we can remove it, but more readable
            next = second.next
            cur.next = prev
            prev = cur  # we can let prev=second, but more readable
            second = next
        second = prev
        # since prev stores the LL

        # prev.display()

        # (3) merge two lists together
        # ############ FIRST VERSION 1.0 ###########################
        # prev = cur = ListNode(-1)
        # while second:
        #     cur.next = head
        #     next = head.next
        #     cur.next.next = second
        #     # print(f"head={head}, head.next={head.next}, nex={next}")
        #     second = second.next
        #     cur = cur.next.next
        #     head = next
        # if head:
        #     cur.next = head
        #     cur.next.next = None
        # head = prev.next
        # head.display()

        # ############ SECOND VERSION 2.0 ###########################
        first, second = head, prev
        print("HERE")
        while second:
            # setting pointers
            nxt_first, nxt_second = first.next, second.next
            print(f"V1 first={first}, second={second}, 1st_next={nxt_first}, 2nd_next={nxt_second}")
            # initilizing first.next 1->5, second.next= 5->2 instead of 5->4
            # since we use first.next, our LL is updated properly
            first.next = second
            second.next = nxt_first
            # moving to next pointers
            first, second = nxt_first, nxt_second
            print(f"V2 first={first}, second={second}, 1st_next={nxt_first}, 2nd_next={nxt_second}")
            print('@@@@')
        # to prevent cyclic LL since we use while second:
        first.next = None
        head.display()
        return ListNode(-1)

    def reorderList(self, head: Optional[ListNode]) -> None:
        return self.reorderList_inplace(head)


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
res = Solution().reorderList(head1)
# res.display()


# head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
# res = Solution().reorderList(head1)
# res.display()


# head1 = ListNode(1, ListNode(2, ListNode(3)))
# res = Solution().reorderList(head1)
# res.display()



# head1 = ListNode(1, ListNode(2))
# res = Solution().reorderList(head1)
# res.display()


# head1 = ListNode(1)
# res = Solution().reorderList(head1)
# res.display()


# head1 = ListNode(1, ListNode(2, ListNode(3)))
# res = Solution().reorderList(head1)
# res.display()
