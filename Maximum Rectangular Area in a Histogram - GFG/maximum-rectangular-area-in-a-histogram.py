#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,h):
        #code here
        left = []
        stack = [[-1,-1]]
        for n,i in enumerate(h):
            while stack and stack[-1][1] >= i:
                stack.pop()
            left.append(stack[-1][0])
            stack.append([n,i])
            
        # print(left)   
        right = []
        stack = [[len(h),-1]]
        output = 0
        for n in range(len(h)-1,-1,-1):
            i = h[n]
            while stack and stack[-1][1] >= i:
                stack.pop()
            right.append(stack[-1][0])
            stack.append([n,i])
        for l,i,r in zip(left,h,right[::-1]):
            # print(l,i,r)
            output = max(output,i*(r-l-1))
        # print(right[::-1])
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends