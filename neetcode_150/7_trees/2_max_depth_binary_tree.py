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
        - video expalantion  `https://www.youtube.com/watch?v=hTM3phVI6YQ`

    """

    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        """
        notes:
            - it worked yaaay
            - the crux of the problem is:
                - treat each root left and right as a subtree with different heights
                - at the end of each sub-tree,
                    check the max depth reached and compare it with the prev depth
                - since we increment n+1 each time, the call stack saves the current depth we reached
                    at that portion of the tree
            - note that the root element n=0, so we increment until null leaft node inclusive

        """
        def recurse(root: TreeNode, h: int) -> None:
            print(f"root={root}, h={h}")
            nonlocal sums
            if not root:
                if h > sums[0]:
                    sums[0] = h
                return None
            recurse(root.left, h + 1)
            recurse(root.right, h + 1)
            print(f"$$$$$ END root={root}, n={h} ")

        if not root:
            return 0
        n = 0
        sums = [-1]
        recurse(root, n)
        print(f"n={n}, sums_array={sums}")
        return sums[0]

    def maxDepth_dfs_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        root_left_h = self.maxDepth_dfs_v2(root.left)
        root_right_h = self.maxDepth_dfs_v2(root.right)
        res = 1 + max(root_left_h, root_right_h)
        print(f"root={root}, res={res}")
        return res
    

    def maxDepth_dfs_iterative(self, root: Optional[TreeNode]) -> int:
        """
        notes:
            - adding node.val for debugging purposes
            - it explains recursive dfs and how it works in an iterative manner
            - preorder traversal
        """
        stack = [[root, 1, str(root.val)]]
        res = 1
        while stack:
            print(f"v1 stack={stack}, res={res}")
            node_root, height, _ = stack.pop()  # root.left is always popped first
            if node_root.right:
                stack.append([node_root.right, height +
                             1, str(node_root.right.val)])
            # order is reversed so we can pop left root first
            if node_root.left:
                stack.append([node_root.left, height +
                             1, str(node_root.left.val)])
            # print(f"--- v2 stack={stack}, res={res}----")
            res = max(res, height)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@")
        return res



    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        """
        notes:
            - the trick here is to empty entire level in the deq

        """
        if not root:
            return 0

        deq = deque([root])
        height = 0
        while deq:

            for _ in range(len(deq)):  # traverse entire level
                node_root = deq.popleft()
                if node_root.left:
                    deq.append(node_root.left)
                if node_root.right:
                    deq.append(node_root.right)

            height += 1

        return height
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepth_dfs_iterative(root)


root = TreeNode(3,
                TreeNode(9),  # left of 3
                TreeNode(20, TreeNode(15), TreeNode(7))   # right of 3
                )

res = Solution().maxDepth(root)
assert res == 3
print("@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@@@@@@")

root = TreeNode(1,
                None,  # left of 1
                TreeNode(2)   # right of 1
                )

res = Solution().maxDepth(root)
assert res == 2
print("@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@@@@@@")


root = TreeNode(1,
                TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))),  # left of 1
                None   # right of 1
                )

res = Solution().maxDepth(root)
assert res == 5
print("@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@@@@@@")

root = TreeNode(1,
                TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, None, TreeNode(10))),
                TreeNode(3, TreeNode(6), TreeNode(7))
)
                

res = Solution().maxDepth(root)
assert res == 4
print("@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@@@@@@")

