class Solution:
    def maxProfit(self, v: List[int]) -> int:
        n = len(v)
        dp = [[[-1,-1,-1],[-1,-1,-1]] for i in v]
        def f(i,b,t):
            if i == n:return 0
            if b and t == 0:return 0
            if dp[i][b][t] != -1 :return dp[i][b][t]
            if b:
                dp[i][b][t] =  max(-v[i] + f(i+1,0,t-1),  f(i+1,1,t))
            else:
                dp[i][b][t] = max(+v[i] + f(i+1,1,t), f(i+1,0,t))
            return dp[i][b][t]
        return f(0,1,2)
        
        
        
        