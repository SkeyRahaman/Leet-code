class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * target for i in range(n)]
        def check(d,f,t):
            if t<0:
                return 0
            if d == 0 and t == 0:
                return 1
            if (d==0 and t != 0) or (d!=0 and t==0) :
                return 0
            if dp[d-1][t-1] != -1:
                return dp[d-1][t-1]
            
            output = 0
            for i in range(1,f+1):
                if t-i<0:
                    break
                output += check(d-1,f,t-i)
            dp[d-1][t-1] = output
            return output
        return check(n,k,target)%1000000007