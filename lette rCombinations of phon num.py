class Solution(object):
    def letterCombinations(self, digits):
        def helper(A, digit):
            if not A: return memo[digit]

            opt = []
            for letter in memo[digit]:
                for string in A:
                    opt.append(string+letter)
            return opt

        ans = []
        memo = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
