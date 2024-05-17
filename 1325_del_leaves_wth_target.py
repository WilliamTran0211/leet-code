"""
1325. Delete Leaves With a Given Value
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:



Input: root = [1,2,3,2,None,2,4], target = 2
Output: [1,None,3,None,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,None,None,2]
Example 3:



Input: root = [1,2,None,2,None,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

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
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)

        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root

    def removeLeafNodesStack(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        stack = [root]
        visited = set()
        parents = {root: None}
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]

                    if not p:
                        return None
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif node not in visited:
                visited.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node

        return root


sol = Solution()
root_lst = [1, 2, 3, 2, None, 2, 4]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.removeLeafNodes(root, 2))

# root_lst = [1, 3, 3, 3, 2]
# root = grow_a_tree_from_list(root_lst)
# print("ans: ", sol.removeLeafNodes(root, 3))

# root_lst = [1, 2, None, 2, None, 2]
# root = grow_a_tree_from_list(root_lst)
# print("ans: ", sol.removeLeafNodes(root, 2))

# root_lst = [2, 2, None, 2, None, 2]
# root = grow_a_tree_from_list(root_lst)
# print("ans: ", sol.removeLeafNodes(root, 2))

# root_lst = [
#     1,
#     2,
#     2,
#     3,
#     None,
#     None,
#     3,
#     4,
#     None,
#     None,
#     4,
#     5,
#     None,
#     None,
#     5,
#     5,
#     None,
#     None,
#     5,
#     5,
#     None,
#     None,
#     5,
#     5,
#     None,
#     None,
#     5,
# ]
# root = grow_a_tree_from_list(root_lst)
# print("ans: ", sol.removeLeafNodes(root, 5))
