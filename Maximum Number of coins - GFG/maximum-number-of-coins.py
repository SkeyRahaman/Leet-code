#User function Template for python3

class Solution():
    def maxCoins(self, n, nums):
        #your code goes here
        dp = [[0] * (len(nums)+1) for _ in range(len(nums)+1)]
        for start in range(len(nums)-1,-1,-1):
            for end in range(start,len(nums)):
                mini_cost = 0
                left = 1 if start < 1 else nums[start-1]
                right = 1 if end>len(nums)-2 else nums[end+1]
                product = left * right
                for i in range(start,end+1):
                    cost = product*nums[i]
                    mini_cost = max(mini_cost,cost+dp[start][i-1] + dp[i+1][end])
                dp[start][end] =  mini_cost
        # print(dp[0])
        return dp[0][len(nums)-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(Solution().maxCoins(n, a))
# } Driver Code Ends