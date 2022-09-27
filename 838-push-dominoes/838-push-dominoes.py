class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        mem = [0] * len(dominoes)
        mem2 = mem[:]
        track = 0
        for i,j in enumerate(dominoes):
            if j == "R":
                mem[i] = 1
                track = 1
            elif j == "L":
                track = 0
            else:
                if track > 0:
                    track += 1
                    mem[i] = track
        track = 0
        for i in range(len(dominoes)-1,-1,-1):
            j = dominoes[i]
            if j == "L":
                track = 1
                mem2[i] = 1
            elif j == "R":
                track = 0
            else:
                if track > 0:
                    track += 1
                    mem2[i] = track
        output = []            
        for i,j in zip(mem,mem2):
            if i == j == 0:
                output.append(".")
            elif i == 0 and j != 0:
                output.append("L")
            elif i != 0 and j == 0:
                output.append("R")
            else:
                if i == j:
                    output.append(".")
                elif i>j:
                    output.append("L")
                else:
                    output.append("R")
            
                
        print(mem)
        print(mem2)
        return "".join(output)
            