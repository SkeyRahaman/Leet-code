
from typing import List


class Solution:
    def maxCoins(self, N : int, arr : List[int]) -> int:
        # code here
        dp = [[-1] * N for _ in range(N)]
        def f(start,end):
            if start>end:return 0
            if dp[start][end] != -1:return dp[start][end]
            output = 0
            left = 1 if start<=0 else arr[start-1]
            right = 1 if end>=N-1 else arr[end+1]
            for i in range(start,end+1):
                cost = left*right*arr[i]
                output = max(output, cost + f(start,i-1) + f(i+1,end))
            dp[start][end] =  output
            return dp[start][end]
        return f(0,len(arr)-1)
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxCoins(N, arr)
        
        print(res)
        

# } Driver Code Ends