class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        M = len(grid)
        @cache
        def helper(i,j1,j2):
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
            
            return maxi
                
                

        return helper(0,0,N-1)