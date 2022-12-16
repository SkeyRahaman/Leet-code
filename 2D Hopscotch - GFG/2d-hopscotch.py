#User function Template for python3

class Solution:
    def hopscotch(self, n, m, mat, ty, i, j):
        # code here
        def f(i,j):
            nbr = set()
            for a in [i-1,i,i+1]:
                for b in [j-1,j,j+1]:
                    if 0<=a<n and 0<=b<m and not (a == i and b == j):
                        nbr.add((a,b))
            # print(nbr)
            if j%2!=0:
                return nbr-{(i-1,j-1),(i-1,j+1)}
            else:
                return nbr-{(i+1,j-1),(i+1,j+1)}
        first_nbr = f(i,j)
        if ty == 0:
            output = 0
            for a,b in first_nbr:
                output += mat[a][b]
            return output
        else:
            sec_nbr = set()
            for a,b in first_nbr:
                buf = f(a,b)
                for x,y in buf:
                    if (x,y) not in first_nbr and (x,y) != (i,j):
                        sec_nbr.add((x,y))
            output = 0
            for a,b in sec_nbr:
                output += mat[a][b]
            return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        ty, i, j = map(int,input().strip().split())
        
        ob = Solution()
        print(ob.hopscotch(n, m, mat, ty, i, j))
# } Driver Code Ends