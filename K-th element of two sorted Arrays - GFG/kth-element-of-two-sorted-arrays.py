#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n>m:
            self.kthElement(arr2,arr1,m,n,k)
        low,high = 0,min(k,n)
        while low<=high:
            c1 = (low+high)>>1
            c2 = k-c1
            if c2>m:
                low = c1+1
                continue
            
            a = float('-inf') if c1 == 0 else arr1[c1-1]
            b = float('-inf') if c2 == 0 else arr2[c2-1]
            c = float('inf') if c1 == len(arr1) else arr1[c1]
            d = float('inf') if c2 == len(arr2) else arr2[c2]
            
            if a<=d and b<=c:
                return max(a,b)
            elif a>d:
                high = c1-1
            else:
                low = c1+1
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends