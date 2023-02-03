#User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        #code here
        x,y = 0,0
        c = [[0,1],[1,0],[0,-1],[-1,0]]
        d = 0
        while True:
            if matrix[x][y] == 1:
                matrix[x][y] = 0
                d = (d+1)%4
            a = x+c[d][0]
            b = y+c[d][1]
            if a<0 or a>=R or b<0 or b>=C:
                return x,y
            x,y=a,b



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends