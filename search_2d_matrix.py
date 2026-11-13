from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Matrix als ein sortiertes 1D-Array der Länge m*n betrachten
        # und darauf binär suchen: O(log(m*n)).
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // n][mid % n]  # 1D-Index -> (Zeile, Spalte)

            if value == target:
                return True
            if value < target:
                left = mid + 1  # rechts weitersuchen
            else:
                right = mid - 1  # links weitersuchen

        return False


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
print(Solution().searchMatrix(matrix, target))
