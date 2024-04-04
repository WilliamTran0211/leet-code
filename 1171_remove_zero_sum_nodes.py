"""
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]


"""


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


from typing import Optional


class Solution:
    def removeZeroSumSubLists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_sum = head.val
        tmp_list = []
        while head is not None:
            current_val = head.val
            if head.next is not None:
                next_val = head.next.val
                print("current ", current_val)
                print("next ", next_val)
                tmp_sum += next_val

                print("current_sum ", tmp_sum)

                if tmp_sum > 0:
                    tmp_list.append(head)
                    head = head.next
                else:
                    head = head.next.next
            else:
                break

        for item in tmp_list:
            print(item)

        return []


my_list = [1, 2, -3, 3, 1]
my_list = [1, 2, 3, -3, 4]

linked_list = create_linked_list(my_list)

sol = Solution()

print(sol.removeZeroSumSubLists(linked_list))
