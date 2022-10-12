class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        a = 1
        output = 2
        for i in range(2,n):
            x = a + output
            a = output
            output = x
        return output
        
        
        
        
        
        
        # mem = {}
        # def helper(n):
        #     if n == 0:return 0
        #     if n in mem:
        #         return mem[n]
        #     output = -1
        #     if n>0:
        #         output += (1 + helper(n-1))
        #     if n>1:
        #         output += (1 + helper(n-2))
        #     mem[n] = output
        #     return output
        # return helper(n) + 1