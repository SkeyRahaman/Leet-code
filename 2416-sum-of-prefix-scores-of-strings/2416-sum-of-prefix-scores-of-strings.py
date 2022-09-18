class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
        
    def addword(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur.children[w].count += 1
            cur = cur.children[w]

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for w in words:
            root.addword(w)
            
        output = []
        for w in words:
            res = 0
            cur = root
            for c in w:
                res += cur.children[c].count
                cur = cur.children[c]
            output.append(res)
        return output
            
        
        
        
        
        
        
        
        
        
        
#         mem = defaultdict(int)
#         for word in words:
#             for i in range(1,len(word)+1):
#                 mem[word[:i]] += 1
#         output = []
#         for word in words:
#             out = 0
#             for i in range(1,len(word)+1):
#                 out += mem[word[:i]]
#             output.append(out)
            
                
#         return output
        