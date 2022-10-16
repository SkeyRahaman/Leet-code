class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [0] * n
        mem[0] = 1
        for _ in range(m):
            for i in range(1,n):
                mem[i] = mem[i] + mem[i-1]
        return mem[-1]