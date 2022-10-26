class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        last = [0] * (len(s2)+1)
        crr = [0] * (len(s2)+1)
        for j in range(len(s2)+1):
            last[j] = j
            
        for i in range(1,len(s1)+1):
            crr[0] = i
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    crr[j] =   last[j-1]
                else:
                    crr[j] =  1 + min(crr[j-1],last[j],last[j-1])
            last = [z for z in crr]
        return last[len(s2)]

        
        
        
        
        
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
        