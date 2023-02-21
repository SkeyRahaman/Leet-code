#User function Template for python3
from collections import deque
class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        # print(
        #     x+y-2,
        #     x+M-y-1,
        #     M-y+N-x,
        #     N-x+y-1
        #     )
        return max(
            x+y-2,
            x+M-y-1,
            M-y+N-x,
            N-x+y-1
            )


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends