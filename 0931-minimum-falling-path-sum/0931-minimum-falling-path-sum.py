class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        
        
        
        
        
        
        
        N = len(matrix)
        @cache
        def helper(i,j):
            if i == 0:
                return matrix[i][j]
            z = helper(i-1,j)
            if j>0:
                z = min(z,helper(i-1,j-1))
            if j<N-1:
                z = min(z,helper(i-1,j+1))
            return matrix[i][j] + z
        
        
        # print([helper(N-1,z) for z in range(N)])
        return min([helper(N-1,z) for z in range(N)])
            
        
        
        
        
        
        
        
        
        n =  len(matrix)
        o = min(matrix[0])
        for i in range(1,n):
            o = 1000
            for j in range(n):
                k = matrix[i-1][j]
                if j>0:
                    k = min(k,matrix[i-1][j-1])
                if j+1<n:
                    k = min(k,matrix[i-1][j+1])
                matrix[i][j] = matrix[i][j] + k
                o = min(o,matrix[i][j])
        print(matrix)
        return o