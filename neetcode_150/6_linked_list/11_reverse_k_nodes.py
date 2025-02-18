from typing import Optional, List, Tuple


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
    def reverse_list(self, head: Optional[ListNode], k: int) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        prev, cur = None, head
        temp = 1
        while cur:
            next = cur.next
            # print(f"V1 prev={prev}, cur={cur}. next={next}")
            cur.next = prev
            prev = cur
            cur = next
            if temp == k:
                # print(f"BREAKING, temp={temp}")
                break
            temp += 1
            # print(f"V2 prev={prev}, cur={cur}. next={next}")

        print(f"@@@ FINISH head={prev}, tail={head}  @@@")
        return prev, head

    def reverseKGroup_brute(self, head: Optional[ListNode],k: int) -> Optional[ListNode]:
        """
        time complexity: O(N)
            - reverse list is O(K) where k number of nodes reversed
            - while loop to iterate on nodes Iterates through the entire list in chunks of k,
                calling reverse_list n/k times
                - so K * (N/K) = N
            - iterates in chunks of k, since it increments pointer until we reach k
                similar to i += k

        space complexity: O(1)

        notes:
            - yay it worked, needed a lot of handling to the pointers
            - it beats 100% (but different submissions got different percentage)
        """
        # cur = ListNode(-1, head)
        result = temp_result = ListNode(-1)
        temp = 1
        i = 1
        cur = head
        while True:
            # print("@@@@@@@@@@@@@@@@")
            if temp > k or not cur:
                # print("OUT K")
                break
            if temp == k:
                # print(f"== K, cur={cur}")
                # reverse list, get start & end and assign new tail
                next = cur.next
                rev_head, rev_tail = self.reverse_list(head, k)
                # print(f"head={head}, reversed_head={rev_head.val}, reversed_tail={rev_tail} NEXT={next}")
                rev_tail.next = next
                # rev_head.display()

                # build our reverse list and move pointer
                temp_result.next = rev_head
                temp_result = rev_tail

                # reset variables
                temp = 1
                head = next
                cur = next
                if head:
                    # print(f"@@@@ head={head}, head_next={head.next}")
                    pass
            else:
                temp += 1
                cur = cur.next if cur else None
            if cur:
                # print(f"-->>> increment temp: {temp}, cur={cur}, cur_next={cur.next}")
                pass
            # print("@@@@@@@@@@@@@@@@")

        return result.next
    

    def reverseKGroup_iterative(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, tail):
            prev, curr = None, head
            while curr != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev  # New head of the reversed group
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # If fewer than k nodes remain

            next_group = kth.next
            new_head = reverse(prev_group.next, kth.next)

            tail = prev_group.next
            prev_group.next = new_head
            tail.next = next_group
            prev_group = tail  # Move prev_group to the end of reversed group

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.reverseKGroup_brute(head, k)



h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
k = 2
res = Solution().reverseKGroup(h1, k)
res.display()


h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
res = Solution().reverseKGroup(h1, k)
res.display()


h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3
res = Solution().reverseKGroup(h1, k)
res.display()
