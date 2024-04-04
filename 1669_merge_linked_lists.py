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
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        head = list1
        count_to = 0
        prev_a = None
        while head is not None:
            current = prev_a
            if count_to < a:
                new_node = ListNode(head.val)

            if count_to == a:
                new_node = ListNode(list2.val, next=list2.next)

            if prev_a is None:
                prev_a = new_node
            else:
                if count_to <= a:
                    while current.next:
                        current = current.next
                    current.next = new_node
                if count_to == b:
                    tail = head.next
                    while current:
                        if current.next is None:
                            current.next = tail
                            break
                        current = current.next

                    break
            head = head.next
            count_to += 1
        return prev_a


sol = Solution()

arr_1 = [0, 1, 2]
arr_2 = [1000000, 1000001, 1000002, 1000003]

list1 = create_linked_list(arr_1)
list2 = create_linked_list(arr_2)
a, b = 1, 1

print(
    "======================================\n fin solution: ",
    sol.mergeInBetween(list1, a, b, list2),
)
