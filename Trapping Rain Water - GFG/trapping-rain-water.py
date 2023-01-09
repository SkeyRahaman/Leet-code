
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        output = 0
        maxi = [0] * n
        track = 0
        for i in range(n-1,-1,-1):
            maxi[i] = track
            track = max(track,arr[i])
        
        track = 0
        for i in range(n):
            height = min(track,maxi[i])
            if height > arr[i]:
                output += (height-arr[i])
            track = max(track,arr[i])
        return output
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends