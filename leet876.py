# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current = head
        size = 0

        while current:
            size += 1
            current = current.next

        middle = size // 2
        current = head

        for _ in range(middle):
            current = current.next

        head = current

        return head