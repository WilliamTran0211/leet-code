"""
404. Sum of Left Leaves
Easy
Topics
Companies
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

example 1:

Input: root = [3,9,20,null,null,15,7]

    3
  /    \
9       20
      /    \
    15      7

Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"  # Py 3.6


def iterativePreOrder(root: Optional[TreeNode]):
    # without RECURSIVE
    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while len(nodeStack) > 0:

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.val, end=" ")

        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)


def printPreOrder(root):

    if root:
        print(root.val, end=" ")
        printPreOrder(root.left)
        printPreOrder(root.right)


def grow_a_tree(root_list: List[int], i=0) -> Optional[TreeNode]:
    if not root_list or i >= len(root_list):
        return None  # Base case: Empty list or out of bounds

    root = TreeNode(root_list[i])  # Create root node with current value

    # Recursively build left and right subtrees
    root.left = grow_a_tree(root_list, 2 * i + 1)  # Left child at 2*i + 1
    root.right = grow_a_tree(root_list, 2 * i + 2)  # Right child at 2*i + 2

    return root


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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        res = []

        def get_left_leaf(res, root, is_left=False):
            if root:
                if root.left and root.left.val is not None:
                    get_left_leaf(res, root.left, is_left=True)
                if root.right and root.right.val is not None:
                    get_left_leaf(res, root.right)
                if root.left is None and root.right is None and is_left == True:
                    res.append(root.val)

        get_left_leaf(res, root)

        return sum(res)


sol = Solution()

list_root = [3, 9, 20, None, None, 15, 7]
root = grow_a_tree_from_list(list_root)
print(root)
print("Ans: ", sol.sumOfLeftLeaves(root))


# list_root = [3, 9, 20, 4, 2, 3, 1, None, None, None, None, 12, 4, 15, 7, 6]
# root = grow_a_tree(list_root)
# print("Ans: ", sol.sumOfLeftLeaves(root))
