# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #this will get us value of peak (there is only 1)
        n = mountainArr.length()
        peak = 0
        low,high = 1,n-2
        while(low<=high):
            mid = low+(high-low)//2

            mid_value = mountainArr.get(mid)
            next = mountainArr.get(mid + 1)
            prev = mountainArr.get(mid - 1)

            if(mid_value>next) and (mid_value>prev):
                peak = mid
                break
            elif(mid_value<next):
                low = mid+1
            else:
                high = mid - 1 

        #now searching left of peak for target
        low,high = 0,peak
        while(low<=high):
            mid = low+(high-low)//2
            mid_value = mountainArr.get(mid)

            if(mid_value==target):
                return mid
            elif(mid_value<target):
                low = mid+1
            else:
                high = mid-1
#searching right side with modified binary search
        low,high = peak+1,n-1
        while(low<=high):
            mid = low+(high-low)//2
            mid_value = mountainArr.get(mid)

            if(mid_value==target):
                return mid
            elif(mid_value>target):
                low = mid+1
            else:
                high = mid-1

        return -1