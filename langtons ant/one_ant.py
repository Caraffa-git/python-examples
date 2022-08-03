import pygame
import time

width, height = 600, 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ants")

FPS = 60
WHITE = (255,255,255,255)
BLACK = (0,0,0)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
x, y = width//2, height//2
ant = [x, y]
ant_dir = 0

def moveForward():
    global ant_dir
    if ant_dir > 3:
        ant_dir = 0
    if ant_dir < 0:
        ant_dir = 3

    if ant_dir == UP:
        ant[1] += 1
    if ant_dir == DOWN:
        ant[1] -= 1
    if ant_dir == LEFT:
        ant[0] -= 1
    if ant_dir == RIGHT:
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


def main():
    clock = pygame.time.Clock()
    run = True
    global ant_dir

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for i in range(100):
            color = window.get_at((ant[0], ant[1]))

            #if ant is on black(empty) pixel
            if color == BLACK:
                ant_dir += 1
                window.set_at((ant[0], ant[1]), WHITE)
            else:
                #if ant is on white(full) pixel
                if color == WHITE:
                    ant_dir -= 1
                    window.set_at((ant[0], ant[1]), BLACK)
                

            moveForward()
        pygame.display.update()

        if run == False:
            pygame.quit()

if __name__=="__main__":
    main()