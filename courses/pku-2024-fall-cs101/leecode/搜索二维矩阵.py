class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        nums=[]
        for i in range(0,m):
            nums+=matrix[i]
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid

        return False
