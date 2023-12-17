class Solution:
    def numberOfPaths(self, rows, cols):
        Mod = 10**9 + 7
        ans = 1
        for i in range(rows - 1):
            ans = (ans*(rows + cols - 2 - i)) % Mod
            ans = (ans*pow(i + 1, Mod - 2, Mod))%Mod
        return ans
