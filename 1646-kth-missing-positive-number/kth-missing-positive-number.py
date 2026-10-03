class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low,high = 0,len(arr)-1
        while(low<=high):
            mid = low+(high-low)//2
            if(arr[mid]-(mid+1)>=k):
                high = mid-1
            else:
                low = mid+1
        return low+k
       
        