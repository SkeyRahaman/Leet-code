class Solution:
    def maxDistance (self, arr, n) : 
        #Complete the function
        max1 = float('-inf')
        max2 = float('-inf')
        min1 = float('inf')
        min2 = float('inf')
        
        for i,j in enumerate(arr):
            max1 = max(max1,i+j)
            max2 = max(max2,i-j)
            
            min1 = min(min1,i+j)
            min2 = min(min2,i-j)
        return max(max1-min1,max2-min2)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = Solution().maxDistance(arr, n)
    print(ans)
    





# } Driver Code Ends