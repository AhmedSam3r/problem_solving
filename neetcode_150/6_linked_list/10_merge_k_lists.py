from typing import Optional, List


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

    def merge(self, h1, h2):
            dummy = cur = ListNode(-1)
            while h1 and h2:
                if h1.val <= h2.val:
                    cur.next = h1
                    h1 = h1.next
                else:
                    cur.next = h2
                    h2 = h2.next
                cur = cur.next
            cur.next = h1 or h2
            return dummy.next

    def mergeKLists_brute(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        time complexity: O(N * K))

        space complexity: O(1)
        notes:
            - Merge Lists One By One 
            - this solution worked (yaay) beats 15% in runtime and beats 88% in memory
        """

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.merge(lists[i], res)

        return res

    def mergeKLists_divide_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        time complexity: O(N * log(k)))
            - Where k is the total number of lists and n is the total number of nodes across k lists
            where n is the number of nodes in linked list
            and log(k) is the number of times/iterations we divide our lists list into 2 until we reach only 1 list                 

        space complexity: O(1)
        notes:
            - instead of Merge Lists One By One, We merge each two lists together,
                leading to logarithmatic time
            - see the difference here `https://www.youtube.com/watch?v=q5a5OiGbT6Q`
            - much faster beats 70% in runtime and less memory beats 50% in memory
            - divide and conquer iterative approach
                - it merges each two adjacent lists together
                - len(lists) = 8
                    - 8 --> 4 --> 2 --> 1 (log(K))

        """
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        indx = 1
        # len(lists) == 1 when we divide and c
        while len(lists) > 1:
            temp_merged_list = []
            print(f"INDEX={indx} :: V1 lists={len(lists)}, temp_merged_list={len(temp_merged_list)}")
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                temp_merged_list.append(self.merge(l1, l2))
            print(f"INDEX={indx} ::  V2 lists={len(lists)}, temp_merged_list={len(temp_merged_list)}")
            lists = temp_merged_list
            indx += 1

        return lists[0]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists_divide_conquer(lists)

# h1 = ListNode(1, ListNode(4, ListNode(5)))
# h2 = ListNode(1, ListNode(3, ListNode(4)))
# h3 = ListNode(10)
# h4 = ListNode(9)


# lists = [h1, h2, h3, h4]
# res = Solution().mergeKLists(lists)
# res.display()


h1 = ListNode(1, ListNode(4, ListNode(5)))
h2 = ListNode(1, ListNode(3, ListNode(4)))
h3 = ListNode(10)
h4 = ListNode(9)


h5 = ListNode(1, ListNode(4, ListNode(5)))
h6 = ListNode(1, ListNode(3, ListNode(4)))
h7 = ListNode(10)
h8 = ListNode(9)


lists = [h1, h2, h3, h4, h5, h6, h7, h8]
res = Solution().mergeKLists(lists)
# res.display()
