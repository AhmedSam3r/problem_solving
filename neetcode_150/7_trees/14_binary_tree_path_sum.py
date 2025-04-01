from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) if self else "EMPTY"


class Solution:
    """
        time complexity: O(N)

        space compleixty: O(N)

        notes:
        - video expalanation `https://www.youtube.com/watch?v=Hr5cWUld4vU`
        - the crux of this problem in this problem is to understand the two cases of:
            - calculating the max path sum WITH splitting
            - calculating the max path sum WITHOUT splitting
        - 
    """

    def maxPathSum_initial(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal total
            if not root:
                return 0

            left_res = dfs(root.left)
            right_res = dfs(root.right)
            if left_res != 0 and right_res != 0:
                # max(left_res+root.val, max(right_res + root.val, max(left_res + right_res + root.val))) 
                max_partial = max(left_res + root.val, right_res + root.val)
                max_full = max(max_partial, left_res + right_res + root.val)
                total += max(total, max_full)

            print(f"==TOTAL=={total}===root={root.val}, left_res={left_res}, right_res={right_res}")

            return root.val

        total = 0
        dfs(root)
        print(f"total={total}")
        print('---------------')
        return total

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal longest
            if not root:
                return 0

            left_res = dfs(root.left)
            right_res = dfs(root.right)

            # longest = max(longest, max(left_res, right_res))
            # max leg representing the max path THROUGH SPLITTING
            # imaginge crossroads you only can go into one path
            max_leg = max(
                root.val,  # root val
                root.val + left_res,  # root and left
                root.val + right_res  # root and right
            )
            longest = max(
                longest,
                max_leg,
                # longest leg representing the maximum path WITHOUT splitting
                root.val + left_res + right_res
            )
            print(f"root={root}, left_res={left_res}, right_res={right_res}, max_leg={max_leg}, $$$ LONGEST $$$$ ={longest}")

            return max_leg

        longest = float("-inf")  # to handle negati ve numbers
        dfs(root)
        print(f"longest={longest}")
        print(f"res  {longest}")
        print('---------------')
        return longest


root = TreeNode(1,
                TreeNode(2),
                TreeNode(3))
res = Solution().maxPathSum(root)
assert res == 6


root = TreeNode(-10,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7)))
res = Solution().maxPathSum(root)
assert res == 42


root = TreeNode(-10,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(-5),
                         TreeNode(7)))
res = Solution().maxPathSum(root)
assert res == 27

root = TreeNode(-3)
res = Solution().maxPathSum(root)
assert res == -3
