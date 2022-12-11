#User function Template for python3

class Solution:
	def canPair(self, nuns, k):
		# Code here
		mem = {}
		for i in nums:
		  #  print(i,mem)
		    i = i%k
		    if i in mem:
		        mem[i] -= 1
		        if mem[i] == 0:
		            del mem[i]
		    else:
		        c = 0 if i == 0 else k-i
		        if c in mem:
		            mem[c] += 1
		        else:
		            mem[c] = 1
# 		print(mem)
	    return len(mem) == 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends