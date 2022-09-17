class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem = set(words)
        mem2 = {}
        output = []
        def dfs(word):
            if word in mem2:
                return mem2[word]
            for i in range(1, len(word)):
                pre = word[:i]
                suf = word[i:]
                
                if (pre in mem and suf in mem) or (pre in mem and dfs(suf)) or (suf in mem and dfs(pre)):
                    mem2[word] = True
                    return True
            mem2[word] = False
            return False
        
        for w in words:
            if dfs(w):output.append(w)
        # print(mem2)
        return output
        