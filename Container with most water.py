class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        ans = 0
        
        while i<j:
            ans = max(ans, min(height[i], height[j])*(j-i))
            if height[i]<height[j]:
                """
                If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line.
                """
                i += 1
            else:
                j -= 1
        return ans
