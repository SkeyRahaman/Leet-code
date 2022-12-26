#User function Template for python3
import bisect
class Solution:
    def __init__(self):
        self.output = []
    def solve (self, L, R):
        # print(self.output[:20])
        l = bisect.bisect_left(self.output, L)
        r = bisect.bisect_right(self.output, R)
        return r-l
        
        # code here
    def precompute (self):
        for i in range(63):
            for j in range(i+1,63):
                for k in range(j+1,63):
                    # A = 
                    # print(i,j,k,A)
                    self.output.append((1<<i) | (1<<j) | (1<<k))
        self.output.sort()
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)




# } Driver Code Ends