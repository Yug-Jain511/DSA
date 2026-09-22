class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)
        while(low<high):
            mid = (high+low)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                low = mid +1
            else:
                high = mid
        return low
      