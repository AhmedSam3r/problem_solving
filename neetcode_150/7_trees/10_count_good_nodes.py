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
    """

    def goodNodes_dfs(self, root: TreeNode) -> int:
        def dfs(root, max_num):
            nonlocal total_count
            if not root:
                return
            print(
                f"root={root}, max_num={max_num}, total_count={total_count}, COND={root.val <= max_num}")
            if root.val >= max_num:
                total_count += 1
            dfs(root.left, max(max_num, root.val))
            dfs(root.right, max(max_num, root.val))

        total_count = 0  # root is always a good node
        dfs(root, float('-inf'))
        print(f"total_count={total_count}")
        print('---------------------------------------')
        return total_count

    def goodNodes_bfs(self, root: TreeNode) -> int:
        """
        notes:
        - it will get us right results
            since we save the max_num alongside left and right children of the root
        """
        total_count = 0
        stack = [(root, float('-inf'))]
        while stack:
            node, max_num = stack.pop()
            if node.val >= max_num:
                total_count += 1
            print(f"@@@ ROOT={node}, max_num={max_num}, total_count={total_count}, COND={node.val >= max_num}")
            max_num = max(max_num, node.val)
            if node.right:
                stack.append((node.right, max_num))
            if node.left:
                stack.append((node.left, max_num))
            # for debugging
            print("stack[root.val:max_num] >> ", end=' ')
            ([print(f"[{x1.val}:{x2}]", end=',,') for x1, x2 in stack])
            print()
            
        print('-------------------------')
        return total_count

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodes_bfs(root)


root = TreeNode(3,
                TreeNode(1,
                         TreeNode(3),
                         None),
                TreeNode(4,
                         TreeNode(1),
                         TreeNode(5),
                         )
                )
res = Solution().goodNodes(root)
assert res == 4

root = TreeNode(3,
                TreeNode(3,
                         TreeNode(4),
                         TreeNode(2))
                )
res = Solution().goodNodes(root)
assert res == 3

root = TreeNode(2,
                None,
                TreeNode(4,
                         TreeNode(10),
                         TreeNode(8,
                                  TreeNode(4),
                                  None)
                         )
                )
res = Solution().goodNodes(root)
assert res == 4
