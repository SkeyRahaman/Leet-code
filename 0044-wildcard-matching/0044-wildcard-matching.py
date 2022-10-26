class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        last = [False] * (len(p)+1)
        cur  = [False] * (len(p)+1)
        last[0] = True
        for j in range(1,len(p)+1):
            last[j] = "*"*(j) == p[:j]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    cur[j] = last[j-1]
                elif p[j-1] == "*":
                    if cur[j-1]:cur[j] = True
                    else:cur[j] = last[j]
                else:
                    cur[j] =  False
            last = cur[::]
        return last[len(p)]
        
        
        
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1,len(p)+1):
            dp[0][j] = "*"*(j) == p[:j]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if dp[i][j-1]:dp[i][j] = True
                    else:dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] =  False
        return dp[len(s)][len(p)]
        
        
        
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
        