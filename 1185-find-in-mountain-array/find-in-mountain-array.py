# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        low,high= 1,n-2
        while(low<=high):
            mid = (low)+((high-low)//2)
            mid_value = mountainArr.get(mid) 
            mid_value_less = mountainArr.get(mid-1)
            mid_value_more = mountainArr.get(mid+1)
            if(mid_value)>(mid_value_more) and (mid_value)>(mid_value_less):
                peak = mid
                break
            elif(mid_value)<(mid_value_more):
                low = mid+1
            else:
                high = mid - 1
        low,high = 0,peak
        while(low<=high):
            mid = (low)+((high-low)//2)
            mid_value = mountainArr.get(mid) 
            if(mid_value==target):
                return mid 
            elif(mid_value>target):
                high = mid-1
            else:
                low = mid+1
        low,high = peak+1,n-1
        while(low<=high):
            mid = (low)+((high-low)//2)
            mid_value = mountainArr.get(mid)
            if(mid_value==target):
                return mid
            elif(mid_value<target):
                high = mid - 1
            else:
                low  = mid + 1
        return -1

            

           
        

        
        
        