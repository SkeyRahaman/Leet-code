class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key=lambda x:x[1])
        last = pairs[0][1]
        output = 1
        for a,b in pairs[1:]:
            if a>last:
                last = b
                output += 1
        return output
            
            
        
            
        