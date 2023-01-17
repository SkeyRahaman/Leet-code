#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        output = []
        def f(i,j,path):
            nonlocal output,m,n
            if i == n-1 and j == n-1:
                output.append("".join(path))
                return
            for i,a,b in [["R",i,j+1],['L',i,j-1],['D',i+1,j],['U',i-1,j]]:
                if 0<=a<n and 0<=b<n and m[a][b] == 1:
                    m[a][b] = 0
                    path.append(i)
                    f(a,b,path)
                    m[a][b] = 1
                    path.pop()
        if m[0][0] == 0:return []
        m[0][0] = 0
        f(0,0,[])
        return output
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends