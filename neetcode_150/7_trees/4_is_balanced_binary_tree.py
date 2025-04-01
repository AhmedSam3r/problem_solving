from typing import Optional


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

    """

    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        """
        """
        def height(root):
            """returns height of the current left and right tree"""
            nonlocal largest_diameter, balanced
            if not root:
                return 0
            if not balanced:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if abs(left_height - right_height) > 1:
                balanced = False

            return 1 + max(left_height, right_height)

        largest_diameter = 0
        balanced = True
        height(root)
        return balanced
