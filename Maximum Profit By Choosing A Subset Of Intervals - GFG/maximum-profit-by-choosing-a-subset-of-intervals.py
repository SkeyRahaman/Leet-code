from typing import List

from sortedcontainers import SortedList
class Solution:
    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
        # code here
        data = sorted(intervals,key=lambda x:x[1])
        output = 0
        dp = SortedList()
        dp.add([0,0])
        for s,e,p in data:
            ptr = dp.bisect_right([s,float('inf')])-1 # dp.bisect_right([s,p])-1
            # print(dp,s,e,p,ptr)
            if dp[ptr][1] + p > dp[-1][1]:
                dp.add([e,dp[ptr][1] + p])
        # print(dp)
        return dp[-1][1]
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maximum_profit(n, intervals)
        
        print(res)
        

# } Driver Code Ends