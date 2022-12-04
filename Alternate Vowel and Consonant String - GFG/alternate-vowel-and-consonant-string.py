#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        def combine(a,b):
            output = []
            while a and b:
                output.append(a.pop())
                output.append(b.pop())
            if a:
                output.append(a.pop())
            return "".join(output)
        # code here
        v = []
        c = []
        V = {z for z in "aeiou"}
        for i in S:
            if i in V:
                v.append(i)
            else:
                c.append(i)
        v.sort(reverse =True)
        c.sort(reverse =True)
        if abs(len(v)-len(c)) > 1:
            return -1
        if len(v)>len(c):
            return combine(v,c)
        elif len(v)<len(c):
            return combine(c,v)
        else:
            if v[-1]>c[-1]:
                return combine(c,v)
            else:
                return combine(v,c)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends