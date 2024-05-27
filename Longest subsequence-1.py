from typing import List

class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        inc_dp = {}
        dec_dp = {}
        max_length = 0
        for num in a:
            inc_dp[num] = inc_dp.get(num - 1, 0) + 1
            dec_dp[num] = dec_dp.get(num + 1, 0) + 1

            max_length = max(max_length, inc_dp[num], dec_dp[num])
            
        return max_length
        
