class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        stack = [(sr, sc)]
        originColor = image[sr][sc]
        
        while stack:
            i, j = stack.pop()
            
            if image[i][j]==newColor or image[i][j]!=originColor: continue

            image[i][j] = newColor
            if i+1<len(image): stack.append((i+1, j))
            if 0<=i-1: stack.append((i-1, j))
            if j+1<len(image[0]): stack.append((i, j+1))
            if 0<=j-1: stack.append((i, j-1))

        return image
