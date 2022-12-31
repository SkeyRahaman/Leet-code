#User function Template for python3
from collections import defaultdict
class Solution: 
    def minLaptops(self, N, start, end):
        # Code here
        mem = defaultdict(int)
        for i, j in zip(start,end):
            mem[i] += 1
            mem[j] -= 1
        
        mem = [[i,j] for i,j in mem.items()]
        mem.sort(key = lambda x:x[0])
        count = 0
        output = 0
        for i,j in mem:
            count += j
            output = max(output,count)
        return output
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends