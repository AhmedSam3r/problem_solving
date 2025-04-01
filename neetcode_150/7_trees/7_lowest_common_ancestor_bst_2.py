
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) if self else "EMPTY"


class OldSolution:
    """"
    - solution isn't working as I excpted him to work
    - before diving deep into implementation, try to find a simpler way/thought
        to solve the problem.

    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_multiple_dimension(root_p, root_q, p_val: int, q_val: int):
            nonlocal found_p, found_q, lcs, found_lcs
            print(f"root_p={root_p}, root_q={root_q}, p_val={p_val}, q_val={q_val}, found_p={found_p}, found_q={found_q}")
            if root and p_val == root_p.val and not found_p:
                found_p = True
                print(f"PPP HORAAAY ! root_p={root_p}::p={p}")
            elif root_p and p_val < root_p.val and not found_p:
                res = dfs_multiple_dimension(root_p.left, root_q, p_val, q_val)
                print(f"^^PP^^LEFT root_p={root_p.val}")
            elif root_p and p_val > root_p.val and not found_p:
                res = dfs_multiple_dimension(root_p.right, root_q, p_val, q_val)
                print(f"^^PP^^RIGHT root_p={root_p.val}")

            if root and q_val == root_q.val and not found_q:
                found_q = True
                print(f"QQQ HORAAAY ! root_q={root_q}::q={q}")
            elif root_q and q_val < root_q.val and not found_q:
                res = dfs_multiple_dimension(root_p, root_q.left, p_val, q_val)
                print(f"^^QQ^^LEFT root_q={root_q.val}")
            elif root_q and q_val > root_q.val and not found_q:
                res = dfs_multiple_dimension(root_p, root_q.right, p_val, q_val)
                print(f"^^QQ^^RIGHT root_q={root_q.val}")

            if (found_p and found_q):
                print(f"==> root_p={root_p}, root_q={root_q}")

            if (not found_lcs and found_p and found_q) and (root_p.val == root_q.val):
                print(f"@@@ FINALLY root_p={root_p}, root_q={root_q}")
                lcs = root_q
                found_lcs = True

        lcs = None
        found_p = found_q = found_lcs = False
        dfs_multiple_dimension(root, root, p.val, q.val)
        print(f"final found_p={found_p}, found_q={found_q}")
        return lcs


class Solution:
    def lowestCommonAncestor_recusive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time complexity O(N)

        space complexity O(N)

        where N is the tree height (h)
        """
        if not root or not p or not q:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_recusive(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_recusive(root.right, p, q)
        else:  # we found the splitting root
            return root

    def lowestCommonAncestor_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time complexity O(n)
            
        space complexity O(1)

        notes:
            - much more efficient
            - use cur not root while comparing `cur.val`
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # Move left
            elif p.val > root.val and q.val > root.val:
                root = root.right  # Move right
            else:
                return root  # Found LCA

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestor_recusive(root.left, p, q)


# root = TreeNode(6,
#                 TreeNode(2,
#                          TreeNode(0),
#                          TreeNode(4,
#                                   TreeNode(3),
#                                   TreeNode(5))),
#                 TreeNode(8,
#                          TreeNode(7),
#                          TreeNode(9))
#                 )
# p = TreeNode(2)
# q = TreeNode(9)
# res = Solution().lowestCommonAncestor(root, p, q)
# print("RES ==>", res)
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')

# root = TreeNode(6,
#                 TreeNode(2,
#                          TreeNode(0),
#                          TreeNode(4,
#                                   TreeNode(3),
#                                   TreeNode(5))),
#                 TreeNode(8,
#                          TreeNode(7),
#                          TreeNode(9))
#                 )
# p = TreeNode(2)
# q = TreeNode(4)
# res = Solution().lowestCommonAncestor(root, p, q)
# print("RES ==>", res)


# root = TreeNode(2,
#                TreeNode(1),
#                None)
# p = TreeNode(1)
# q = TreeNode(2)
# res = Solution().lowestCommonAncestor(root, p, q)
# print("RES ==>", res)



root = TreeNode(5,
                TreeNode(3,
                         TreeNode(2,
                                  TreeNode(1),
                                  None),
                         TreeNode(4)
                         ),
                TreeNode(6)                
                )
p = TreeNode(1)
q = TreeNode(4)
res = Solution().lowestCommonAncestor(root, p, q)
print("RES ==>", res)




