class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getSize(l1) < self.getSize(l2):
            maxl = l2
            minl = l1
        else:
            maxl = l1
            minl = l2

        index = - self.getSize(maxl) - 1
        head = maxl
        while (head != None):
            index += 1
            head.val += self.get(abs(index), minl)[0]
            head = head.next
        return self.ret(maxl)

    def ret(self, head, depth=1):
        flag = False
        if head.next != None:
            flag = self.ret(head.next, depth + 1)
        if flag:
            head.val += 1
        if head.val >= 10:
            head.val = head.val % 10
            if depth == 1:
                print("进入")
                pre = ListNode(1)
                pre.next = head
                head = pre
                return head
            return True
        else:
            if depth == 1:
                return head
            return False

    def getSize(self, head):
        return 1 + self.getSize(head.next) if head != None else 0

    def get(self, index, head):
        ret = [0, -1]
        if head.next != None:
            ret = self.get(index, head.next)

        if head.next == None:
            ret[1] = 1
        else:
            ret[1] += 1
        if ret[1] == index:
            ret[0] = head.val
        return ret

