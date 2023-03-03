#User function Template for python3

class Solution:
    def minimumSquares(self, L, B):
        # code here
        def computeGCD(x, y):
            while(y):
               x, y = y, x % y
            return abs(x)
        n = computeGCD(L,B)
        return (L//n)*(B//n),n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends