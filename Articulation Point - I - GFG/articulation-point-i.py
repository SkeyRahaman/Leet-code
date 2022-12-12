#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        visited = set()
        output = [False] * V
        tin = [0] * V
        tmin = [0] * V
        self.count = 0
        def f(node,par):
            visited.add(node)
            self.count += 1
            tin[node] = tmin[node] = self.count
            cn = 0
            for i in adj[node]:
                if i == par:
                    continue
                if i in visited:
                    tmin[node] = min(tin[i],tmin[node])
                else:
                    cn += 1
                    f(i,node)
                    tmin[node] = min(tmin[i],tmin[node])
                    if tmin[i] >= tin[node] and par != -1:
                        output[node] = True
            if cn > 1 and par == -1:output[node] = True
                
        for i in range(V):
            if i not in visited:
                f(0,-1)
        output =  [i for i,j in enumerate(output) if j]
        return [-1] if len(output) == 0 else output


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends