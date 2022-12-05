#User function Template for python3
from collections import deque
class Solution:
    def shotestPath(self, grid, n, m, k):
        if k >= m + n - 2:                     #early return
            return m + n - 2
        visited = set()
        q = deque([[0,0,k,0]])
        visited = set([(0,0,k)])
        
        
        while len(q) != 0:
            x,y,wall,step = q.popleft()
            if x == n-1 and y == m-1:return step
            for i,j in [[-1,0],[0,1],[1,0],[0,-1]]:
                new_x = x+i
                new_y = y+j
                if 0<=new_x<n and 0<=new_y<m:
                    if grid[new_x][new_y] == 1:
                        if wall>0 and (new_x,new_y,wall-1) not in visited:
                            visited.add((new_x,new_y,wall-1))
                            q.append([new_x,new_y,wall-1,step+1])
                    elif (new_x,new_y,wall) not in visited:
                        visited.add((new_x,new_y,wall))
                        q.append([new_x,new_y,wall,step+1])
        return -1
        
            
        # code here 

    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m,k=map(int,input().split())
        mat=[]
        for i in range(n):
            row = list(map(int,input().split()))
            mat.append(row)
        
        ob = Solution()
        print(ob.shotestPath(mat,n,m,k))
# } Driver Code Ends