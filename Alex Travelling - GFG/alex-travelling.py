#User function Template for python3

from typing import List
import heapq
from collections import defaultdict
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, kk : int) -> int:
        # code here
        d = [float("inf")] * (n+1)
        d[kk] = 0
        adj = defaultdict(list)
        for i,j,k in flights:
            adj[i].append([j,k])
        heap = []
        heapq.heappush(heap, (0,kk))
        
        while len(heap) != 0:
            dis,node = heapq.heappop(heap)
            for i,j in adj[node]:
                nd = dis + j
                if d[i] > nd:
                    d[i] = nd
                    heapq.heappush(heap, (nd,i))
        output = max(d[1:])

        return output if output != float("inf") else -1
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends