#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
from collections import deque

class Solution:
    def __init__(self):
        # Every index of prime stores zero or one
        # If prime[i] is zero means i is not a prime
        # If prime[i] is one means i is a prime
        self.prime=[1 for i in range(10001)]
        for i in range(2,(10001//2)+1):
            if self.prime[i] == 1:
                cnt = i + i
                while cnt<=10000:
                    self.prime[cnt] = 0
                    cnt += i
        
                    

    def shortestPath(self,Num1,Num2):
        # Complete this function using prime list
        if Num1 == Num2:return 0
        q = deque([Num1])
        visited = set()
        visited.add(Num1)
        output = -1
        while q:
            output += 1
            for _ in range(len(q)):
                node = q.popleft()
                for i in range(4):
                    for j in range(10):
                        if i==j==0:continue
                        nxt = str(node)
                        nxt = int(nxt[:i] + str(j) + nxt[i+1:])
                        if self.prime[nxt] and nxt not in visited:
                            if nxt == Num2:return output+1
                            visited.add(nxt)
                            q.append(nxt)
        return -1
        
                    
                
        




#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    ob = Solution()
    for _ in range (t):
        Num1,Num2=map(int,input().split())
        print(ob.shortestPath(Num1,Num2))

# } Driver Code Ends