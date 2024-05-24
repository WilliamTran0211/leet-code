"""
2331. Evaluate Boolean Binary Tree
You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:
Input: root = [2,1,3,null,null,0,1]
Output: true

      OR
    /   \
 True   AND
        /  \
    False  True     

    => False AND True = FALSE
      |
      V

      OR
    /   \
 True   False

    => True OR False = TRUE (that is the answer)

Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.

Example 2:
Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.

** post order DFS
link: https://www.youtube.com/watch?v=9a_cP54jn8Q
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"  # Py 3.6


def grow_a_tree_from_list(root_lst: List[int]) -> Optional[TreeNode]:
    # this is better because it dont create node with None value
    root_node = TreeNode(val=root_lst[0])
    nodes = [root_node]
    for i, val in enumerate(root_lst[1:]):
        if val is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2) == 0
        node = TreeNode(val=val)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if not root.left:
            return root.val == 1

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)

    def evaluateTreeStack(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        value = {}

        while stack:
            node = stack.pop()
            # leaf_node
            if not node.left:
                value[node] = node.val == 1
            # non leaf_node
            else:
                # children visited
                if node.left in value:
                    if node.val == 3:
                        value[node] = value[node.left] and value[node.right]
                    if node.val == 2:
                        value[node] = value[node.left] or value[node.right]
                # otherwise add children
                else:
                    stack.extend([node, node.left, node.right])

        return value[root]


sol = Solution()
root_lst = [2, 1, 3, None, None, 0, 1]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.evaluateTree(root))
