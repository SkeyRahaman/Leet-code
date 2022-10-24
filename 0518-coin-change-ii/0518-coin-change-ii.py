class Solution:
    def change(self, t: int, nums: List[int]) -> int:
        dp = [[0] * (t+1) for _ in nums]
        for i in range(t+1):
            if i%nums[0] == 0:
                dp[0][i] = 1
        for i in range(1,len(nums)):
            for j in range(t+1):
                notTake = dp[i-1][j]
                take = 0
                if nums[i] <= j:
                    take = dp[i][j-nums[i]]
                dp[i][j] =  take + notTake
        return dp[len(nums)-1][t]

        
        
        
        
        
        
        dp = [[-1] * (t+1) for _ in nums]
        def helper(i,t):
            if i == 0:
                if t%nums[0]==0:
                    return 1
                else:
                    return 0
            if dp[i][t] != -1:
                return dp[i][t]
            notTake = helper(i-1,t)
            take = 0
            if nums[i] <= t:
                take = helper(i,t-nums[i])
            dp[i][t] =  take + notTake
            return dp[i][t]
        return helper(len(nums)-1,t)
            