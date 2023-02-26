#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        # code here
        # print(adj,V)
        v= set()
        output = 0
        def check(node):
            
            ref = {node}
            for i in adj[node]:
                v.add(i)
                ref.add(i)
            q = deque([i for i in ref])
            while len(q) != 0:
                n = q.pop()
                if len(adj[n]) != len(ref)-1:return False
                for i in adj[n]:
                    if i not in ref:
                        return False
            return True
                
                
                
        for i in range(1,V+1):
            if i not in v:
                v.add(i)
                # print(check(i),i)
                output += check(i)
        return output
        print(adj)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            a,b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
            
        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends