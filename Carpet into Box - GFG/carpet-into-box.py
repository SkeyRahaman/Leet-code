#User function Template for python3


class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        a = [A,B]
        b = [C,D]
        output = 0
        while True:
            
            a.sort()
            b.sort()
            # print(a,b)
            if a[1]>b[1]:
                a[1] >>= 1
                output += 1
            elif a[0] > b[0]:
                a[0] >>= 1
                output += 1
            else:
                return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends