class Solution:
    def addBinary(self, s1, s2):
        num1 = int(s1, 2)
        num2 = int(s2, 2)
        
        # Add the two integers
        sum_num = num1 + num2
        result = bin(sum_num)[2:]
        
        return result
