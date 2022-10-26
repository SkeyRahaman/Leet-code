class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        dp = [[-1] * (len(s2)+1) for i in range(len(s1)+1)]
        def helper(i,j):
            if j == -1:
                return i +1
            if i == -1:
                return j + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] =   helper(i-1,j-1)
            else:
                insert = helper(i,j-1)
                delete = helper(i-1,j)
                replace = helper(i-1,j-1)
                dp[i][j] =  1 + min(insert,delete,replace)
            return dp[i][j]
        return helper(len(s1)-1,len(s2)-1)
        