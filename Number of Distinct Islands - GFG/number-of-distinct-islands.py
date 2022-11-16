#User function Template for python3

import sys
from typing import List
class Solution:
    sys.setrecursionlimit(10**8)
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        visited = set()
        mem = set()
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and (row,col) not in visited:
                    q = [[row,col]]
                    output = []
                    while q:
                        r,c = q.pop()
                        if r<0 or c<0 or r>=n or c>=m or (r,c) in visited or grid[r][c] == 0:continue
                        visited.add((r,c))
                        output.append(r-row)
                        output.append(c-col)
                        q.append([r+1,c])
                        q.append([r-1,c])
                        q.append([r,c+1])
                        q.append([r,c-1])
                    mem.add(tuple(x for x in output))
                    
                    
        # print(mem) 
        return len(mem)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends