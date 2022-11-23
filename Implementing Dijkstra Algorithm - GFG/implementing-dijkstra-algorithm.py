import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        heap = []
        output = [float('inf') for _ in range(V)]
        heapq.heappush(heap,(0,S))
        output[S] = 0
        while heap:
            dis,ver = heapq.heappop(heap)
            # print(dis,ver)
            for i,j in adj[ver]:
                to_dis = j+dis
                if to_dis<output[i]:
                    heapq.heappush(heap,(to_dis,i))
                    output[i] = to_dis
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends