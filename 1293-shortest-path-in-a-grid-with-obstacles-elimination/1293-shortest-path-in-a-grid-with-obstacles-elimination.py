class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if k >= m + n - 2:                     #early return
            return m + n - 2
        
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        
        while queue:
            x, y, k, steps = queue.popleft()
            
            if x == m-1 and y == n-1: 
                return steps
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1 and (i, j, k-1) not in visited and k > 0:    #using a ticket to go to a point
                        queue.append((i, j, k-1, steps+1))
                        visited.add((i, j, k-1))
                    elif grid[i][j] == 0 and (i, j, k) not in visited:              #without using ticket 
                        queue.append((i, j, k, steps+1))
                        visited.add((i, j, k))
        
        return -1
    
    
        m = len(grid)
        n = len(grid[0])
        @cache
        def f(i,j,k):
            if i<0 or i>=m or j<0 or j>=n or (grid[i][j] == 1 and k<1):
                return float('inf')
            if i==0 and j==0:
                return 0
            if grid[i][j] == 1:
                # print(i,j,1 + min(f(i-1,j,k-1),f(i,j-1,k-1)))
                return 1 + min(f(i-1,j,k-1),f(i,j-1,k-1),f(i+1,j,k-1),f(i,j+1,k-1))
            else:
                # print(i,j,1 + min(f(i-1,j,k),f(i,j-1,k)))
                return 1 + min(f(i-1,j,k),f(i,j-1,k),f(i+1,j,k),f(i,j+1,k))
        z = f(m-1,n-1,k)
        if z == float('inf'):
            return -1
        return z
        