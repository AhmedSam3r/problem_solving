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


class OlderSolution:
    def __init__(self):
        self.found = False

    def isSubtree_v1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        this code passes 181/184 cases,
            - it can't handle when there's only one node in the subroot
            - my approach won't work as 
        """
        root_stack = [root]
        subroot_stack = [subRoot]
        found = False
        while root_stack:
            if not subroot_stack:  # we found a subtree
                found = True
                break
            curr_root = root_stack.pop()
            curr_subroot = subroot_stack.pop()
            if curr_root == curr_subroot == None:
                continue
            print(f"curr_root={curr_root}, curr_subroot={curr_subroot}")
            if curr_root:
                root_stack.append(curr_root.right)
                root_stack.append(curr_root.left)
            # print(f"{curr_root.val} == {curr_subroot.val}, type({type(curr_root.val)}::{type(curr_subroot.val)}), equal={curr_root.val == curr_subroot.val}")
            if curr_root and curr_subroot and (curr_root.val == curr_subroot.val):
                subroot_stack.append(curr_subroot.right)
                subroot_stack.append(curr_subroot.left)
            elif curr_subroot:  # Only reset if we have NOT fully matched subRoot
                subroot_stack = [subRoot]  # Reset subroot validation
            # else:
            #     subroot_stack = [subRoot]
        print(
            f"root_stack={root_stack},,sub_root_stack=={subroot_stack}, len={len(subroot_stack)}, found={found}")

        # handling edge case of with tree of
        if len(subroot_stack) == 0 or found:
            print("if len(subroot_stack) == 0:")
            return True
        print("@@@@@@@@@@@@@@@@@@@@@@")
        return False


class Solution:
    def __init__(self):
        self.found = False

    def isSubtree_dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        time complexity O(M x N)
            - where M is the number of root nodes
                and N is the number of subroot nodes
            - we traverse each N node in worst case
            - we compare each root tree with subroot tree

        space complexity: O(N)
            - N is the height of the call stack during the recursive traversal.
            - In the worst case, when the trees are skewed (completely unbalanced), the space complexity is O(n).
            - In the best case, when the trees are perfectly balanced, the space complexity is O(log(n)).


        notes:
            - watch this video for explanation `https://www.youtube.com/watch?v=E36O5SWp-LE`
                and for code `https://www.youtube.com/watch?v=HdMs2Fl_I-Q`
            - note this code `if root.val != subRoot.val: return False` 
                is what prevents us from visiting each node twice as it elinates the recursive call
                    in case the root != subroot
            - variables is made this way for better debugging
        """
        print(f"START isSubtree root={root}, subroot={subRoot}")
        if not root:
            return False
        if not subRoot:
            return True
        if self.found:
            print("BREAKING CONDITION")
            return True
        print("-------------DFS------------")
        is_same = self.same_tree(root, subRoot)
        print("-------------END------------")
        if is_same:
            self.found = True
            return True
        else:
            left_match = self.isSubtree(root.left, subRoot)
            right_match = self.isSubtree(root.right, subRoot)
            return (left_match or right_match)

    def same_tree(self, root, subRoot):
        print(f"same tree root={root}, subroot={subRoot}")
        if not root or not subRoot:
            return root == subRoot
        if root.val != subRoot.val:
            return False
        left_match = self.same_tree(root.left, subRoot.left)
        right_match = self.same_tree(root.right, subRoot.right)
        return left_match and right_match

    def isSubtree_serialize(self, root, subRoot):
        """
        time complexity O(M + N)
            - where M is the number of root nodes
                and N is the number of subroot nodes

        space complexity: O(N)

        notes:
            - watch this video for explanation `https://www.youtube.com/watch?v=GZ8g8KdavUo`
            - this is a preorder traversal (dfs) where we visit each node and look for similarity
            - to avoid [1, null, 2] and [1, 2, null] case, we must make sure of null ordering by returning #
            - the comma "," avoids us the root=[12] and subroot=[1,2] case to make distinct seperation of nodes values

        """
        def serialize(node):
            if not node:
                return "#"
            print(f"root={node}", end=" ")
            left_str = serialize(node.left)
            print(f"left_str={left_str}", end=" ")
            right_str = serialize(node.right)
            print(f"right_str={right_str}")
            concat_str = f",{node.val}" + left_str + right_str
            return concat_str
        print('------------left serialzie----------------')
        subRoot_str = serialize(subRoot)
        print('----------------------------')
        print(f"subRoot_str={subRoot_str}")
        root_str = serialize(root)
        print(f"root_str={root_str}")
        print("@@@@@@@@@@@@@@@@@@@@@@")

        return subRoot_str in root_str

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtree_serialize(root, subRoot)


tree = TreeNode(3,
                TreeNode(4, TreeNode(1), TreeNode(2)),
                TreeNode(5)
                )
sub_tree = TreeNode(4,
                    TreeNode(1),
                    TreeNode(2))
res = Solution().isSubtree(tree, sub_tree)
assert res is True


# tree = TreeNode(3,
#                 TreeNode(4,
#                          TreeNode(1),
#                          TreeNode(2)),
#                 TreeNode(5)
#                 )
# sub_tree = TreeNode(4,
#                     TreeNode(1),
#                     TreeNode(2, TreeNode(0)))
# res = Solution().isSubtree(tree, sub_tree)
# assert res is False


# p = TreeNode(1, TreeNode(2))
# q = TreeNode(1, None, TreeNode(2))
# res = Solution().isSubtree(p, q)
# assert res is False


# p = TreeNode(1, None)
# q = TreeNode(1, None)
# res = Solution().isSubtree(p, q)
# assert res is True


# p = TreeNode(1, TreeNode(1))
# q = TreeNode(1, None)
# res = Solution().isSubtree(p, q)
# assert res is True
