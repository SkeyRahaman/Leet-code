class Solution:
    def change(self, t: int, nums: List[int]) -> int:
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
            