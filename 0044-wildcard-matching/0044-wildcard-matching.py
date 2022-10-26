class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def helper(i,j):
            #base case
            if i == -1 and j==-1:
                return True
            if j == -1:
                return False
            if i == -1:
                return "*"*(j+1) == p[:j+1]
            
            if s[i] == p[j] or p[j] == "?":
                return helper(i-1,j-1)
            elif p[j] == "*":
                if helper(i,j-1):return True
                return helper(i-1,j)
            else:
                return False
        return helper(len(s)-1,len(p)-1)
        