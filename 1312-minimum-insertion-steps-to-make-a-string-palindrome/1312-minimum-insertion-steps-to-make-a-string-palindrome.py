class Solution:
    def minInsertions(self, s1: str) -> int:
        s2 = s1[::-1]
        n = len(s1)
        last = [0] * (n+1)
        cur = [0] * (n+1)
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i] == s2[j]:
                    cur[j] = 1 + last[j+1]
                else:
                    cur[j] = max(last[j],cur[j+1])
            last = [z for z in cur]
        return n-last[0]
        