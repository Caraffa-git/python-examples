import pygame
import math
import numpy as np

window_width, window_height = 200, 200
window = pygame.display.set_mode((window_width,window_width))
pygame.display.set_caption("Reaction Diffusion")

dA = 1
dB = 0.5
feed = 0.055
k =    0.062

data = []
next = []

def init_arrays():
    global data, next, data, next
    for x in range(window_width):
        data.append([])
        next.append([])
        for y in range(window_height):
            #               a   b
            data[x].append([1.0, 0.0])
            next[x].append([1.0, 0.0])

    # Draw rectangles
    for x in range(90- 50, 120 - 50):
            for y in range(90 - 50, 120 - 50):
                data[x][y][1] = 1.0

    for x in range(90+ 50, 120 + 50):
        for y in range(90 + 50, 120 + 50):
            data[x][y][1] = 1.0

def draw():
    global data, next, feed, dA, dB, k
    for x in range(1, window_width - 1):
        for y in range(1, window_height - 1):
            # 0 - a, 1 - b
            a = data[x][y][0] 
            b = data[x][y][1] 
            next[x][y][0] = a + (dA * laplace(x, y, 0)) - (a * b * b) + (feed * (1 - a))
            next[x][y][1] = b + (dB * laplace(x, y, 1)) + (a * b * b) - ((k + feed) * b)

            next[x][y][0] = constrain(next[x][y][0], 0, 1);
            next[x][y][1] = constrain(next[x][y][1], 0, 1);
    
    # Update screen
    for x in range(1, window_width - 1):
        for y in range(1, window_height - 1):
            val = math.floor((next[x][y][0]-next[x][y][1]) * 255)
            val = constrain(val, 0, 255)
            window.set_at((x,y), (val,val,val,255))

    pygame.display.update()

    data, next = next, data
    

def laplace(x ,y ,val):
    global data
    sum = 0

    sum += data[x][y][val] * -1
    sum += data[x - 1][y][val] * 0.2
    sum += data[x + 1][y][val] * 0.2
    sum += data[x][y + 1][val] * 0.2
    sum += data[x][y - 1][val] * 0.2
    sum += data[x - 1][y - 1][val] * 0.05
    sum += data[x + 1][y - 1][val] * 0.05
    sum += data[x + 1][y + 1][val] * 0.05
    sum += data[x - 1][y + 1][val] * 0.05
    return sum

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

if __name__ == "__main__":
    init_arrays()
    run = True
    window.fill((255,255,255,255))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()