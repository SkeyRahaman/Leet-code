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
    def numProvinces(self, adj, V):
        # code here 
        dj = DisjointSet(V)
        for i in range(V):
            for j in range(i+1,V):
                if adj[i][j] == 1:
                    dj.union_by_size(i,j)
        output = set()
        for i in range(V):
            output.add(dj.find_u_par(i))
        # print(dj.par)
        return len(output)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends