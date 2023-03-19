from typing import List
from collections import Counter,defaultdict

class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        # code here
        left = defaultdict(int)
        right = Counter(A)
        output = []
        for i in A:
            right[i] -= 1
            if right[i] == 0:
                del right[i]
            output.append(len(left)-len(right))
            left[i] += 1
        return output
        



#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends