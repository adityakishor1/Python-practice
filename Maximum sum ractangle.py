class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')

        for left in range(m):
            temp = [0] * n

            for right in range(left, m):
                for i in range(n):
                    temp[i] += mat[i][right]
                curr_sum = temp[0]
                max_curr = temp[0]
                for i in range(1, n):
                    curr_sum = max(temp[i], curr_sum + temp[i])
                    max_curr = max(max_curr, curr_sum)
                max_sum = max(max_sum, max_curr)

        return max_sum
