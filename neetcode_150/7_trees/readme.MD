# Generic rules about trees
Nice! Since you've worked on **inverting a binary tree** and **finding maximum depth**, you've already applied some traversal techniques like **BFS (Breadth-First Search) and DFS (Depth-First Search)**. Let's break down **tree traversal methods** and their differences.

---

## **1. Tree Traversal Types**
Tree traversal is how we visit all nodes in a tree in a systematic way. There are **two main categories**:

### **A. Depth-First Search (DFS)**
DFS explores as far as possible along each branch before backtracking. It has three main types:
1. **Preorder Traversal (Root → Left → Right)**
   - Visit the root node first.
   - Then recursively visit the left subtree.
   - Finally, visit the right subtree.
   - **Use case**: Used in tree cloning, prefix expressions.

2. **Inorder Traversal (Left → Root → Right)**
   - Visit the left subtree first.
   - Then visit the root node.
   - Finally, visit the right subtree.
   - **Use case**: Retrieves sorted elements in BSTs.

3. **Postorder Traversal (Left → Right → Root)**
   - Visit the left subtree.
   - Then visit the right subtree.
   - Finally, visit the root node.
   - **Use case**: Used in deleting nodes, evaluating expressions.

---

### **B. Breadth-First Search (BFS)**
Instead of exploring deep into one branch, BFS visits **all nodes at the same depth level** before moving to the next level.

1. **Level Order Traversal (Left to Right, Level by Level)**
   - Visit the root first.
   - Then visit all nodes at depth 1, then depth 2, and so on.
   - Uses a **queue (FIFO)**
   - **Use case**: Used in shortest path problems (e.g., in graphs).

---

## **2. Key Differences**
| Traversal Type  | Order | Implementation | Use Cases |
|----------------|--------|---------------|-------------|
| **Preorder**  | Root → Left → Right | DFS (recursion/stack) | Copying trees, prefix expressions |
| **Inorder**   | Left → Root → Right | DFS (recursion/stack) | Sorting BST elements |
| **Postorder** | Left → Right → Root | DFS (recursion/stack) | Deleting nodes, postfix expressions |
| **Level Order** | Level by level | BFS (queue) | Shortest path problems, hierarchical processing |

---

## **3. BFS vs DFS**
| Factor | BFS (Level Order) | DFS (Preorder, Inorder, Postorder) |
|--------|------------------|--------------------------------|
| **Exploration** | Explores all nodes at the same level before moving deeper | Explores one branch deeply before backtracking |
| **Memory Usage** | Uses a queue (can be large for wide trees) | Uses a stack or recursion (better for balanced trees) |
| **Best for** | Shortest path, tree height, balanced trees | Searching, deep trees, expression evaluation |

---

Since you're working on trees, mastering **DFS and BFS** will help in many problems like **Lowest Common Ancestor, Balanced Binary Tree, Binary Tree Paths, and Tree Serialization**.  

Let me know if you want a deeper dive into any of these! 🚀



# (2) diameter binary tree
Best Case (balanced tree): 
O(log(n))
Worst Case (degenerate tree): 
O(n)

#  (3) (4) problems

- using DFS recursively bottom up is O(N) more optimized as we don't calculate the height from bottom up and pass the height to the upper 
- if we used top bottom approach, we will find oursevles recalculating the tree height at each node
- see example for reference `https://www.youtube.com/watch?v=QfJsau0ItOY`


## Balanced Binary Tree
[text](https://www.geeksforgeeks.org/balanced-binary-tree/)
- **A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. **
- For Example
  - **the AVL tree maintains O(Log n) height by making sure that the difference between the heights of the left and right subtrees is at most 1.** 
  - **Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root-to-leaf path is the same and that there are no adjacent red nodes.**
- **Balanced Binary Search trees are performance-wise good as they provide O(log n) time for search, insert and delete**. 

- **A single node is always balanced. It is also referred to as a height-balanced binary tree.**
- **An empty tree (Root = Null) is also always considered as balanced.**

## Degenerate Binary Tree

- **Every non-leaf node has just one child in a binary tree known as a Degenerate Binary tree. The tree effectively transforms into a linked list as a result, with each node linking to its single child.**
- **When a straightforward and effective data structure is required, degenerate binary trees, a special case of binary trees, may be employed.** 
- **For instance, a degenerate binary tree can be used to create a stack data structure since each node simply needs to store a reference to the next node.**
- **Degenerate binary trees are less effective than balanced binary trees at searching, inserting, and deleting data, though. This is due to the fact that degenerate binary trees may become unbalanced, resulting in performance that is comparable to a linked list in the worst case.**
- **Degenerate binary trees are rarely employed by themselves as a data structure in general. Rather, they are frequently utilized as a component of other data structures like linked lists, stacks, and queues. **
- **Degenerate binary trees can also be utilized as a particular instance to take into account in algorithms that traverse or search over binary trees.**

### Degenerate Binary tree is of two types:
- **Left-skewed Tree**:  If all the nodes in the degenerate tree have only a left child.
- **Right-skewed Tree**: If all the nodes in the degenerate tree have only a right child.


# (6)

revisit the subtree problem, it confused me.
it's considered of two problems same tree and same subtree


# (13) construct binary tree
the hardest problem i've ever faced.

# (14) binary tree path sum
you need to understand the rules well and visualize the problem 

# (15) serialize and deserialize tree
Let's break this down clearly, explain how this method works, and debug the confusing part where it **returns the node**.

---

### **How This Method Works**
This function **deserializes** a binary tree from a serialized string. It reconstructs the tree using **depth-first search (DFS) recursion**. Let's go step by step.

#### **1. `dfs()` is a recursive function**
- This function **reads values** from a list (`vals`) **one by one**.
- `index` keeps track of the current position in `vals`.

#### **2. Base Case: Handling `None` (Leaf Nodes)**
```python
if vals[index] == "N": 
    index += 1
    return None
```
- If the value at `index` is `"N"`, it means **this is a `null` node (leaf node's child)**.
- So, **increment `index` to move to the next value** and return `None`.

#### **3. Creating the Current Node**
```python
node = TreeNode(int(vals[index]))
print(f"IND:{index}, current node = {node}")
index += 1
```
- If it's **not `"N"`**, create a new `TreeNode` with the integer value at `vals[index]`.
- **Move to the next value in `vals`**.

#### **4. Recursively Constructing Left and Right Subtrees**
```python
node.left = dfs()
node.right = dfs()
```
- **First, recursively construct the left child** by calling `dfs()`.
- **Then, recursively construct the right child** by calling `dfs()`.
- Since DFS is used, **left subtree is always built before the right subtree**.

#### **5. Returning the Node**
```python
return node
```
- This ensures that **each recursive call returns a constructed subtree**.
- At the end of the recursion, the **root node of the entire tree is returned**.

---

### **Debugging & Clearing the Confusion**
You might be confused about what happens when the function returns `node`.

#### **Step-by-step Execution**
Imagine `vals = ["1", "2", "N", "N", "3", "N", "N"]`, which represents:
```
    1
   / \
  2   3
```
**Execution Flow:**
1. `index = 0`: **Create Node(1)**
   - Call `dfs()` for the **left subtree**.
2. `index = 1`: **Create Node(2)**
   - Call `dfs()` for `Node(2).left` (index moves to 2).
3. `index = 2`: Found `"N"`, return `None` → `Node(2).left = None`
4. `index = 3`: Found `"N"`, return `None` → `Node(2).right = None`
5. **Return Node(2)** (completed subtree)
6. `index = 4`: **Create Node(3)**
   - Call `dfs()` for `Node(3).left` (index moves to 5).
7. `index = 5`: Found `"N"`, return `None` → `Node(3).left = None`
8. `index = 6`: Found `"N"`, return `None` → `Node(3).right = None`
9. **Return Node(3)** (completed subtree)
10. **Return Node(1)** (the root, with left and right subtrees attached)

---

### **Key Takeaways**
1. **DFS ensures the left child is built before the right.**
2. **Returning `node` at the end ensures that each subtree is built correctly.**
3. **At the end, the very first call to `dfs()` returns the root of the entire reconstructed tree.**
4. **Index is shared across recursive calls, which ensures correct traversal order.**

Would you like me to help debug your case further with print statements?


### BFS VS DFS result list
- **BFS: ['1', '2', 'N', 'N', '3', 'N', 'N']**
- **DFS: ['1', '2', 'N', '3', 'N', 'N', 'N']**
  - you can find extra N here since we recurse in depth