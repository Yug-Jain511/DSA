class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #Krunga me khud se
        low,high=1,max(piles)
        def isValid(speed):
            hours_taken = 0
            for i in range(0,len(piles)):
                required = (piles[i] + speed - 1) // speed
                hours_taken += required 
            return(hours_taken<=h)
        while(low<=high):
            mid = low+(high-low)//2
            if(isValid(mid)):
                high = mid-1
            else:
                low = mid+1
        return low





