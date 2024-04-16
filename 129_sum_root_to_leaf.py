"""
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

example 1:
Input: root = [1,2,3]

      1
    /   \
   2     3 

Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


example 2:
Input: root = [4,9,0,5,1]
            4
           / \
          9   0   
        /   \
       5     1
        
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        his = []
        count_deep = 0

        def get_numbers(his, root, tmp, is_left=False):
            if root:
                nonlocal count_deep
                tmp.append(str(root.val))
                print(tmp)
                if root.left and root.left.val is not None:
                    get_numbers(his, root.left, tmp, is_left=True)
                    count_deep += 1
                if root.right and root.right.val is not None:
                    get_numbers(his, root.right, tmp, is_left=False)
                    count_deep += 1
                if root.left is None and root.right is None:
                    print(tmp, count_deep, len(tmp), len(tmp) - 1 - count_deep)
                    his.append(int("".join(tmp)))
                    tmp = tmp[: len(tmp) - 1 - count_deep]
                    print("final", tmp)

        get_numbers(his, root, tmp=[], is_left=False)

        return sum(his)


sol = Solution()
root_lst = [1, 2, 3]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.sumNumbers(root))


root_lst = [4, 9, 0, 5, 1, 5, 2]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.sumNumbers(root))


root_lst = [6, 4, 1, 6, None, None, None, None, 4, 2, None, 6]
root = grow_a_tree_from_list(root_lst)
print("ans: ", sol.sumNumbers(root))
