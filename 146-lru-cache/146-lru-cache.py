class Node:
    def __init__(self,key=0,val=0):
        self.key,self.val = key,val
        self.pre , self.next = None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.mem = {}
        self.left , self.right = Node(), Node()
        self.left.next , self.right.pre = self.right, self.left
        self.cap = capacity
     

    def insert(self, node):
        previous , nxt = self.right.pre,  self.right
        node.pre, node.next = previous , nxt
        self.right.pre = node
        previous.next = node
    
    def remove(self, node):
        node.pre.next, node.next.pre = node.next , node.pre
        

    def get(self, key: int) -> int:
        if key in self.mem:
            self.remove(self.mem[key])
            self.insert(self.mem[key])
            return self.mem[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self.remove(self.mem[key])
        self.mem[key] = Node(key,value)
        self.insert(self.mem[key])
        if len(self.mem) > self.cap:
            k = self.left.next.key
            self.remove(self.left.next)
            del self.mem[k]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)