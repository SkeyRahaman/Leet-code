class Solution:
    def noConseBits(self, n : int) -> int:
        # code here
        return int(bin(n)[2:].replace("111","110"),2)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends