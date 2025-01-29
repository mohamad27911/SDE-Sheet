# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        nodeIndex = length - n
        current = head
        if nodeIndex == 0:
            return current.next
        c = 1
        while current:
            if nodeIndex == c:
                current.next = current.next.next
                return head
            current = current.next
            c += 1
        return None
        