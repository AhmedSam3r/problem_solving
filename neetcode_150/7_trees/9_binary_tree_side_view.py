from typing import Optional, List

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
    """"
    time complexity O(N)

    space complexity O(N)

    notes:
        - bfs is more efficient

    """

    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        """
        notes:
            - notice we traverse from right first instead of left
            - `depth == len(res)` this condition ensures that we append only once
                in case that the current level isn't populated with the RHS item 
        """
        res = []

        def dfs(node, depth):
            if not node:
                return None
            print(f"root={node}, depth={depth}, len(res)={len(res)}, COND={depth == len(res)}")
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        print(f"result={res}")
        print("----------------")

        return res

    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        deq = deque([root])

        while deq:
            len_deq = len(deq)
            if deq:
                rhs = deq[-1].val
                result.append(rhs)
            for _ in range(len_deq):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

        print(f"result={result}")
        print("----------------")
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.rightSideView_dfs(root)


root = TreeNode(1,
                TreeNode(2,
                         None,
                         TreeNode(5)),
                TreeNode(3,
                         None,
                         TreeNode(4),
                         )
                )
res = Solution().rightSideView(root)


root = TreeNode(1,
                TreeNode(2,
                         None,
                         TreeNode(4,
                                  None,
                                  TreeNode(5))),
                TreeNode(3)
                )
res = Solution().rightSideView(root)
