
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(-1).next=head
        pre = dummyHead
        while pre.next!=None:
            if pre.next.val==val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummyHead.next
