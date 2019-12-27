#! /local/bin/python3

def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    rl = len(image)
    cl = len(image[0])
    oldColor = image[sr][sc]
    def fill(image, sr, sc, oldColor, newColor):
        if image[sr][sc] != oldColor:
            return
        image[sr][sc] = newColor
        if sr > 0:
            fill(image, sr - 1, sc, oldColor, newColor)
        if sr < rl - 1:
            fill(image, sr + 1, sc, oldColor, newColor)
        if sc > 0:
            fill(image, sr, sc - 1, oldColor, newColor)
        if sc < cl - 1:
            fill(image, sr, sc + 1, oldColor, newColor)
    
    fill(image, sr, sc, oldColor, newColor)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, newColor = 1, 1, 2
floodFill(image, sr, sc, newColor)

print(image)