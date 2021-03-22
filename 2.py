# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode():
    pass

class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = p = ListNode()
        s = 0
        while l1 or l2 or s:
            s += l1.val if l1 else 0 + l2.val if l2 else 0
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            l1 = l1.next
            l2 = l2.next
        return dummy.next