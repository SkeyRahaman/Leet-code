#User function Template for python3

class Solution:

    def buildLowestNumber(self, S,N):
        # code here
        # print(S,N)
        stack = []
        for i in S:
            while stack and int(stack[-1]) > int(i) and N>0:
                stack.pop()
                N -= 1
            stack.append(i)
        while N>0:
            stack.pop()
            N -= 1
        return str(int("".join(stack)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends