#User function Template for python3

class Solution:
    def uniquePaths(self, n, m, grid):
        # code here 
        dp  = [0] * m
        dp[0] = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dp[j] = 0
                else:
                    
                    if j != 0:
                        dp[j] += dp[j-1]
                        dp[j] %= (1000000007)
                        # print(i,j,dp)
        # print(dp)
        return dp[-1]
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        
        grid=[]
        for i in range(n):
            col = list(map(int,input().split()))
            grid.append(col)
        
        ob = Solution()
        print(ob.uniquePaths(n,m,grid))
# } Driver Code Ends