
class Solution(object):
    def middleNode(self, head):
      
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        middle_index = length // 2
        
        current = head
        for _ in range(middle_index):
            current = current.next
        
        return current
    def middleNode2(self, head):
      
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Alternative solution
