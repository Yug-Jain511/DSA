class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low,high = 0,0
        for i in weights:
            high += i
            if i>low:
                low = i
        def isValid(weights, days, capacity):
            d = 1
            current = 0

            for weight in weights:
                if current + weight > capacity:
                    d += 1
                    current = 0

                current += weight

            return d <= days
        while(low<=high):
            mid = low+(high-low)//2
            if(isValid(weights,days,mid)):
                high= mid-1
            else:
                low = mid+1
        return low