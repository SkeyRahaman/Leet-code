#User function Template for python3
from collections import defaultdict


class Solution():
    def longestString(self, arr, n):
        #Tire
        class Tirenode:
            def __init__(self,char="",end=False):
                self.char = char
                self.end = end
                self.children = {}
        class Tire:
            def __init__(self):
                self.head = Tirenode()
            def add(self,word):
                ptr = self.head
                for i in range(len(word)):
                    if word[i] not in ptr.children:
                        ptr.children[word[i]] = Tirenode(char=word[i])
                    ptr = ptr.children[word[i]]
                    if i == len(word)-1:
                        ptr.end = True
            def check(self,word):
                ptr = self.head
                for i in word:
                    ptr = ptr.children[i]
                    if not ptr.end:return False
                return True
        T = Tire()
        for i in arr:
            T.add(i)
        output = ""
        for i in arr:
            if len(i) >= len(output):
                if T.check(i):
                    if len(i) > len(output):
                        output = i
                    else:
                        output = min(output,i)
        return output
                
        
        
        
        
        
        #your code goes here
        # Brute Force
        dp = set(arr)
        def check(s):
            nonlocal dp
            for i in range(1,len(s)+1):
                if s[:i] not in dp:
                    return False
            return True
        output = ""
        for i in arr:
            if len(i) >= len(output):
                if check(i):
                    if len(i) > len(output):
                        output = i
                    else:
                        output = min(output,i)
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends