from typing import Optional
from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def display(self):
        temp = self
        print("--------------DISPLAY-----------------------------")
        while temp:
            print(
                f"val={temp.val}, current={temp}, random={temp.random}, next={temp.next}")
            temp = temp.next
        print("--------------DISPLAY-----------------------------")

    def __str__(self):
        if self.val is not None:
            return str(self.val)
        return "EMPTY"


def get_head(head1_list):
    # head1_list = [(Node(3), None), (Node(3), 0), (Node(3), None)]
    head = cur = Node(-1)
    for i in range(len(head1_list)):
        cur.next = head1_list[i][0]   # Node(head1_list[i][0])
        random_idx = head1_list[i][1]
        if random_idx is not None:
            # print("head1_list[random_idx][0]=",head1_list[random_idx][0])
            cur.next.random = head1_list[random_idx][0]
        cur = cur.next
    head = head.next
    return head


class Solution:
    """
    nice to watch `https://www.youtube.com/watch?v=g7U-FPBR_gQ`
    one pass with no memory 
    """
    def __init__(self):
        self.old_to_new = {}

    def copyRandomList_two_pass(self, head: Optional[Node]) -> Optional[Node]:
        """
        time complexity O(N)

        space complexity O(N)

        notes:
            - expalanation video 'https://www.youtube.com/watch?v=5Y2EiZST97Y'
            - you can use a store DS such as hashmap, it doesn't to be a list
            - new_copy works as the new_copy doesn't have references yet to random and next,
                so it works well along with `cur=cur.next`
        """
        old_to_new = {None: None}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        # head.display()

        cur = head
        while cur:
            new_copy = old_to_new[cur]
            new_copy.next = old_to_new[cur.next]
            new_copy.random = old_to_new[cur.random]
            cur = cur.next
        # old_to_new[head] has the new_copy head which has the whole LL
        return old_to_new[head]

    def copyRandomList_recusion(self, head: 'Node') -> 'Node':
        """
        time complexity O(N)

        space complexity O(N)

        notes:
            - we are sure that our old_to_new is fully populated from this method calling
            - new_copy.next ensures that in the second call that
                new_copy is the head and the prev stack return will be its next
            - new_copy.next = prev_stack_return_with_prev_new_copy

        """
        if head is None:
            return None

        if head in self.old_to_new:
            return self.old_to_new[head]

        new_copy = Node(head.val)
        self.old_to_new[head] = new_copy
        new_copy.next = self.copyRandomList_recusion(head.next)
        new_copy.random = self.old_to_new.get(head.random)

        return new_copy

    def copyRandomList_one_pass(self, head: 'Node') -> 'Node':
        """
        notes:
            1. the trick here is we make a lambda method to create a new copy 
            if not exists then update its value to the new copy value
            2. t`new_copy.next=old_to_new[cur.next]` & `new_copy.random=old_to_new[cur.random]`
                does the trick here, why ?
                - as they're pointing to references not values
                - when their turn comes, their value will be modified like in step (1)
        """
        old_to_new = defaultdict(lambda: Node(0))
        old_to_new[None] = None

        cur = head
        print("old_to_new==>", old_to_new.items())
        while cur:
            # using lambda: Node(0), it get us new copy with value 0
            new_copy = old_to_new[cur]
            new_copy.val = cur.val  # modify 0 default value
            # old_to_new[cur.next] creates new node of next if not exists
            new_copy.next = old_to_new[cur.next]
            new_copy.random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        return self.copyRandomList_one_pass(head)

# My starting point
# head1_list = [(3, None), (3, 0), (3, None)]
# head1 = get_head(head1_list)
# head1.display()
# res = Solution().copyRandomList(head1)
# res.display()


head2_list = [[Node(7), None], [Node(13), 0], [Node(11), 4], [Node(10), 2], [Node(1), 0]]
head2 = get_head(head2_list)
# head2.display()
res = Solution().copyRandomList(head2)
res.display()
