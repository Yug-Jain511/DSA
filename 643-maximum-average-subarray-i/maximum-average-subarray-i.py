class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxAverage = float('-inf')
        average= 0
        total = 0
        start,end = 0,0
        for end in range(len(nums)):
            total += nums[end]
            if(end-start)+1 == k:
                avrg = total/k
                if(avrg>maxAverage):
                    maxAverage = avrg
                total -= nums[start]
                start +=1
        return maxAverage