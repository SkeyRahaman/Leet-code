#User function Template for python3


class Solution():
    def longestString(self, arr, n):
        #your code goes here
        dp = set(arr)
        def check(s):
            nonlocal dp
            for i in range(1,len(s)+1):
                if s[:i] not in dp:
                    return False
            return True
        output = ""
        for i in arr:
            if len(i) >= len(output):
                if check(i):
                    if len(i) > len(output):
                        output = i
                    else:
                        output = min(output,i)
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends