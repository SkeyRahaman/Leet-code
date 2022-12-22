#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        dp = defaultdict(int)
        #return: count of sub-arrays having their sum equal to 0
        count = 0
        dp[0] = 1
        output = 0
        for i in arr:
            count += i
            if dp[count] != 0:
                output += dp[count]
            dp[count] += 1
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends