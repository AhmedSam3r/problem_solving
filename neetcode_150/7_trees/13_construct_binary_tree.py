from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) if self else "EMPTY"

    @staticmethod
    def display_tree(root: Optional['TreeNode']) -> None:
        """display tree dfs to keep track of root"""
        def dfs(root: Optional['TreeNode']) -> None:
            """
            time complexity O(N)

            space complexity O(N)
            """
            if not root:
                return
            print(f"root={root}, left={root.left}, right={root.right}")
            dfs(root.left)
            dfs(root.right)

        print('////// Display \\\\\\\\')
        dfs(root)
        print('////// END \\\\\\\\')


class Solution:
    """
    notes:
        - expalanation video  `https://www.youtube.com/watch?v=PbPS460rbMo`
        - the key trick is to understand how to divide this problem 
            into smaller sub problems (divide and conquer)
    """
    def buildTree_dummy(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """initial not working version"""
        root_val = preorder[0]
        print(f"root_val={root_val}")
        inorder_root_idx = inorder.index(root_val)
        level_order = [root_val]
        visited = [False] * len(preorder)
        visited[0] = True
        print(f"inorder_root_idx={inorder_root_idx}")
        print(f"levelorder={level_order},,, visited={visited}")
        for i in range(1, len(preorder)):
            print(f"preorder[{i}]={preorder[i]}", end=' ')
            # checking left
            if inorder.index(preorder[i]) < inorder_root_idx and not visited[i]:
                print("LESS THAN")
                visited[i] = True
                level_order.append(preorder[i])
            # checking right
            elif inorder.index(preorder[i]) > inorder_root_idx:
                print("GREAT THAN")
                level_order.append(preorder[i])

        print(f'FINAL__BFS = {level_order}, visited={visited}')
        print('@@@@@@@@@@@@')

    def buildTree_dfs_brute(self, preorder: List[int], inorder: List[int]):
        """
        time complexity O(N^2)

        space complexity O(N)

        notes:
            - this approach can be enhanced since we used
                - 1st issue: `index()` O(N) search time complexity 
                    - can we optimize that part ? yes, use dictionnary
                - 2nd issue: list slicing creating a new list O(left_size) space complexity
                    - can we optimize that part ? yes, use pointers
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        # find index of the pre order root in the inorder
        left_size = inorder.index(preorder[0])

        print(f"root={root}, LEFT_SIZE={left_size}, preorder={preorder}, inorder={inorder}")
        # create left subtree
        root.left = self.buildTree_dfs_brute(preorder[1:left_size+1], inorder[:left_size])
        root.right = self.buildTree_dfs_brute(preorder[left_size + 1:], inorder[left_size+1:])
        return root

    def buildTree_dfs_v1(self, preorder: List[int], inorder: List[int]):
        def traverse(preorder: List[int], inorder: List[int]):
            nonlocal inorder_mapper
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])

            # find index of the pre order root in the inorder
            left_size = inorder_mapper[preorder[0]]

            print(f"root={root}, LEFT_SIZE={left_size}, preorder={preorder}, inorder={inorder}")
            # create left subtree
            root.left = self.buildTree_dfs_brute(preorder[1:left_size+1], inorder[:left_size])
            root.right = self.buildTree_dfs_brute(preorder[left_size + 1:], inorder[left_size+1:])
            return root

        inorder_mapper = {key: ind for ind, key in enumerate(inorder)} # solved first issue

        print(inorder_mapper)
        return traverse(preorder, inorder)

    def buildTree_dfs_optimal_v1(self, preorder: List[int], inorder: List[int]):
        """
        notes:
            - utilized dictionnary for inorder index
            - left and right pointer version 
        """
        def construct_tree(left, right):
            nonlocal pre_start, inorder_mapper
            if left > right:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            # we are sure that the preorder contains the root of the tree
            # incrementing pre_start, ensures to get the root before recursion
            pre_start += 1
            inorder_index = inorder_mapper[root_val]
            print(f"L={left}, R={right}:: root={root}, inorder_index={inorder_index}, inorder={inorder[left:right+1]}")  # debugging

            root.left = construct_tree(left, inorder_index - 1)
            root.right = construct_tree(inorder_index + 1, right)

            return root

        inorder_mapper = {key: ind for ind, key in enumerate(inorder)}
        pre_start = 0
        print(inorder)
        res = construct_tree(0, len(inorder) - 1)
        return res

    def buildTree_dfs_optimal_v2(self, preorder: List[int], inorder: List[int]):
        """
        notes:
            - preorder and in order pointers approach
            - to understand this code, watch the code expalanation here
                `https://youtu.be/aZNaLrVebKQ`
            - this approach has more pointers but it's more close to the conceptual expalantion
            - we replaced `buildTree_dfs_v1()` array slicing by left and right pointerss
            - to get the left tree
                - `pre_start + 1`: we skip the current root node to the next one in the preorder
                - `pre_start + left_size`: we get the left tree by adding the left size we calculated to get left tree elements in preorder
                - `in_start`: since we're on the left, keep in_start as it is
                - `inorder_index - 1`: since we're on the left, we will get left tree from inorder from the start until before the root index (inorder_index)
            - to get the right tree
                - `pre_start + left_size + 1`: to reach the end of the left tree from preorder we skip by the length of prestart+left_size and add one to get the start of right tree
                - `pre_end`: it will be at the end
                - `inorder_index + 1`: to get the right tree we increment inorder by one
                - `in_end`:  it will be at the end
        """
        def construct_tree(pre_start, pre_end, in_start, in_end):
            nonlocal preorder, inorder, inorder_mapper
            if (pre_start > pre_end) or (in_start > in_end):
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            inorder_index = inorder_mapper[root_val]
            # to get the number of elements, similar to window size right - left
            left_size = inorder_index - in_start

            print(f"root={root}, preorder[{pre_start}:{pre_end}]={preorder[pre_start: pre_end+1]}, inorder[{in_start}:{in_end}]={inorder[in_start:in_end+1]}")  # for debugging
            root.left = construct_tree(
                pre_start + 1, pre_start + left_size,
                in_start, inorder_index - 1)
            root.right = construct_tree(
                pre_start + left_size + 1,
                pre_end, inorder_index + 1, in_end)
            return root

        inorder_mapper = {key: ind for ind, key in enumerate(inorder)}
        res = construct_tree(0, len(preorder) - 1, 0, len(inorder) - 1)
        return res

    def buildTree(self, preorder: List[int], inorder: List[int]):
        return self.buildTree_dfs_optimal_v2(preorder, inorder)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7))
                )


res = Solution().buildTree(preorder, inorder)
# print(f"res={res}, type={type(res)}")
# TreeNode.display_tree(res)


# root = TreeNode(3,
#                 TreeNode(9,
#                          TreeNode(1),
#                          TreeNode(2)
#                          ),
#                 TreeNode(20,
#                          None,
#                          TreeNode(7))
#                 )
print('---')

# preorder = [3, 9, 1, 2, 20, 7]
# inorder = [1, 9, 2, 3, 20, 7]
# root_result = Solution().buildTree(preorder, inorder)

# TreeNode.display_tree(root_result)
# print('---')

preorder = [8, 2, 7, 1, 9, 3, 6]
inorder = [7, 2, 1, 8, 3, 9, 6]
# how to determine that 7 is right
root_result = Solution().buildTree(preorder, inorder)
# print('display')
# TreeNode.display_tree(root_result)
