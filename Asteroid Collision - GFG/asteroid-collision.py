#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        output = []
        for i in asteroids:
            
            
            # positive astroid
            if i > 0:
                output.append(i)
            
            #negative astroid
            else:
                while True:
                    if output and output[-1] > 0:
                        if output[-1] < abs(i):
                            output.pop()
                        elif output[-1] == abs(i):
                            output.pop()
                            break
                        else:
                            break
                    else:
                        output.append(i)
                        break
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends