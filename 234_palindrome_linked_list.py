"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.


Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next is None:
            return True
        elif head.next.next is None:
            if head.next.val != head.val:
                return False
            else:
                return True
        else:
            current = head
            res = []

            while current:
                res.append(current.val)

                current = current.next

        return res == res[::-1]


sol = Solution()

arr = [1, 2, 3, 2, 1]
linked = create_linked_list(arr)
print(arr, "this must be TRUE, ans: ", sol.isPalindrome(linked))

# arr = [1, 2]
# linked = create_linked_list(arr)
# print(arr, "this must be False, ans: ", sol.isPalindrome(linked))

# arr = [1, 1]
# linked = create_linked_list(arr)
# print(arr, "this must be TRUE, ans: ", sol.isPalindrome(linked))


arr = [1, 2, 3, 2, 3, 1]
linked = create_linked_list(arr)
print(arr, "this must be FALSE, ans: ", sol.isPalindrome(linked))
