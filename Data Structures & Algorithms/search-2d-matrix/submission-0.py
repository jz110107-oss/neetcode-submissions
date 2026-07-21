class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, l2 ,r1, r2 = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        while l2 <= r2:
            middle = (l2 + r2)//2

            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                l2, r2 = middle, middle
                break
            elif target > matrix[middle][-1]:
                l2 = middle + 1
            else:
                r2 = middle - 1
        
        if l2 != r2:
            return False

        while l1 <= r1:
            middle = (l1 + r1)//2

            if matrix[l2][middle] == target:
                return True
            elif matrix[l2][middle] > target:
                r1 = middle - 1
            else:
                l1 = middle + 1
        
        return False
