class Solution:
    def minSteps(self, s : str) -> int:
        # code here
        last = "z"
        a = 0
        b = 0
        for i in s:
            if i == last:
                continue
            elif i == 'a':
                a += 1
            else:
                b += 1
            last = i
        return 1 + min(a,b)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends