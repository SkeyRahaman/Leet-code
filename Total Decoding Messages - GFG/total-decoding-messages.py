#User function Template for python3

class Solution:
	def CountWays(self, str):
		# Code here
		dp = [-1] * len(str)
		def f(node):
		    output = 0
		    if node == len(str):
		        return 1
		    if dp[node] != -1:
		        return dp[node]
		    if str[node] != '0':
		        output += f(node+1)
		    if str[node] != '0' and node+1<len(str) and 0<int(str[node:node+2])<=26:
		        output += f(node+2)
		    dp[node] = output%1000000007
		    return dp[node]
		return f(0)
		    
		        
		  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends