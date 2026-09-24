class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix) 
        cols = len(matrix[0])
        low,high = 0,rows*cols - 1
        while(low<=high):
            mid=low+(high-low)//2
            current= matrix[int(mid/cols)][mid%cols]
            if(current==target):
                return True
            elif(current<target):
                low = mid+1
            else:
                high = mid-1
        return False