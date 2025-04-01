from typing import Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) if self else "EMPTY"


class Solution:
    """
    time complexity O(N)

    space complexity O(N)

    notes:
        - it's all about how to visualize the problem well, so you can solve it
        - expalanation video ` `https://www.youtube.com/watch?v=s6ATEkipzow`.
    """

    def isValidBST_my(self, root: Optional[TreeNode]) -> bool:
        """my solution it worked using my initial idea and neetcode expalantion video"""
        def dfs(root, left_bound, right_bound):
            nonlocal valid
            if not root:
                return
            if not valid:
                return
            print(
                f"comparing: {root.left} < {root} < {root.right} && left_bound={left_bound}, right_bound={right_bound}")
            if (root.left and root.left.val >= root.val) or (
                root.right and root.right.val <= root.val
            ):
                valid = False
            if not (left_bound < root.val < right_bound):
                valid = False

            dfs(root.left, min(root.val, left_bound), min(root.val, right_bound))
            dfs(root.right, max(root.val, left_bound), max(root.val, right_bound))

        if not root:
            return False
        valid = True
        dfs(root, float("-inf"), float("inf"))
        return valid

    def isValidBST_neet(self, root: Optional[TreeNode]) -> bool:
        """
        - much simpler than my solution
        - min max approach
        """
        def valid(node, min_val, max_val):
            if not node:
                return True

            print(
                f"comparing: {node.left} < {node} < {node.right} && left={min_val}, right={max_val}")
            if not (min_val < node.val < max_val):
                return False

            # every value in the left subtree must be less than the parent(root)
            # so we fix left and pass node.val
            # left < node.val < right
            valid_left = valid(node.left, min_val, node.val)
            # every node in the right subtree must be greater than the parent
            valid_right = valid(node.right, node.val, max_val)
            return valid_left and valid_right

        return valid(root, float("-inf"), float("inf"))

    def isValidBST_neet_bfs(self, root: Optional[TreeNode]) -> bool:
        """
        same as the previous one but recursive
        what makes it work, that we pass the correct min and max value in each level
        """
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, min_val, max_val = q.popleft()
            if not (min_val < node.val < max_val):
                return False
            if node.left:
                q.append((node.left, min_val, node.val))
            if node.right:
                q.append((node.right, node.val, max_val))

        return True

    def isValidBST_in_order_recursive(self, root: Optional[TreeNode]) -> bool:
        """
        - watch `https://www.youtube.com/watch?v=sLoZJ2E4ZDs` and why pre-order won't work
        - since the BST left subtree < root < right subtree
            then if we traversed in order, we must find the ordering in an ascending manner
        """
        def dfs(node):
            if not node:
                return

            print(f"comparing: {node.left} < {node} < {node.right}")
            dfs(node.left)
            print(f"curr = {node.val}")
            in_order_values.append(node.val)
            dfs(node.right)

        in_order_values = []
        valid = True
        dfs(root)
        print(f"inorder==>", in_order_values)
        prev = in_order_values[0]
        for i in range(1, len(in_order_values)):
            print(f"{prev} > {in_order_values[i]}")
            if (prev >= in_order_values[i]):
                valid = False
                break
            prev = in_order_values[i]
        print(f"valid -- {valid}")
        print("@@@@@@@@@@@@@@@@@@@@@@@@")
        return valid

    # def isValidBST_in_order_iterative(self, root: Optional[TreeNode]) -> bool:
    # """Understood this solution in the next problem"""
    #     stack = []
    #     min_val, max_val = float("-inf"), float("inf")

    #     while stack or root:

    #         while root:
    #             stack.append((root, root.val))
    #             root = root.left
    #         print(f"stack={stack}, root={root}, min_val={min_val}")
    #         root, _ = stack.pop()
    #         if root.val <= min_val:
    #             return False
    #         min_val = root.val
    #         root = root.right
    #     print("@@@@@@@@@@@@@")
    #     return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBST_in_order_recursive(root)


root = TreeNode(2,
                TreeNode(1),
                TreeNode(3))

res = Solution().isValidBST(root)
assert res is True
print('----------')


root = TreeNode(5,
                TreeNode(1),
                TreeNode(4,
                         TreeNode(3),
                         TreeNode(6)))

res = Solution().isValidBST(root)
assert res is False
print('----------')

root = TreeNode(2,
                TreeNode(2),
                TreeNode(2))

res = Solution().isValidBST(root)
assert res is False
print('----------')

# root = TreeNode(5,
#                 TreeNode(4),
#                 TreeNode(6,
#                          TreeNode(3),
#                          TreeNode(7)))

# res = Solution().isValidBST(root)
# assert res is False
# print('----------')

root = TreeNode(5,
                TreeNode(3),
                TreeNode(7,
                         TreeNode(4),
                         TreeNode(8)))

res = Solution().isValidBST(root)
assert res is False
print('----------')
