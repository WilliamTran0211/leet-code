from typing import Any, Optional


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


def print_list(lst):
    values = []
    while lst is not None:
        values.append(lst.val)
        lst = lst.next
    return values


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        print(print_list(head))

        tmp = []

        node = head

        while node is not None:

            tmp.append(node)

            node = node.next

        # keys = tmp.keys()

        middle = len(tmp) // 2

        print(tmp)

        print(middle)

        return []


my_list = [1, 2, 3, 4, 5, 6]

linked_list = create_linked_list(my_list)


sol = Solution()
print(sol.middleNode(linked_list))
