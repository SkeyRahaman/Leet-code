#User function Template for python3

import heapq
class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        heap = []
        output = 0
        for i in arr:
            heapq.heappush(heap,i)
        while len(heap)>1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            z = a + b
            output += z
            heapq.heappush(heap,z)
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends