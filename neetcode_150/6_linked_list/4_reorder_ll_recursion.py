
# from typing import Optional

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


class Sol:
    def __init__(self):
        self.front_pointer = None
        self.reordering_done = False

    def reorderList_recurse_v3(self, start_node, end_node):
        if not end_node:
            return

        # Move end_node to the last node via recursion
        if self.front_pointer is None:
            self.reorder_recursive(start_node, end_node.next)

        # If reordering is complete, exit
        if self.reordering_done:
            return

        if self.front_pointer:
            # Stop when reaching the middle in an odd-length list
            # Stop when reaching the middle in an even-length list
            if self.front_pointer == end_node:
                self.front_pointer.next = None
                self.reordering_done = True
                return

            elif self.front_pointer.next == end_node:
                self.front_pointer.next.next = None
                self.reordering_done = True
                return

            # Otherwise, reorder by swapping
            else:
                temp_next = self.front_pointer.next
                self.front_pointer.next = end_node
                end_node.next = temp_next
                self.front_pointer = temp_next

        else:
            temp_next = start_node.next
            start_node.next = end_node
            end_node.next = temp_next
            self.front_pointer = temp_next

    def reorderList_v3(self, head: ListNode) -> None:
        # base case when list contains 0, 1 or 2 elements only
        # no swap needed
        if not head or not head.next or not head.next.next:
            return
        self.front_pointer = head
        self.reorderList_recurse_v3(head, head.next)
        self.front_pointer.display()
        head.display()
