class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = {i for i in bank}
        if end not in bank:return -1
        gens = [i for i in 'ACGT']
        visited = set(start)
        q1 = [[i for i in start]]
        q2 = []
        output = 0
        while q1:
            q2 = copy.deepcopy(q1)
            q1 = []
            output += 1
            for gen in q2:
                for i in range(8):
                    # if gen[i] == end[i]:
                    #     continue
                    for j in range(4):
                        x = [z for z in gen]
                        if x[i] != gens[j]:
                            x[i] = gens[j]
                            y = "".join(x)
                            if y == end:
                                return output
                            if y not in visited and y in bank:
                                q1.append(y)
        return -1
                                
                            