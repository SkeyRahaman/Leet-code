from collections import Counter
class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        c = Counter('balloon')
        d = Counter(s)
        output = float('inf')
        for i in c.keys():
            output = min(output,d[i]//c[i])
        return output if output != float('inf') else 0
            
        
        
        
        
        def swap(i,j,nums):
            nums[i],nums[j] = nums[j],nums[i]
            
        


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.maxInstance(s)
        
        print(res)

# } Driver Code Ends