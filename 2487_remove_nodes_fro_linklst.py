"""
2487. Remove Nodes From Linked List
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "val: " + str(self.val) + " | next: " + str(self.next)


def create_linked_list(my_list):
    head = None
    for idx, item in enumerate(my_list):
        new_node = ListNode(item)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
    return head


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            # the code below is monotonic stack
            while stack and current.val > stack[-1]:
                stack.pop()
            stack.append(current.val)
            current = current.next

        new_head = ListNode()
        current = new_head
        for n in stack:
            current.next = ListNode(n)
            current = current.next

        return new_head.next


sol = Solution()
input_lst = [5, 2, 13, 3, 8]
head = create_linked_list(input_lst)
print("ans: ", sol.removeNodes(head))


input_lst = [1, 1, 1, 1, 1]
head = create_linked_list(input_lst)
print("ans: ", sol.removeNodes(head))


input_lst = [19, 2, 13, 3, 8, 1, 4, 12, 6, 1, 21]
head = create_linked_list(input_lst)
print("ans: ", sol.removeNodes(head))


input_lst = [5, 2, 13, 3, 8, 1, 4, 12, 6, 1]
head = create_linked_list(input_lst)
print("ans: ", sol.removeNodes(head))
