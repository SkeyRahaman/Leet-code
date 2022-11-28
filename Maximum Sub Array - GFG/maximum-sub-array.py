#User function Template for python3

class Solution:

	def findSubarray(self,a, n):
    	# code here
    	output = []
    	osum = 0
    	run = []
    	rsum = 0
    	for i in a:
            if i<0:
                if rsum>osum:
                    output = [z for z in run]
                    osum = rsum
                elif rsum==osum and len(output) < len(run):
                    output = [z for z in run]
                run = []
                rsum = 0
            else:
                run.append(i)
                rsum += i
        if rsum>osum:
            output = [z for z in run]
            osum = rsum
        elif rsum==osum and len(output) < len(run):
            output = [z for z in run]
        return [-1] if len(output) == 0 else output
        
    	   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int, input().strip().split()))
	    ob = Solution()
	    ans=ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends