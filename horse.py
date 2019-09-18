import numpy as np
matrix = np.zeros((8,8))
file = open("text.txt", "r")
horse = file.readline().split()
xh = int(horse[0])
yh = int(horse[1])
matrix[xh][yh] = 1
food = file.readline().split()
xf = int(food[0])
yf = int(food[1])
file.close()
matrix[xf][yf] = 2
read = 0
steps = 1
while(read == 0):
    if((xh + 1) <= 7)and((yh + 2) <= 7)and(matrix[xh+1][yh+2] == 0):
        matrix[xh + 1][yh + 2] = 1
        xh += 1
        yh += 2
        steps += 1
    elif((xh - 1) >= 0)and((yh + 2) <= 7)and(matrix[xh-1][yh+2] == 0):
        matrix[xh - 1][yh + 2] = 1
        xh -= 1
        yh += 2
        steps += 1
    elif((xh - 2) >= 0)and((yh + 1) <= 7)and(matrix[xh-2][yh + 1] == 0):
        matrix[xh - 2][yh + 1] = 1
        xh -= 2
        yh += 1
        steps += 1
    elif((xh - 2) >= 0)and((yh - 1) >= 0)and(matrix[xh-2][yh - 1] == 0):
        matrix[xh - 2][yh - 1] = 1
        xh -= 2
        yh -= 1
        steps += 1
    elif((xh - 1) >= 0)and((yh - 2) >= 0)and(matrix[xh - 1][yh - 2] == 0):
        matrix[xh - 1][yh - 2] = 1
        xh -= 1
        yh -= 2
        steps += 1
    elif((xh + 1) <= 7)and((yh - 2) >= 0)and(matrix[xh + 1][yh - 2] == 0):
        matrix[xh + 1][yh - 2] = 1
        xh += 1
        yh -= 2
        steps += 1
    elif((xh + 2) <= 7)and((yh - 1) >= 0)and(matrix[xh + 2][yh - 1] == 0):
        matrix[xh + 2][yh - 1] = 1
        xh += 2
        yh -= 1
        steps += 1
    elif((xh + 2) <= 7)and((yh + 1) <= 7)and(matrix[xh + 2][yh + 1] == 0):
        matrix[xh + 2][yh + 1] = 1
        xh += 2
        yh += 1
        steps += 1
#    print(xh,yh)
    if((xh + 1) <= 7)and((yh + 2) <= 7)and(matrix[xh+1][yh+2] == 2): break
    elif((xh - 1) >= 0)and((yh + 2) <= 7)and(matrix[xh-1][yh+2] == 2): break
    elif((xh - 2) >= 0)and((yh + 1) <= 7)and(matrix[xh-2][yh + 1] == 2): break
    elif((xh - 2) >= 0)and((yh - 1) >= 0)and(matrix[xh-2][yh - 1] == 2): break
    elif((xh - 1) >= 0)and((yh - 2) >= 0)and(matrix[xh - 1][yh - 2] == 2): break
    elif((xh + 1) <= 7)and((yh - 2) >= 0)and(matrix[xh + 1][yh - 2] == 2): break
    elif((xh + 2) <= 7)and((yh - 1) >= 0)and(matrix[xh + 2][yh - 1] == 2): break
    elif((xh + 2) <= 7)and((yh + 1) <= 7)and(matrix[xh + 2][yh + 1] == 2): break
file = open("text.txt", "a")
file.write("\nThere were ")
file.write(str(steps))
file.write(" steps.")
file.close()
    
