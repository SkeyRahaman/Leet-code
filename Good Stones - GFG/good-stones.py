#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def goodStones(self, n, arr) -> int:
        # code here
        output = [[False, -1] for _ in range(n)]
        visited_count = 0
    
        def dfs(node):
            nonlocal visited_count
            if output[node][0]:
                if output[node][1] == -1:
                    output[node][1] = False
                    return False
                else:
                    return output[node][1]
    
            output[node][0] = True
            nxt = arr[node] + node
            if 0 <= nxt < n:
                res = dfs(nxt)
                if res:visited_count += 1
                output[node][1] = res
                return res
            else:
                visited_count += 1
                output[node][1] = True
                return True
                
                
        for i in range(n):
            if not output[i][0]:
                dfs(i)
        # count = 0
        # # print(output)
        # for i in output:
        #     if i[1]:count += 1
        return visited_count
            

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        obj=Solution()
        print(obj.goodStones(n, arr))
        
# } Driver Code Ends