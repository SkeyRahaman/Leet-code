class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        mem = [0] * (len(s)+1)
        # print(mem)
        mem[0] = 1
        mem[1] = 0 if s[0] == "0" else 1
        
        for i in range(2,len(s)+1):
            if s[i-1] != "0":
                mem[i] += mem[i-1]
            if 10<=int(s[i-2:i])<=26:
                mem[i] += mem[i-2]
        return mem[len(s)]
        