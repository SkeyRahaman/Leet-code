class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = []
        x = 0
        for i in grid[0]:
            x += i
            dp.append(x)
        for i in range(1,len(grid)):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1,len(grid[0])):
                dp[j] = grid[i][j] + min(dp[j],dp[j-1])
                
            print(dp)
        return dp[-1]
        