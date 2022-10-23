class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        dp = [[-1] * (2*S+5) for i in nums]
        @cache
        def helper(i,m):
            if i == 0:
                output = 0
                if m + nums[0] == target:
                    output += 1
                if m - nums[0] == target:
                    output += 1
                return output
            if dp[i][m] != -1:
                return dp[i][m]
            dp[i][m] =  helper(i-1,m+nums[i]) + helper(i-1,m-nums[i])
            return dp[i][m]
        
        x = helper(len(nums)-1,0)
        # print(dp)
        return x
        