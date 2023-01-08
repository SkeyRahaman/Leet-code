#User function Template for python3
from collections import deque

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    def mergell(ptr1,ptr2):
        output = Node(-1)
        ptr = output
        while ptr1 and ptr2:
            if ptr1.data <= ptr2.data:
                node = ptr1
                ptr1 = ptr1.bottom
            else:
                node = ptr2
                ptr2 = ptr2.bottom
            node.bottom = None
            ptr.bottom = node
            ptr = ptr.bottom
        if ptr1:
            ptr.bottom = ptr1
        if ptr2 :
            ptr.bottom = ptr2
        return output.bottom
        
    q = deque()
    ptr = root
    while ptr :
        q.append(ptr)
        ptr = ptr.next
    while len(q) != 1:
        l1 = q.popleft()
        l2 = q.popleft()
        q.appendleft(mergell(l1,l2))
    return q.popleft()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag == 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 == 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends