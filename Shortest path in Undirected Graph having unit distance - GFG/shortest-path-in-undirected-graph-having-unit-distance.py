#User function Template for python3
from collections import deque, defaultdict
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        output = [float('inf') for i in range(n)]
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        q = deque()
        q.append([src,0])
        visited = set()
        while q:
            node,dis = q.popleft()
            output[node] = min(output[node],dis)
            if node not in visited:
                for i in adj[node]:
                    q.append([i,dis+1])
            visited.add(node)
        # print(output)
        return [-1 if i == float('inf') else i for i in output]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends