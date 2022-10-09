class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        output = [pref[0]]
        last = pref[0]
        for i in pref[1:]:
            output.append(last^i)
            last ^= (last^i)
        return output
        
        
        
        
        
        
        # output = []
        # x = 0
        # l = 0
        # for i in pref:
        #     y = int(bin(~i)[3:],2)
        #     x ^= i
        #     output.append(x)
        # return output
        