# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:     
    def mergeTwoLists(list1, list2):
        lst = list1+list2

        lst.sort()

        return lst

test = Solution
print(test.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))