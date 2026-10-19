class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        arr = []

        for row in matrix:
            arr += row

        l, r = 0, len(arr) - 1

        while (l <= r):

            mid = (l + r) // 2

            if arr[mid] == target:
                return True

            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False



        

        
        