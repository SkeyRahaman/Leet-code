class Solution:
    def maxProfit(self, k: int, v: List[int]) -> int:
        n = len(v)
        dp = [[[0,0] for _ in range(k+1)] for i in range(n+ 1)]
        last = [[0,0] for _ in range(k+1)]
        cur = [[0,0] for _ in range(k+1)]
        for i in range(n-1,-1,-1):
            for j in range(1,k+1):
                cur[j][0] = max( v[i] +last[j-1][1],  last[j][0] )
                cur[j][1] = max(-v[i] +last[j][0],    last[j][1] )
            last = [x[::] for x in cur]
        # print(dp)
        return last[k][1]
        
        
        
        
        
        
        
        
        
        
        
        
        n = len(v)
        dp = [[[-1,-1] for _ in range(k+2)] for i in range(n)]
        # @cache
        def f(i,k,b):
            if i==n or (b and k<=0) :return 0
            
            if dp[i][k][b] != -1:return dp[i][k][b]
            if b:
                dp[i][k][b] = max(-v[i] + f(i+1,k-1,0),f(i+1,k,1))
            else:
                dp[i][k][b] =  max( v[i] +f(i+1,k,1),f(i+1,k,0) )
            return dp[i][k][b]
        return f(0,k,1)
            
        