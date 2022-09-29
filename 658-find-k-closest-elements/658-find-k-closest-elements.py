from sortedcontainers import SortedList
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
#         def binary_search(array,key,start,end):
#             if start > end:
#                 return -1
#             if start == end:
#                 if array[start] == key:
#                     return start
#                 else:
#                     return -1
                
#             mid = start + ((end-start) // 2)
#             if array[mid] == key:
#                 return mid
#             if array[mid] > key:
#                 return binary_search(array,key,start,mid-1)
#             else:
#                 return binary_search(array,key,mid+1,end)
        arr = SortedList(arr)
        key = arr.bisect_left(x)
        # print(key)
        # return 
        output = deque()
        k1,k2 = key-1,key
        while len(output) != k:
            
            if k1>-1 and k2<n:
                if abs(arr[k1] - x) > abs(arr[k2] - x):
                    output.append(arr[k2])
                    k2 += 1
                else:
                    output.appendleft(arr[k1])
                    k1 -= 1
                    
            elif k1>-1:
                output.appendleft(arr[k1])
                k1 -= 1
            else:
                output.append(arr[k2])
                k2 += 1
            # print(output)
        return list(output)
        