#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,w, N, K):
        # print(w,type(w))
        al = "abcdefghijklmnopqrstuvwxyz"
        adj = defaultdict(set)
        ind = defaultdict(int)
        queue = deque()
        output = []
        outputset = set()
        for i in range(len(w)-1):
            for j in range(min(len(w[i]),len(w[i+1]))):
                if w[i][j] != w[i+1][j]:
                    adj[w[i][j]].add(w[i+1][j])
                    # print(w[i][j],w[i+1][j])
                    break
        # print(adj)
        for i in adj:
            for j in adj[i]:
                ind[j] += 1
        # print(ind)
        for i in adj:
            if ind[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            output.append(node)
            outputset.add(node)
            for i in adj[node]:
                ind[i] -= 1
                if ind[i] == 0:
                    queue.append(i)
        # print(output)
        if len(output) != K:
            for letter in al[:k]:
                if letter not in outputset:
                    output.append(letter)
                    outputset.add(letter)
                    if len(output) == K:
                        break
        return "".join(output)
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends