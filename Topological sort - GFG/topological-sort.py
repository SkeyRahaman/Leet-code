from collections import defaultdict,deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        indeg = defaultdict(int)
        for i in range(V):
            for n in adj[i]:
                indeg[n] += 1
        # print(indeg)
        
        q = deque()
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        output = []
        while q:
            node = q.popleft()
            output.append(node)
            for i in adj[node]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        return output
                
                
                
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Code here
        visited = set()
        output = []
        def dfs(node):
            if node in visited:return 
            visited.add(node)
            for i in adj[node]:
                dfs(i)
            output.append(node)
            # print(output)
        for n in range(V):
            if n not in visited :dfs(n)
        # print(output)
        return output[::-1]



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends