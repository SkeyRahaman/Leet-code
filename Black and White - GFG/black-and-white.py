#User function Template for python3


#Function to find out the number of ways we can place a black and a white
#Knight on this chessboard such that they cannot attack each other.
def numOfWays(M, N):
    # code here
    def get(i,j):
        out = 0
        for x,y in [[-2,1],[-2,-1],[2,1],[2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]:
            x += i
            y += j
            if 0<=x<N and 0<=y<M:
                out += 1
        return out
    
    count = (N*M)**2 - (N*M)
    for i in range(N):
        for j in range(M):
            count -= get(i,j)
    return count%((10**9)+7) 
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m,n = map(int,input().strip().split())
        print(numOfWays(m,n))

# } Driver Code Ends