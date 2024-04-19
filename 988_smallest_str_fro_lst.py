"""
988. Smallest String Starting From Leaf

You are given the root of a binary tree where each node has a value in the range [0, 25] 
representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:
Input: root = [0,1,2,3,4,3,4]
        0                                         
      /   \
     1     2
    / \   / \
   3  4  3   4 
      
       ||

        a
      /   \
     b     c
    / \   / \
   d  e  d   e 
       
Output: "dba"

Example 2:
root = [25,1,3,1,3,0,2]
        25                                         
      /   \
     1     3
    / \   / \
   1  3  0   2 
      
       ||

        z
      /   \
     b     d
    / \   / \
   b  d  a   c 
       
Output: "adz"


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
    # this is better because it dont create node with None value for example leaf nodes cases
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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # number to characters in alphabet a = 97, b = 98, .... then a = 0 + 97, b = 1 + 97

        res = []

        def get_characters(res, root, tmp=[]):
            if root:
                tmp.append(chr(root.val + 97))
                if root.left and root.left.val is not None:
                    get_characters(res, root.left, tmp)
                if root.right and root.right.val is not None:
                    get_characters(res, root.right, tmp)
                if root.left is None and root.right is None:
                    rev = tmp[::-1]
                    if len(res) == 0:
                        res.extend(rev)
                    else:
                        if "".join(res) > "".join(rev):
                            res.clear()
                            res.extend(rev)
                tmp.pop(-1)

        get_characters(res, root, tmp=[])

        return "".join(res)


sol = Solution()
root_lst = [0, 1, 2, 3, 4, 3, 4]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.smallestFromLeaf(root))


root_lst = [25, 1, 3, 1, 3, 0, 2]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.smallestFromLeaf(root))


root_lst = root = [2, 2, 1, None, 1, 0, None, 0]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.smallestFromLeaf(root))
