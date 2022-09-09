class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[(i*i + j*j),i,j] for i,j in points]
        return [[a,b] for x,a,b in sorted(points, reverse=True, key=lambda x:x[0])[-k:]]
        