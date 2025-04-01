from typing import Optional
# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) if self else "EMPTY"


def levelOrder_bfs(root: Optional[TreeNode]) -> None:
    """
    time complexity O(N)

    space complexity O(N)
    """
    deq = deque([root])
    result = []
    print('---------------')
    if not root:
        return result
    while deq:
        level = []
        deq_len = len(deq)
        for _ in range(deq_len):
            node = deq.popleft()
            level.append(node.val)
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)

        result.append(level)
    print(result)
    print('---------------')


def dfs_order(root: Optional[TreeNode]) -> None:
    def dfs(root: Optional[TreeNode]) -> None:
        if not root:
            return
        print(f"root={root}, left={root.left}, right={root.right}")
        dfs(root.left)
        dfs(root.right)
    print('-------------')
    dfs(root)
    print('-------------')


class MyCodecSol:
    """
    time complexity: O(N)

    space complexity O(N)

    notes:
        - we're using BFS technique utilizing deque DS
        - we know the order of nodes insertion so we can utilize that using the for loop
        - it worked when we fixed casting the node value result_str properly
        - we can reduce code by removing position part,
            where we keep in mind first is root, second left and third is right
    """
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result_str = ""
        if not root:
            return ""

        deq = deque([(root, 'ROOT')])

        while deq:
            len_level = len(deq)
            for _ in range(len_level):
                node, pos = deq.popleft()
                # print(f"node={node}, pos={pos}")
                node_str = node.val if node else 'None'
                result_str += f"{node_str}${pos}$"
                if node:
                    deq.append((node.left, 'LEFT'))
                    deq.append((node.right, 'RIGHT'))

        return result_str

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def assign(root_node, value, pos):
            nonlocal deq, root_list
            if value == 'None':
                value = None

            if pos == "LEFT":
                root_node.left = TreeNode(int(value)) if value else None
                if root_node.left:
                    # print(f"appendl={root_node.left}")
                    deq.append(root_node.left)
                    # root_list.append(root_node.left.val)
            if pos == "RIGHT":
                # print(f"value={value}, type:{type(value)}, is={value is None}, 2={value == 'None'}")
                root_node.right = TreeNode(int(value)) if value else None
                # root_list.append(root_node.right)
                if root_node.right:
                    # print(f"appendR={root_node.right}, type={root_node.right}, COND={root_node.right is None}")
                    deq.append(root_node.right)

        if not data:
            return None

        splitted = data.split('$')
        print(f"ROOT, value={splitted[0]}, type={type(splitted[0])}")
        root = TreeNode(int(splitted[0]))
        root_list = [root.val]
        print(splitted)
        deq = deque([root])
        root_node = deq.popleft()
        # taking left and right
        for i in range(2, len(splitted), 4):
            value_1 = splitted[i]
            if not value_1:
                continue
            pos_1 = splitted[i + 1]
            assign(root_node, value_1, pos_1)  # assign left node
            value_2 = splitted[i + 2]
            pos_2 = splitted[i + 3]
            assign(root_node, value_2, pos_2)  # assign right node
            print(f"|||rootNod={root_node.val}|||val_1={value_1}, pos_1={pos_1}, val_2={value_2}, pos_2={pos_2}")
            if deq:
                root_node = deq.popleft()

        return root


class NeetCodeSolDFS:
    """
    - this is a preorder traversal
    """
    def serialize(self, root) -> str:
        def dfs(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        print(f"res =={res}\n")
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        def dfs():
            nonlocal vals, index
            if vals[index] == "N":
                index += 1
                return None

            node = TreeNode(int(vals[index]))
            print(f"IND:{index}, current node = {node}")
            index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        vals = data.split(",")
        index = 0
        print(f"vals == {vals}")
        res = dfs()
        return res


class NeetCodeSolBFS:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        by default the left and right node is null,
            so no need to check null nodes
        """
        vals = data.split(",")
        if vals[0] == "N":
            return None
        print(vals)
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        for index in range(1, len(vals), 2):
            node = queue.popleft()
            print(f"vals[{index}]=={vals[index]} :: vals[{index+1}]=={vals[index+1]},")
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)

            if vals[index + 1] != "N":
                node.right = TreeNode(int(vals[index + 1]))
                queue.append(node.right)
        return root


def initialize_class():
    return NeetCodeSolDFS()


root = TreeNode(1,
                TreeNode(2,
                         None,
                         TreeNode(3))
                )

ser = initialize_class()
result = ser.serialize(root)
deser = initialize_class()
ans = deser.deserialize(result)
dfs_order(ans)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# root = TreeNode(1,
#                 TreeNode(2,
#                          TreeNode(3),
#                          TreeNode(4)),
#                 TreeNode(5,
#                          TreeNode(6))
#                 )
# ser = initialize_class()
# result = ser.serialize(root)
# print(f"result={result}")
# deser = initialize_class()
# ans = deser.deserialize(result)
# dfs_order(ans)
# print('@@@@@@@@@@')

# root = TreeNode(1,
#                 TreeNode(2,
#                          TreeNode(4),
#                          None),
#                 TreeNode(3,
#                          None,
#                          TreeNode(5)))
# ser = initialize_class()
# result = ser.serialize(root)
# print(f"result={result}")
# deser = initialize_class()
# ans = deser.deserialize(result)
# dfs_order(ans)


# root = TreeNode(1,
#                 TreeNode(2,
#                          None,
#                          None),
#                 TreeNode(3,
#                          TreeNode(4),
#                          TreeNode(5)))
# ser = initialize_class()
# result = ser.serialize(root)
# print(f"result={result}")
# deser = initialize_class()
# ans = deser.deserialize(result)
# dfs_order(ans)
# print('@@@@@@@@@@@@@@@')

# # root = None
# # ser = Codec()
# # result = ser.serialize(root)
# # print(f"result={result}")
# # deser = Codec()
# # ans = deser.deserialize(result)
# # dfs_order(ans)


# # Your Codec object will be instantiated and called as such:
# ser = initialize_class()
# deser = initialize_class()
# ans = deser.deserialize(ser.serialize(root))
