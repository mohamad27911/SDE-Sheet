class Node:
    data = None
    next = None
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    head = None
    def __init__(self):
        self.head= Node()
        
    def append(self, data):
        node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
        
    def length(self):
        current = self.head
        count = 0
        while current.next != None:
            count+=1
            current = current.next
        return count
    
    def get(self, index):
        c = 0
        current = self.head
        while current.next != None and c <= index:
            c += 1
            current = current.next
        return current.data
    
    def delete(self, index):
        if index == 0:
            self.head = self.next
        elif index >= self.length():
            return
        else: 
            current = self.head
            c = 0
            while current.next != None and c <= index-1:
                current = current.next
                c += 1
            current.next = current.next.next
        
        
    def display(self):
        arr =[]
        current = self.head
        while current.next != None:
            current = current.next
            arr.append(current.data)
        print(arr)
                
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print("length: "+ ll.length())
print(ll.get(1))
ll.display()