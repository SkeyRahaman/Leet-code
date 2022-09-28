class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        SUM = sum(machines)
        N = len(machines)
        
        if SUM%N != 0:return -1
        
        
        avg = SUM//N
        leftsum = [0]
        rightsum = [0]
        s = 0
        for i in machines[:-1]:
            s+=i
            leftsum.append(s)
        s = 0
        for i in range(N-1,0,-1):
            s+=machines[i]
            rightsum.append(s)
        rightsum =rightsum[::-1]
        
        print(leftsum,rightsum)
        
        output = 0
        for i in range(len(machines)):
            left = avg * i
            right = avg * (N-i-1)
            l,r=0,0
            if left>leftsum[i]:
                l = left - leftsum[i]
            if right>rightsum[i]:
                r = right-rightsum[i]
            output = max(output,l+r)
        return output
        