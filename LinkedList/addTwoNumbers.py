# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum1 = length1 = length2 = 0
        dummy = ListNode()
        res = dummy
        
        # calculate length of list 1
        current = l1
        while current:
            length1 += 1
            current = current.next
            
        # calculate length of list 2
        current = l2
        while current:
            length2 += 1
            current = current.next
            
        # calculate sum of list2
        copyLength = length1
        while l1:
            sum1 += (l1.val *(10**copyLength))
            l1 = l1.next
            copyLength -= 1
        copyLength = length2
        
        # calculate sum of list2
        current = l2
        while current:
            sum1 += (current.val *(10**copyLength))
            current = current.next
            copyLength -= 1
            
        # convert sum to linked list
        while sum1:
            res.next = ListNode(sum1 % 10)
            res = res.next
            sum1 //= 10
            
        return dummy.next
        