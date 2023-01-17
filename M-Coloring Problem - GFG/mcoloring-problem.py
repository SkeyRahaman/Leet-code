#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    # print(graph,k,V)
    col = [-1] * V
    def check(node,c):
        for i,j in enumerate(graph[node]):
            if j == 1 and i!=node and col[i] == c:
                return False
        return True
        
    def f(node):
        if node == V:return True
        
        for i in range(k):
            if check(node,i):
                col[node] = i
                if f(node+1):return True
                col[node] = -1
        return False
        
        
        
        
        
    for i in range(V):
        if col[i] == -1:
            if not f(i):return 0
    return 1 
                
    #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends