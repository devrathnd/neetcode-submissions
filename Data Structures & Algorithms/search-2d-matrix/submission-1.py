class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                left = 0
                right = len(matrix[mid]) - 1
                
                while (left <= right):
                    hmid = (left + right) // 2
                    midElement = matrix[mid][hmid]

                    if target == midElement:
                        return True
                    elif target < midElement:
                        right = hmid - 1
                    else:
                        left = hmid + 1
                break

        return False

        