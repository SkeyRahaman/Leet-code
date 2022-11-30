#User function Template for python3

#User function Template for python3
from collections import deque
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        mem = deque()
        ptr = head
        while ptr:
            mem.append(ptr)
            ptr = ptr.next
        output = node(0)
        ptr = output
        while mem:
            ptr.next = mem.popleft()
            ptr = ptr.next
            if mem:
                ptr.next = mem.pop()
                ptr = ptr.next
        ptr.next = None
        return output.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends