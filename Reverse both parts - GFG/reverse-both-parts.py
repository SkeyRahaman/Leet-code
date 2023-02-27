
from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        def rev(node):
            output = None
            while node:
                tmp = node
                node = node.next
                tmp.next = output
                output = tmp
            return output
            
            
        ptr = head
        last = None
        for _ in range(k):
            last = ptr
            ptr = ptr.next
        last.next = None
        
        a = rev(head)
        b = rev(ptr)
        head.next = b
        return a
        
        
        
        
        
        return rev(head)
        # code here
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.reverse(head, k)
        
        printList(res)
        

# } Driver Code Ends