class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        maxi = []
        lm = height[-1]
        for i in range(len(height)-1,-1,-1):
            lm = max(lm,height[i])
            maxi.append(lm)
        maxi = maxi[::-1]
        last = 0
        for i,j in zip(height,maxi):
            
            cap = min(last,j) - i
            # print(last,i,j,cap,output)
            if cap > 0:
                output += cap
            last =  max(i,last)
        return output
            