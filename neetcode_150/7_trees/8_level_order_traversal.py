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
    def levelOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time complexity O(N)

        space complexity O(N)
        """
        deq = deque([root])
        result = []
        if not root:
            return result
        while deq:
            level = []
            deq_len = len(deq)
            for _ in range(deq_len):
                node = deq.popleft()
                print(f"inside for loop ==> {node}, len={deq_len}")
                level.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            print(f"level={level}")
            result.append(level)

        return result

    def levelOrder_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time complexity O(N)

        space complexity O(N)
        """
        def dfs(root, h):
            nonlocal result
            if not root:
                return
            print(f"root: {root}, h={h}, result={result}")
            # replace these
            # if h < len(result) and type(result[h]) is list:
            #     result[h].append(root.val)
            # else:
            #     result.append([root.val])
            # much more simpler
            if len(result) <= h:
                result.append([])
            result[h].append(root.val)

            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
        result = []
        print(f"result==>{result}")
        dfs(root, 0)
        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrder_dfs(root)


# root = TreeNode(5,
#                 TreeNode(3,
#                          TreeNode(2,
#                                   TreeNode(1),
#                                   None),
#                          TreeNode(4)
#                          ),
#                 TreeNode(6)
#                 )
# res = Solution().levelOrder(root)


root = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7),
                         )
                )
res = Solution().levelOrder(root)

print(f"-----res--------- {res}")
