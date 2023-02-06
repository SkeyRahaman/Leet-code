#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def verticallyDownBST(self, rt, target):
        #code here
        def find(root):
            nonlocal T
            output = -1
            if root.data == target:
                return root
            else:
                if root.left:
                    output = find(root.left)
                    if output != -1:
                        return output
                if root.right:
                    output = find(root.right)
                    if output != -1:
                        return output
            return output
        def dfs(node,deg):
            nonlocal ans
            if deg == 0:
                ans+=node.data
            if node.left:
                dfs(node.left,deg-1)
            if node.right:
                dfs(node.right,deg+1)
        T = -1
        rt = find(rt)
        if rt == -1:return rt
        ans = -rt.data
        dfs(rt,0)
        return ans 
            
                    

#{ 
 # Driver Code Starts.

from collections import defaultdict
from collections import deque
from sys import stdin, stdout
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        target = int(input())
        N = input()
        root = buildTree(N)
        res = Solution().verticallyDownBST(root, target)
        print(res)
# } Driver Code Ends