class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
#         dp = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
#         for i in range(len(s1)-1,-1,-1):
#             for j in range(len(s2)-1,-1,-1):
#                 if s1[i] == s2[j]:
#                     dp[i+1][j+1]
        
        
        
        
        
        
        
        
        
        
        
        dp = [[-1] * (len(s2)+1) for i in range(len(s1)+1)]
        def helper(i,j):
            if i<0 or j<0:
                return 0 
            # print(i,j)
            if dp[i][j] != -1:
                return dp[i][j] 
            if s1[i] == s2[j]:
                dp[i][j]  = 1 + helper(i-1,j-1)
            else:
                dp[i][j] =  max(helper(i-1,j),helper(i,j-1))
            return dp[i][j] 
            
        return helper(len(s1)-1,len(s2)-1)
        