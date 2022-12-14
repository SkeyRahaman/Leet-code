#User function Template for python3
from collections import defaultdict
class Solution:

	def findRange(self,a, size):
    	# code here
    	
        aa = [1 if i == "0" else -1 for i in a]
        if aa.count(-1)==len(a):return [-1]
        mem = defaultdict(list)
        output = 0
        outstart = -1
        outend = -1
        loc = 0
        for j,i in enumerate(aa):
            # print(i,j)
            loc += i
            if loc<0:
                loc = 0
                outstart = -1
                outend = -1
            else:
                if outstart == -1:
                    outstart = j
                    outend = j
                else:
                    outend = j
                if loc>=output:
                    output = loc
                    mem[output].append([outstart,outend])
        # print(mem)
        a,b = list(sorted(mem[output]))[0]
        return [a+1,b+1]
        
#{ 
 # Driver Code Starts
if __name__ == '__main__': 


	tc=int(input())
	while tc > 0:
	    n=int(input())
	    s=input()
	    ob = Solution()
	    ans = ob.findRange(s, n)
	    if len(ans)==1:
	        print(ans[0])
	    else:
	        print(str(ans[0])+" "+str(ans[1]))
	    tc=tc-1
# } Driver Code Ends