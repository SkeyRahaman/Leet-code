#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
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