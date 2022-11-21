#User function Template for python3

class Solution:
    def UniquePartitions(self, n):
        m=[]
        def dfs(n,s,l,m):
    
            if s==n:
    
                m.append(l)
    
                return
    
            if s>n:
    
                return
    
            for i in range(n,0,-1):
    
                if len(l)==0 or l[-1]>=i:
    
                    dfs(n,s+i,l+[i],m)
        
        
        
        dfs(n,0,[],m)
        
        return m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.UniquePartitions(n)
		for a in ans:
			for b in a:
				print(b, end = " ")
		print()

# } Driver Code Ends