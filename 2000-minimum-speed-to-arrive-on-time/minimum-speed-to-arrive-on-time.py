class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        low,high = 1,10**7
        def isValid(speed):
            hours_taken = 0
            for i in range(0,len(dist)-1):
                if(dist[i]%speed == 0):
                    hours_taken += dist[i]/speed
                else:
                    hours_taken += math.ceil(dist[i]/speed)
            hours_taken  += dist[len(dist)-1]/speed
            return(hours_taken<=hour)
        while(low<=high):
            mid = low+(high-low)//2
            if(isValid(mid)):
                high = mid-1
            else:
                low = mid+1
        return low 


        