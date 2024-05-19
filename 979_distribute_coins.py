"""
979. Distribute Coins in Binary Tree
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(current):

            if not current:
                return [0, 0]

            l_size, l_coin = dfs(current.left)
            r_size, r_coin = dfs(current.right)

            size = 1 + l_size + r_size
            coins = current.val + l_coin + r_coin

            self.res += abs(size - coins)
            return [size, coins]

        dfs(root)

        return self.res


sol = Solution()
root_lst = [3, 0, 0]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.distributeCoins(root))

root_lst = [0, 3, 0]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.distributeCoins(root))


root_lst = [0, 0, None, 4, 0]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.distributeCoins(root))
