import pygame
import random

width, height = 600, 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ants")

FPS = 60

WHITE = (255,255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

random.seed()
Ax, Ay = random.randrange(width), random.randrange(height)
random.seed()
Bx, By = random.randrange(width), random.randrange(height)
random.seed()
Cx, Cy = random.randrange(width), random.randrange(height)

A_ant = [Ax, Ay]
B_ant = [Bx, By]
C_ant = [Cx, Cy]

random.seed()
A_dir = random.randrange(3)
random.seed()
B_dir = random.randrange(3)
random.seed()
C_dir = random.randrange(3)

def moveForward(dir, ant = []):
    if dir > 3:
        dir = 0
    if dir < 0:
        dir = 3

    if dir == UP:
        ant[1] += 1
    if dir == DOWN:
        ant[1] -= 1
    if dir == LEFT:
        ant[0] -= 1
    if dir == RIGHT:
        ant[0] += 1

    #if ant is out of border
    #x
    if ant[0] > width - 1:
         ant[0] = 0
    else: 
        if ant[0] < 0:
            ant[0] = width - 1

    #y
    if ant[1] > height - 1:
         ant[1] = 0
    else: 
        if ant[1] < 0:
            ant[1] = height - 1

    return dir, ant


def main():
    clock = pygame.time.Clock()
    run = True
    global A_dir, B_dir, C_dir
    global A_ant, B_ant, C_ant

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for i in range(300):
            A_color = window.get_at((A_ant[0], A_ant[1]))
            B_color = window.get_at((B_ant[0], B_ant[1]))
            C_color = window.get_at((C_ant[0], C_ant[1]))

            #if ant is on black(empty) pixel
            if A_color == BLACK:
                A_dir += 1
                window.set_at((A_ant[0], A_ant[1]), GREEN)
            else:
                #if ant is on white(full) pixel
                if A_color != BLACK:
                    A_dir -= 1
                    window.set_at((A_ant[0], A_ant[1]), BLACK)

            if B_color == BLACK:
                B_dir += 1
                window.set_at((B_ant[0], B_ant[1]), RED)
            else:
                if B_color != BLACK:
                    B_dir -= 1
                    window.set_at((B_ant[0], B_ant[1]), BLACK)  
                    
            if C_color == BLACK:
                C_dir += 1
                window.set_at((C_ant[0], C_ant[1]), BLUE)
            else:
                if C_color != BLACK:
                    C_dir -= 1
                    window.set_at((C_ant[0], C_ant[1]), BLACK)              

            A_dir, A_ant = moveForward(A_dir, A_ant)
            B_dir, B_ant = moveForward(B_dir, B_ant)
            C_dir, C_ant = moveForward(C_dir, C_ant)

        pygame.display.update()

        if run == False:
            pygame.quit()

if __name__=="__main__":
    main()