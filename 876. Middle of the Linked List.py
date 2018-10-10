# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head, depth=1, stop=-1):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if stop == -1:
            stop = (self.getSize() + 1) // 2
        return head if depth == stop else self.middleNode(hean.next, depth + 1, stop)

    def getSize(self, head):
        return 1 + self.getSize(head.next) if head.next != Nonde else 0
