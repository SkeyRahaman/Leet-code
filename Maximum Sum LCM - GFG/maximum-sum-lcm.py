#User function Template for python3
class Solution:
    def maxSumLCM (self, n):
        output = 0
        i = 1
        while i*i<=n:
            if n%i == 0:
                output += i;
                if i*i != n:
                    output += (n/i)
            i += 1
        return int(output)
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends