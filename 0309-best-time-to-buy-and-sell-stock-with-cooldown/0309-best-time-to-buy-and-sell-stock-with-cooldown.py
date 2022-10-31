class Solution:
    def maxProfit(self, v: List[int]) -> int:
        n = len(v)
        last = [[0 for z in range(2)] for _  in range(2)]
        cur = [[0 for z in range(2)] for _  in range(2)] 
        for i in range(n-1,-1,-1):
            for b in range(2):
                for c in range(2):
                    if c == 0:
                        if b:
                            cur[b][c] =  max(-v[i] + last[0][0], last[1][0])
                        else:
                            cur[b][c] =  max(v[i] + last[1][1], last[0][0])
                    else:
                        cur[b][c] =  last[b][c-1]
            last = copy.deepcopy(cur)
        return last[1][0]

        
        
        
        
        
        
        n = len(v)
        @cache
        def f(i,b,c):
            if i == n:
                return 0
            if c == 0:
                if b:
                    return max(-v[i] + f(i+1,0,0), f(i+1,1,0))
                else:
                    return max(v[i] + f(i+1,1,1), f(i+1,0,0))
            else:
                return f(i+1,b,c-1)
        return f(0,1,0)
        