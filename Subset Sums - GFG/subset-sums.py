#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    output = [0]
		# code here
		def f(i,summ):
		    nonlocal output
		    if i >= N:
		        return 
		    output.append(summ+arr[i])
		    f(i+1,summ)
		    f(i+1,summ+arr[i])
		f(0,0)
		return output
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends