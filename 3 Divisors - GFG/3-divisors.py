#User function Template for python3

from math import sqrt,ceil,floor
class Solution:
	def threeDivisors(self, query, q):
		# code here
		n = max(query)
		n = sqrt(n)
# 		print(ceil(n))
		dp = [True] * (ceil(n)+1)
		dp[0] = dp[1] = False
		for i in range(ceil(n)+1):
		    if dp[i]:
    		    a = 2
    		    while i*a<ceil(n):
    		        dp[i*a] = False
    		        a += 1
    # 	print(dp)
		mem = [0] *  (ceil(n)+1)     
		c = 0
		for j,i in enumerate(dp):
		    if i:c += 1
		    mem[j] = c
		
# 		print(mem)
		return [mem[floor(sqrt(i))] for i in query]


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends