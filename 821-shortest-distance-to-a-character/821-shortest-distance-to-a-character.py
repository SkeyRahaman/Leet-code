class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        track = 99999
        output = []
        for i in s:
            if i == c:
                track = -1
            if track != 99999:
                track += 1
            output.append(track)
        track = 99999
        for i in range(len(s)-1,-1,-1):
            j = s[i]
            if j == c:
                track = -1
            if track != 99999:
                track += 1
            output[i] = min(output[i],track)
        return output
                
        
        