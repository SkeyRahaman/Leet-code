class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        mem = [i for i in range(n)]
        # print(mem)
        for i in range(m):
            
            for k,j in enumerate(mem):
                if j != -1:
                    if grid[i][j] == 1:
                        if j<n-1 and grid[i][j+1] == 1:
                            mem[k] = j+1
                        else:
                            mem[k] = -1
                    else:
                        if j>0 and grid[i][j-1] == -1:
                            mem[k] = j-1
                        else:
                            mem[k] = -1
            # print(mem)
        return mem
                        
        