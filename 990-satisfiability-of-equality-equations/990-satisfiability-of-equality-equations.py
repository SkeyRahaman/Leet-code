class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        mem = {a : a for a in string.ascii_lowercase}
        
        
        def find(a):
            if a != mem[a]:
                mem[a] = find(mem[a])
            return mem[a]
        
        for a,b,_,c in equations:
            if b == "=":
                mem[find(a)] = mem[find(c)]
                
        for a,b,_,c in equations:
            if b == "!":
                if find(a) == find(c):
                    return False
        return True