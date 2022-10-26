class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @cache
        def helper(i,j):
            if j == -1:
                return i +1
            if i == -1:
                return j + 1
            
            if s1[i] == s2[j]:
                return  helper(i-1,j-1)
            insert = helper(i,j-1)
            delete = helper(i-1,j)
            replace = helper(i-1,j-1)
            return 1 + min(insert,delete,replace)
        return helper(len(s1)-1,len(s2)-1)
        