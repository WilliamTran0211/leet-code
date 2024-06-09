"""
2816. Double a Number Represented as a Linked List
You are given the head of a non-empty linked list representing 
a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189.
 Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

trả về kết quả là 1 linked list với các phần tử là kết quả của phép nhân đôi linked list ban đầu
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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = ""

        current = head

        while current:
            tmp += str(current.val)
            current = current.next

        cal_res = int(tmp) * 2

        tmp_list = list(str(cal_res))

        new_head = ListNode(tmp_list[0])
        current = new_head
        for n in tmp_list[1:]:
            current.next = ListNode(n)
            current = current.next

        return new_head


sol = Solution()
head = create_linked_list([1, 8, 9])
print("asn: ", sol.doubleIt(head))

head = create_linked_list([9, 9, 9])
print("asn: ", sol.doubleIt(head))

head = create_linked_list([1, 8, 9, 2, 3])
print("asn: ", sol.doubleIt(head))
