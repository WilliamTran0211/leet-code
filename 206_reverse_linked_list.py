"""

206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


"""

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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tracking = []
        # current = head
        # if current is not None:
        #     if current.next is not None:
        #         while current.next:
        #             tracking.append(current.val)
        #             current = current.next
        #         tracking.append(current.val)
        #         tracking.reverse()

        # return create_linked_list(tracking)

        current = head

        return head


sol = Solution()

list = [1, 2, 3, 4, 5]
head = create_linked_list(list)
print(sol.reverseList(head))

# list = [1, 2]
# head = create_linked_list(list)
# print(sol.reverseList(head))

# list = [1]
# head = create_linked_list(list)
# print(sol.reverseList(head))
