#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        
            
        stalls.sort()
        maxi = stalls[-1]
        mini = stalls[0]
        def canplace(i):
            last = stalls[0] - i
            cows = k
            for c in stalls:
                if c-last >= i:
                    last = c
                    cows -= 1
            return cows <= 0
            
            
            
            
            
            
            
        low = 1
        high = maxi-mini
        output = 1
        while low<=high:
            mid = (low + high)//2
            if canplace(mid):
                output = max(output,mid)
                low = mid + 1
            else:
                high = mid -1
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends