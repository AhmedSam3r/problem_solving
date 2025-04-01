from typing import Optional

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self.val is not None:
            return str(self.val)
        return "EMPTY"


class Solution:
    """
    time complexity: O(N)

    space complexity: O(N)

    notes:
        - we're inverting each sub-tree except for root, so it's recursive problem by nature
        explains both approaches
        - explain recursive and iterative `https://www.youtube.com/watch?v=ck23lNqbLjI`
    """
    def investTree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(f"left={root.left}, root={root}, right={root.right}")
        # print(f"              root={root}         ")
        # print("             /            \ ")
        # print(f"left={root.left}            right={root.right}")
        if root.left:
            self.investTree_dfs(root.left)
            # print(f"-------- after left dfs root={root}, left={root.left}, right={root.right}-------")

            # i'm targeting the current root node
            # this line only, it skips the leaf nodes
            # root.left, root.right = root.right, root.left
        if root.right:
            # print(f"BEFORE RIGHT PORTION::: left={root.left}, root={root}, right={root.right}")
            self.investTree_dfs(root.right)
            # print(f"@@@@@ RIGHT PORTION root={root}, left={root.left}, , right={root.right} @@@@@")
        # this line makes it work
        root.left, root.right = root.right, root.left
        pass  # for seeing root.left and root.right in the debugger trace

    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while len(queue) >= 1:
            node_root = queue.popleft()
            print(f"node_root={node_root}")
            if node_root.left:
                queue.append(node_root.left)
            if node_root.right:
                queue.append(node_root.right)
            # swap the tree
            print(f"---- swapping left={node_root.left} && right={node_root.right}---- ")
            node_root.left, node_root.right = (
                node_root.right, node_root.left
            )

        return root

    def invertTree_dfs_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            node.left, node.right = node.right, node.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTree_bfs(root)

root = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),  # left of 4
                TreeNode(7, TreeNode(6), TreeNode(9))   # right of 4
                )

res = Solution().invertTree(root)
print('-----------display-----------------')
print(f"root={root.left.right}")

