class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        n = len(mat[0])
        choice = list(combinations([i for i in range(n)],cols))
        mem = defaultdict(int)
        for c,i in enumerate(choice):
            for row in mat:
                w = row[:]
                for a in i:
                    w[a] = 0
                if 1 not in w:
                    mem[c] += 1
        if mem.items():
            return max(mem.items(),key=lambda x:x[1])[1]
        else:
            return 0
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(mat)
        # c = [[i[j] for i in mat] for j in range(len(mat[0]))]
        # ans = 0
        # for i in list(combinations(c, cols)):
        #     # print(i)
        #     output = int(f"0b1{n*'0'}",2)
        #     for s in i:
        #         # print(s)
        #         t = "0b1"
        #         for kk in s:
        #             t += str(kk)
        #         # print(t)
        #         output = output | int(t,2)
        #     output = bin(output)
        #     # print(output)
        #     ans = max(ans,(str(output).count('1') - 1))
        # # print(str(bin(0b10001 or 0b10010))
        # # print(bin(int(f"0b10000",2) | int("0b10011",2)))
        # return ans
                
        