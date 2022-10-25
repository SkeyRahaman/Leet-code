class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        dp = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        i = 0
        j = 0
        output = []
        while i<len(s1) and j <len(s2):
            if s1[i] == s2[j]:
                output.append(s1[i])
                i += 1
                j += 1
            else:
                if dp[i+1][j] > dp[i][j+1]:
                    output.append(s1[i])
                    i += 1
                else:
                    output.append(s2[j])
                    j+=1
        output.append(s1[i:])
        output.append(s2[j:])
        return "".join(output)
        # print(output)
        j,k=0,0
        o=[]
        for i in output:
            while j<len(s1) and s1[j] != i:
                o.append(s1[j])
                j += 1
            while k<len(s2) and s2[k] != i:
                o.append(s2[k])
                k+=1
            o.append(i)
            j+=1
            k+=1
        o.append(s1[j:])
        o.append(s2[k:])
        return "".join(o)
            