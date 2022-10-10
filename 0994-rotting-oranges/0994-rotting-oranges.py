class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        root = []
        visited = set()
        count = 0
        output = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    root.append((i,j))
                    visited.add((i,j))
                    
        while count!=0 and root:
            # print(root)
            output += 1
            q = deque([x for x in root])
            root = list()
            while q:
                i,j = q.popleft()
                if i-1 >= 0  and (i-1,j) not in visited and grid[i-1][j] == 1:
                    count -= 1
                    root.append((i-1,j))
                    visited.add((i-1,j))
                if i+1 < n  and (i+1,j) not in visited and grid[i+1][j] == 1:
                    count -= 1
                    root.append((i+1,j))
                    visited.add((i+1,j))
                if j-1 >= 0  and (i,j-1) not in visited and grid[i][j-1] == 1:
                    count -= 1
                    root.append((i,j-1))
                    visited.add((i,j-1))
                if j+1 < m  and (i,j+1) not in visited and grid[i][j+1] == 1:
                    count -= 1
                    root.append((i,j+1))
                    visited.add((i,j+1))
        return output if count == 0 else -1
                    
        