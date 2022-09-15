class TireNode:
    def __init__(self,val,end, next_):
        self.val = val
        self.end = end
        self.next = next_
        
        
class Trie:

    def __init__(self):
        self.root = TireNode(val="$",end=True,next_=[])
    def print_tree(self, r):
        q = deque()
        q.extend(r.next)
        while q:
            n = q.popleft()
            print(n.val, n.end)
            q.extend(n.next)
        
        
        
        
        
    def insert(self, q: str) -> None:

        node, q = self.get_last_node(self.root,q)

        last = node
        for i in q:
            n = TireNode(val=i,end=False,next_=list())
            last.next.append(n)
            last = n
        last.end = True
    
    def get_last_node(self, r,word):

        if len(word) == 0:

            return r, word
        for i in r.next:
            if i.val == word[0]:
                x,w = self.get_last_node(i,word[1:])
                if x is not i:

                    return x,w

                return i,word[1:]

        return r,word
        
        
        
        
        
        
        

    def search(self, word: str) -> bool:
        return self.find_word(word,self.root)
        
    def find_word(self, x,node):
        if len(x) == 0:
            return node.end
        for i in node.next:
            if i.val == x[0]:
                return self.find_word(x[1:],i)
        return False

    
    
    
    
    def startsWith(self, prefix: str) -> bool:
        return self.find_part(prefix,self.root)
        
    
    
    def find_part(self, z, node):
        if len(z) == 0:
            return True
        for i in node.next:
            if i.val == z[0]:
                return self.find_part(z[1:],i)
        return False
    
    
                
                
        
                
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)