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
    check `https://www.youtube.com/watch?v=vRbbcKXCxOw` for expalanation
    """

    def isSameTree_bfs_v1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        notes:
            - pay attention to setting the base conditions
        """
        def is_same_root(p_root, q_root):
            if p_root == q_root == None:
                return True
            if p_root.val != q_root.val:
                return False
            return True

        # base conditions
        if p == q == None:
            return True
        if (p and not q) or (q and not p):
            return False

        p_deq = deque([p])
        q_deq = deque([q])
        same = True
        while p_deq and q_deq:
            p_root = p_deq.popleft()
            q_root = q_deq.popleft()
            print(f"p_root={p_root}, q_root={q_root}")

            if not is_same_root(p_root, q_root):
                return False

            if p_root.left and q_root.left:
                p_deq.append(p_root.left)
                q_deq.append(q_root.left)
            elif not (p_root.left == q_root.left == None):
                same = False
                break

            if p_root.right and q_root.right:
                p_deq.append(p_root.right)
                q_deq.append(q_root.right)
            elif not (p_root.right == q_root.right == None):
                same = False
                break

        print(f"p_deq={p_deq}, q_deq={q_deq}")
        if len(p_deq) != len(q_deq):
            same = False
        print(f"p={p}, q={q}")
        print("@@@@@@@@@@@@@@@")
        return same

    def isSameTree_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        time complexity O(N)
            - best case would be O(logN) balanced tree
            - Worst Case (degenerate tree) O(N)
            - if two trees are identical in size each node must be visited
            - if not identical O(min(p, q))

            - N as the two trees are traversed in the same time 
        space complexity O(N)
        notes:
            - we can add nonlocal same variable to prevent iterations if subtree are not the same
                this would make the time compleixty O(min(p, q)) if not identical
            - The only thing that you should mention always when 
                discussing a recursive solution is a possibility of a stack overflow. 
            - In this exact problem this is not an issue 
                because it's mentioned there could be maximum 100 elements in a tree.
            - But if you fail to ask for a maximum possible number of elements in a data structure 
                and you implement a recursive solution in an interview, 
                you can expect to lose some points.
        """
        # if one of them is empty, we check if both equal null or not
        # smarter condition
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        # check left subtree
        same_left = self.isSameTree_dfs(p.left, q.left)
        # check right subtree
        same_right = self.isSameTree_dfs(p.right, q.right)
        # (self.isSameTree_dfs(p.left, q.left)) and (self.isSameTree_dfs(p.right, q.right)
        return same_left and same_right

    def isSameTree_bfs_v2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """much cleaner code"""
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameTree_dfs(p, q)


p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
res = Solution().isSameTree(p, q)
assert res is True


p = TreeNode(1, TreeNode(2))
q = TreeNode(1, TreeNode(2), TreeNode(3))
res = Solution().isSameTree(p, q)
assert res is False


p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
res = Solution().isSameTree(p, q)
assert res is False


p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
res = Solution().isSameTree(p, q)
assert res is False


p = TreeNode(1, )
q = TreeNode(1, TreeNode(1), TreeNode(2))
res = Solution().isSameTree(p, q)
assert res is False
