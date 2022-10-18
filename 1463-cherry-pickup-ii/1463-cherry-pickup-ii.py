
from copy import deepcopy
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        M = len(grid)
        # @cache
        front = [[-1] * N for _ in range(N)]
        cur = [[-1] * N for _ in range(N)]
        for i in range(M-1,-1,-1):
            for j1 in range(N):
                for j2 in range(N):
                    if i == M-1:
                        if j1 == j2:
                            cur[j1][j2] = grid[i][j1]
                        else:
                            cur[j1][j2] = grid[i][j1] + grid[i][j2]
                    else:
                        maxi = float('-inf')
                        for d1 in [-1,0,1]:
                            for d2 in [-1,0,1]:
                                if 0<=(j1+d1)<N and 0<=(j2+d2)<N :
                                    if j1 != j2:
                                        maxi = max(maxi,grid[i][j1] + grid[i][j2] + front[j1+d1][j2+d2])
                                    else:
                                        maxi = max(maxi,grid[i][j1] + front[j1+d1][j2+d2])
                        cur[j1][j2] = maxi
            front = deepcopy(cur)
            # cur = [[-1] * N for _ in range(N)]
        return front[0][N-1]
        
        
        
        
        
        
        
        
        
        
        
        N = len(grid[0])
        M = len(grid)
        # @cache
        dp = [[[-1] * N for _ in range(N)] for _ in range(M)]
        def helper(i,j1,j2):
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            if i == M-1:
                if j1 == j2 :return grid[i][j2]
                return grid[i][j1] + grid[i][j2]
            maxi = float('-inf')
            for d1 in [-1,0,1]:
                for d2 in [-1,0,1]:
                    if 0<=(j1+d1)<N and 0<=(j2+d2)<N :
                        if j1 != j2:
                            maxi = max(maxi,grid[i][j1] + grid[i][j2] + helper(i+1,j1+d1,j2+d2))
                        else:
                            maxi = max(maxi,grid[i][j1] + helper(i+1,j1+d1,j2+d2))
            
            dp[i][j1][j2] = maxi
            return maxi
                
                

        return helper(0,0,N-1)