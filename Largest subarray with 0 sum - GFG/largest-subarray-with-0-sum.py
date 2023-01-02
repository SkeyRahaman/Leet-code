#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        mem = {0:-1}
        summ = 0
        output = 0
        for i,j in enumerate(arr):
            summ+=j
            if summ in mem:
                output = max(output,i-mem[summ])
            else:
                mem[summ] = i
        return output
        
        

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends