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
        - video expalantion  `https://www.youtube.com/watch?v=hTM3phVI6YQ`

    """

    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        def dfs(root, h):
            nonlocal res
            if not root:
                return 0
            root_left_h = dfs(root.left, h + 1)
            root_right_h = dfs(root.right, h + 1)
            res = max(root_left_h, root_right_h) + 1
            print(f"H={h}, root={root}, Left={root_left_h}, right={root_right_h}, res={res}")

            return res

        if not root:
            return 0
        res = 0
        res = dfs(root, 0)
        print(f"FINAL res={res}")
        print("@@@@@@@@@@@@@@@@@@@@")
        return res

    def maxDepth_dfs_v2(self, root: Optional[TreeNode]) -> int:
        """
        Best Case (balanced tree): O(log(n)) 
        Worst Case (degenerate tree): O(n)

        notes:
            - great explanation video `https://www.youtube.com/watch?v=6lJZ_xj1mEo`
            - the crux of the problem to make a clear distinction between
                the diameter & the height and determine what to store and what to return
        """
        def height(root):
            """returns height of the current left and right tree"""
            nonlocal largest_diameter
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = (left_height + right_height)
            # this line which makes the problem work
            largest_diameter = max(largest_diameter, diameter)
            print(f"left_height={left_height}")
            return 1 + max(left_height, right_height)

        largest_diameter = 0
        height(root)
        return largest_diameter

    def treeDepth(self, root: TreeNode) -> int:
        """ Helper function to compute the depth of a subtree. """
        if not root:
            return 0
        return 1 + max(self.treeDepth(root.left), self.treeDepth(root.right))

    def diameterOfBinaryTree_brute(self, root: TreeNode) -> int:
        """ Brute force approach: check diameter at each node. """
        if not root:
            return 0

        # Get depths of left and right subtrees
        left_depth = self.treeDepth(root.left)
        right_depth = self.treeDepth(root.right)

        # Diameter through the current root
        diameter_through_root = left_depth + right_depth

        # Recursively compute diameter for left and right subtrees
        left_diameter = self.diameterOfBinaryTree_brute(root.left)
        right_diameter = self.diameterOfBinaryTree_brute(root.right)

        # Return the maximum diameter found
        return max(diameter_through_root, left_diameter, right_diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.maxDepth_dfs_v2(root)




root = TreeNode(1, TreeNode(2))

res = Solution().diameterOfBinaryTree(root)
assert res == 1


root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3))

res = Solution().diameterOfBinaryTree(root)
assert res == 3


root = TreeNode(3,
                TreeNode(9),  # left of 3
                TreeNode(20, TreeNode(15), TreeNode(7))   # right of 3
                )
res = Solution().diameterOfBinaryTree(root)
assert res == 3
