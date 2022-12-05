#User function Template for python3
import heapq
class DisjointSet:
    def __init__(self, length: int):
        self.size = [1] * length
        self.par = [i for i in range(length)]

    def find_u_par(self, node):
        if self.par[node] != node:
            self.par[node] = self.find_u_par(self.par[node])
        return self.par[node]

    def union_by_size(self, a, b):
        par_a = self.find_u_par(a)
        par_b = self.find_u_par(b)
        if self.size[par_a] > self.size[par_b]:
            self.size[par_a] += self.size[par_b]
            self.par[par_b] = par_a
        else:
            self.size[par_b] += self.size[par_a]
            self.par[par_a] = par_b

    def check_same_set(self, a, b):
        return self.find_u_par(a) == self.find_u_par(b)
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        edg = []
        for i in range(V):
            for j,w in adj[i]:
                edg.append([w,i,j])
        edg.sort(key = lambda x :x[0])
        # print(edg)
        output = 0
        dj = DisjointSet(V+1)
        for w,i,j in edg:
            if not dj.check_same_set(i,j):
                # print(i,j)
                dj.union_by_size(i,j)
                output += w
        return output
        
        
        
        
        
        
        
        
        
        
        # Prime's Algorithm
        heap = []
        heapq.heappush(heap, (0,0,-1))
        visited = set()
        mst = []
        output = 0
        while len(heap) != 0:
            cost, node, frm = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            mst.append([frm,node])
            output += cost
            for i,j in adj[node]:
                heapq.heappush(heap, (j,i,node))
        return output
            
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends