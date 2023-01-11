#User function Template for python3

class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        arr.sort()
        last = 0
        output = 0
        for i in arr:
            if i <= last:
                output += (last - i + 1)
                last += 1
            else:
                last = i
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr,N))
        
        T -= 1
# } Driver Code Ends