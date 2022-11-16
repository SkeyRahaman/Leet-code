#User function Template for python3
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        # print(V,adj)
        visited = set()
        v2 = set()
        def dfs(node):
            # print(node,v2,node in v2)
            if node in v2:
                return 1
            if node in visited:
                return 0
            v2.add(node)
            visited.add(node)
            for i in adj[node]:
                if dfs(i) == 1:return 1
            v2.remove(node)
            return 0
        for i in range(V):
            if i not in visited:
                if dfs(i) == 1:return True
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends