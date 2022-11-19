#User function Template for python3

from typing import List
from collections import defaultdict
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        stack = []
        output = [float("inf")] * n
        visited = set()
        adj = defaultdict(list)
        for i,j,k in edges:
            adj[i].append([j,k])
        
        
        
        def dfs(node):
            if node in visited:return 
            visited.add(node)
            for i,k in adj[node]:
                dfs(i)
            stack.append(node)
        dfs(0)
        # print(stack)   
        output[0] = 0
        while stack:
            node = stack.pop()
            for i,k in adj[node]:
                pre = 0 if output[node] == float('inf') else output[node]
                output[i] = min(output[i],pre+k)
        
                
        # print(output)
        return [i if i != float('inf') else -1 for i in output]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends