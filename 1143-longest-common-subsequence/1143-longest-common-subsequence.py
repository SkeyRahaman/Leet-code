class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        @cache
        def helper(i,j):
            if i<0 or j<0:
                return 0
            if s1[i] == s2[j]:
                return 1 + helper(i-1,j-1)
            else:
                return max(helper(i-1,j),helper(i,j-1))
        return helper(len(s1)-1,len(s2)-1)
        