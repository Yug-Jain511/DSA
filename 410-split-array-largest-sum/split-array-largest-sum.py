class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low,high = 0,0
        for num in nums:
            if num > low:
                low = num
            high += num
        def isValid(mid):
            split = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if(current_sum>mid):
                    split += 1
                    current_sum = num
            return(split<=k) 
        while(low<=high):
            mid = low+(high-low)//2
            if(isValid(mid)):
                high = mid-1
            else:
                low = mid+1
        return low



        