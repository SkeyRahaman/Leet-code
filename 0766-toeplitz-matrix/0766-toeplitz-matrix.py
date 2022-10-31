class Solution:
    def isToeplitzMatrix(self, ma: List[List[int]]) -> bool:
        m = len(ma)
        n = len(ma[0])
        q1 = set()
        q1.add((0,n-1))
        while q1:
            q2 = set(q1)
            q1 = set()
            q1v = set()
            # print(q2)
            for a,b in q2:
                q1v.add(ma[a][b])
                if b>0:
                    q1.add((a,b-1))
                if a<m-1:
                    q1.add((a+1,b))
            
                
            if len(q1v) != 1:
                return False
        return True