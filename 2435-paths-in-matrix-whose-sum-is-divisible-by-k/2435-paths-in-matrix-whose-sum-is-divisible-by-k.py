class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mem = [[defaultdict(int) for _ in range(cols)] for _ in range(rows)]
        mem[0][0][grid[0][0]%k] = 1
        for i in range(rows):
            for j in range(cols):
                for key, value in mem[i][j].items():
                    #push in j +1
                    if j+1<cols:
                        mem[i][j+1][(key+grid[i][j+1])%k] += value
                    if i+1<rows:
                        mem[i+1][j][(key+grid[i+1][j])%k] += value
        return mem[-1][-1][0]%(10**9 + 7)
                        
        