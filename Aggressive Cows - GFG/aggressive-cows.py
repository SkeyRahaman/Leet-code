#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        def place(i):
            nonlocal k
            cow = k
            last = float('-inf')
            for s in stalls:
                if s-last>=i:
                    last = s
                    cow -= 1
            return cow <= 0
        # for i in range(max(stalls)):
        #     print(i,place(i))
        stalls.sort()
        left = 1
        right = stalls[-1]
        output = 1
        while left<=right:
            mid = (left+right)>>1
            if place(mid):
                output = max(output,mid)
                left = mid+1
            else:
                right = mid - 1
                
        return output
        return 0
        pass


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