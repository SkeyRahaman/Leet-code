#User function Template for python3

from typing import List
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
        # print(self.size, self.par)

    def check_same_set(self, a, b):
        return self.find_u_par(a) == self.find_u_par(b)

class Solution:
    def numOfIslands(self, n: int, m : int, operators : List[List[int]]) -> List[int]:
        # code here
        dj = DisjointSet(n*m)
        mem = [[0] * m for _ in range(n)]
        output = []
        iland = 0
        for i ,j in operators:
            if mem[i][j] == 1:
                output.append(iland)
                continue
            merging = set()
            for x,y in [[0,1],[0,-1],[1,0],[-1,0]]:
                a = i + x
                b = j + y
                if 0<=a<n and 0<=b<m and mem[a][b] == 1:
                    # if i == 1 and j == 2:
                        # print(a,b,dj.find_u_par((a*m)+b))
                    merging.add(dj.find_u_par((a*m)+b))
            # print(i,j,merging)
            for zz in merging:
                dj.union_by_size((i*m)+j,zz)
            # print(dj.par)
            if len(merging) == 0:
                iland += 1
            else:
                iland -= (len(merging) - 1)
            output.append(iland)
            mem[i][j] = 1
        return output
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends