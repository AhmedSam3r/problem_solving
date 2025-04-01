from typing import Optional
import heapq


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
        - each approach we use inorder traversal to get the sorted array

    """

    def kthSmallest_dfs_recursive(self, root: Optional[TreeNode],
                                  k: int) -> int:
        """
        - my solution worked, yaay
        - used inorder traversal technique which works with BST and gives us a sorted list ascendingly
        - can we use heap and do it iteratively ?
        """
        def dfs(root):
            if not root:
                return
            # here root.val
            print(
                f'root={root}, left={root.left}, right={root.right}, ::: heap_now={heap_list}')
            # for deubgging, gave same results
            heapq.heappush(heap_list, root.val)
            dfs(root.left)
            # root.left.val
            inorder_list.append(root.val)

            dfs(root.right)
            # root.right.val

        inorder_list = []
        heap_list = []
        dfs(root)
        print(f"list: {inorder_list} ::: heap list = {heap_list}")
        print("@@@@@@@@@@@")
        # k is 1 indexed
        return inorder_list[k-1]

    def kthSmallest_dfs_optimal_recusive(self, root: Optional[TreeNode],
                                         k: int) -> int:
        """
        - my solution worked, yaay
        - used inorder traversal technique which works with BST and gives us a sorted list ascendingly
        - can we use heap and do it iteratively ?
        """
        def dfs(root):
            nonlocal k, res
            if not root:
                return
            # here root.val
            print(f'root={root}, left={root.left}, right={root.right}')
            dfs(root.left)
            # root.left.val
            k -= 1
            # if k == 0 then we found the element in the correct index
            if k == 0:
                res = root.val
                return
            dfs(root.right)
            # root.right.val
        res = 0
        dfs(root)
        print(f"res={res}")
        print("@@@@@@@@@@@")
        # k is 1 indexed
        return res

    def kthSmallest_dfs_optimal_iterative(self, root: Optional[TreeNode],
                                          k: int) -> int:
        """
        - watch `https://www.youtube.com/watch?v=5LUXSvjmGCw`
        - iterate through left until you reach leaf node
            then start to go right and repeat the process

        """
        count = 0
        stack = []
        stack_debug = []
        cur = root
        while cur or stack:
            # when this loop is done, so we reached the lowest left leaf node
            while cur:
                stack.append(cur)
                stack_debug.append(cur.val)
                cur = cur.left
            print(f'V1:: root={cur}, stack={stack_debug}', end='  |||||  ')
            cur = stack.pop()
            stack_debug.pop()
            print(f'V2:: root={cur}, stack={stack_debug}\\\\END\\\\')
            count += 1
            if count == k:
                return cur.val
            # what if we didn't find our node ? then start search in the right subtree

            cur = cur.right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kthSmallest_dfs_optimal_iterative(root, k)


root = TreeNode(5,
                TreeNode(3),
                TreeNode(7,
                         TreeNode(4),
                         TreeNode(8)))
k = 1
res = Solution().kthSmallest(root, k)
assert res == 3
print('----------')


root = TreeNode(3,
                TreeNode(1,
                         None,
                         TreeNode(2)),
                TreeNode(4)
                )
k = 1
res = Solution().kthSmallest(root, k)
assert res == 1
print('----------')


root = TreeNode(5,
                TreeNode(3,
                         TreeNode(2,
                                  TreeNode(1),
                                  None),
                         TreeNode(4)),
                TreeNode(6)
                )
k = 6
res = Solution().kthSmallest(root, k)
assert res == 6
print('----------')
