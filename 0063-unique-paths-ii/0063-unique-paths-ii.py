class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        
        
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for j in range(len(obstacleGrid)):
            if obstacleGrid[j][0] == 1:
                dp[0] = 0
            for i in range(1,len(obstacleGrid[0])):
                if obstacleGrid[j][i] == 0:
                    dp[i] = dp[i] + dp[i-1]
                else:
                    dp[i] = 0
            print(dp)
        return dp[-1]
        