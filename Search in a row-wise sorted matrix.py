class Solution:
    def searchRowMatrix(self, mat, x):
        from bisect import bisect_left

        for row in mat:
            idx = bisect_left(row, x)
            if idx < len(row) and row[idx] == x:
                return True

        return False
