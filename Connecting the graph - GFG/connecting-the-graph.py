#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
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
    def Solve(self, n, adj):
        # Code here
        unused = 0
        dj = DisjointSet(n)
        for i,j in adj:
            if not dj.check_same_set(i,j):
                dj.union_by_size(i,j)
            else:
                unused += 1
        union = set()
        for i in range(n):
            union.add(dj.find_u_par(i))
        union = len(union)
        # print(dj.par,union,unused)
        if union-1 <= unused:
            return union-1
        return -1
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends