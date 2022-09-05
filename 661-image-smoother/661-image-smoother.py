class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        def helper(a,b,img):
            summ = 0
            count = 0
            for i in range(a-1,a+2):
                for j in range(b-1,b+2):
                    if 0<=i<m and 0<=j<n:
                        summ += img[i][j]
                        count += 1
            return summ//count
        return [[helper(i,j,img) for j in range(n)] for i in range(m)]
        