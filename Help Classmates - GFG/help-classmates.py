#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack = [-1]
        output = []
        for i in arr[::-1]:
            while stack[-1] >= i:
                stack.pop()
            output.append(stack[-1])
            stack.append(i)
        return output[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends