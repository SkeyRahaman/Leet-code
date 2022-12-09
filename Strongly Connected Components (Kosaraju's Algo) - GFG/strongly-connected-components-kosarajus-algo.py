#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        STACK = []
        visited1 = set()
        visited2 = set()
        def dfs1(node):
            visited1.add(node)
            for i in adj[node]:
                if i not in visited1:
                    dfs1(i)
            STACK.append(node)
        def dfs2(node):
            visited2.add(node)
            for i in adj2[node]:
                if i not in visited2:
                    dfs2(i)
        
        for i in range(V):
            if i not in visited1:
                dfs1(i)
        adj2 = [[] for _ in range(V)]
        for i,tos in enumerate(adj):
            for j in tos:
                adj2[j].append(i)
        
        output = 0
        while STACK:
            node = STACK.pop()
            if node not in visited2:
                output += 1
                dfs2(node)
            
                
                
        # print(adj,adj2,STACK)
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends