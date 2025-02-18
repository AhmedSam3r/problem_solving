from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

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
    def hasCycle_v1(self, head: Optional[ListNode]) -> bool:
        """
        time complexity: O(n)
        space complexity: O(n)
        run time beats 20%, may be there's optimization
        """
        if not head or not head.next:
            return False
        visited = set()
        while head:
            addr = id(head)
            print(f"addr = {addr}")
            if addr in visited:
                print(f"@pos={head.val}")
                return True
            visited.add(addr)
            head = head.next

        return False
    
    def hasCycle_v2(self, head: Optional[ListNode]) -> bool:
        """
        it doesnot work
        time complexity: O(n)
        space complexity: O(1)
        """
        if not head or not head.next:
            return False
        prev_addr = id(head)
        head = head.next
        while head:
            curr_addr = id(head)
            print(f"cur_addr={curr_addr} vs prev={prev_addr}, prev_addr < curr_addr: {prev_addr < curr_addr}")
            if prev_addr < curr_addr:
                prev_addr = curr_addr
            else:
                print(f"@pos={head.val}")
                return True
            head = head.next

        return False

    def hasCycle_v3(self, head):
        """
        time complexity: O(n)
        space complexity: O(1)
        notes
        - slow-fast pointers approach
        - if slow and fast pointer meet, then there must be a cycle. they don't have to meet at the entry point
        - it's guranteed that the two pointers will catch at the cyclic node
        - Floyd's cycle detection algorithm (Tortoise and hare)
            - If there is a cycle, fast will eventually meet slow. If fast reaches None, then there's no cycle.
        - watch this video
            - `https://www.youtube.com/watch?v=y-ckZ2hpC8Y`
            - `https://www.youtube.com/watch?v=gBTe7lFR3vc`
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hasCycle_v2(head)

ll = ListNode(3)
ll.next = save = ListNode(2)
ll.next.next = ListNode(0)
ll.next.next.next = ListNode(-4)
ll.next.next.next.next = save
# ll.display()
res = Solution().hasCycle(ll)
assert res is True
print("@@@@@@@@@@@@@@")

ll2 = ListNode(3)
res = Solution().hasCycle(ll2)
assert res is False
print("@@@@@@@@@@@@@@")

ll3 = save = ListNode(1)
ll3.next = ListNode(2)
ll3.next.next = save
res = Solution().hasCycle(ll3)
assert res is True
print("@@@@@@@@@@@@@@")
