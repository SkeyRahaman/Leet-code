class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1] * len(p) for _ in range(len(s))]
        def helper(i,j):
            #base case
            if i == -1 and j==-1:
                return True
            if j == -1:
                return False
            if i == -1:
                return "*"*(j+1) == p[:j+1]
            if dp[i][j] != -1:return dp[i][j]
            if s[i] == p[j] or p[j] == "?":
                dp[i][j] = helper(i-1,j-1)
            elif p[j] == "*":
                if helper(i,j-1):dp[i][j] = True
                else:dp[i][j] = helper(i-1,j)
            else:
                dp[i][j] =  False
            return dp[i][j]
        return helper(len(s)-1,len(p)-1)
        