#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        output = [0] * N
        for i,j in enumerate(Edge):
            if j != -1:
                output[j] += i
        out = -1
        maxi = 0
        for i,j in enumerate(output):
            if j>=maxi:
                out = i
                maxi = j
        return out
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends