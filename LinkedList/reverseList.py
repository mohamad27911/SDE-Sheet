# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current != None:
            nextNode = current.next
            nextNode.next = prev
            prev = current
            current = nextNode
        return head
    
        