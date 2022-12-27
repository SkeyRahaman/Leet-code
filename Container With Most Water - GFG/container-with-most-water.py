#User function Template for python3



def maxArea(A,le):
    #code here
    low = 0
    high = le-1
    output = 0
    while low<high:
        output = max(output,min(A[low],A[high])*(high-low))
        if A[low]>A[high]:
            high -= 1
        else:
            low += 1
    return output
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends