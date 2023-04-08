#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        output = []
        for i in arr:
            if len(output)!=0 and ((output[-1]<0 and i>=0) or (i<0 and output[-1]>=0)):
                output.pop()
            else:
                output.append(i)
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends