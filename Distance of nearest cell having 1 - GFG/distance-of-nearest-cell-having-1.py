class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		output = [[0] * len(grid[0]) for _ in range(len(grid))]
		
		def get_nearest(i,j):
		    q1 = [(i,j)]
		    visited = set()
		    count = -1
		    while q1:
		        q2 = [z for z in q1]
		        q1 = []
		        count += 1
		        while q2:
		            a,b = q2.pop()
		            if a<0 or a>=len(grid) or b<0 or b>= len(grid[0]) or (a,b) in visited:continue
		            if grid[a][b] == 1:
		                return count
		            visited.add((a,b))
		            q1 += [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]
		    return 0
		            
		            
		
		
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 0:
		            output[i][j] = get_nearest(i,j)
		return output


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends